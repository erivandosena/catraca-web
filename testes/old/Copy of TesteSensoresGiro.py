#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
from time import sleep
from catraca.pinos import PinoControle
from catraca.dispositivos import solenoide
from catraca.dispositivos import painel_leds
from catraca.dispositivos import sensor_optico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()

sensor_1 = rpi.ler(6)['gpio']
sensor_2 = rpi.ler(13)['gpio']

solenoide_1 = rpi.ler(19)['gpio']
solenoide_2 = rpi.ler(26)['gpio']

baixo = rpi.baixo()
alto = rpi.alto()


def registra_giro():
    # tempo para o giro
    codigo_giro = ''
    for segundo in range(6000, -1, -1):
        sleep(0.001)
        print str(segundo/1000) + ' segundos restantes'

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
                print codigo_giro 
                print '*' * 30
                print 'giro finalizado p/ direita! '+ codigo_giro
                print '*' * 30
                print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                break
            elif codigo_giro == '00': 
                codigo_giro = str(sensor_optico.ler_sensor(1)) + '' +str(sensor_optico.ler_sensor(2))
                print codigo_giro 
                print '*' * 30
                print 'giro finalizado p/ direita! '+ codigo_giro
                print '*' * 30
                print 'Em ' +str(6-(segundo/1000))+ ' segundos'
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
                print codigo_giro 
                print '*' * 30
                print 'giro finalizado p/ esquerda! '+ codigo_giro
                print '*' * 30
                print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                break
            elif codigo_giro == '00': 
                codigo_giro = str(sensor_optico.ler_sensor(2)) + '' +str(sensor_optico.ler_sensor(1))
                print codigo_giro 
                print '*' * 30
                print 'giro finalizado p/ esquerda! '+ codigo_giro
                print '*' * 30
                print 'Em ' +str(6-(segundo/1000))+ ' segundos'
                break

def main():
    """Bloco principal do programa.
    """

    registra_giro()


if __name__ == '__main__':
    main()
    