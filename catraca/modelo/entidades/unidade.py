#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Unidade(object):
    
    def __init__(self):
        self.__unid_id = None
        self.__unid_nome = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
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
        