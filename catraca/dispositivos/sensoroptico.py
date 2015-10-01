#!/usr/bin/env python
# -*- coding: latin-1 -*-


import subprocess
import threading
from multiprocessing import Process
from threading import Thread
from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos.solenoide import Solenoide
from catraca.util import Util


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    log = Logs()
    util = Util()
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    solenoide = Solenoide()

    def __init__(self):
        super(SensorOptico, self).__init__()

    def ler_sensor(self, sensor):
        if sensor == 1:
            return self.rpi.estado(self.sensor_1)
        elif sensor == 2:
            return self.rpi.estado(self.sensor_2)
        
    def registra_giro(self, tempo, catraca):
        finaliza_giro = False
        tempo_giro = tempo
        # cronômetro regressivo para o giro
        try:
            for segundo in range(tempo, -1, -1):
                self.tempo_decorrido =  tempo/1000 - segundo/1000
                self.log.logger.debug(str(self.tempo_decorrido) + ' seg. restantes para expirar o tempo de giro.')
                if self.obtem_codigo_sensores() == '00':
                    self.log.logger.debug('Catraca em repouso, codigo sensores: '+ self.obtem_codigo_sensores())
                elif self.obtem_codigo_sensores() == '10':
                    self.log.logger.info('Girou a catraca no sentido '+self.obtem_direcao_giro())
                    while self.obtem_codigo_sensores() == '10':
                        self.log.logger.debug('Continuou o giro '+self.obtem_direcao_giro()+', codigo sensores: '+ self.obtem_codigo_sensores())
                    cronometro_beep = 0
                    while self.obtem_codigo_sensores() == '11':
                        self.log.logger.debug('No meio do giro '+self.obtem_direcao_giro()+', codigo sensores: '+ self.obtem_codigo_sensores())
                         
                        # giro incompleto com uso do cartao
                        #while self.sensor_optico.obtem_codigo_sensores() == '11':
                        #    if self.solenoide.obtem_estado_solenoide(1) == 1 or self.solenoide.obtem_estado_solenoide(2) == 1:
                        
                        if self.solenoide.obtem_estado_solenoide(1) == 0:
                            self.solenoide.ativa_solenoide(1,1)
                        elif self.solenoide.obtem_estado_solenoide(2) == 0:
                            self.solenoide.ativa_solenoide(2,1)

                        cronometro_beep += 1
                        if cronometro_beep/1000 >= 50: # 5seg.
                            self.util.beep_buzzer(840, 1, 1)
                            
                    while self.obtem_codigo_sensores() == '01':
                        self.log.logger.debug('Finalizando o giro '+self.obtem_direcao_giro()+', codigo sensores: '+ self.obtem_codigo_sensores())
                    if self.obtem_codigo_sensores(catraca.operacao) == '01':
                        self.log.logger.info('Giro '+self.obtem_direcao_giro()+' finalizado em '+ str(tempo_giro/1000)+' segundo(s) no codigo: '+ self.obtem_codigo_sensores())
                        finaliza_giro = True
                        return finaliza_giro
                    elif self.obtem_codigo_sensores() == '00': 
                        self.log.logger.info('Giro '+self.obtem_direcao_giro()+' finalizado em '+ str(tempo_giro/1000)+' segundo(s) no codigo: '+ self.obtem_codigo_sensores())
                        finaliza_giro = True
                        return finaliza_giro   
            if self.tempo_decorrido == tempo/1000:
                self.log.logger.info('Tempo expirado em '+ str(tempo_giro/1000)+' segundo(s) sem giro '+self.obtem_direcao_giro())
                finaliza_giro = False
                return finaliza_giro
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
        finally:
            return finaliza_giro
        
    def obtem_codigo_sensores(self):
        return str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
    
    def obtem_direcao_giro(self):
        opcoes = {
                   '10' : 'horario',
                   '01' : 'antihorario',
                   '11' : 'incompleto',
                   '00' : 'repouso',
        }
        return opcoes.get(self.obtem_codigo_sensores(), None)
    