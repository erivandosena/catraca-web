#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from catraca.controle.raspberrypi.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Pictograma(object):
    
    rpi = PinoControle()
    sd = rpi.ler(11)['gpio']
    se = rpi.ler(22)['gpio']
    x = rpi.ler(18)['gpio']
    
    def __init__(self):
        super(Pictograma, self).__init__()
        
    def seta_direita(self, comando):
        if comando:
            return self.rpi.atualiza(self.sd, comando)
        else:
            return self.rpi.atualiza(self.sd, comando)
    
    def seta_esquerda(self, comando):
        if comando:
            return self.rpi.atualiza(self.se, comando)
        else:
            return self.rpi.atualiza(self.se, comando)
    
    def xis(self, comando):
        if comando:
            return self.rpi.atualiza(self.x, comando)
        else:
            return self.rpi.atualiza(self.x, comando)
        