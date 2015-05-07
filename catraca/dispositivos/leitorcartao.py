#!/usr/bin/env python
# -*- coding: latin-1 -*-

from time import sleep
from catraca.pinos import PinoControle

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 

class LeitorCartao(object):
    
    bits = ''
    numero_cartao = ''
    
    def __init__(self):
        super(LeitorCartao, self).__init__()
        self.erro = None
    
    @classmethod    
    def zero(self):
        #global bits
        self.bits = self.bits + '0'
    
    @classmethod
    def um(self):
        #global bits
        self.bits = self.bits + '1'

    @classmethod
    def ler(self):
        #display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
        #global bits
        #global numero_cartao
        try:
            rpi = PinoControle()
            D0 = rpi.ler(17)['gpio']
            D1 = rpi.ler(27)['gpio']
            rpi.evento_falling(D0, LeitorCartao.zero)
            rpi.evento_falling(D1, LeitorCartao.um)
            while True:
                sleep(0.5)
                if len(self.bits) == 32:
                    sleep(0.1)
                    numero_cartao = int(str(bits), 2)
                    self.bits = ''
                    return numero_cartao
                    #ler_cartao(numero_cartao)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.bits = ''
                    return None
                    #display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",0,True,False)
        #except KeyboardInterrupt, ki:
        #    self.erro = str(ki)
        #except Exception, e:
        #    self.erro = str(e)
        finally:
            pass
        
    def getErro(self):
        return self.erro
