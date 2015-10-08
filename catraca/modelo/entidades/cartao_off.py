#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoOff(object):
    
    def __init__(self):
        self.__caof_id = None
        self.__caof_numero = None
        self.__caof_creditos = None
        self.__tipo = None
    
    @property
    def id(self):
        return self.__caof_id
    
    @id.setter
    def id(self, valor):
        self.__caof_id = valor
    
    @property
    def numero(self):
        return self.__caof_numero
    
    @numero.setter
    def numero(self, valor):
        self.__caof_numero = valor
    
    @property
    def creditos(self):
        return self.__caof_creditos
    
    @creditos.setter
    def creditos(self, valor):
        self.__caof_creditos = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo = obj
        