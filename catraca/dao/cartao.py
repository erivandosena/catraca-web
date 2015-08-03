#!/usr/bin/env python
# -*- coding: latin-1 -*-


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
        self.__cart_vlr_credito = None
        self.__cart_tipo = None
        self.__cart_dt_acesso = None

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
    def valor(self):
        return self.__cart_vlr_credito
 
    @valor.setter
    def valor(self, valor):
        self.__cart_vlr_credito = valor

    @property
    def tipo(self):
        return self.__cart_tipo

    @tipo.setter
    def tipo(self, valor):
        self.__cart_tipo = valor
    
    @property
    def data(self):
        return self.__cart_dt_acesso

    @data.setter
    def data(self, valor):
        self.__cart_dt_acesso = valor
