#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Isencao(object):
    
    def __init__(self):
        self.__isen_id = None
        self.__isen_inicio = None
        self.__isen_fim = None
        self.__cartao = None
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.inicio, 
                 self.fim, 
                 self.cartao) == (obj.id, 
                                     obj.inicio, 
                                     obj.fim, 
                                     obj.cartao))
        
    @property
    def id(self):
        return self.__isen_id
    
    @id.setter
    def id(self, valor):
        self.__isen_id = valor
        
    @property
    def inicio(self):
        return self.__isen_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__isen_inicio = valor
        
    @property
    def fim(self):
        return self.__isen_fim
    
    @fim.setter
    def fim(self, valor):
        self.__isen_fim = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        