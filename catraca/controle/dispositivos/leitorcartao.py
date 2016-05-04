 #!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import locale
import threading
import datetime
from time import sleep
from contextlib import closing
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.pictograma import Pictograma
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.controle.restful.relogio import Relogio
from catraca.modelo.dao.cartao_valido_dao import CartaoValidoDAO
from catraca.modelo.dao.isencao_dao import IsencaoDAO


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(Relogio):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    pino_controle = PinoControle()

    cartao_dao = CartaoDAO()
    cartao_valido_dao = CartaoValidoDAO()
    isencao_dao = IsencaoDAO()
    registro_dao = RegistroDAO()
    custo_refeicao_dao = CustoRefeicaoDAO()
    D0 = pino_controle.ler(17)['gpio']
    D1 = pino_controle.ler(27)['gpio']
    bits = '' #11101110000100010000010011101110 #10111111010000100010001101010
    numero_cartao = None
    CATRACA = None
    CARTAO = None
    TURNO = None
    contador_local = 0
    uso_do_cartao = False
    
    def __init__(self, intervalo=0.2):
        super(LeitorCartao, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread LeitorCartao'
        
    def run(self):
        print "%s. Rodando... " % self.name
        
        self.obtem_catraca_turno()

        self.pino_controle.evento_both(self.D0, self.zero)
        self.pino_controle.evento_both(self.D1, self.um)
        
        while True:
#             self.CATRACA = Relogio.catraca
#             if self.CATRACA:
#                 self.TURNO = Relogio.turno
            self.ler()
            sleep(self.intervalo)

    def zero(self, obj):
        if obj:
            self.bits += '0'
            
    def um(self, obj):
        if obj:
            self.bits += '1'
        
    def obtem_numero_cartao_rfid(self):
        id = None
        try:
            while True:
                if self.bits:
                    print self.bits
                    LeitorCartao.uso_do_cartao = True
                    self.aviso.exibir_aguarda_consulta()
                    self.log.logger.info('Binario obtido corretamente. [Cartao n.] '+str(self.bits))
                    id = str(int(self.bits, 2))
                    id = id.zfill(10)
                    if (len(self.bits) == 32) and (len(id) == 10):
                        self.numero_cartao = id
                        self.util.beep_buzzer(860, .1, 1)
                        print "Leu CARTAO N. " +str(self.numero_cartao) +"  BINARIO: "+ str(self.bits)
                        return self.numero_cartao
                    else:
                        print "Erro ao ler cartao N. " +str(id)
                        self.log.logger.warn('Binario ou inteiro obtido incorretamente. [cartao n.] ' + str(self.bits), exc_info=True)
#                         self.util.beep_buzzer(250, .1, 3)
                        self.aviso.exibir_erro_leitura_cartao()
                        self.bloqueia_acesso()
                        id = None
                        return None
                else:
                    return id
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro ao obter binario. [cartao n.] ' + str(self.bits), exc_info=True)
        finally:
            self.bits = ''
            
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
                if Relogio.periodo:
                    self.obtem_catraca_turno()
                    if self.CATRACA.operacao == 5:
                        self.aviso.exibir_acesso_livre()
                        return None
                    if self.CATRACA.operacao <= 0 or self.CATRACA.operacao >= 6:
                        self.aviso.exibir_bloqueio_total()
                        return None
                    self.valida_cartao(self.numero_cartao)
                else:
                    self.obtem_catraca_turno()
                    self.aviso.exibir_horario_invalido()
                    self.bloqueia_acesso()
                    return None
            else:
                return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro ao ler. [cartao n.] ' + str(self.numero_cartao), exc_info=True)
        finally:
            LeitorCartao.uso_do_cartao = False
        
    def valida_cartao(self, numero):
        cartao = Cartao()
        registro = Registro()
        cartao_json = CartaoJson()
        registro_json = RegistroJson()
        
        giro_completo = False
        try:
            ##############################################################
            ## CONSULTA SE O CARTAO ESTA CADASTRADO NO BANCO DE DADOS
            ##############################################################
            self.CARTAO = self.obtem_cartao(numero)
            if self.CARTAO is None:
                self.log.logger.info('Identificacao invalida. [cartao n.] ' + str(numero))
                self.util.beep_buzzer(250, .1, 3) #0 seg.
                self.aviso.exibir_cartao_nao_cadastrado()
                return None
            else:
                ##############################################################
                ## OBTEM AS INFORMACOES DO CARTAO CONSULTADO NO BANCO DE DADOS
                ##############################################################
                self.log.logger.info('Identificacao valida. [cartao n.] ' + str(numero))
                cartao_id = self.CARTAO.id
                self.numero_cartao = self.CARTAO.numero
                cartao_total_creditos = self.CARTAO.creditos
                cartao_valor_tipo = self.CARTAO.valor
                cartao_limite_utilizacao = self.CARTAO.refeicoes
                cartao_tipo_id = self.CARTAO.tipo
                cartao_vinculo_id = self.CARTAO.vinculo
                cartao_vinculo_descricao = self.CARTAO.descricao
                cartao_usuario_nome = self.CARTAO.nome
                ##############################################################
                ## VERIFICA SE O CARTAO POSSUI ISENCAO DE PAGAMENTO
                ##############################################################
                self.aviso.exibir_saldo_cartao(cartao_usuario_nome, locale.currency(float(cartao_total_creditos)).format())
                saldo_creditos = 0.00
                cartao_isento = True
                """ DESABILITADO TEMPORARIAMENTE
                cartao_isento = False
                ISENCAO = self.obtem_isencao(self.numero_cartao)
                if ISENCAO is None:
                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                    ##############################################################
                    if (float(cartao_total_creditos) < float(cartao_valor_tipo)):
                        self.log.logger.info('Credito invalido. [cartao n.] ' + str(self.numero_cartao))
                        self.aviso.exibir_saldo_insuficiente()
                        self.util.beep_buzzer(250, .1, 3)
                        return None
                    else:
                        self.log.logger.info('Credito valido. [cartao n.] ' + str(self.numero_cartao))
                        saldo_creditos = float(cartao_total_creditos) - float(cartao_valor_tipo)
                else:
                    self.log.logger.info('Isento. [cartao n.] ' + str(self.numero_cartao))
                    cartao_isento = True
                    self.aviso.exibir_cartao_isento( datetime.datetime.strptime(str(ISENCAO.fim),'%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M') )
                """
                ##############################################################
                ## VERIFICA O LIMITE PERMITIDO DE USO DO CARTAO DURANTE TURNO
                ##############################################################
                if self.obtem_limite_utilizacao(cartao_id) >= cartao_limite_utilizacao:
                    self.log.logger.info('Limite de uso atingido. [cartao n.] ' + str(self.numero_cartao))
                    self.util.beep_buzzer(250, .1, 3)
                    self.aviso.exibir_cartao_utilizado(self.TURNO.descricao)
                    return None
                else:
                    #cartao
                    cartao.id = cartao_id
                    cartao.numero = self.numero_cartao
                    cartao.creditos =  cartao_total_creditos if cartao_isento else saldo_creditos
                    cartao.tipo = cartao_tipo_id
                    #registro
                    registro.data = self.util.obtem_datahora_postgresql()
                    registro.pago = 0.00 if cartao_isento else float(cartao_valor_tipo)
                    registro.custo = self.obtem_custo_refeicao()
                    registro.cartao = cartao_id
                    registro.catraca = self.CATRACA.id
                    registro.vinculo = cartao_vinculo_id
                    ##############################################################
                    ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                    ##############################################################
                    self.desbloqueia_acesso()
                    while True:
                        if self.sensor_optico.registra_giro(self.CATRACA.tempo, self.CATRACA):
                            print "GIROU!"
                            self.log.logger.info('Girou catraca. [cartao n.] ' + str(self.numero_cartao))
                            giro_completo = True
                            return None
                        else:
                            print "NAO GIROU!"
                            self.log.logger.info('Nao girou catraca. [cartao n.] ' + str(self.numero_cartao))
                            return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro ao validar informacoes. [cartao n.] ' + str(self.numero_cartao), exc_info=True)
        finally:
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.bloqueia_acesso()
            if giro_completo:
#                 # insere registro remoto
#                 registro_json.objeto_json(registro)
                giro_completo = False
#                 #registro_json.registro_get(True, False)
#                 # atualiza cartao remoto
#                 cartao_json.objeto_json(cartao)
#                 #cartao_json.cartao_get(True, False)
            else:
                cartao = None
                registro = None
            
    def obtem_csv(self, numero_cartao):
        with open(self.util.obtem_path('cartao.csv')) as csvfile:
            reader = csv.reader(csvfile)
            if reader:
                for row in reader:
                    if row[0] == str(numero_cartao):
                        self.log.logger.info('Solicitacao de '+str(row[1])+'. [cartao n.] ' + str(numero_cartao))
                        return row[1]
                
    def obtem_cartao(self, numero):
        #remoto
        cartao_valido = self.recursos_restful.cartao_json.cartao_valido_get(numero)
        if cartao_valido is None:
            #local
            cartao_valido = self.cartao_valido_dao.busca_cartao_valido(numero)
        if cartao_valido:
            self.CARTAO = cartao_valido
            return cartao_valido
        else:
            return None
        
    def obtem_isencao(self, numero_cartao):
        #remoto
        isencao_ativa = self.recursos_restful.isencao_json.isencao_ativa_get(numero_cartao)
        if isencao_ativa is None:
            #local
            isencao_ativa = self.isencao_dao.busca_isencao(numero_cartao)
        if isencao_ativa:
            return isencao_ativa
        else:
            return None
        
    def obtem_limite_utilizacao(self, cartao_id):
        #remoto
        limite_utilizacao = self.recursos_restful.registro_json.registro_utilizacao_get(Relogio.hora_inicio, Relogio.hora_fim, cartao_id)
        if limite_utilizacao is None:
            #local
            limite_utilizacao = self.registro_dao.busca_utilizacao(Relogio.hora_inicio, Relogio.hora_fim, cartao_id)
        if limite_utilizacao:
            return limite_utilizacao
        else:
            return 0
        
    def obtem_custo_refeicao(self):
        #remoto
        custo_refeicao_atual = self.recursos_restful.custo_refeicao_json.custo_refeicao_atual_get()
        if custo_refeicao_atual is None:
            #local
            custo_refeicao_atual = self.custo_refeicao_dao.busca()
        if custo_refeicao_atual:
            return float(custo_refeicao_atual.valor)
        else:
            return 0.00
        
    def bloqueia_acesso(self):
        self.aviso.exibir_acesso_bloqueado()
        if self.CATRACA.operacao == 1 or self.CATRACA.operacao == 3:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.CATRACA.operacao == 2 or self.CATRACA.operacao == 4:
            self.solenoide.ativa_solenoide(2,0)
            self.pictograma.seta_direita(0)
            self.pictograma.xis(0)
        self.log.logger.info('Bloqueia. [cartao n.] ' + str(self.numero_cartao))
        self.aviso.exibir_aguarda_cartao()
    
    def desbloqueia_acesso(self):
        self.aviso.exibir_acesso_liberado()
#         self.util.beep_buzzer(860, .2, 1)
        if self.CATRACA.operacao == 1 or self.CATRACA.operacao == 3:
            self.solenoide.ativa_solenoide(1,1)
            self.pictograma.seta_esquerda(1)
            self.pictograma.xis(1)
        if self.CATRACA.operacao == 2 or self.CATRACA.operacao == 4:
            self.solenoide.ativa_solenoide(2,1)
            self.pictograma.seta_direita(1)
            self.pictograma.xis(1)
        self.log.logger.info('Libera. [cartao n.] ' + str(self.numero_cartao))
        
        
    def obtem_catraca_turno(self):
        #while self.CATRACA is None:
        self.CATRACA = Relogio.catraca
        while self.CATRACA is None:
            self.CATRACA = Relogio.catraca
            print "tentando obter catraca no alerta"
        #self.TURNO = Relogio.turno
            #print "tentando obter catraca no leitor"
        if self.CATRACA:
            self.TURNO = Relogio.turno