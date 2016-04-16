#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
import subprocess
import threading
from multiprocessing import Process
from threading import Thread
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from _ast import While
from __builtin__ import True


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    log = Logs()
    util = Util()
    aviso = Aviso()
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    solenoide = Solenoide()
    tempo_decorrido = 0
    tempo_decorrente = 0
    finaliza_giro = False
    status_alerta = False
    tempo = 0

    def __init__(self):
        super(SensorOptico, self).__init__()

    def ler_sensor(self, sensor):
        if sensor == 1:
            return self.rpi.estado(self.sensor_1)
        elif sensor == 2:
            return self.rpi.estado(self.sensor_2)
        
    def registra_giro(self, tempo, catraca):
        #tempo = tempo*1000
#         confirma_giro_completo = ''
#         codigo_giro_completo = ''
#         giro = None
        giro = self.obtem_codigo_sensores()
        contragiro = self.obtem_codigo_sensores()
        try:
            while self.tempo < tempo*tempo:
                self.tempo +=1
                #print str(self.tempo) + " de "+ str(tempo*tempo)
                
                if catraca.operacao == 1 or catraca.operacao == 2:
                    
                    giro = self.obtem_codigo_sensores()
                    giro += self.obtem_codigo_sensores()
                    print giro[0:8]
                    
                    if self.obtem_codigo_sensores() != "00":
                        
                        giro = giro[0:2]    
                        giro += self.obtem_codigo_sensores()
                        while self.obtem_codigo_sensores() == "01" or self.obtem_codigo_sensores() == "10" or self.obtem_codigo_sensores() == "11":
                            
                            giro = giro[0:4]
                            giro += self.obtem_codigo_sensores()
                            print giro[0:6]
                            
#                         giro = giro[0:6]
#                         giro += self.obtem_codigo_sensores()
#                         print giro[0:8]
                        
                    if catraca.operacao == 1 and giro[0:8] == "10100100":
                        return True
                    if catraca.operacao == 2 and giro[0:8] == "10100100":
                        return True
                    
                sleep(0.1)
            return False
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
        finally:
            self.tempo = 0
            #giro = self.obtem_codigo_sensores()
#             self.tempo_decorrente = 0
#             confirma_giro_completo = ''
#             codigo_giro_completo = ''
#             giro = None
#             return self.finaliza_giro

    def obtem_codigo_sensores(self):
        return str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
    
    def detecta_giro_completo(self, codigo_sensores):
        retorno = True
        if codigo_sensores != "10" or codigo_sensores != "01":
            if codigo_sensores != "11":
                if codigo_sensores == "00":
                    retorno = False
            return retorno
    
    def obtem_direcao_giro(self):
        opcoes = {
                   '10' : 'horario',
                   '01' : 'antihorario',
                   '11' : 'incompleto',
                   '00' : 'repouso',
        }
        return opcoes.get(self.obtem_codigo_sensores(), None)
    
    def obtem_giro_iniciado(self, modo_operacao):
        opcoes = {
                   'horario' : 1,
                   'antihorario' : 2,
        }
        return opcoes.get(modo_operacao, None)
   
    def cronometro_tempo(self, tempo_decorrido, tempo, milissegundos):
        self.tempo_decorrente += milissegundos
        if tempo_decorrido > tempo/1000:
            self.finaliza_giro = False
            return self.finaliza_giro
        else:
            return True
        