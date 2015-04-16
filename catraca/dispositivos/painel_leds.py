#!/usr/bin/env python
# -*- coding: latin-1 -*-


import pingo 
from time import sleep
from catraca import configuracao 
#from catraca.dispositivos import display, leitor_rfid, solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


#placa = configuracao.pinos_rpi()
placa = pingo.detect.MyBoard()
sensor_1 = placa.pins[19]
sensor_2 = placa.pins[21]
sensor_1.mode = configuracao.pino_entrada()
sensor_2.mode = configuracao.pino_entrada()
baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()

def acende_senta_direira():
    return placa.pins

def ler_sensores():
    pass

def ler_sensor_1():
    pass

def ler_sensor_2():
    pass

