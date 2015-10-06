#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Transacao(object):
    
    def __init__(self):
        self.__tran_id = None
        self.__tran_valor = None
        self.__tran_descricao = None
        self.__tran_data = None
        self.__usuario = None
    
    @property
    def id(self):
        return self.__tran_id
    
    @id.setter
    def id(self, valor):
        self.__tran_id = valor
        
    @property
    def valor(self):
        return self.__tran_valor
    
    @valor.setter
    def valor(self, valor):
        self.__tran_valor = valor
        
    @property
    def descricao(self):
        return self.__tran_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__tran_descricao = valor
        
    @property
    def data(self):
        return self.__tran_data
    
    @data.setter
    def data(self, valor):
        self.__tran_data = valor
        
    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, obj):
        self.__usuario = obj
        