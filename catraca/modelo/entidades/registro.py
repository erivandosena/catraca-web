#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Registro(object):

    def __init__(self):
        super(Registro, self).__init__()
        self.__regi_id = None
        self.__regi_data = None
        self.__regi_valor_pago = None
        self.__regi_valor_custo = None
        self.__cartao = None
        self.__turno = None
        self.__catraca = None
 
    @property
    def id(self):
        return self.__regi_id
    
    @id.setter
    def id(self, valor):
        self.__regi_id = valor
        
    @property
    def data(self):
        return self.__regi_data
    
    @data.setter
    def data(self, valor):
        self.__regi_data = valor
        
    @property
    def pago(self):
        return self.__regi_valor_pago
    
    @pago.setter
    def pago(self, valor):
        self.__regi_valor_pago = valor
        
    @property
    def custo(self):
        return self.__regi_valor_custo
    
    @custo.setter
    def custo(self, valor):
        self.__regi_valor_custo = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        
    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, obj):
        self.__turno = obj
        
    @property
    def catraca(self):
        return self.__catraca

    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        