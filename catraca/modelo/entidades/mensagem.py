#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Mensagem(object):
    
    def __init__(self):
        self.__mens_id = None
        self.__mens_inicializacao = None
        self.__mens_saldacao = None
        self.__mens_aguardacartao = None
        self.__mens_erroleitor = None
        self.__mens_bloqueioacesso = None
        self.__mens_liberaacesso = None
        self.__mens_semcredito = None
        self.__mens_semcadastro = None
        self.__mens_cartaoinvalido = None
        self.__mens_turnoinvalido = None
        self.__mens_datainvalida = None
        self.__mens_cartaoutilizado = None
        self.__mens_institucional1 = None
        self.__mens_institucional2 = None
        self.__mens_institucional3 = None
        self.__mens_institucional4 = None
        self.__catraca = None
    
    @property
    def id(self):
        return self.__mens_id
    
    @id.setter
    def id(self, valor):
        self.__mens_id = valor
        
    @property
    def msg_inicializacao(self):
        return self.__mens_inicializacao
    
    @msg_inicializacao.setter
    def msg_inicializacao(self, valor):
        self.__mens_inicializacao = valor
        
    @property
    def msg_saldacao(self):
        return self.__mens_saldacao
    
    @msg_saldacao.setter
    def msg_saldacao(self, valor):
        self.__mens_saldacao = valor
        
    @property
    def msg_aguardacartao(self):
        return self.__mens_aguardacartao
    
    @msg_aguardacartao.setter
    def msg_aguardacartao(self, valor):
        self.__mens_aguardacartao = valor
        
    @property
    def msg_erroleitor(self):
        return self.__mens_erroleitor
    
    @msg_erroleitor.setter
    def msg_erroleitor(self, valor):
        self.__mens_erroleitor = valor
        
        
    @property
    def msg_bloqueioacesso(self):
        return self.__mens_bloqueioacesso
    
    @msg_bloqueioacesso.setter
    def msg_bloqueioacesso(self, valor):
        self.__mens_bloqueioacesso = valor
        
    @property
    def msg_liberaacesso(self):
        return self.__mens_liberaacesso
    
    @msg_liberaacesso.setter
    def msg_liberaacesso(self, valor):
        self.__mens_liberaacesso = valor
        
    @property
    def msg_semcredito(self):
        return self.__mens_semcredito
    
    @msg_semcredito.setter
    def msg_semcredito(self, valor):
        self.__mens_semcredito = valor
        
    @property
    def msg_semcadastro(self):
        return self.__mens_semcadastro
    
    @msg_semcadastro.setter
    def msg_semcadastro(self, valor):
        self.__mens_semcadastro = valor

    @property
    def msg_cartaoinvalido(self):
        return self.__mens_cartaoinvalido
    
    @msg_cartaoinvalido.setter
    def msg_cartaoinvalido(self, valor):
        self.__mens_cartaoinvalido = valor
        
    @property
    def msg_turnoinvalido(self):
        return self.__mens_turnoinvalido
    
    @msg_turnoinvalido.setter
    def msg_turnoinvalido(self, valor):
        self.__mens_turnoinvalido = valor
        
    @property
    def msg_datainvalida(self):
        return self.__mens_datainvalida
    
    @msg_datainvalida.setter
    def msg_datainvalida(self, valor):
        self.__mens_datainvalida = valor
          
    @property
    def msg_cartaoutilizado(self):
        return self.__mens_cartaoutilizado
    
    @msg_cartaoutilizado.setter
    def msg_cartaoutilizado(self, valor):
        self.__mens_cartaoutilizado = valor
        
    @property
    def msg_institucional1(self):
        return self.__mens_institucional1
    
    @msg_institucional1.setter
    def msg_institucional1(self, valor):
        self.__mens_institucional1 = valor
        
    @property
    def msg_institucional2(self):
        return self.__mens_institucional2
    
    @msg_institucional2.setter
    def msg_institucional2(self, valor):
        self.__mens_institucional2 = valor
        
    @property
    def msg_institucional3(self):
        return self.__mens_institucional3
    
    @msg_institucional3.setter
    def msg_institucional3(self, valor):
        self.__mens_institucional3 = valor
        
    @property
    def msg_institucional4(self):
        return self.__mens_institucional4
    
    @msg_institucional4.setter
    def msg_institucional4(self, valor):
        self.__mens_institucional4 = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        