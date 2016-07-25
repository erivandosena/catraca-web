#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Mensagem(object):
    
    def __init__(self):
        self.__mens_id = None
        self.__mens_institucional1 = None
        self.__mens_institucional2 = None
        self.__mens_institucional3 = None
        self.__mens_institucional4 = None
        self.__catraca = None
        
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
        return self.__mens_id
    
    @id.setter
    def id(self, valor):
        self.__mens_id = valor
        
    @property
    def institucional1(self):
        return self.__mens_institucional1
    
    @institucional1.setter
    def institucional1(self, valor):
        self.__mens_institucional1 = valor
        
    @property
    def institucional2(self):
        return self.__mens_institucional2
    
    @institucional2.setter
    def institucional2(self, valor):
        self.__mens_institucional2 = valor
        
    @property
    def institucional3(self):
        return self.__mens_institucional3
    
    @institucional3.setter
    def institucional3(self, valor):
        self.__mens_institucional3 = valor
        
    @property
    def institucional4(self):
        return self.__mens_institucional4
    
    @institucional4.setter
    def institucional4(self, valor):
        self.__mens_institucional4 = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        