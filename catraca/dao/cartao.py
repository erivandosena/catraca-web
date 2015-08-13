#!/usr/bin/env python
# -*- coding: latin-1 -*-

from perfil import Perfil

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Cartao(object):

    def __init__(self):
        super(Cartao, self).__init__()
        self.__cart_id = None
        self.__cart_numero = None
        self.__cart_qtd_creditos = None
        self.__perfil = Perfil()
        
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
        return self.__cart_qtd_creditos
 
    @creditos.setter
    def creditos(self, valor):
        self.__cart_qtd_creditos = valor
        
    @property
    def perfil(self):
        return self.__perfil

    @perfil.setter
    def perfil(self, obj):
        self.__perfil = obj
        