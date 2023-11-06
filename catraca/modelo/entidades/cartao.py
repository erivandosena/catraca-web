#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Cartao(object):
    
    def __init__(self):
        self.__cart_id = None
        self.__cart_numero = None
        self.__cart_creditos = None
        self.__tipo_id = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    def json_encode(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        raise TypeError(repr(obj) + " nao JSON serializado")
    
    @property
    def id(self):
        return self.__cart_id
    
    @id.setter
    def id(self, valor):
        self.__cart_id = valor
    
    @property
    def numero(self):
        return self.__cart_numero
    
    @numero.setter
    def numero(self, valor):
        self.__cart_numero = valor
    
    @property
    def creditos(self):
        return self.__cart_creditos
    
    @creditos.setter
    def creditos(self, valor):
        self.__cart_creditos = valor
    
    @property
    def tipo(self):
        return self.__tipo_id
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo_id = obj
        