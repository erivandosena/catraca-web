#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos import solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    log = Logs()
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    
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
    
    def registra_giro(self, tempo):
        codigo_giro = ''
        # cronômetro regressivo para o giro
        finaliza_giro = True
        try:
            for segundo in range(tempo, -1, -1):
                self.tempo_decorrido = (tempo/1000)-(segundo/1000)
                print str(self.tempo_decorrido)+" de "+str(tempo/1000)
                self.log.logger.debug(str(segundo ) + ' seg. restantes para expirar o tempo para giro.')
                self.log.logger.debug('Catraca em repouso, codigo sensores: '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2)))
                """
                # GIRO HORARIO
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
                """
                #el
                if self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                    self.log.logger.info('Girou a catraca no sentido antihorario.')
                    while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                        codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                        self.log.logger.debug('Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro))
                        codigo_giro = ''
                    while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 1:
                        codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                        self.log.logger.debug('No meio do giro antihorario, codigo sensores: '+ str(codigo_giro))
                    while self.ler_sensor(2) == 0 and self.ler_sensor(1) == 1:
                        codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                        self.log.logger.debug('Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro))
                    if codigo_giro == '01':
                        codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                        self.log.logger.info('Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
                        self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                        finaliza_giro = False
                        print 'Finalizou no girou 01'
                        return finaliza_giro
                    elif codigo_giro == '00':
                        codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                        self.log.logger.info('Giro antihorario finalizado em '+ str(self.tempo_decorrido)+' segundo(s).')
                        self.log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                        finaliza_giro = False
                        print 'Finalizou no girou 00'
                        return finaliza_giro
                if self.tempo_decorrido == tempo/1000:
                    finaliza_giro = False
                    print 'Finalizou no tempo decorrido de: '+ str(self.tempo_decorrido)
                    return finaliza_giro
            finaliza_giro = False
            return finaliza_giro
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
        finally:
            pass
        