#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoValido(object):
    
    def __init__(self):
        super(CartaoValido, self).__init__()
        self.__cart_id = None
        self.__cart_numero = None
        self.__cart_creditos = None
        self.__tipo_valor = None
        self.__vinc_refeicoes = None
        self.__vinc_descricao = None
        self.__nome_usuario = None
        self.__tipo = None
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
    def valor(self):
        return self.__tipo_valor
    
    @valor.setter
    def valor(self, valor):
        self.__tipo_valor = valor
        
    @property
    def refeicoes(self):
        return self.__vinc_refeicoes
    
    @refeicoes.setter
    def refeicoes(self, valor):
        self.__vinc_refeicoes = valor
        
    @property
    def descricao(self):
        return self.__vinc_descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__vinc_descricao = valor
    @property
    def nome(self):
        return self.__nome_usuario
    
    @nome.setter
    def nome(self, valor):
        self.__nome_usuario = valor

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, obj):
        self.__tipo = obj
        
    @property
    def vinculo(self):
        return self.__vinculo
    
    @vinculo.setter
    def vinculo(self, obj):
        self.__vinculo = obj
        