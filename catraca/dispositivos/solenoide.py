#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pingo 
from time import sleep
from catraca import configuracao 
from catraca.dispositivos import display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


placa = configuracao.pinos_rpi()

solenoide_1 = placa.pins[23]
solenoide_2 = placa.pins[13]

solenoide_1.mode = configuracao.pino_saida()
solenoide_2.mode = configuracao.pino_saida()

baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()


def magnetiza_solenoide_1(estado):
    if estado == alto:
        solenoide_1.state = alto
    else:
        solenoide_1.state = baixo


def magnetiza_solenoide_2(estado):
    if estado == alto:
        solenoide_2.state = alto
    else:
        solenoide_2.state = baixo

