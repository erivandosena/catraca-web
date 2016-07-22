#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Cartao(object):
    
    def __init__(self):
        self.__cart_id = None
        self.__cart_numero = None
        self.__cart_creditos = None
        self.__tipo = None
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.numero, 
                 self.creditos, 
                 self.tipo) == (obj.id, 
                                     obj.numero, 
                                     obj.creditos, 
                                     obj.tipo))
        
    def __ne__(self, obj):
        return not self == obj
     
    @property
    def id(self):
        return self.__cart_id
    
    @id.setter
    def id(self, valor):
        self.__cart_id = valor
    
    @property
    def numero(self):
        return self.__cart_numero
    
    @numero.setter
    def numero(self, valor):
        self.__cart_numero = valor
    
    @property
    def creditos(self):
        return self.__cart_creditos
    
    @creditos.setter
    def creditos(self, valor):
        self.__cart_creditos = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo = obj
        