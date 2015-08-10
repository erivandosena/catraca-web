#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Tipo(object):

    def __init__(self):
        super(Tipo, self).__init__()
        self.__tipo_id = None
        self.__tipo_nome = None
        
    @property
    def id(self):
        return self.__tipo_id
    
    @id.setter
    def id(self, valor):
        self.__tipo_id = valor
        
    @property
    def nome(self):
        return self.__tipo_nome
    
    @nome.setter
    def nome(self, valor):
        self.__tipo_nome = valor
        