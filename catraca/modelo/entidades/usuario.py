#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Usuario(object):
    
    def __init__(self):
        self.__usua_id = None
        self.__usua_nome = None
        self.__usua_email = None
        self.__usua_login = None
        self.__usua_senha = None
        self.__usua_nivel = None
        self.__id_base_externa = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    @property
    def id(self):
        return self.__usua_id
    
    @id.setter
    def id(self, valor):
        self.__usua_id = valor
        
    @property
    def nome(self):
        return self.__usua_nome
    
    @nome.setter
    def nome(self, valor):
        self.__usua_nome = valor
        
    @property
    def email(self):
        return self.__usua_email
    
    @email.setter
    def email(self, valor):
        self.__usua_email = valor
        
    @property
    def login(self):
        return self.__usua_login
    
    @login.setter
    def login(self, valor):
        self.__usua_login = valor
    
    @property
    def senha(self):
        return self.__usua_senha
    
    @senha.setter
    def senha(self, valor):
        self.__usua_senha = valor
        
    @property
    def nivel(self):
        return self.__usua_nivel
    
    @nivel.setter
    def nivel(self, valor):
        self.__usua_nivel = valor
        
    @property
    def idexterno(self):
        return self.id_base_externa
    
    @idexterno.setter
    def idexterno(self, valor):
        self.id_base_externa = valor
        