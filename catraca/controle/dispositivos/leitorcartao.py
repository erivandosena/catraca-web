 #!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import csv
import locale
import threading
import datetime
import calendar
from time import sleep
from unicodedata import normalize
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.pictograma import Pictograma
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.registro_offline_dao import RegistroOfflineDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson

from catraca.controle.recursos.usuario_json import UsuarioJson

from catraca.controle.api.gerenciador import Gerenciador
from catraca.modelo.dao.cartao_valido_dao import CartaoValidoDAO
from catraca.modelo.dao.isencao_dao import IsencaoDAO
from catraca.controle.api.rede import Rede
from catraca.controle.recursos.recursos_restful import RecursosRestful

from catraca.modelo.dao.tipo_dao import TipoDAO

from catraca.modelo.entidades.vinculo import Vinculo
from catraca.modelo.dao.vinculo_dao import VinculoDAO
from catraca.controle.recursos.vinculo_json import VinculoJson
from _ast import Return

__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(threading.Thread):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    pino_controle = PinoControle()
    recursos_restful = RecursosRestful()
    

    cartao_dao = CartaoDAO()
    cartao_valido_dao = CartaoValidoDAO()
    isencao_dao = IsencaoDAO()
    registro_dao = RegistroOfflineDAO()
    custo_refeicao_dao = CustoRefeicaoDAO()
    D0 = pino_controle.ler(17)['gpio']
    D1 = pino_controle.ler(27)['gpio']
    bits = None #11101110000100010000010011101110 #10111111010000100010001101010
    numero_cartao = None
    CARTAO = ""
    contador_local = 0
    uso_do_cartao = False
    
    def __init__(self, intervalo=0.2):
        #super(LeitorCartao, self).__init__()
        #Gerenciador.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread LeitorCartao'
        
    def run(self):
        print "%s. Rodando... " % self.name

        self.pino_controle.evento_both(self.D0, self.zero)
        self.pino_controle.evento_both(self.D1, self.um)
        
        while True:
            self.ler()
            if not self.bits:
                Gerenciador.uso_do_cartao = False
            sleep(self.intervalo)

    def zero(self, obj):
        if obj:
            self.bits += '0'
            
    def um(self, obj):
        if obj:
            self.bits += '1'
        
    def obtem_numero_cartao_rfid(self):
        Gerenciador.uso_do_cartao = True
        id = None
        try:
            while True:
                if self.bits:
                    self.aviso.exibir_aguarda_consulta()
                    id = str(int(self.bits, 2))
                    id = id.zfill(10)
                    if (len(self.bits) == 32) and (len(id) == 10):
                        self.numero_cartao = id
                        self.util.beep_buzzer(860, .1, 1)
                        print "Leu CARTAO N. " +str(self.numero_cartao) +"  BINARIO: "+ str(self.bits)
                        return self.numero_cartao
                    else:
#                         self.util.beep_buzzer(250, .1, 3)
                        print "ERRO CARTAO N. " +str(self.numero_cartao) +"  BINARIO: "+ str(self.bits)
                        self.aviso.exibir_erro_leitura_cartao()
                        self.bloqueia_acesso()
                        id = None
                        return None
                else:
                    return id
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
#         finally:
#             self.bits = ''
            
    def ler(self):
        try:
            if self.obtem_numero_cartao_rfid():
                csv = self.obtem_csv(self.numero_cartao)
                if csv == "Reiniciar Catraca":
                    self.aviso.exibir_reinicia_catraca()
                    self.util.reinicia_raspberrypi()
                if csv == "Desligar Catraca":
                    self.aviso.exibir_desliga_catraca()
                    self.util.desliga_raspberrypi()
                if csv == "Liberar Catraca":
                    self.aviso.exibir_acesso_livre()
                    self.desbloqueia_acesso()
                    sleep(4)
                    self.bloqueia_acesso()
                    return None
                if Gerenciador.periodo:
                    if Gerenciador.catraca.operacao == 5:
                        self.aviso.exibir_acesso_livre()
                        return None
                    if Gerenciador.catraca.operacao < 1 or Gerenciador.catraca.operacao > 5:
                        self.aviso.exibir_bloqueio_total()
                        return None
                    self.valida_cartao(self.numero_cartao)
                else:
                    self.aviso.exibir_horario_invalido()
                    self.bloqueia_acesso()
                    return None
            else:
                return None
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        finally:
            self.bits = ""
            #Gerenciador.uso_do_cartao = False
        
    def valida_cartao(self, numero):
        cartao = Cartao()
        reg = Registro()
        registro = []
        cartao_json = CartaoJson()
        registro_json = RegistroJson()
        giro_completo = False
        try:
            ##############################################################
            ## CONSULTA SE O CARTAO ESTA CADASTRADO NO BANCO DE DADOS
            ##############################################################
            self.CARTAO = self.obtem_cartao(numero)
            if self.CARTAO is None:
                self.util.beep_buzzer(250, .1, 3)
                self.aviso.exibir_cartao_nao_cadastrado()
                return None
            else:
                ##############################################################
                ## OBTEM INFORMACOES SOBRE A VALIDADE DO VINCULO DO CARTAO
                ##############################################################
                if not self.obtem_vinculo(self.CARTAO):
                    self.util.beep_buzzer(250, .1, 3)
                    if not self.CARTAO.avulso:
                        return self.renova_vinculo(self.CARTAO)
                    return None
                ##############################################################
                ## OBTEM AS INFORMACOES DO CARTAO CONSULTADO NO BANCO DE DADOS
                ##############################################################
                cartao_id = self.CARTAO.id
                self.numero_cartao = self.CARTAO.numero
                cartao_total_creditos = self.CARTAO.creditos
                cartao_valor_tipo = self.CARTAO.valor
                cartao_limite_utilizacao = self.CARTAO.refeicoes
                cartao_tipo_id = self.CARTAO.tipo
                cartao_vinculo_id = self.CARTAO.vinculo
                cartao_vinc_avulso = self.CARTAO.avulso
                cartao_vinculo_descricao = self.CARTAO.descricao
                cartao_vinculo_inicio = self.CARTAO.inicio
                cartao_vinculo_fim = self.CARTAO.fim
                cartao_usuario_nome = self.CARTAO.nome
                ##############################################################
                ## VERIFICA O STATUS DO MODO FINANCEIRO DA CATRACA
                ##############################################################
                saldo_creditos = 0.00
                cartao_isento = False
                self.aviso.exibir_saldo_cartao(cartao_usuario_nome, locale.currency(float(cartao_total_creditos)).format())
                if Gerenciador.catraca.financeiro:
                    print Gerenciador.catraca.financeiro
                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI ISENCAO DE PAGAMENTO
                    ##############################################################
                    ISENCAO = self.obtem_isencao(self.numero_cartao)
                    if ISENCAO is None:
                        ##############################################################
                        ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                        ##############################################################
                        if (float(cartao_total_creditos) < float(cartao_valor_tipo)):
                            self.aviso.exibir_saldo_insuficiente()
                            self.util.beep_buzzer(250, .1, 3)
                            return None
                        else:
                            saldo_creditos = float(cartao_total_creditos) - float(cartao_valor_tipo)
                    else:
                        cartao_isento = True
                        self.aviso.exibir_cartao_isento( datetime.datetime.strptime(str(ISENCAO.fim),'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M') )
                ##############################################################
                ## VERIFICA O LIMITE PERMITIDO DE USO DO CARTAO DURANTE TURNO
                ##############################################################
                print "TESTE->: "+str(self.obtem_limite_utilizacao(cartao_id))+ " >= " +str(cartao_limite_utilizacao)
                if self.obtem_limite_utilizacao(cartao_id) >= cartao_limite_utilizacao:
                    self.util.beep_buzzer(250, .1, 3)
                    self.aviso.exibir_cartao_utilizado(Gerenciador.turno.descricao)
                    return None
                else:
                    #cartao
                    cartao.id = cartao_id
                    cartao.numero = self.numero_cartao
                    cartao.creditos =  cartao_total_creditos if cartao_isento or not Gerenciador.catraca.financeiro else saldo_creditos
                    cartao.tipo = cartao_tipo_id
                    
                    print "exibindo cartao utilizado"
                    print "*" * 40
                    print cartao.id
                    print cartao.numero
                    print cartao.creditos
                    print cartao.tipo
                    
                    #registro
#                     registro.cartao = cartao_id
#                     registro.catraca = Gerenciador.catraca.id
#                     registro.data = self.util.obtem_datahora_postgresql()
#                     registro.custo = self.obtem_custo_refeicao()
#                     registro.pago = 0.00 if cartao_isento else float(cartao_valor_tipo)
#                     registro.vinculo = cartao_vinculo_id

                    reg.cartao = cartao_id
                    reg.catraca = Gerenciador.catraca.id
                    reg.data = self.util.obtem_datahora_postgresql()
                    reg.custo = self.obtem_custo_refeicao()
                    reg.pago = 0.00 if cartao_isento else float(cartao_valor_tipo)
                    reg.vinculo = cartao_vinculo_id

                    registro.insert(0, cartao_id)
                    registro.insert(1, Gerenciador.catraca.id)
                    registro.insert(2, self.util.obtem_datahora_postgresql())
                    registro.insert(3, self.obtem_custo_refeicao())
                    registro.insert(4, 0.00 if cartao_isento else float(cartao_valor_tipo))
                    registro.insert(5, cartao_vinculo_id)                
                    print "exibindo registro utilizado"
                    print "*" * 40
                    #print self.registro_dao.busca_ultimo_registro() + 1
#                     print registro.data
#                     print registro.pago
#                     print registro.custo
#                     print registro.cartao
#                     print registro.catraca
#                     print registro.vinculo
                    print registro[0]
                    print registro[1]
                    print registro[2]
                    print registro[3]
                    print registro[4]
                    print registro[5]
                    
                    ##############################################################
                    ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                    ##############################################################
                    self.desbloqueia_acesso()
                    while True:
                        if self.sensor_optico.registra_giro(Gerenciador.catraca.tempo, Gerenciador.catraca):
                            print "GIROU!"
                            self.log.logger.info('Girou catraca. [cartao n.] ' + str(self.numero_cartao))
                            giro_completo = True
                            return None
                        else:
                            print "NAO GIROU!"
                            self.log.logger.info('Nao girou catraca. [cartao n.] ' + str(self.numero_cartao))
                            return None
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        finally:
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.bloqueia_acesso()
            if giro_completo:
                if Rede.status:
                    # insere registro remoto
                    #registro_json.lista_json(registro)

                    if registro_json.objeto_json(reg) == 200:
                        print ">>> Registro inserido no remoto com sucesso!"
                    else:
                        print "ERRO ENVIANDO REGISTRO..."
                    # atualiza cartao remoto
                    #cartao_json.objeto_json(cartao)
                    if Gerenciador.catraca.financeiro:
                        if cartao_json.objeto_json(cartao) == 200:
                            print ">>> Cartao atualizado no remoto com sucesso!"
                        else:
                            print "ERRO ENVIANDO CARTAO..."
                else:
                    # insere registro local
                    #registro.id = self.registro_dao.busca_ultimo_registro() + 1000
                    if self.registro_dao.insere(registro):
                        print self.registro_dao.aviso
                    # atualiza cartao local
                    if Gerenciador.catraca.financeiro:
                        if self.cartao_dao.atualiza_exclui(cartao, False):
                            print self.cartao_dao.aviso
                    
                giro_completo = False
            else:
                cartao = None
                registro = None
            
    def obtem_csv(self, numero_cartao):
        try:
            with open(self.util.obtem_path('cartao.csv')) as csvfile:
                reader = csv.reader(csvfile)
                if reader:
                    for row in reader:
                        if row[0] == str(numero_cartao):
                            self.log.logger.info('Solicitacao de '+str(row[1])+'. [cartao n.] ' + str(numero_cartao))
                            return row[1]
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
                
    def obtem_cartao(self, numero):
        try:
            #remoto
            if Rede.status:
                cartao_valido = self.recursos_restful.cartao_json.cartao_valido_get(numero)
                print "[ACESSO REMOTO] "+ str(cartao_valido)
                self.CARTAO = cartao_valido
                return cartao_valido
            else:
                 #local
                cartao_valido = self.cartao_valido_dao.busca_cartao_valido(numero)
                if cartao_valido:
                    self.CARTAO = cartao_valido
                    print "[ACESSO LOCAL] "+ str(self.CARTAO)
                    return cartao_valido
                else:
                    return None
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_vinculo(self, cartao):
        try:
            atual = self.util.obtem_datahora()
            if cartao:
                atual = datetime.datetime(atual.year, atual.month, atual.day, atual.hour, atual.minute, atual.second)
                inicio = datetime.datetime.strptime(str(cartao.inicio), "%Y-%m-%d %H:%M:%S")
                inicio = datetime.datetime(inicio.year, inicio.month, inicio.day, inicio.hour, inicio.minute, inicio.second)
                fim = datetime.datetime.strptime(str(cartao.fim), "%Y-%m-%d %H:%M:%S")
                fim = datetime.datetime(fim.year, fim.month, fim.day, fim.hour, fim.minute, fim.second)
                print inicio <= atual <= fim , cartao.avulso
                if inicio <= atual <= fim: # and not cartao.avulso:
                    print "VINCULO ATIVO"
                    return True
                else:
                    print "VINCULO VENCIDO"
                    self.aviso.exibir_vinculo_invalido()
                    return False
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def renova_vinculo(self, cartao_valido):
        self.aviso.exibir_renova_vinculo_vencido()
        try:
            if cartao_valido:
                usuario_json = UsuarioJson()
                usuario_externo = usuario_json.status_usuario_externo_get(cartao_valido.idexterno) #(testes ok) 5138 5129 5093 2916 1179 564
                
                if usuario_externo:
                    id_status_servidor  = usuario_externo.id_status_servidor
                    status_discente     = usuario_externo.status_discente.strip().lower() if usuario_externo.status_discente else usuario_externo.status_discente
                    status_servidor     = usuario_externo.status_servidor.strip().lower() if usuario_externo.status_servidor else usuario_externo.status_servidor

#                     print "\nID_STATUS_SERVIDOR: " + str(id_status_servidor)
#                     print "STATUS_DISCENTE: " + str(status_discente)
#                     print "STATUS_SERVIDOR: " + str(status_servidor)
                    
                    status = False
                    if id_status_servidor is not None and id_status_servidor == 1:
                        status = True
                    else:
                        if status_discente is not None and "ativo" in status_discente:
                                status = True
                        else:
                            if status_servidor is not None and "ativo" in status_servidor:
                                status = True    
                    if status:
                        #RENOVA
                        vinculo = None
                        vinculo_dao = VinculoDAO()
                        #remoto
                        if Rede.status:
                            vinculo = VinculoJson().obtem_vinculo_id_get(cartao_valido.vinculo)
                            print "[ACESSO REMOTO->] "+ str(vinculo)
                        else:
                            #local
                            vinculo = vinculo_dao.busca(cartao_valido.vinculo)
                            print "[ACESSO LOCAL ->] "+ str(vinculo)
                        if vinculo and Rede.status:
                            data_atual = self.util.obtem_datahora()
                            nova_data = datetime.datetime(data_atual.year, data_atual.month + 3, data_atual.day, data_atual.hour, data_atual.minute, data_atual.second)
                            vinculo.fim = nova_data.strftime("%Y-%m-%d %H:%M:%S")
                            nova_data.strftime("%Y-%m-%d %H:%M:%S")
                            #atualiza vinculo remoto
                            if VinculoJson().objeto_json(vinculo) == 200:
                                # atualiza vinculo local
                                if vinculo_dao.atualiza_exclui(vinculo, False):
                                    print vinculo_dao.aviso
                                self.aviso.exibir_vinculo_renovado()
                                self.valida_cartao(self.numero_cartao)
                            else:
                                return self.aviso.exibir_vinculo_nao_renovado()
                        else:
                            # NAO RENOVA
                            return self.aviso.exibir_vinculo_nao_renovado()
                    else:
                        return self.aviso.exibir_vinculo_nao_renovado()
                else:
                    return self.aviso.exibir_vinculo_nao_renovado()
                        
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_isencao(self, numero_cartao):
        try:
            #remoto
            if Rede.status:
                isencao_ativa = self.recursos_restful.isencao_json.isencao_ativa_get(numero_cartao)
                print "[ACESSO REMOTO] "+ str(isencao_ativa)
                return isencao_ativa
            else:
                #local
                isencao_ativa = self.isencao_dao.busca_isencao(self.numero_cartao)
                if isencao_ativa:
                    print "[ACESSO LOCAL] "+ str(isencao_ativa)
                    return isencao_ativa
                else:
                    return None
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        
    def obtem_limite_utilizacao(self, cartao_id):
        try:
            #remoto
            if Rede.status:
                limite_utilizacao = self.recursos_restful.registro_json.registro_utilizacao_get(Gerenciador.hora_inicio, Gerenciador.hora_fim, cartao_id)
                print "[ACESSO REMOTO] "+ str(limite_utilizacao)
                return limite_utilizacao
            else:
                #local
                limite_utilizacao = self.registro_dao.busca_utilizacao(Gerenciador.hora_inicio, Gerenciador.hora_fim, cartao_id)
                if limite_utilizacao:
                    print "[ACESSO LOCAL] "+ str(limite_utilizacao)
                    return limite_utilizacao
                else:
                    return 0
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        
    def obtem_custo_refeicao(self):
        try:
            #remoto
            if Rede.status:
                custo_refeicao_atual = self.recursos_restful.custo_refeicao_json.custo_refeicao_atual_get()
                print custo_refeicao_atual
                print "[ACESSO REMOTO] "+ str(float(custo_refeicao_atual))
                return float(custo_refeicao_atual)
            else:
                #local
                custo_refeicao_atual = self.custo_refeicao_dao.busca_custo()
                print custo_refeicao_atual
                print "[ACESSO LOCAL] "+ str(float(custo_refeicao_atual))
                return float(custo_refeicao_atual)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        
    def bloqueia_acesso(self):
        try:
            self.aviso.exibir_acesso_bloqueado()
            if Gerenciador.catraca:
                if Gerenciador.catraca.operacao == 1 or Gerenciador.catraca.operacao == 3:
                    self.solenoide.ativa_solenoide(1,0)
                    self.pictograma.seta_esquerda(0)
                    self.pictograma.xis(0)
                if Gerenciador.catraca.operacao == 2 or Gerenciador.catraca.operacao == 4:
                    self.solenoide.ativa_solenoide(2,0)
                    self.pictograma.seta_direita(0)
                    self.pictograma.xis(0)
                self.aviso.exibir_aguarda_cartao()
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
    
    def desbloqueia_acesso(self):
        try:
            if Gerenciador.catraca.operacao == 1 or Gerenciador.catraca.operacao == 3:
                self.solenoide.ativa_solenoide(1,1)
                self.pictograma.seta_esquerda(1)
                self.pictograma.xis(1)
            if Gerenciador.catraca.operacao == 2 or Gerenciador.catraca.operacao == 4:
                self.solenoide.ativa_solenoide(2,1)
                self.pictograma.seta_direita(1)
                self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
        except Exception:
            self.log.logger.error("Exception", exc_info=True)

    def remove_acentos(self, texto):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            return normalize('NFKD', texto.decode("utf-8","ignore")).encode('ascii','ignore')
        except UnicodeDecodeError:
            self.log.logger.error("UnicodeDecodeError", exc_info=True)
            