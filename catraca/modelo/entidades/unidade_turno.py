#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeTurno(object):
    def __init__(self):
        self.__untu_id = None
        self.__turno = None
        self.__unidade = None
        
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
        return self.__untu_id
    
    @id.setter
    def id(self, valor):
        self.__untu_id = valor
        
    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, obj):
        self.__turno = obj
        
    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, obj):
        self.__unidade = obj
        