#!/usr/bin/env python
# -*- coding: latin-1 -*-

from threading import Thread
from catraca.dispositivos import sensor


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Sensores(Thread):

    def __init__(self, nome):
        super(Sensores, self).__init__()
        self.nome = nome

    def run(self):
        sensor.ler_sensores()


