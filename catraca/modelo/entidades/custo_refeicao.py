#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoRefeicao(object):
    
    def __init__(self):
        self.__cure_id = None
        self.__cure_valor = None
        self.__cure_data = None
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.valor, 
                 self.data) == (obj.id, 
                                     obj.valor, 
                                     obj.data))
        
    def __ne__(self, obj):
        return not self == obj
     
    @property
    def id(self):
        return self.__cure_id
    
    @id.setter
    def id(self, valor):
        self.__cure_id = valor
    
    @property
    def valor(self):
        return self.__cure_valor
    
    @valor.setter
    def valor(self, valor):
        self.__cure_valor = valor
    
    @property
    def data(self):
        return self.__cure_data
    
    @data.setter
    def data(self, valor):
        self.__cure_data = valor
        