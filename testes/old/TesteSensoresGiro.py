#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
from time import sleep
from catraca.pinos import PinoControle
from catraca.dispositivos import solenoide
from catraca.dispositivos import painel_leds
from catraca.dispositivos import sensor_optico
from catraca.dispositivos.sensor_optico import SensorOptico


__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, ©"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "Copyright"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Protótipo"


rpi = PinoControle()

sensor_1 = rpi.ler(6)['gpio']
sensor_2 = rpi.ler(13)['gpio']

solenoide_1 = rpi.ler(19)['gpio']
solenoide_2 = rpi.ler(26)['gpio']

baixo = rpi.baixo()
alto = rpi.alto()

def ler_sensor(sensor):
    if sensor == 1:
    #print str(sensor) + ' 1 = '+ str(self.rpi.estado(self.sensor_1))
        return rpi.estado(sensor_1)
    if sensor == 2:
    #print str(sensor) + ' 2 = '+ str(self.rpi.estado(self.sensor_2))
        return rpi.estado(sensor_2)


def registra_giro(tempo):
    codigo_giro = ''
    # tempo para o giro
    for segundo in range(tempo, -1, -1):
        sleep(0.001)
        print str(segundo/1000) + ' segundos restantes'
        
        print 'Estado repouso ' +str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))

        # GIRO HORARIO
        if sensor_optico.ler_sensor(1) == 1 and sensor_optico.ler_sensor(2) == 0:
            print 'Giro para direita...'
            
            while sensor_optico.ler_sensor(1) == 1 and sensor_optico.ler_sensor(2) == 0:
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                print 'iniciou o giro horario... '+ str(codigo_giro)
                codigo_giro = ''

            while sensor_optico.ler_sensor(1) == 1 and sensor_optico.ler_sensor(2) == 1:
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                print 'no meio do giro... '+ str(codigo_giro)

            while sensor_optico.ler_sensor(1) == 0 and sensor_optico.ler_sensor(2) == 1:
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                print 'finalizando o giro '+ str(codigo_giro)

            if codigo_giro == '01': 
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                #print codigo_giro 
                #print 'finalizou no 01'
                #print '*' * 30
                #print 'giro finalizado p/ direita! '+ codigo_giro
                #print '*' * 30
                #print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                return True
                print 'antes de break'
                break
            elif codigo_giro == '00': 
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                #print codigo_giro 
                #print 'finalizou no 00'
                #print '*' * 30
                #print 'giro finalizado p/ direita! '+ codigo_giro
                #print '*' * 30
                #print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                return True
                print 'antes de break'
                break
 
        # GIRO ANTIHORARIO
        elif sensor_optico.ler_sensor(2) == 1 and sensor_optico.ler_sensor(1) == 0:
            print 'Giro para esquerda...'
            
            while sensor_optico.ler_sensor(2) == 1 and sensor_optico.ler_sensor(1) == 0:
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                print 'iniciou o giro antihorario... '+ str(codigo_giro)
                codigo_giro = ''

            while sensor_optico.ler_sensor(2) == 1 and sensor_optico.ler_sensor(1) == 1:
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                print 'no meio do giro... '+ str(codigo_giro)

            while sensor_optico.ler_sensor(2) == 0 and sensor_optico.ler_sensor(1) == 1:
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                print 'finalizando o giro '+ str(codigo_giro)


            if codigo_giro == '01':
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                #print codigo_giro 
                #print '*' * 30
                #print 'giro finalizado p/ esquerda! '+ codigo_giro
                #print '*' * 30
                #print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                return True
                print 'antes de break'
                break
            elif codigo_giro == '00': 
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                #print codigo_giro 
                #print '*' * 30
                #print 'giro finalizado p/ esquerda! '+ codigo_giro
                #print '*' * 30
                #print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                return True
                print 'antes de break'
                break
            
    return False

def main():
    """Bloco principal do programa.
    """
    solenoide.ativa_solenoide(1,1)
    painel_leds.leds_se(1)
    painel_leds.leds_x(1)
    giro = SensorOptico()
    while True:
        if giro.registra_giro(10000):
            print 'GIROU A CATRACA'
            solenoide.ativa_solenoide(1,0)
            painel_leds.leds_se(0)
            painel_leds.leds_x(0)
            break
        else:
            print 'NÃO GIROU A CATRACA'
            solenoide.ativa_solenoide(1,0)
            painel_leds.leds_se(0)
            painel_leds.leds_x(0)
            break


if __name__ == '__main__':
    main()
    