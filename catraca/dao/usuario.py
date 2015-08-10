#!/usr/bin/env python
# -*- coding: latin-1 -*-

from tipo import Tipo

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Usuario(object):

    def __init__(self):
        super(Usuario, self).__init__()
        self.__usua_id = None
        self.__usua_nome = None
        self.__usua_email = None
        self.__usua_login = None
        self.__usua_senha = None
        self.__usua_nivel = None
        self.__id_externo = None
        self.__usua_num_doc = None
        self.__tipo = Tipo()

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
    def externo(self):
        return self.__id_externo
    
    @externo.setter
    def externo(self, valor):
        self.__id_externo = valor
        
    @property
    def documento(self):
        return self.__usua_num_doc
    
    @documento.setter
    def documento(self, valor):
        self.__usua_num_doc = valor
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo = obj
        