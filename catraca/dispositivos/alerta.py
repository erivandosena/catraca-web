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
        self.util.cronometro = 0
        #print self.sensor_optico.obtem_codigo_sensores()
        while (self.sensor_optico.obtem_direcao_giro() == 'horario' and \
            self.solenoide.obtem_estado_solenoide(1) == 0) or \
            (self.sensor_optico.obtem_direcao_giro() == 'antihorario' and \
            self.solenoide.obtem_estado_solenoide(2) == 0):
            self.util.emite_beep(860, 1, 1, 15) #15 = 1.5 seg

            