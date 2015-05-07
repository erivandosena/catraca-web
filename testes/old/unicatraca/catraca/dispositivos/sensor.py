#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#import RPi.GPIO as GPIO
import pingo
from time import sleep 

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Universidade da Integração Internacional da Lusofonia Afro-Brasileira"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def ativaChaveOptica1():
    placa = pingo.rpi.RaspberryPi()
    sensor = placa.pins[19]
    sensor.mode = pingo.IN
    estado = pingo.LOW
    while True:
	if estado == pingo.LOW:
		#print("Catraca aguardando giro horário")
                return 'Catraca aguardando giro horário. <a href="javascript:window.history.go(-1)">Voltar</a>'
        	if estado == pingo.HIGH:
            		#print("GIROU A CATRACA NO SENTIDO HORÁRIO")
                        return 'GIROU A CATRACA NO SENTIDO HORÁRIO. <a href="javascript:window.history.go(-1)">Voltar</a>'

def ativaChaveOptica2():
    placa = pingo.rpi.RaspberryPi()
    sensor = placa.pins[21]
    sensor.mode = pingo.IN
    estado = pingo.LOW
    while True:
        if estado == pingo.LOW:
                print("Catraca aguardando giro antihorário")
                if estado == pingo.HIGH:
                        print("GIROU A CATRACA NO SENTIDO ANTIHORÁRIO")
