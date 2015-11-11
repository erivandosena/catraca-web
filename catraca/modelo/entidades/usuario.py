#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Usuario(object):
    
    def __init__(self):
        self.__usua_id = None
        self.__usua_nome = None
        self.__usua_email = None
        self.__usua_login = None
        self.__usua_senha = None
        self.__usua_nivel = None
<<<<<<< HEAD
=======
        self.__id_base_externa = None
>>>>>>> remotes/origin/web_backend
    
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
        
<<<<<<< HEAD
=======
    @property
    def id_externo(self):
        return self.__id_base_externa
    
    @id_externo.setter
    def id_externo(self, valor):
        self.__id_base_externa = valor
>>>>>>> remotes/origin/web_backend
        