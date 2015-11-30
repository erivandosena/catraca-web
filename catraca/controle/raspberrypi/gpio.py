#!/usr/bin/env python
# -*- coding: latin-1 -*-

import RPi.GPIO as GPIO

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class PinosGPIO(object):
    
    gpio = None

    def __init__(self):
        self.gpio = GPIO
        #print "GPIO v." + str(self.gpio.VERSION)