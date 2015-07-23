#!/usr/bin/env python
# -*- coding: latin-1 -*-

from threading import Thread
from catraca.dispositivos import leitor_rfid

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Leitor(Thread):
    def __init__(self):
        super(Leitor, self).__init__()

    def run(self):
        #leitor_rfid.cartao()
        leitor_rfid.ler_cartao()
