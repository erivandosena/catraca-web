#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import datetime


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Isencao(object):
    
    def __init__(self):
        self.__isen_id = None
        self.__isen_inicio = None
        self.__isen_fim = None
        self.__cartao = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    def json_encode(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        raise TypeError(repr(obj) + " nao JSON serializado")
    
    
    @property
    def id(self):
        return self.__isen_id
    
    @id.setter
    def id(self, valor):
        self.__isen_id = valor
        
    @property
    def inicio(self):
        return self.__isen_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__isen_inicio = valor
        
    @property
    def fim(self):
        return self.__isen_fim
    
    @fim.setter
    def fim(self, valor):
        self.__isen_fim = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        