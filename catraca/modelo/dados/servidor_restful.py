#!/usr/bin/env python
# -*- coding: latin-1 -*-


import requests


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class ServidorRestful(object):

    def __init__(self):
        super(ServidorRestful, self).__init__()
        self.URL = 'http://10.5.0.123:27289/api/'
        self.__usuario = "catraca"
        self.__senha = "catraca"
        self.instancia_sessao = None
        
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
        
    def obter_conexao(self):
        sessao = requests.Session() 
        try:   
            #with requests.Session() as sessao:
            sessao.timeout = 10
            sessao.auth = (self.usuario, self.senha)
            sessao.headers = {'Content-type': 'application/json'}
            return sessao
        finally:
            sessao.close()

    def obter_servidor(self):
        return self.obter_conexao()
#         #Singleton
#         if self.instancia_sessao is None:
#             self.instancia_sessao = self.obter_conexao()
#         return self.instancia_sessao
