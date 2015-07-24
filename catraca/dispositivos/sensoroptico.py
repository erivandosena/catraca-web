#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle
from catraca.dispositivos import solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    
    def __init__(self):
        super(SensorOptico, self).__init__()
        self.__erro = None

    @classmethod
    def ler_sensor(self, sensor):
        if sensor == 1:
            return self.rpi.estado(self.sensor_1)
        elif sensor == 2:
            return self.rpi.estado(self.sensor_2)
    
    @classmethod
    def registra_giro(self, tempo):
        codigo_giro = ''
        # cronômetro regressivo para o giro
        for segundo in range(tempo, -1, -1):
            sleep(0.001)
            print str(segundo / 1000) + ' segundos restantes p/ o giro'
            print 'Em repouso '+ str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
            # GIRO HORARIO
            if self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
                print 'girou horario'
                while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 0:
                    codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                    codigo_giro = ''
                while self.ler_sensor(1) == 1 and self.ler_sensor(2) == 1:
                    codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                while self.ler_sensor(1) == 0 and self.ler_sensor(2) == 1:
                    codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                if codigo_giro == '01': 
                    codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                    return True
                    #break
                elif codigo_giro == '00': 
                    codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                    return True
                    #break
            # GIRO ANTIHORARIO
            elif self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                print 'girou antihorario'
                while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 0:
                    codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                    codigo_giro = ''
                while self.ler_sensor(2) == 1 and self.ler_sensor(1) == 1:
                    codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                while self.ler_sensor(2) == 0 and self.ler_sensor(1) == 1:
                    codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                if codigo_giro == '01':
                    codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                    return True
                    #break
                elif codigo_giro == '00': 
                    codigo_giro = str(self.ler_sensor(2)) + '' + str(self.ler_sensor(1))
                    return True
                    #break
        return False
