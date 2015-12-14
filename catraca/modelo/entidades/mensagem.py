#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Mensagem(object):
    
    def __init__(self):
        self.__mens_id = None
        self.__mens_institucional1 = None
        self.__mens_institucional2 = None
        self.__mens_institucional3 = None
        self.__mens_institucional4 = None
        self.__catraca = None
    
    @property
    def id(self):
        return self.__mens_id
    
    @id.setter
    def id(self, valor):
        self.__mens_id = valor
        
    @property
    def institucional1(self):
        return self.__mens_institucional1
    
    @institucional1.setter
    def institucional1(self, valor):
        self.__mens_institucional1 = valor
        
    @property
    def institucional2(self):
        return self.__mens_institucional2
    
    @institucional2.setter
    def institucional2(self, valor):
        self.__mens_institucional2 = valor
        
    @property
    def institucional3(self):
        return self.__mens_institucional3
    
    @institucional3.setter
    def institucional3(self, valor):
        self.__mens_institucional3 = valor
        
    @property
    def institucional4(self):
        return self.__mens_institucional4
    
    @institucional4.setter
    def institucional4(self, valor):
        self.__mens_institucional4 = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        