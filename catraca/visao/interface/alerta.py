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
    status_alerta = False
    catraca = None
    
    def __init__(self, intervalo=1):
        super(Alerta, self).__init__()
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Alerta(Sonoro).'
        
    def run(self):
        print "%s Rodando... " % self.name
        mensagens = Mensagem()
        while True:
#             if self.solenoide.obtem_estado_solenoide(2) == 0:
#                 self.solenoide.ativa_solenoide(2,1)
#                 print "SOLENOIDE ATIVADO"
                
            if self.status_alerta:
                self.status_alerta = False
                self.aviso.exibir_aguarda_cartao()
            self.verifica_giro_irregular()
            
            # trata exibicao de mensagens padroes quando nao houver turno ativo
            if not Relogio.periodo:
                # durante a leitura de um cartao
                if LeitorCartao.uso_do_cartao:
                    if mensagens.isAlive():
                        mensagens.join()
                else:
                    if not mensagens.isAlive():
                        mensagens = Mensagem()
                        mensagens.start()
                # durante a sincronizacao da catraca com o servidor RESTful
                if RecursosRestful.obtendo_recurso:
                    if mensagens.isAlive():
                        mensagens.join()
                else:
                    if not mensagens.isAlive():
                        mensagens = Mensagem()
                        mensagens.start()

            #sleep(self.intervalo)

    def verifica_giro_irregular(self):
        self.catraca = Relogio().obtem_catraca()
        if self.catraca.operacao == 1 or self.catraca.operacao == 2:
#             if self.solenoide.obtem_estado_solenoide(2) == 1:
#                 self.solenoide.ativa_solenoide(2,0)
#                 print "SOLENOIDE DESATIVADO"
            while (self.sensor_optico.obtem_direcao_giro() == 'horario' and \
                   self.solenoide.obtem_estado_solenoide(1) == 0) or \
                   (self.sensor_optico.obtem_direcao_giro() == 'antihorario' and \
                    self.solenoide.obtem_estado_solenoide(2) == 0):
                if (self.sensor_optico.obtem_codigo_sensores() == "01") or (self.sensor_optico.obtem_codigo_sensores() == "10"):
                    if self.util.cronometro == 0:
                        self.aviso.exibir_uso_incorreto()
                        self.status_alerta = True
                    self.util.beep_buzzer_delay(860, 1, 1, 5) #15 = 5 seg
                    if self.util.cronometro/1000 == 5:
                        self.util.cronometro = 0
                else:
                    break
        # horario/livre
        if self.catraca.operacao == 3:
            if self.sensor_optico.obtem_codigo_sensores() == "10":
                self.solenoide.ativa_solenoide(2,0)
                while (self.sensor_optico.obtem_direcao_giro() == 'horario' and self.solenoide.obtem_estado_solenoide(1) == 0):
                    self.solenoide.ativa_solenoide(2,0)
                    if (self.sensor_optico.obtem_codigo_sensores() == "10"):
                        if self.util.cronometro == 0:
                            self.aviso.exibir_uso_incorreto()
                            self.status_alerta = True
                        self.util.beep_buzzer_delay(860, 1, 1, 5) #15 = 5 seg
                        if self.util.cronometro/1000 == 5:
                            self.util.cronometro = 0
                    else:
                        break

            if self.sensor_optico.obtem_codigo_sensores() == "01":
                self.solenoide.ativa_solenoide(2,1)
                self.pictograma.seta_direita(1)
                self.aviso.exibir_acesso_liberado()
                while (self.sensor_optico.obtem_codigo_sensores() == "01" or self.sensor_optico.obtem_codigo_sensores() == "11"):
                    if self.pictograma.obtem_estado_pictograma("x") == 0:
                        self.pictograma.xis(1)
                self.bloqueia_acesso()
                
    def desbloqueia_acesso(self):
        self.solenoide.ativa_solenoide(2,1)
        self.pictograma.seta_direita(1)
        self.pictograma.xis(0)
        self.aviso.exibir_acesso_liberado()
        
    def bloqueia_acesso(self):
        self.solenoide.ativa_solenoide(2,0)
        self.pictograma.seta_direita(0)
        self.pictograma.xis(0)
        self.aviso.exibir_acesso_bloqueado()
        
    def detecta_solenoide(self, num_solenoide):
        pino_solenoide_1 = self.solenoide.gpio_solenoide1
        pino_solenoide_2 = self.solenoide.gpio_solenoide2
        if num_solenoide == 1:
            pass
        
        