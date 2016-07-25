#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Vinculo(object):
    def __init__(self):
        self.__vinc_id = None
        self.__vinc_avulso = None
        self.__vinc_inicio = None
        self.__vinc_fim = None
        self.__vinc_descricao = None
        self.__vinc_refeicoes = None
        self.__cartao = None
        self.__usuario = None
        
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
        return self.__vinc_id
    
    @id.setter
    def id(self, valor):
        self.__vinc_id = valor
        
    @property
    def avulso(self):
        return self.__vinc_avulso
    
    @avulso.setter
    def avulso(self, valor):
        self.__vinc_avulso = valor
        
    @property
    def inicio(self):
        return self.__vinc_inicio
    
    @inicio.setter
    def inicio(self, valor):
        self.__vinc_inicio = valor
        
    @property
    def fim(self):
        return self.__vinc_fim
    
    @fim.setter
    def fim(self, valor):
        self.__vinc_fim = valor
        
    @property
    def descricao(self):
        return self.__vinc_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__vinc_descricao = valor
        
    @property
    def refeicoes(self):
        return self.__vinc_refeicoes
    
    @refeicoes.setter
    def refeicoes(self, valor):
        self.__vinc_refeicoes = valor
        
    @property
    def cartao(self):
        return self.__cartao

    @cartao.setter
    def cartao(self, obj):
        self.__cartao = obj
        
    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, obj):
        self.__usuario = obj
        