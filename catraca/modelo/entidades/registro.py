#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal
import datetime


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Registro(object):

    def __init__(self):
        super(Registro, self).__init__()
        self.__regi_id = None
        self.__regi_data = None
        self.__regi_valor_pago = None
        self.__regi_valor_custo = None
        self.__cartao = None
        self.__catraca = None
        self.__vinculo = None
        
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
        return self.__regi_id
    
    @id.setter
    def id(self, valor):
        self.__regi_id = valor
        
    @property
    def data(self):
        return self.__regi_data
    
    @data.setter
    def data(self, valor):
        self.__regi_data = valor
        
    @property
    def pago(self):
        return self.__regi_valor_pago
    
    @pago.setter
    def pago(self, valor):
        self.__regi_valor_pago = valor
        
    @property
    def custo(self):
        return self.__regi_valor_custo
    
    @custo.setter
    def custo(self, valor):
        self.__regi_valor_custo = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        
    @property
    def catraca(self):
        return self.__catraca

    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        
    @property
    def vinculo(self):
        return self.__vinculo

    @vinculo.setter
    def vinculo(self, obj):
        self.__vinculo = obj
        