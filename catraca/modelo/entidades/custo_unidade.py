#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib

__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoUnidade(object):
    
    def __init__(self):
        self.__cuun_id = None
        self.__unid_id = None
        self.__cure_id = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=False, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    @property
    def id(self):
        return self.__cuun_id
    
    @id.setter
    def id(self, valor):
        self.__cuun_id = valor
    
    @property
    def unidade(self):
        return self.__unid_id
    
    @unidade.setter
    def unidade(self, valor):
        self.__unid_id = valor
    
    @property
    def custo(self):
        return self.__cure_id
    
    @custo.setter
    def custo(self, valor):
        self.__cure_id = valor
        