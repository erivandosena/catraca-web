#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Tipo(object):
    
    def __init__(self):
        self.__tipo_id = None
        self.__tipo_nome = None
        self.__tipo_valor = None
        
    def __eq__(self, outro):
        if outro is None:
            return False
        return (self.id, self.nome, self.valor) == (outro.id, outro.nome, outro.valor)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
        #return not self == outro
        
#     def __eq__(self, obj):
#         return ((self.id, 
#                  self.nome, 
#                  self.valor) == (obj.id, 
#                                      obj.nome, 
#                                      obj.valor))
#         
#     def __ne__(self, obj):
#         return not self.__eq__(obj)
    
    @property
    def id(self):
        return self.__tipo_id
    
    @id.setter
    def id(self, valor):
        self.__tipo_id = valor
    
    @property
    def nome(self):
        return self.__tipo_nome
    
    @nome.setter
    def nome(self, valor):
        self.__tipo_nome = valor
    
    @property
    def valor(self):
        return self.__tipo_valor
    
    @valor.setter
    def valor(self, valor):
        self.__tipo_valor = valor
        