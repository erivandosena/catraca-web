#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroOff(object):

    def __init__(self):
        super(RegistroOff, self).__init__()
        self.__reof_id = None
        self.__reof_data = None
        self.__reof_valor_pago = None
        self.__reof_valor_custo = None
        self.__cartao = None
        self.__catraca = None
 
    @property
    def id(self):
        return self.__reof_id
    
    @id.setter
    def id(self, valor):
        self.__reof_id = valor
        
    @property
    def data(self):
        return self.__reof_data
    
    @data.setter
    def data(self, valor):
        self.__reof_data = valor
        
    @property
    def pago(self):
        return self.__reof_valor_pago
    
    @pago.setter
    def pago(self, valor):
        self.__reof_valor_pago = valor
        
    @property
    def custo(self):
        return self.__reof_valor_custo
    
    @custo.setter
    def custo(self, valor):
        self.__reof_valor_custo = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        
    @property
    def catraca(self):
        return self.__catraca

    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        