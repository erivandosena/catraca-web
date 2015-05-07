#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
led_sd = rpi.ler(11)['gpio']
led_se = rpi.ler(22)['gpio']

sensor_1 = rpi.ler(6)['gpio']
sensor_2 = rpi.ler(13)['gpio']

baixo = rpi.baixo()
alto = rpi.alto()

def mostra_pictograma():
    #if rpi.estado(sensor_1):
        
        
    #rpi.atualiza(led_sd, baixo)
    #rpi.atualiza(led_se, baixo)

    #print rpi.estado(led_sd)
    #print rpi.estado(sensor_2)
    pass





def leds_sd(comando):
    if comando:
        return rpi.atualiza(led_sd, comando)
    else:
        return rpi.atualiza(led_sd, comando)

def leds_se(comando):
    if comando:
        return rpi.atualiza(led_se, comando)
    else:
        return rpi.atualiza(led_se, comando)

"""
def leds_x(comando):
    if comando:
        return rpi.atualiza(led_x, comando)
    else:
        return rpi.atualiza(led_x, comando)
"""

def main():
    """Bloco principal do programa.
    """
    mostra_pictograma()
    

if __name__ == '__main__':
    main()
    
