#!/usr/bin/env python
# -*- coding: latin-1 -*-


import pingo
from catraca import configuracao


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 

placa = configuracao.pinos_rpi()
#leds_seta_direita = placa.pins[19]
#leds_seta_esquerda = placa.pins[21]
#leds_X = placa.pins[21]
#sensor_1.mode = configuracao.pino_entrada()
#sensor_2.mode = configuracao.pino_entrada()
#baixo = configuracao.pino_baixo()
#alto = configuracao.pino_alto()


class Leds(object):
    def __init__(self, pino, estado):
        super(Leds, self).__init__()
        self.pino = pino
        self.estado = estado

    def acender(self):
        print self.placa.pins

