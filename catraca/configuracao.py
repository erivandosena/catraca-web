#!/usr/bin/env python
# -*- coding: latin-1 -*-

from catraca.pinos import PinoControle
#import pingo
#import RPi.GPIO as GPIO

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production

pino = PinoControle()

def pinos_rpi():
    #return pingo.rpi.RaspberryPi()
    return pino.ler_todos()


def pino_entrada():
    #return pingo.IN
    return pino.gpio.IN


def pino_saida():
    #return pingo.OUT
    return pino.gpio.OUT


def pino_baixo():
    #return pingo.LOW
    return pino.gpio.LOW


def pino_alto():
    #return pingo.HIGH
    return pino.gpio.HIGH


def ativa_avisos():
    #GPIO.setwarnings(True)
    pino.gpio.setwarnings(True)


def desativa_avisos():
    #GPIO.setwarnings(False)
    pino.gpio.setwarnings(False)


def limpa_pinos():
    #GPIO.cleanup()
    pino.gpio.cleanup()


def protege_pino_entrada_up(num_pino):
    #GPIO.setup(int(pino), GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pino.gpio.setup(num_pino, pino.gpio.IN, pull_up_down=pino.gpio.PUD_UP)

def detecta_evento(num_pino,obj):
    #GPIO.add_event_detect(int(pino), GPIO.FALLING, callback=obj)
    pino.gpio.add_event_detect(num_pino, pino.gpio.FALLING, callback=obj)
