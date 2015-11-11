#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Fluxo(object):
    
    def __init__(self):
        self.__flux_id = None
        self.__flux_data = None
        self.__flux_valor = None
        self.__flux_descricao = None
        self.__guiche = None
    
    @property
    def id(self):
        return self.__flux_id
    
    @id.setter
    def id(self, valor):
        self.__flux_id = valor
        
    @property
    def data(self):
        return self.__flux_data
    
    @data.setter
    def data(self, valor):
        self.__flux_data = valor
        
    @property
    def valor(self):
        return self.__flux_valor
    
    @valor.setter
    def valor(self, valor):
        self.__flux_valor = valor
        
    @property
    def descricao(self):
        return self.__flux_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__flux_descricao = valor
        
    @property
    def guiche(self):
        return self.__guiche

    @guiche.setter
    def guiche(self, obj):
        self.__guiche = obj
        