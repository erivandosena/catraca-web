#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import locale
import datetime
import threading
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.pictograma import Pictograma
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.giro_dao import GiroDAO
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.entidades.registro_off import RegistroOff
from catraca.modelo.entidades.giro import Giro
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.controle.restful.recursos_restful import RecursosRestful
from catraca.controle.restful.relogio import Relogio


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(Relogio, threading.Thread):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
#     log = Logs()
#     util = Util()
#     aviso = Aviso()
    rpi = PinoControle()
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    giro = Giro()
    cartao = Cartao()
    registro = Registro()
    giro_dao = GiroDAO()
#     turno_dao = TurnoDAO()
    cartao_dao = CartaoDAO()
    catraca_dao = CatracaDAO()
    registro_dao = RegistroDAO()
    custo_refeicao_dado = CustoRefeicaoDAO()

    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    
    bits = '' #11101110000100010000010011101110
    numero_cartao = None
    giro = []
#     turno = []
    cartoes = []
    TURNO = []
    CARTAO = []
    CATRACA = None
#     hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
#     hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
#     hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    contador = 30
    
    def __init__(self, intervalo=1):
        super(LeitorCartao, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread LeitorCartao'
        thread = threading.Thread(target=self.run(), args=())
        thread.daemon = True # Daemonize thread
        #self.aviso.exibir_aguarda_sincronizacao()
        #self.aviso.exibir_aguarda_cartao()
        
    def run(self):
        print "%s. Rodando... " % self.name
        while True:
#             if self.periodo:
#                 print self.periodo
#                 self.TURNO = self.turno
#                 print self.TURNO
#                 self.CATRACA = self.catraca
#                 print self.CATRACA
            #self.ler()
            print self.obtem_numero_cartao_rfid()
            sleep(self.intervalo)
    
    def zero(self, obj):
        self.bits = self.bits + '0'
    
    def um(self, obj):
        self.bits = self.bits + '1'
        
    def obtem_numero_cartao_rfid(self):
        id = None
        try:
            self.rpi.evento_rising_ou_falling(self.D0, self.zero)
            self.rpi.evento_rising_ou_falling(self.D1, self.um)
            while True:
                #sleep(1)
                if self.bits:
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
                    print self.bits
                    id = int(str(self.bits), 2)
                    if (len(self.bits) == 32) and (len(str(id)) == 10):
                        self.numero_cartao = id
                        self.util.beep_buzzer(860, .1, 1)
                        #self.aviso.exibir_aguarda_consulta()
                        return self.numero_cartao
                    else:
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
            while True:
                print self.obtem_numero_cartao_rfid()
#                 if self.obtem_numero_cartao_rfid():
# 
#                     self.util.beep_buzzer(860, .1, 1)
# #                     self.aviso.exibir_aguarda_consulta()
#  
#                     csv = self.obtem_csv(self.numero_cartao)
#                     if csv == "Reiniciar Catraca":
#                         self.util.reinicia_raspberrypi()
#                     if csv == "Desligar Catraca":
#                         self.util.desliga_raspberrypi()
#                          
#                     print "consultando... "+ str(self.numero_cartao)  
#                     self.valida_cartao(self.numero_cartao)
#                      
#                 else:
#                     self.util.emite_beep(250, .1, 3, 0) #0 seg.
#                     self.log.logger.error('Erro obtendo binario: '+str(self.bits))
#                     #self.aviso.exibir_erro_leitura_cartao()
#                     #self.aviso.exibir_aguarda_cartao()
#                     return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro consultando numero do cartao.', exc_info=True)
        finally:
            self.gpio.limpa()
            pass
#             self.numero_cartao = 0
#             self.bits = ''
#             pass
#             slf.bits = ''
#             self.numero_caertao = 0
        
#     def ler(self):
#         try:            
#             self.rpi.evento_falling(self.D0, self.zero)
#             self.rpi.evento_falling(self.D1, self.um)
#             while True:
#                 sleep(1)
# 
#                 if self.periodo is None:
#                     print "ATENÇÃO: Nao existem Turnos cadastrados para funcionamento da catraca!"
#                 else:
#                     self.TURNO = self.turno
#                     self.CATRACA = self.catraca
#                 #sleep(self.intervalo)# delay de 1 segundo
#                  
#                 #self.bits = '11101110000100010000010011101110'
#                 if len(self.bits) == 32:
#                     self.util.beep_buzzer(860, .1, 1)
#                     self.aviso.exibir_aguarda_consulta()
#                     self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
#                     self.numero_cartao = int(str(self.bits), 2)
#                     self.bits = ''
#                     csv = self.obtem_csv(self.numero_cartao)
#                     if csv == "Reiniciar Catraca":
#                         self.util.reinicia_raspberrypi()
#                     if csv == "Desligar Catraca":
#                         self.util.desliga_raspberrypi()
#                     self.valida_cartao(self.numero_cartao)
#                 elif (len(self.bits) > 0) or (len(self.bits) > 32):
#                     self.util.emite_beep(250, .1, 3, 0) #0 seg.
#                     self.log.logger.error('Erro obtendo binario: '+str(self.bits))
#                     self.numero_cartao = 0
#                     self.bits = ''
#                     self.aviso.exibir_erro_leitura_cartao()
#                     self.aviso.exibir_aguarda_cartao()
#                 self.numero_cartao = 0
#                 self.bits = ''
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception, e:
#             self.log.logger.error('Erro lendo cartao.', exc_info=True)
#         finally:
#             pass
# #             self.bits = ''
# #             self.numero_cartao = 0

    def valida_cartao(self, id_cartao):
        #self.hora_atual = self.util.obtem_hora()
        print "ID CARTAO +++++++++++++++++++++++++++++++++++++++++++++++++++++: "+ str(id_cartao)
        try:
            ##############################################################
            ## VERIFICA SE EXISTE TURNO NO HORARIO DE FUNCIONAMENTO
            ############################################################## 
            if self.TURNO is not []:
                ##############################################################
                ## CONSULTA SE O CARTAO ESTA CADASTRADO NO BANCO DE DADOS
                ##############################################################
                self.CARTAO = self.obtem_cartao(id_cartao)
                print "CARTAO OBTIDO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: "
                print self.CARTAO
                print "CARTAO OBTIDO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: "
                if self.CARTAO == []:
                    self.util.emite_beep(250, .1, 3, 0) #0 seg.
                    self.aviso.exibir_cartao_nao_cadastrado()
                    self.aviso.exibir_aguarda_cartao()
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
                    
                    print ">=<>=<" * 20
                    print cartao_id
                    print cartao_numero
                    print cartao_total_creditos
                    print cartao_valor_tipo
                    print cartao_limite_utilizacao
                    print cartao_id_tipo
                    print ")=<>=(" * 20

                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                    ##############################################################
                    if (float(cartao_total_creditos) < float(cartao_valor_tipo)):
                        self.aviso.exibir_cartao_sem_saldo()
                        self.util.emite_beep(250, .1, 3, 0) #0 seg.
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Cartao sem credito ID:'+ str(cartao_numero))
                        return None
                    ##############################################################
                    ## VERIFICA O LIMITE PERMITIDO DE USO DO CARTAO DURANTE TURNO
                    ##############################################################
                    elif int(self.registro_dao.busca_utilizacao(str(self.util.obtem_data()) + " " + str(self.hora_inicio), str(self.util.obtem_data()) + " " + str(self.hora_fim), cartao_id)[0]) > int(cartao_limite_utilizacao):
                        print self.registro_dao.busca_utilizacao(str(self.util.obtem_data()) + " " + str(self.hora_inicio), str(self.util.obtem_data()) + " " + str(self.hora_fim), cartao_id)[0]
                        print self.util.obtem_data() + " " + str(self.hora_inicio)
                        print self.util.obtem_data() + " " + str(self.hora_fim)
                        #self.aviso.exibir_cartao_sem_saldo()
                        self.util.emite_beep(250, .1, 3, 0) #0 seg.
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Limite de uso por turno ID:'+ str(cartao_numero))
                        return None
                    else:
                        ##############################################################
                        ## EXIBE O SALDO DOS CREDITOS PARA O UTILIZADOR DO CARTAO
                        ##############################################################
                        self.aviso.exibir_cartao_valido("  R$ "+str(float(cartao_total_creditos))+"")
                        ##############################################################
                        ## VERIFICA SE O CARTAO POSSUI ISENCAO DE PAGAMENTO
                        ##############################################################
                        saldo_creditos = 0.00
                        if self.cartao_dao.busca_isencao():
                            self.log.logger.info('Cartao isento ID:'+ str(cartao_numero))
                            saldo_creditos = float(cartao_total_creditos)
                        else:
                            saldo_creditos = float(cartao_total_creditos) - float(cartao_valor_tipo)
                        self.cartao.numero = cartao_numero
                        self.cartao.creditos = saldo_creditos
                        self.cartao.tipo = cartao_id_tipo
                        self.aviso.exibir_aguarda_liberacao()
                        ##############################################################
                        ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        #self.desbroqueia_acesso()
                        print "self.desbroqueia_acesso() =>"
                        ##############################################################
                        ## AGUARDA UTILIZADOR PASSAR NA CATRACA E REALIZAR O GIRO
                        ##############################################################
                        while True:
#                             print self.sensor_optico.registra_giro(self.catraca.tempo, self.catraca)
#                             print "%.2f" % round(self.sensor_optico.tempo_decorrido, 2)
#                             break
#                             print self.sensor_optico.finaliza_giro
                            if self.sensor_optico.registra_giro(self.CATRACA.tempo, self.CATRACA):                                
                                self.log.logger.info('Utilizador REALIZOU GIRO na catraca.')
                                print 'Utilizador REALIZOU GIRO na catraca.'
#                                 ############################################################
#                                  EFETIVA A OPERACAO DE DECREMENTO DE CREDITO DO CARTAO
#                                 ############################################################
                                ##############################################################
                                ## ENVIA ATUALIZACAO DE CREDITO DO CARTAO PARA O SERVIDOR REST
                                ##############################################################
                                
                                
#                                 if not CartaoJson().objeto_json(self.cartao):
#                                     if not self.cartao_dao.mantem_cartao_off(self.cartao,False):
#                                         self.log.logger.error('[Cartao Off] ' + self.cartao_dao.aviso)
#                                         #raise Exception('Erro atualizando valores no cartao off.')
#                                     else:
#                                         self.log.logger.info("[Cartao Off] " + self.cartao_dao.aviso)
                                        
                                        
                                ##############################################################
                                ## REGISTRA INFORMACOES DA OPERACAO REALIZADA COM EXITO
                                ##############################################################
                                ##############################################################
                                ## ENVIA REGISTRO DE USO DO CARTAO PARA O SERVIDOR REST
                                ##############################################################
                                
#                                 self.registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                                 self.registro.pago = cartao_valor_tipo
#                                 self.registro.custo = self.custo_refeicao_dado.busca().valor
#                                 self.registro.cartao = CartaoDAO().busca(cartao_id)
#                                 self.registro.turno = TurnoDAO().busca(TURNO[0])
#                                 self.registro.catraca = self.CATRACA
#                                 if not RegistroJson().objeto_json(self.registro):
#                                     if not self.registro_dao.mantem_registro_off(self.registro,False):
#                                         self.log.logger.error('[Registro Off] ' + self.registro_dao.aviso)
#                                         #raise Exception('Erro atualizando valores no registro off.')
#                                     else:
#                                         self.log.logger.info("[Registro Off] " + self.registro_dao.aviso)
                                        
                                ##############################################################
                                ## REGISTRA INFORMACOES DE GIRO REALIZADO NA CATRACA
                                ##############################################################   
                                ##############################################################
                                ## ENVIA REGISTRO DE GIRO DA CATRACA PARA O SERVIDOR REST
                                ##############################################################
                                
                                
#                                 self.giro.horario = 1 if self.CATRACA.operacao == 1 else 0
#                                 self.giro.antihorario = 1 if self.CATRACA.operacao == 2 else 0
#                                 self.giro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                                 self.giro.catraca = self.CATRACA
#                                 if not RegistroJson().objeto_json(self.registro):
#                                     if not self.registro_dao.mantem_registro_off(self.registro,False):
#                                         self.log.logger.error('[Giro Off] ' + self.registro_dao.aviso)
#                                         #raise Exception('Erro atualizando valores no giro off.')
#                                     else:
#                                         self.log.logger.info("[Giro Off] " + self.registro_dao.aviso)               
                                break
                            else:
                                self.log.logger.info('Utilizador NAO realizou GIRO na catraca.')
                                print "Utilizador NAO realizou GIRO na catraca."
#                                 self.cartao = None
#                                 self.registro = None
#                                 self.giro = None
                                break
#                             print self.sensor_optico.finaliza_giro
                        ##############################################################
                        ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        self.broqueia_acesso()
                        ##############################################################
                        ## VERIFICA ATUALIZACOES NO TURNO DE FUNCIONAMENTO
                        ##############################################################
                        #self.obtem_catraca()
                        #self.obtem_turno()
                        #UsuarioJson().usuario_get()
                        #TipoJson().tipo_get()
                        #CartaoJson().cartao_get()
                        #VinculoJson().vinculo_get()        
            else:
                ##############################################################
                ## CANCELA ACESSO PELA INVALIDADE DO ID DO CARTAO APRESENTADO
                ##############################################################
                print "Fora do turno!"
                self.log.logger.info('Cartao apresentado fora do horario de atendimento')
                return None
        except SystemExit, KeyboardInterrupt:
            raise
#         except Exception:
#             self.log.logger.error('Erro realizando operacoes de validacao no acesso.')
#             if self.cartao_dao.conexao_status():
#                 self.cartao_dao.rollback()
#                 self.log.logger.info("Alteracao no cartao cancelada! (rollback)")
        finally:
            self.bits = ''
            self.numero_cartao = 0
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.broqueia_acesso()
            ##############################################################
            ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
            ##############################################################
            self.aviso.exibir_aguarda_cartao()
            ##############################################################
            ## FECHA POSSIVEIS CONEXOES ABERTAS COM O BANCO DE DADOS
            ##############################################################
            if self.cartao_dao.conexao_status():
                self.cartao_dao.fecha_conexao()
                self.log.logger.debug('[Cartao] Conexao finalizada com o BD.')
            if self.registro_dao.conexao_status():
                self.registro_dao.fecha_conexao()
                self.log.logger.debug('[Registro] Conexao finalizada com o BD.')
            if self.giro_dao.conexao_status():
                self.giro_dao.fecha_conexao()
                self.log.logger.debug('[Giro] Conexao finalizada com o BD.')
                     
    def obtem_recursos_do_servidor(self):
        RecursosRestful().obtem_recursos()

    def obtem_catraca(self):
        IP = Util().obtem_ip()
        self.CATRACA = self.catraca_dao.busca_por_ip(IP)
               
#     def obtem_turno(self):   
#         self.TURNO = self.turno_dao.busca_por_catraca(self.CATRACA)
#         if self.TURNO:
#             self.TURNO.sort()
#             for turno in self.TURNO:
#                 self.hora_atual = self.util.obtem_hora()
#                 self.hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
#                 self.hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
#                 if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
#                     return turno
#                     break
#             return None
    
    def obtem_cartao(self, numero):
        lista = self.cartao_dao.busca_cartao_valido(numero)
        self.CARTAO = lista
        return lista

#     def verifica_turnos(self):
#         self.catraca = self.obtem_catraca()
#         self.turno = self.obtem_turno(self.catraca)
#         self.turno_atual = self.turno_dao.busca(self.turno[0]) if self.turno != None else None #Op. ternario
    
    def broqueia_acesso(self):
        if self.CATRACA.operacao == 1:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.CATRACA.operacao == 2:
            self.solenoide.ativa_solenoide(2,0)
            self.pictograma.seta_direita(0)
            self.pictograma.xis(0)
        ##############################################################
        ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
        ##############################################################
        self.aviso.exibir_aguarda_cartao()
    
    def desbroqueia_acesso(self):
        self.util.beep_buzzer(950, .1, 2)
        if self.CATRACA.operacao == 1:
            self.solenoide.ativa_solenoide(1,1)
            self.pictograma.seta_esquerda(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
        if self.CATRACA.operacao == 2:
            self.solenoide.ativa_solenoide(2,1)
            self.pictograma.seta_direita(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
            
    def obtem_csv(self, numero_cartao):
        with open(Util().obtem_path('cartao.csv')) as csvfile:
            reader = csv.reader(csvfile)
            if reader:
                for row in reader:
                    if row[0] == str(numero_cartao):
                        print row[1]
                        return row[1]
                    