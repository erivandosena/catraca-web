#!/usr/bin/env python
# -*- coding: latin-1 -*-

import RPi.GPIO as GPIO

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class PinosGPIO(object):
    
    gpio = None

    def __init__(self):
        self.gpio = GPIO
        #print "GPIO v." + str(self.gpio.VERSION)