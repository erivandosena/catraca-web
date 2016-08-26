#!/usr/bin/env python
# -*- coding: latin-1 -*-


import requests
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ServidorRestful(object):
    
    #URL = 'http://10.5.0.123:27289/api/'
    #URL = 'catraca.unilab.edu.br:27289/api/'
    #URL = 'http://10.5.0.15:27289/api/'
    
    def __init__(self):
        super(ServidorRestful, self).__init__()
        self.URL = 'http://10.5.0.123:27289/api/'
        self.__usuario = "catraca"
        self.__senha = "CaTr@CaUniLab2015"
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
#         sessao = requests.Session()    
        with requests.Session() as sessao:
            sessao.timeout = 10
            sessao.auth = (self.usuario, self.senha)
            sessao.headers = {'Content-type': 'application/json'}
            return sessao

    def obter_servidor(self):
        #Singleton
        try:
            if self.instancia_sessao is None:
                self.instancia_sessao = self.obter_conexao()
            return self.instancia_sessao
        except Timeout as e:
            print "Tempo desolicitacao expirada!", e
            return None
        except HTTPError as e:
            print "Resposta HTTP invalida!", e
            return None
        except TooManyRedirects as e:
            print "Numero de redirecionamentos excedido!", e
            return None
        except RequestException as e:
            print "Erro no request!", e
            return None
        except ConnectionError as e:
            print "Falha na conexao com o host!", e
            return None
        except Exception as e:
            print "Erro geral!", e
            return None
        