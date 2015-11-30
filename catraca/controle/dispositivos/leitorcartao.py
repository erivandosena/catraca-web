#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import locale
import threading
from time import sleep
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.pictograma import Pictograma
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.giro_dao import GiroDAO
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.entidades.registro_off import RegistroOff
from catraca.modelo.entidades.giro import Giro
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.controle.restful.controle_api import ControleApi
from catraca.controle.restful.relogio import Relogio


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

    giro_dao = GiroDAO()
    cartao_dao = CartaoDAO()
    registro_dao = RegistroDAO()
    D0 = pino_controle.ler(17)['gpio']
    D1 = pino_controle.ler(27)['gpio']
    bits = '' #11101110000100010000010011101110
    numero_cartao = None
    CARTAO = []
    contador_local = 0
    
    def __init__(self, intervalo=1):
        super(LeitorCartao, self).__init__()
        threading.Thread.__init__(self)
        Relogio.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread LeitorCartao'
        thread = threading.Thread(group=None, target=self.run(), args=())
        thread.daemon = True
        
    def run(self):
        print "%s. Rodando... " % self.name

        self.pino_controle.evento_both(self.D0, self.zero)
        self.pino_controle.evento_both(self.D1, self.um)

        while True:
            self.obtem_status()
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
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
                    id = int(str(self.bits), 2)
                    if (len(self.bits) == 32) and (len(str(id)) == 10):
                        self.aviso.exibir_aguarda_consulta()
                        self.numero_cartao = id
                        self.util.beep_buzzer(860, .1, 1)
                        return self.numero_cartao
                    else:
                        self.util.beep_buzzer(250, .1, 3) #0 seg.
                        self.aviso.exibir_erro_leitura_cartao()
                        self.aviso.exibir_aguarda_cartao()
                        id = None
                        return id
                else:
                    return id
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro lendo cartao rfid.', exc_info=True)
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
                    self.desbroqueia_acesso()
                    sleep(4)
                    self.broqueia_acesso()
                    return None
                print self.turno
                if self.turno:
                    self.valida_cartao(self.numero_cartao)
                else:
                    self.aviso.exibir_horario_invalido()
                    self.broqueia_acesso()
                    return None
            else:
                return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro consultando numero do cartao.', exc_info=True)
        finally:
            pass
        
    def valida_cartao(self, id_cartao):
        try:
            ##############################################################
            ## CONSULTA SE O CARTAO ESTA CADASTRADO NO BANCO DE DADOS
            ##############################################################
            self.CARTAO = self.obtem_cartao(id_cartao)
            if self.CARTAO is None:
                self.util.beep_buzzer(250, .1, 3) #0 seg.
                self.aviso.exibir_cartao_nao_cadastrado()
                self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                return None
            else:
                ##############################################################
                ## OBTEM AS INFORMACOES DO CARTAO CONSULTADO NO BANCO DE DADOS
                ##############################################################
                cartao_id = self.CARTAO[0]
                cartao_numero = self.CARTAO[1]
                cartao_total_creditos = self.CARTAO[2]
                cartao_valor_tipo = self.CARTAO[3]
                cartao_limite_utilizacao = self.CARTAO[4]
                cartao_id_tipo = self.CARTAO[5]
                
#                         print ">=<>=<" * 10
#                         print cartao_id
#                         print cartao_numero
#                         print cartao_total_creditos
#                         print cartao_valor_tipo
#                         print cartao_limite_utilizacao
#                         print cartao_id_tipo
#                         print ")=<>=(" * 10

                ##############################################################
                ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                ##############################################################
                if (float(cartao_total_creditos) < float(cartao_valor_tipo)):
                    self.aviso.exibir_saldo_insuficiente()
                    self.aviso.exibir_saldo_cartao(locale.currency(float(cartao_total_creditos)).format())
                    self.util.beep_buzzer(250, .1, 3) #0 seg.
                    self.aviso.exibir_acesso_bloqueado()
                    self.log.logger.error('Cartao sem credito ID:'+ str(cartao_numero))
                    return None
                ##############################################################
                ## VERIFICA O LIMITE PERMITIDO DE USO DO CARTAO DURANTE TURNO
                ##############################################################
                elif int(self.registro_dao.busca_utilizacao(str(self.util.obtem_data()) + " " + str(self.hora_inicio), str(self.util.obtem_data()) + " " + str(self.hora_fim), cartao_id)[0]) > int(cartao_limite_utilizacao):
                    self.util.beep_buzzer(250, .1, 3) #0 seg.
                    self.aviso.exibir_cartao_utilizado()
                    self.aviso.exibir_acesso_bloqueado()
                    self.log.logger.error('Limite de uso por turno ID:'+ str(cartao_numero))
                    return None
                else:
                    ##############################################################
                    ## EXIBE O SALDO DOS CREDITOS PARA O UTILIZADOR DO CARTAO
                    ##############################################################
                    self.aviso.exibir_saldo_cartao(locale.currency(float(cartao_total_creditos)).format())
                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI ISENCAO DE PAGAMENTO
                    ##############################################################
                    saldo_creditos = 0.00
                    if self.cartao_dao.busca_isencao():
                        self.log.logger.info('Cartao isento ID:'+ str(cartao_numero))
                        saldo_creditos = float(cartao_total_creditos)
                    else:
                        saldo_creditos = float(cartao_total_creditos) - float(cartao_valor_tipo)
                    cartao = Cartao()
                    cartao.numero = cartao_numero
                    cartao.creditos = saldo_creditos
                    cartao.tipo = cartao_id_tipo
                    ##############################################################
                    ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                    ##############################################################
                    self.desbroqueia_acesso()
                    while True:
                        print "STATUS >>>> " + str( self.sensor_optico.registra_giro(self.catraca.tempo, self.catraca) )
                        if self.sensor_optico.registra_giro(self.catraca.tempo, self.catraca):                         
                            self.log.logger.info('Girou a catraca.')
                            print 'Utilizador >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIROU catraca.'
                            
#                             registro = Registro()
#                             registro.data = self.util.obtem_datahora_postgresql()
#                             registro.pago = float(cartao_valor_tipo)
#                             print float(CustoRefeicaoDAO().busca()[1])
#                             registro.custo = float(CustoRefeicaoDAO().busca()[1])
#                             registro.cartao = cartao_id
#                             registro.catraca = self.catraca.id
#                             
#                             print ">=<>=<" * 10
#                             print registro.data
#                             print registro.pago 
#                             print registro.custo
#                             print registro.cartao
#                             print registro.catraca
#                             print ">=<>=<" * 10
#                             
#                             giro = Giro()
#                             giro.horario = 1 if self.catraca.operacao == 1 else 0
#                             giro.antihorario = 1 if self.catraca.operacao == 2 else 0
#                             giro.data = registro.data
#                             giro.catraca = registro.catraca
#                             
#                             print ")=[]=(" * 10
#                             print giro.horario
#                             print giro.antihorario
#                             print giro.data
#                             print giro.catraca
#                             print ")=[]=(" * 10
                            
                            self.broqueia_acesso()
                            break
                        else:
                            self.log.logger.info('Nao girou a catraca.')
                            print "Utilizador >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NAO girou catraca."
                            
                            self.broqueia_acesso()
                            break
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro realizando operacoes de validacao no acesso.')
        finally:
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.broqueia_acesso()

    def obtem_csv(self, numero_cartao):
        with open(self.util.obtem_path('cartao.csv')) as csvfile:
            reader = csv.reader(csvfile)
            if reader:
                for row in reader:
                    if row[0] == str(numero_cartao):
                        print row[1]
                        return row[1]
                
    def obtem_cartao(self, numero):
        lista = self.cartao_dao.busca_cartao_valido(numero)
        self.CARTAO = lista
        return lista

    def broqueia_acesso(self):
        if self.catraca.operacao == 1:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.catraca.operacao == 2:
            self.solenoide.ativa_solenoide(2,0)
            self.pictograma.seta_direita(0)
            self.pictograma.xis(0)
        self.aviso.exibir_aguarda_cartao()
    
    def desbroqueia_acesso(self):
        self.util.beep_buzzer(860, .2, 1)
        if self.catraca.operacao == 1:
            self.solenoide.ativa_solenoide(1,1)
            self.pictograma.seta_esquerda(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
        if self.catraca.operacao == 2:
            self.solenoide.ativa_solenoide(2,1)
            self.pictograma.seta_direita(1)
            self.pictograma.xis(1)
        self.aviso.exibir_acesso_liberado()
        
                    