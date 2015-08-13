#!/usr/bin/env python
# -*- coding: latin-1 -*-

from tipo import Tipo

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Perfil(object):

    def __init__(self):
        super(Perfil, self).__init__()
        self.__perf_id = None
        self.__perf_nome = None
        self.__perf_email = None
        self.__perf_tel = None
        self.__perf_datanascimento = None
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
    def telefone(self):
        return self.__perf_tel
    
    @telefone.setter
    def telefone(self, valor):
        self.__perf_tel = valor
        
    @property
    def nascimento(self):
        return self.__perf_datanascimento
    
    @nascimento.setter
    def nascimento(self, valor):
        self.__perf_datanascimento = valor
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo = obj