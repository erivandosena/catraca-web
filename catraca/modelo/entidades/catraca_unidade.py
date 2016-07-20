#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaUnidade(object):
    
    def __init__(self):
        self.__caun_id = None
        self.__catraca = None
        self.__unidade = None
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.catraca, 
                 self.unidade) == (obj.id, 
                                     obj.catraca, 
                                     obj.unidade))
        
    @property
    def id(self):
        return self.__caun_id
    
    @id.setter
    def id(self, valor):
        self.__caun_id = valor
    
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
    
    @property
    def unidade(self):
        return self.__unidade
    
    @unidade.setter
    def unidade(self, obj):
        self.__unidade = obj
        