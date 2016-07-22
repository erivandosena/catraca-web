#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Unidade(object):
    
    def __init__(self):
        self.__unid_id = None
        self.__unid_nome = None
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.nome) == (obj.id, 
                                     obj.nome))
        
    def __ne__(self, obj):
        return not self == obj
     
    @property
    def id(self):
        return self.__unid_id
    
    @id.setter
    def id(self, valor):
        self.__unid_id = valor
    
    @property
    def nome(self):
        return self.__unid_nome
    
    @nome.setter
    def nome(self, valor):
        self.__unid_nome = valor
        