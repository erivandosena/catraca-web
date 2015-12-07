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
    status_alerta = False
 
    def __init__(self, intervalo=1):
        super(Alerta, self).__init__()
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Alerta(Sonoro).'
#         thread = threading.Thread(group=None, target=self.run(), name=None, args=(), kwargs={})
#         thread.daemon = False
#         thread.start()
        
    def run(self):
        print "%s Rodando... " % self.name
        while True:
            if self.status_alerta:
                self.status_alerta = False
                self.aviso.exibir_aguarda_cartao()
            self.verifica_giro_irregular()
            sleep(self.intervalo)

    def verifica_giro_irregular(self):
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
 

                  