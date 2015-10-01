#!/usr/bin/env python
# -*- coding: latin-1 -*-


import subprocess
import threading
from multiprocessing import Process
from threading import Thread
from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos import solenoide
from __builtin__ import str


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    log = Logs()
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    pino_buzzer = rpi.ler(21)['gpio']
    
    thread_buzzer = None
    
    cronometro_cod11 = 0
    
    def __init__(self):
        super(SensorOptico, self).__init__()
        self.__erro = None
        self.__tempo_decorrido = 0
        
    @property
    def tempo_decorrido(self):
        return self.__tempo_decorrido
    
    @tempo_decorrido.setter
    def tempo_decorrido(self, tempo):
        self.__tempo_decorrido = tempo

    def ler_sensor(self, sensor):
        if sensor == 1:
            return self.rpi.estado(self.sensor_1)
        elif sensor == 2:
            return self.rpi.estado(self.sensor_2)
        
    def registra_giro(self, tempo, catraca):
        finaliza_giro = False
        self.cronometro_cod11 = 0
        codigo_giro = ''
        tempo_giro = tempo
        # cronômetro regressivo para o giro
        try:
            for segundo in range(tempo, -1, -1):
                self.tempo_decorrido =  tempo/1000 - segundo/1000
                #print self.tempo_decorrido
                self.log.logger.debug(str(self.tempo_decorrido) + ' seg. restantes para expirar o tempo para giro.')
                self.log.logger.debug('Catraca em repouso, codigo sensores: '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2)))
                # GIRO HORARIO
                if catraca.operacao == 1:
                    if self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
                        self.log.logger.info('Girou catraca no sentido horario.')
                        while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.debug('Continuou o giro horario, codigo sensores: '+ str(codigo_giro))
                            codigo_giro = ''
                        while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 1:
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.debug('No meio do giro horario, codigo sensores: '+ str(codigo_giro))
                        while self.ler_sensor(1) == 0 and self.ler_sensor(2) == 1:
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.debug('Finalizando o giro horario, codigo sensores: '+ str(codigo_giro))
                        if codigo_giro == '01': 
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.info('Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).')
                            self.log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
                            return True
                        elif codigo_giro == '00': 
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.info('Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).')
                            self.log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
                            return True
                # GIRO ANTIHORARIO
                if catraca.operacao == 2:
                    if self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                        self.log.logger.info('Girou a catraca no sentido antihorario.')
                        while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                            codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                            self.log.logger.debug('Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro))
                            codigo_giro = ''
                        while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 1:
                            codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                            self.log.logger.debug('No meio do giro antihorario, codigo sensores: '+ str(codigo_giro))
                            
                            self.cronometro_cod11 += 1
                            if self.cronometro_cod11/1000 > 5:
                                self.beep_buzzer(840, 1, 3)
                            
                        while self.ler_sensor(2) == 0 and self.ler_sensor(1) == 1:
                            codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                            self.log.logger.debug('Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro))
                        if codigo_giro == '01':
                            codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                            self.log.logger.info('Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).')
                            self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                            finaliza_giro = True
                            return finaliza_giro
                        elif codigo_giro == '00': 
                            codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                            self.log.logger.info('Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).')
                            self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                            finaliza_giro = True
                            return finaliza_giro
                if self.tempo_decorrido == tempo/1000:
                    finaliza_giro = False
                    return finaliza_giro
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
        finally:
            return finaliza_giro
        
    def obtem_codigo_sensores(self,s1,s2):
        return str(self.ler_sensor(s1)) + '' + str(self.ler_sensor(s2))
        
    def buzzer(self, frequencia, intensidade):
        period = 1.0 / frequencia
        delay = period / 2.0
        cycles = int(intensidade * frequencia)
        retorno = False
        for i in range(cycles):
            self.rpi.atualiza(self.pino_buzzer, True)
            sleep(delay)
            self.rpi.atualiza(self.pino_buzzer, False)
            sleep(delay)
            retorno = True
        return retorno
    
    def beep_buzzer(self, frequencia, intensidade, quantidade_beep):
        contador = 0
        while contador < quantidade_beep:
            self.rpi.atualiza(self.pino_buzzer, True)
            self.buzzer(frequencia, intensidade)
            print 'beeep!'
            sleep(intensidade)
            self.rpi.atualiza(self.pino_buzzer, False)
            contador += 1
    
#     def registra_giro(self, tempo, cronometro, catraca):
#         codigo_giro = ''
#         conta_tempo = tempo
#         #cronometro = 0
#         finaliza_giro = True
#         try:
#             # GIRO HORARIO
#             if catraca.operacao == 1:
#                 for segundo in range(tempo, -1, -1):
#                     self.tempo_decorrido = (tempo/1000)-(segundo/1000)
#                     print str(self.tempo_decorrido)+" de "+str(tempo/1000)
#                     self.log.logger.debug(str(segundo/1000 ) + ' seg. restantes para expirar o tempo para giro.')
#                     self.log.logger.debug('Catraca em repouso, codigo sensores: '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2)))
#                     if self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
#                         codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                         self.log.logger.info('Girou catraca no sentido horario, codigo sensores: '+ str(codigo_giro))
#                         while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
#                             codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                             self.log.logger.debug('Continuou o giro horario, codigo sensores: '+ str(codigo_giro))
#                             codigo_giro = ''
#                         while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 1:
#                             codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                             self.log.logger.debug('No meio do giro horario, codigo sensores: '+ str(codigo_giro))
#                             #self.alerta_sonoro(10,codigo_giro)
#                         while self.ler_sensor(1) == 0 and self.ler_sensor(2) == 1:
#                             codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                             self.log.logger.debug('Finalizando o giro horario, codigo sensores: '+ str(codigo_giro))
#                         if codigo_giro == '01': 
#                             codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                             self.log.logger.info('Giro horario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
#                             self.log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
#                             finaliza_giro = False
#                             #print 'Finalizou no girou 01'
#                             return finaliza_giro
#                         elif codigo_giro == '00': 
#                             codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                             self.log.logger.info('Giro horario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
#                             self.log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
#                             finaliza_giro = False
#                             #print 'Finalizou no girou 00'
#                 finaliza_giro = False
#             # GIRO ANTIHORARIO
#             if catraca.operacao == 2:
#                 self.tempo_decorrido = cronometro
#                 print str((tempo/1000)-cronometro) + ' seg. restantes para expirar o tempo para giro.'
#                 print 'Catraca em repouso, codigo sensores: '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
#                 if self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
#                     codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                     print 'Girou a catraca no sentido antihorario, codigo sensores: '+ str(codigo_giro)
#                     while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
#                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                         #print 'Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro)
#                         
#                         
#                         if self.tempo_decorrido == (tempo/1000)-1:
#                             if codigo_giro == '10':
#                                 self.beep_buzzer(840, 1, 10)
#                         
#                         #self.alerta_sonoro(10,codigo_giro)
#                         codigo_giro = ''
#                     while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 1:
#                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                         #self.alerta_sonoro(10,codigo_giro)
#                         print 'No meio do giro antihorario, codigo sensores: '+ str(codigo_giro)
#                     while self.ler_sensor(2) == 0 and self.ler_sensor(1) == 1:
#                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                         print 'Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro)
#                         #self.alerta_sonoro(10,codigo_giro)
#                     if codigo_giro == '01':
#                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                         print 'Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).'
#                         print 'Giro antihorario completo no codigo: '+ str(codigo_giro)
#                         finaliza_giro = False
#                         #print 'Finalizou no girou 01'
#                         return finaliza_giro
#                     elif codigo_giro == '00':
#                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
#                         print 'Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).'
#                         print 'Giro antihorario completo no codigo: '+ str(codigo_giro)
#                         finaliza_giro = False
#                         #print 'Finalizou no girou 00'
#                         return finaliza_giro
# 
# #                 for segundo in range(tempo, -1, -1):
# #                     #self.tempo_decorrido = (tempo/1000)-(segundo/1000)
# #                     self.tempo_decorrido = (tempo/1000)-(conta_tempo/1000)
# #                     print str(self.tempo_decorrido)+" de "+str(tempo/1000)
# #                     self.log.logger.debug(str(segundo/1000 ) + ' seg. restantes para expirar o tempo para giro.')
# #                     self.log.logger.debug('Catraca em repouso, codigo sensores: '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2)))
# #                     if self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
# #                         codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                         self.log.logger.info('Girou a catraca no sentido antihorario, codigo sensores: '+ str(codigo_giro))
# #                         while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
# #                             codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                             self.log.logger.debug('Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro))
# #                             #self.alerta_sonoro(10,codigo_giro)
# #                             codigo_giro = ''
# #                         while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 1:
# #                             codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                             #self.alerta_sonoro(10,codigo_giro)
# #                             self.log.logger.debug('No meio do giro antihorario, codigo sensores: '+ str(codigo_giro))
# #                         while self.ler_sensor(2) == 0 and self.ler_sensor(1) == 1:
# #                             codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                             self.log.logger.debug('Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro))
# #                             #self.alerta_sonoro(10,codigo_giro)
# #                         if codigo_giro == '01':
# #                             codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                             self.log.logger.info('Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
# #                             self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
# #                             finaliza_giro = False
# #                             #print 'Finalizou no girou 01'
# #                             return finaliza_giro
# #                         elif codigo_giro == '00':
# #                             codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
# #                             self.log.logger.info('Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
# #                             self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
# #                             finaliza_giro = False
# #                             #print 'Finalizou no girou 00'
# #                             return finaliza_giro
#                     
# #                 finaliza_giro = False
#             #return finaliza_giro    
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception:
#             self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
#         finally:
#             return finaliza_giro 
           
        
#     def beep(sel, mp3):
#         process = subprocess.Popen(['mpg321 -q -g 100 '+mp3, '-R player'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #STDOUT
#         stdout_value = process.communicate()[0]
#         
#     def alerta_sonoro(self, tempo, codigo):
#         if codigo == '11':
#             contador = 0
#             while contador < tempo:
#                 sleep(1)
#                 contador += 1
#                 print str(contador)
#             else:
#                 while (codigo == '11'):
#                     self.beep('audio/beep-04.mp3')
#                     print str(self.beep('audio/beep-04.mp3'))
#                     print 'alertando...'
#                     sleep(1)
                    
                    
                