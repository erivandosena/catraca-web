#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        
    def __eq__(self, obj):
        return ((self.id, 
                 self.avulso, 
                 self.inicio, 
                 self.fim, 
                 self.descricao, 
                 self.refeicoes, 
                 self.cartao, 
                 self.usuario) == (obj.id, 
                                     obj.avulso, 
                                     obj.inicio, 
                                     obj.fim, 
                                     obj.descricao, 
                                     obj.refeicoes, 
                                     obj.cartao, 
                                     obj.usuario))
        
    def __ne__(self, obj):
        return not self == obj
     
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
        