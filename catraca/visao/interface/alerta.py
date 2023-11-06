#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
import datetime
import calendar
import threading
from multiprocessing import Process
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.controle.dispositivos.leitorcartao import LeitorCartao
from catraca.controle.api.gerenciador import Gerenciador
from catraca.controle.dispositivos.pictograma import Pictograma


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Alerta(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    solenoide = Solenoide()
    sensor_optico = SensorOptico()
    pictograma = Pictograma()

    def __init__(self, intervalo=0.1):
        super(Alerta, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Alerta(Sonoro).'
        


    # returns the elapsed milliseconds since the start of the program
    def millis(self, *hora):
        start_time = datetime.time(12, 0, 0)
        dt = datetime.datetime.now().time() - start_time
        ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
        return ms
        
        
    def run(self):
        print "%s Rodando... " % self.name
        segundo = 0
        while not self._stopevent.isSet():
            
            segundo += 1
            if segundo == 10:
                if (self.util.obtem_datahora().time().replace(microsecond=0) == datetime.time(0, 0, 0)) or \
                (self.util.obtem_datahora().time().replace(microsecond=0) == datetime.time(12, 0, 0)) or \
                (self.util.obtem_datahora().time().replace(microsecond=0) == datetime.time(18, 0, 0)):
                    self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), str(self.util.obtem_hora()), 2)
                segundo = 0
            
            catraca = Gerenciador.catraca
            if (catraca and Gerenciador.catraca.operacao == 1) or (catraca and Gerenciador.catraca.operacao == 2) or (catraca and Gerenciador.catraca.operacao == 3) or (catraca and Gerenciador.catraca.operacao == 4) or (catraca and Gerenciador.catraca.operacao == 5):
                #print "passou inicio"
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
                    if self.sensor_optico.obtem_codigo_sensores() != "00":
                        self.define_acesso_livre()
                        self.aviso.exibir_acesso_livre()
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
                            
                self.verifica_giro_irregular(catraca)
                
            else:
                if self.sensor_optico.obtem_codigo_sensores() != "00":
                    self.define_bloqueio_total()
                    self.aviso.exibir_bloqueio_total()
                    
            Gerenciador.uso_irregular = False
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % self.getName()
            
    def define_acesso_livre(self):
        try:
            if not self.solenoide.obtem_estado_solenoide(2):
                self.solenoide.ativa_solenoide_individual(2,1)
            if not self.solenoide.obtem_estado_solenoide(1):
                self.solenoide.ativa_solenoide_individual(1,1)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def define_bloqueio_total(self):
        try:
            if self.solenoide.obtem_estado_solenoide(2):
                self.solenoide.ativa_solenoide(2,0)
            if self.solenoide.obtem_estado_solenoide(1):
                self.solenoide.ativa_solenoide(1,0)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
  
    def verifica_giro_inverso(self, catraca):
        try:
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
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
           
    def verifica_meio_giro(self):
        ##############################################################
        ## VERIFICA SE A CATRACA SE ENCONTRA EM MEIO GIRO
        ##############################################################
        while self.sensor_optico.obtem_codigo_sensores() == "11":
            Gerenciador.uso_irregular = True
            self.util.beep_buzzer_delay(860, 1, 1, 40)
            if self.util.cronometro/1000 == 40:
                self.aviso.exibir_uso_incorreto()
                self.util.cronometro = 0
        self.util.cronometro = 0
        
    def verifica_giro_irregular(self, catraca):
        try:
            if catraca.operacao == 1 or catraca.operacao == 2 or catraca.operacao <= 0 or catraca.operacao >= 6:
                while (self.sensor_optico.obtem_direcao_giro() == 'horario' and self.solenoide.obtem_estado_solenoide(1) == 0) or \
                       (self.sensor_optico.obtem_direcao_giro() == 'antihorario' and  self.solenoide.obtem_estado_solenoide(2) == 0):
                    if (self.sensor_optico.obtem_codigo_sensores() == "01") or (self.sensor_optico.obtem_codigo_sensores() == "10"):
                        Gerenciador.uso_irregular = True
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
                            Gerenciador.uso_irregular = True
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
                            Gerenciador.uso_irregular = True
                            self.util.beep_buzzer_delay(860, 1, 1, 10)
                            if self.util.cronometro/1000 == 10:
                                self.aviso.exibir_uso_incorreto()
                                self.util.cronometro = 0
                        else:
                            break
                                   
            self.verifica_meio_giro()
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        