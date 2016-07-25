#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal
import datetime

__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoRefeicao(object):
    
    def __init__(self):
        self.__cure_id = None
        self.__cure_valor = None
        self.__cure_data = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    def json_encode(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return str(obj)
        raise TypeError(repr(obj) + " nao JSON serializado")
    
    @property
    def id(self):
        return self.__cure_id
    
    @id.setter
    def id(self, valor):
        self.__cure_id = valor
    
    @property
    def valor(self):
        return self.__cure_valor
    
    @valor.setter
    def valor(self, valor):
        self.__cure_valor = valor
    
    @property
    def data(self):
        return self.__cure_data
    
    @data.setter
    def data(self, valor):
        self.__cure_data = valor
        