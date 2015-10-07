#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoCartao(object):
    
    def __init__(self):
        self.__cuca_id = None
        self.__cuca_valor = None
        self.__cuca_data = None
    
    @property
    def id(self):
        return self.__cuca_id
    
    @id.setter
    def id(self, valor):
        self.__cuca_id = valor
    
    @property
    def valor(self):
        return self.__cuca_valor
    
    @valor.setter
    def valor(self, valor):
        self.__cuca_valor = valor
    
    @property
    def data(self):
        return self.__cuca_data
    
    @data.setter
    def data(self, valor):
        self.__cuca_data = valor
        