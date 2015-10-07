#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Finalidade(object):

    def __init__(self):
        super(Finalidade, self).__init__()
        self.__fina_id = None
        self.__fina_nome = None
        
    @property
    def id(self):
        return self.__fina_id
    
    @id.setter
    def id(self, valor):
        self.__fina_id = valor
        
    @property
    def nome(self):
        return self.__fina_nome
    
    @nome.setter
    def nome(self, valor):
        self.__fina_nome = valor
        
        