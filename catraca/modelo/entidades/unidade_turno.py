#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeTurno(object):
    def __init__(self):
        self.__untu_id = None
        self.__turno = None
        self.__unidade = None
    
    @property
    def id(self):
        return self.__untu_id
    
    @id.setter
    def id(self, valor):
        self.__untu_id = valor
        
    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, obj):
        self.__turno = obj
        
    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, obj):
        self.__unidade = obj
        