#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import threading
from time import sleep
from threading import Thread
from catraca.logs import Logs
from catraca.util import Util
from catraca.dispositivos.leitorcartao import LeitorCartao
from catraca.dispositivos.solenoide import Solenoide
from catraca.dispositivos.sensoroptico import SensorOptico
#from catraca.pinos import PinoControle

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Alerta(Thread):
    
    log = Logs()
    util = Util()
    solenoide = Solenoide()
    sensor_optico = SensorOptico()
    leitor = LeitorCartao()
 
    def __init__(self, intervalo=1):
        super(Alerta, self).__init__()
        Thread.__init__(self)
        self.name = 'Thread Alerta(Sonoro).'
        self.intervalo = intervalo
        thread = Thread(target=self.run, args=())
        thread.daemon = True # Daemonize thread
        thread.start()

    def run(self):
        print "%s Rodando... " % self.name
        while True:
            self.verifica_giro_irregular()
            sleep(self.intervalo)

    def verifica_giro_irregular(self):
        cronometro_beep = 0

        # giro incorreto sem uso do cartao
        while self.sensor_optico.obtem_codigo_sensores() == '10' or self.sensor_optico.obtem_codigo_sensores() == '01':
            if self.solenoide.obtem_estado_solenoide(1) == 0 or self.solenoide.obtem_estado_solenoide(2) == 0:
                cronometro_beep += 1
                if cronometro_beep/1000 >= 20: # 2seg.
                    self.util.beep_buzzer(840, 1, 1)
#         # giro incompleto com uso do cartao
#         while self.sensor_optico.obtem_codigo_sensores() == '11':
#             if self.solenoide.obtem_estado_solenoide(1) == 1 or self.solenoide.obtem_estado_solenoide(2) == 1:
#                 cronometro_beep += 1
#                 if cronometro_beep/1000 >= 30: # 3seg.
#                     self.util.beep_buzzer(840, 1, 1)
#                 #print 'giro incompleto com uso do cartao'
