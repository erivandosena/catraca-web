#!/usr/bin/env python
# -*- coding: latin-1 -*-


import requests


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ServidorRestful(object):
    
    URL = 'http://200.129.19.65:27289/api/'
    #URL = 'http://10.5.0.15:27289/api/'
    timeout_conexao = 0.2 #0.0009

    def __init__(self):
        super(ServidorRestful, self).__init__()
        self.__usuario = "catraca"
        self.__senha = "CaTr@CaUniLab2015"
        
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
        try:
            response = requests.get(url=self.URL, timeout=(self.timeout_conexao, 10.0))
        except requests.exceptions.ConnectTimeout as excecao:
            print "rede off"
            return None
        except Exception as excecao:
            print "rede off"
            return None
        else:
            print "rede ok"
            return self.URL
        finally:
            pass
        