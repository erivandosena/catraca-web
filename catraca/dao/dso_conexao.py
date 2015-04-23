#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class ConexaoFactory():

    def __init__(self):
        super(ConexaoFactory, self).__init__()
        self.__POSTGRESQL = 1
        self.__MYSQL = 2
        self.__erroCon = None
        self.__factory = None
 
    # Cria Factory para objetos
    def getConexao(self, banco):
 
        # Define conexão e fonte de dados
        con = None
        self.__factory = banco
 
        # Cria string de conexãopostgres
        if (banco == self.__POSTGRESQL):
            sconexao = "user/pass@localhost/XE"
            try:
                con = cx_Oracle.connect(sconexao)
            except Exception, e:
                self.__erroCon = str(e)
 
        # Cria string de conexãomysql
        if (banco == self.__MYSQL):
            sconexao = "DATABASE=DEVA" + \
                       ";HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;" + \
                       "UID=user;" + \
                       "PWD=pass"
            try:
                self.__IBMDriver = ibm_db
                con = ibm_db.connect(sconexao, "", "")
            except Exception, e:
                self.__erroCon = str(e)
 
        return con
 
    # Retorna Erros
    def getErros(self):
        return self.__erroCon
 
    # Retorna Factory da conexão
    def getFactory(self):
        return self.__factory
