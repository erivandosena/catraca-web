#!/usr/bin/env python
# -*- coding: latin-1 -*-


import json
import requests


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ServidorRestful(object):
    
    URL = 'http://10.5.0.15:27289/api/'

    def __init__(self):
        super(ServidorRestful, self).__init__()
        self.__usuario = "teste"
        self.__senha = "teste"
        
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, valor):
        self.__usuario = valor
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, valor):
        self.__senha = valor
        
    def obter_servidor(self):
        return self.URL
    