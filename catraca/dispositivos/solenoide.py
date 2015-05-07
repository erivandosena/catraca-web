#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
solenoide_1 = rpi.ler(19)['gpio']
solenoide_2 = rpi.ler(26)['gpio']
baixo = rpi.baixo()
alto = rpi.alto()

def ativa_solenoide(solenoide,estado):
    if solenoide == 1:
        if estado:
            rpi.atualiza(solenoide_1, alto)
            rpi.atualiza(solenoide_2, baixo)
        else:
            rpi.atualiza(solenoide_1, baixo)
    elif solenoide == 2:
        if estado:
            rpi.atualiza(solenoide_2, alto)
            rpi.atualiza(solenoide_1, baixo)
        else:
            rpi.atualiza(solenoide_2, baixo)


