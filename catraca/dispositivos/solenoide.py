#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
solenoide_1 = rpi.ler(11)['gpio']
solenoide_2 = rpi.ler(27)['gpio']
baixo = rpi.baixo()
alto = rpi.alto()


def magnetiza_solenoide_1(estado):
    if estado == alto:
        rpi.atualiza(solenoide_1, alto)
    else:
        rpi.atualiza(solenoide_1, baixo)

def magnetiza_solenoide_2(estado):
    if estado == alto:
        rpi.atualiza(solenoide_2, alto)
    else:
        rpi.atualiza(solenoide_2, baixo)

