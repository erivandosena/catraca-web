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
        self.__finalidade = None
        self.__catraca = None

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
    def finalidade(self):
        return self.__finalidade
    
    @finalidade.setter
    def finalidade(self, valor):
        self.__finalidade = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        