#!/usr/bin/env python
# -*- coding: latin-1 -*-

#import pingo 
from time import sleep
from catraca.pinos import PinoControle
from catraca import configuracao 
from catraca.dispositivos import display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


#placa = configuracao.pinos_rpi()
rpi = PinoControle()

solenoide_1 = rpi.ler(11)['gpio']#placa.pins[23]
solenoide_2 = rpi.ler(27)['gpio']#placa.pins[13]

#solenoide_1.mode = configuracao.pino_saida()
#solenoide_2.mode = configuracao.pino_saida()

baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()


def magnetiza_solenoide_1(estado):
    if estado == alto:
        #solenoide_1.state = alto
        rpi.atualiza(solenoide_1, alto)
    else:
        #solenoide_1.state = baixo
        rpi.atualiza(solenoide_1, baixo)

def magnetiza_solenoide_2(estado):
    if estado == alto:
        #solenoide_2.state = alto
        rpi.atualiza(solenoide_2, alto)
    else:
        #solenoide_2.state = baixo
        rpi.atualiza(solenoide_2, baixo)

