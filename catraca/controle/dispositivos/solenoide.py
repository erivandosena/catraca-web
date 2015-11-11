#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.controle.raspberrypi.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Solenoide(object):
    
    rpi = PinoControle()
    solenoide_1 = rpi.ler(19)['gpio']
    solenoide_2 = rpi.ler(26)['gpio']
    baixo = rpi.baixo() # = 0
    alto = rpi.alto()   # = 1
    
    def __init__(self):
        super(Solenoide, self).__init__()
        
    def ativa_solenoide(self,solenoide,estado):
        if solenoide == 1:
            if estado:
                self.rpi.atualiza(self.solenoide_1, self.alto)
                self.rpi.atualiza(self.solenoide_2, self.baixo)
                return True
            else:
                self.rpi.atualiza(self.solenoide_1, self.baixo)
                return False
        elif solenoide == 2:
            if estado:
                self.rpi.atualiza(self.solenoide_2, self.alto)
                self.rpi.atualiza(self.solenoide_1, self.baixo)
                return True
            else:
                self.rpi.atualiza(self.solenoide_2, self.baixo)
                return False
            
    def obtem_estado_solenoide(self,solenoide):
        if solenoide == 1:
            return self.rpi.estado(self.solenoide_1)
        elif solenoide == 2:
            return self.rpi.estado(self.solenoide_2)
        
                
