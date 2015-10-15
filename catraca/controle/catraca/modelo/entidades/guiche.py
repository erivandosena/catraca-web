#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Guiche(object):
    
    def __init__(self):
        self.__guic_id = None
        self.__guic_abertura = None
        self.__guic_encerramento = None
        self.__guic_ativo = None
        self.__unidade = None
        self.__usuario = None
    
    @property
    def id(self):
        return self.__guic_id
    
    @id.setter
    def id(self, valor):
        self.__guic_id = valor
        
    @property
    def abertura(self):
        return self.__guic_abertura
    
    @abertura.setter
    def abertura(self, valor):
        self.__guic_abertura = valor
        
    @property
    def encerramento(self):
        return self.__guic_encerramento
    
    @encerramento.setter
    def encerramento(self, valor):
        self.__guic_encerramento = valor
        
    @property
    def ativo(self):
        return self.__guic_ativo
    
    @ativo.setter
    def ativo(self, valor):
        self.__guic_ativo = valor
        
    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, obj):
        self.__unidade = obj
        
    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, obj):
        self.__usuario = obj
        