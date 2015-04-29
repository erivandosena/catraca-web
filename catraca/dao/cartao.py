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
 
    def getId(self):
        return self.__cart_id
 
    def setId(self, valor):
        self.__cart_id = valor
 
    def getNumero(self):
        return self.__cart_numero
 
    def setNumero(self, valor):
        self.__cart_numero = valor
 
    def getCreditos(self):
        return self.__cart_qtd_creditos
 
    def setCreditos(self, valor):
        self.__cart_qtd_creditos = valor
 
    def getValor(self):
        return self.__cart_vlr_credito
 
    def setValor(self, valor):
        self.__cart_vlr_credito = valor
 
    def getTipo(self):
        return self.__cart_tipo
 
    def setTipo(self, valor):
        self.__cart_tipo = valor

    def getData(self):
        return self.__cart_dt_acesso

    def setData(self, valor):
        self.__cart_dt_acesso = valor
