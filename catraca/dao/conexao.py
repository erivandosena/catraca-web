#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import psycopg2
#import mysql.connector
import sqlite3
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class ConexaoFactory(object):

    log = Logs()

    def __init__(self):
        super(ConexaoFactory, self).__init__()
        self.__POSTGRESQL = 1
        self.__MYSQL = 2
        self.__SQLITE = 3
        self.__erroCon = None
        self.__factory = None
 
    def getConexao(self, banco):
        con = None
        self.__factory = banco
        # PostgreSQL
        if (banco == self.__POSTGRESQL):
            str_conexao = "\
                    dbname='raspberry'\
                    user='postgres'\
                    host='localhost'\
                    password='postgres'\
                    "
            try:
                con = psycopg2.connect(str_conexao)
            except Exception, e:
                self.__erroCon = str(e)
            finally:
                pass
#                 #con.close()
#                 print "Conexão finalizada"
#                 self.log.logger.debug('Conexão com o Bd finalizada.')
                
        # MySQL
        if (banco == self.__MYSQL):
            str_conexao = "user='%s', password='%s', host='%s', database='%s'" % (usuario, senha, localhost, banco)
            try:
                #con = mysql.connector.connect(str_conexao)
                pass
            except Exception, e:
                self.__erroCon = str(e)
        # SQLite
        if (banco == self.__SQLITE):
            str_conexao = "'%s'" % (os.path.join(os.path.dirname(os.path.abspath(__file__)),"banco.db"))
            try:
                con = sqlite3.connect(str_conexao)
            except Exception, e:
                self.__erroCon = str(e)
        return con

    def getErros(self):
        return self.__erroCon
 
    def getFactory(self):
        return self.__factory
    