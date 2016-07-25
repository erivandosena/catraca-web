#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Turno(object):
    
    def __init__(self):
        self.__turn_id = None
        self.__turn_hora_inicio = None
        self.__turn_hora_fim = None
        self.__turn_descricao = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode_decimal, use_decimal=False, ensure_ascii=False, sort_keys=False, encoding='utf-8')).hexdigest()
    
    def json_encode_decimal(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        raise TypeError(repr(obj) + " nao JSON serializado")
    
    @property
    def id(self):
        return self.__turn_id
    
    @id.setter
    def id(self, valor):
        self.__turn_id = valor
        
    @property
    def inicio(self):
        return self.__turn_hora_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__turn_hora_inicio = valor
        
    @property
    def fim(self):
        return self.__turn_hora_fim
    
    @fim.setter
    def fim(self, valor):
        self.__turn_hora_fim = valor
        
    @property
    def descricao(self):
        return self.__turn_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__turn_descricao = valor
        