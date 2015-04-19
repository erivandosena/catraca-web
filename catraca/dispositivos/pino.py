#!/usr/bin/env python
# -*- coding: latin-1 -*-

import RPi.GPIO as GPIO

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Pino(object):

    

    def __init__(self, nome, gpio):
        super(Pino, self).__init__()
        self.nome = nome
        self.gpio = gpio

    def entrada(self):
        return self.nome

    def saida(self):
        return self.nome

    def alto(self):
        return self.nome

    def baixo(self):
        return self.nome

    def descricao(self):
        return self.nome

    def gpio(self):
        return self.gpio
