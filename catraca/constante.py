#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Constante(object):

    def __init__(self, valor):
        super(Constante, self).__init__()
        self.valor = valor
        
    def __get__(self, obj, type=None):
        return self.valor

    def __set__(self, obj, valor):
        pass
    