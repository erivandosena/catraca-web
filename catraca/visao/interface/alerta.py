#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
from multiprocessing import Process
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.controle.dispositivos.leitorcartao import LeitorCartao
from catraca.visao.interface.mensagem import Mensagem
from catraca.controle.restful.relogio import Relogio
from catraca.controle.restful.recursos_restful import RecursosRestful
from catraca.controle.dispositivos.pictograma import Pictograma


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production 


class Alerta(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    solenoide = Solenoide()
    sensor_optico = SensorOptico()
    pictograma = Pictograma()
    mensagem_final = 0
    exibicao = False
    mensagens = Mensagem()

    def __init__(self, intervalo=0.1):
        super(Alerta, self).__init__()
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Alerta(Sonoro).'
        
    def run(self):
        print "%s Rodando... " % self.name
        #mensagens = Mensagem()
        while True:
            catraca = Relogio.catraca
            if catraca:
                # quando nao houver leitura de cartao em andamento
                if not LeitorCartao.uso_do_cartao:
                    if catraca.operacao == 1 or catraca.operacao == 2:
                        if self.sensor_optico.obtem_codigo_sensores() != "00":
                            if self.solenoide.obtem_estado_solenoide(2):
                                self.solenoide.ativa_solenoide(2,0)
                            if self.solenoide.obtem_estado_solenoide(1):
                                self.solenoide.ativa_solenoide(1,0)
                                
                    if catraca.operacao == 3:
                        if self.sensor_optico.obtem_codigo_sensores() != "00":
                            if not self.solenoide.obtem_estado_solenoide(2):
                                self.solenoide.ativa_solenoide(2,1)
                            if self.solenoide.obtem_estado_solenoide(1):
                                self.solenoide.ativa_solenoide(1,0)

                            self.pictograma.xis(1)
                            if self.sensor_optico.obtem_codigo_sensores() == "01":
                                
                                self.pictograma.seta_direita(1)
                                self.aviso.exibir_acesso_liberado()
                                self.verifica_giro_inverso(catraca)
                            
                            self.pictograma.xis(0)
                            
                    if catraca.operacao == 4:
                        if self.sensor_optico.obtem_codigo_sensores() != "00":
                            if not self.solenoide.obtem_estado_solenoide(1):
                                self.solenoide.ativa_solenoide(1,1)
                            if self.solenoide.obtem_estado_solenoide(2):
                                self.solenoide.ativa_solenoide(2,0)
                                
                            self.pictograma.xis(1)
                            if self.sensor_optico.obtem_codigo_sensores() == "10":
                                
                                self.pictograma.seta_esquerda(1)
                                self.aviso.exibir_acesso_liberado()
                                self.verifica_giro_inverso(catraca)

                            self.pictograma.xis(0)
                            
                if catraca.operacao == 5:
                    self.mensagem_final = 5
                    if self.sensor_optico.obtem_codigo_sensores() != "00":
                        
                        self.exibicao = False
                        
                        self.define_acesso_livre()
                            
                        if not self.exibicao:
                            self.aviso.exibir_acesso_livre()
                            self.exibicao = True
                            
                        if self.sensor_optico.obtem_codigo_sensores() == "01":
                            self.pictograma.seta_direita(1)
                            while self.sensor_optico.detecta_giro_completo(self.sensor_optico.obtem_codigo_sensores()):
                                self.verifica_meio_giro()
                            self.pictograma.seta_direita(0)
                        if self.sensor_optico.obtem_codigo_sensores() == "10":
                            self.pictograma.seta_esquerda(1)
                            while self.sensor_optico.detecta_giro_completo(self.sensor_optico.obtem_codigo_sensores()):
                                self.verifica_meio_giro()
                            self.pictograma.seta_esquerda(0)
                                
                if catraca.operacao <= 0 or catraca.operacao >= 6:
                    self.mensagem_final = 6
                    if self.sensor_optico.obtem_codigo_sensores() != "00":
                        self.exibicao = False
                        
                        self.define_bloqueio_total()
                            
                        if not self.exibicao:
                            self.aviso.exibir_bloqueio_total()
                            self.exibicao = True
                            
                self.verifica_giro_irregular(catraca)
                    
                # trata exibicao de mensagens padroes quando nao houver turno ativo
                # trata exibicao de mensagens padroes quando o tipo de giro definido for igual a 5
                # trata exibicao de mensagens padroes quando o tipo de giro definido nao for igual a 1,2,3,4,5
                # trata exibicao de mensagens durante a sincronizacao da catraca com o servidor RESTful
                # trata exibicao de mensagens se a catraca retornar vazio(None)
                if not Relogio.periodo or catraca.operacao == 5 or catraca.operacao <= 0 or catraca.operacao >= 6 or RecursosRestful.obtendo_recurso:
                    # durante a leitura de um cartao
                    if LeitorCartao.uso_do_cartao:
                        if self.mensagens.isAlive():
                            self.exibicao = False
                            self.mensagens.join()
                    else:
                        if not self.mensagens.isAlive():
                            self.mensagens = Mensagem()
                            self.mensagens.start()
                else:
                    self.mensagem_final = 1
                    if self.mensagens.isAlive():
                        self.exibicao = False
                        self.mensagens.join()
                        
                if self.mensagem_final == 1:
                    if not self.exibicao:
                        self.exibicao = True
                        self.aviso.exibir_aguarda_cartao()
                if self.mensagem_final == 5:
                    if not self.exibicao:
                        self.aviso.exibir_acesso_livre()
                        self.exibicao = True
                if self.mensagem_final == 6:
                    if not self.exibicao:
                        self.exibicao = True
                        self.aviso.exibir_bloqueio_total()
                        
            else:
                self.mensagem_final = 6
                
                if not self.exibicao:
                    self.aviso.exibir_bloqueio_total()
                    self.exibicao = True
                    
                if catraca is None:
                    if not self.mensagens.isAlive():
                        self.mensagens = Mensagem()
                        self.mensagens.start()
                else:
                    if self.mensagens.isAlive():
                        self.exibicao = False
                        self.mensagens.join()
                
                if self.sensor_optico.obtem_codigo_sensores() != "00":
                    self.exibicao = False
                    
                    self.define_bloqueio_total()
                    
                    if not self.exibicao:
                        self.aviso.exibir_bloqueio_total()
                        self.exibicao = True
                        
            sleep(self.intervalo)
            
    def define_acesso_livre(self):
        if not self.solenoide.obtem_estado_solenoide(2):
            self.solenoide.ativa_solenoide_individual(2,1)
        if not self.solenoide.obtem_estado_solenoide(1):
            self.solenoide.ativa_solenoide_individual(1,1)
            
    def define_bloqueio_total(self):
        if self.solenoide.obtem_estado_solenoide(2):
            self.solenoide.ativa_solenoide(2,0)
        if self.solenoide.obtem_estado_solenoide(1):
            self.solenoide.ativa_solenoide(1,0)
  
    def verifica_giro_inverso(self, catraca):
        if catraca.operacao == 3 and self.pictograma.obtem_estado_pictograma('esquerda') == 0:
            if self.solenoide.obtem_estado_solenoide(2):
                while self.sensor_optico.detecta_giro_completo(self.sensor_optico.obtem_codigo_sensores()):
                    self.verifica_meio_giro()
                self.pictograma.seta_direita(0)
                
        if catraca.operacao == 4 and self.pictograma.obtem_estado_pictograma('direita') == 0:
            if self.solenoide.obtem_estado_solenoide(1):
                while self.sensor_optico.detecta_giro_completo(self.sensor_optico.obtem_codigo_sensores()):
                    self.verifica_meio_giro()
                self.pictograma.seta_esquerda(0)
                
        self.pictograma.xis(0)
        self.aviso.exibir_acesso_bloqueado()
        self.exibicao = False
            
    def verifica_meio_giro(self):
        ##############################################################
        ## VERIFICA SE A CATRACA SE ENCONTRA EM MEIO GIRO
        ##############################################################
        while self.sensor_optico.obtem_codigo_sensores() == "11":
            
#             if self.mensagens.isAlive():
#                 self.exibicao = False
#                 self.mensagens.join()
                
            self.util.beep_buzzer_delay(860, 1, 1, 40)
            if self.util.cronometro/1000 == 40:
                self.aviso.exibir_uso_incorreto()
                self.util.cronometro = 0
        self.util.cronometro = 0
        
    def verifica_giro_irregular(self, catraca):
        if catraca.operacao == 1 or catraca.operacao == 2 or catraca.operacao <= 0 or catraca.operacao >= 6:
            while (self.sensor_optico.obtem_direcao_giro() == 'horario' and self.solenoide.obtem_estado_solenoide(1) == 0) or \
                   (self.sensor_optico.obtem_direcao_giro() == 'antihorario' and  self.solenoide.obtem_estado_solenoide(2) == 0):
                if (self.sensor_optico.obtem_codigo_sensores() == "01") or (self.sensor_optico.obtem_codigo_sensores() == "10"):
#                     if self.util.cronometro == 0:
#                         self.status_alerta = True
                    self.util.beep_buzzer_delay(860, 1, 1, 10)
                    if self.util.cronometro/1000 == 10:
                        self.aviso.exibir_uso_incorreto()
                        self.util.cronometro = 0
                else:
                    break
                 
        if catraca.operacao == 3:
            if self.sensor_optico.obtem_codigo_sensores() == "10":
                while (self.sensor_optico.obtem_direcao_giro() == 'horario' and self.solenoide.obtem_estado_solenoide(1) == 0):
                    if (self.sensor_optico.obtem_codigo_sensores() == "10"):
#                         if self.util.cronometro == 0:
#                             self.status_alerta = True
                        self.util.beep_buzzer_delay(860, 1, 1, 10)
                        if self.util.cronometro/1000 == 10:
                            self.aviso.exibir_uso_incorreto()
                            self.util.cronometro = 0
                    else:
                        break
                    
        if catraca.operacao == 4:
            if self.sensor_optico.obtem_codigo_sensores() == "01":
                while (self.sensor_optico.obtem_direcao_giro() == 'antihorario' and self.solenoide.obtem_estado_solenoide(2) == 0):
                    if (self.sensor_optico.obtem_codigo_sensores() == "01"):
#                         if self.util.cronometro == 0:
#                             self.status_alerta = True
                        self.util.beep_buzzer_delay(860, 1, 1, 10)
                        if self.util.cronometro/1000 == 10:
                            self.aviso.exibir_uso_incorreto()
                            self.util.cronometro = 0
                    else:
                        break
                               
        self.verifica_meio_giro()
        
        
        