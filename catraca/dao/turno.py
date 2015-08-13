#!/usr/bin/env python
# -*- coding: latin-1 -*-

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Turno(object):

    def __init__(self):
        super(Turno, self).__init__()
        self.__turn_id = None
        self.__turn_hora_inicio = None
        self.__turn_hora_fim = None
        self.__turn_data = None
        self.__turn_continuo = None

    @property
    def id(self):
        return self.__turn_id
    
    @id.setter
    def id(self, valor):
        self.__turn_id = valor
    
    @property
    def inicio(self):
        return self.__turn_hora_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__turn_hora_inicio = valor
    
    @property
    def fim(self):
        return self.__turn_hora_fim
    
    @fim.setter
    def fim(self, valor):
        self.__turn_hora_fim = valor
    
    @property
    def data(self):
        return self.__turn_data
    
    @data.setter
    def data(self, valor):
        self.__turn_data = valor
    
    @property
    def continuo(self):
        return self.__turn_continuo
    
    @continuo.setter
    def continuo(self, valor):
        self.__turn_continuo = valor
        