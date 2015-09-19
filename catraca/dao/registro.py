#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Registro(object):

    def __init__(self):
        super(Registro, self).__init__()
        self.__regi_id = None
        self.__regi_datahora = None
        self.__regi_giro = 0
        self.__regi_valor = 0.00
        self.__cartao = None
        self.__turno = None

    @property
    def id(self):
        return self.__regi_id
    
    @id.setter
    def id(self, valor):
        self.__regi_id = valor
    
    @property
    def data(self):
        return self.__regi_datahora
    
    @data.setter
    def data(self, valor):
        self.__regi_datahora = valor
    
    @property
    def giro(self):
        return self.__regi_giro
    
    @giro.setter
    def giro(self, valor):
        self.__regi_giro = valor
    
    @property
    def valor(self):
        return self.__regi_valor
    
    @valor.setter
    def valor(self, valor):
        self.__regi_valor = valor
    
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
        
        