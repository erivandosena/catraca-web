#!/usr/bin/env python
# -*- coding: latin-1 -*-


from threading import Thread
from catraca.dispositivos import sensor_optico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Sensor(Thread):
    def __init__(self, nome):
        super(Sensor, self).__init__()
        self.nome = nome

    def run(self):
        sensor_optico.ler_sensores()

