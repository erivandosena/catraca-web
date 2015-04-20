#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
led_sd = rpi.ler(28)['gpio']
led_se = rpi.ler(29)['gpio']
led_x = rpi.ler(30)['gpio']


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

def leds_x(comando):
    if comando:
        return rpi.atualiza(led_x, comando)
    else:
        return rpi.atualiza(led_x, comando)


