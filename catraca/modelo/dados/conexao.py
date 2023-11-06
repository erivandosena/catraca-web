#!/usr/bin/env python
# -*- coding: utf-8 -*-


import psycopg2
import sqlite3
from psycopg2 import extras
from psycopg2 import extensions
from psycopg2 import DataError
from psycopg2 import ProgrammingError
from psycopg2 import OperationalError
from catraca.logs import Logs


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class ConexaoFactory(object):
    
    log = Logs()
    
    def __init__(self):
        super(ConexaoFactory, self).__init__()
        self.__POSTGRESQL = 1
        self.__SQLITE = 2
        self.__extras = extras
        self.__extensoes = extensions
        self.data_error = DataError
        self.programming_error = ProgrammingError
        self.operational_error = OperationalError

    @property
    def extras(self):
        return self.__extras
    
    @property
    def extensoes(self):
        return self.__extensoes
    
    def conexao(self, tipo_banco):
        con = None
        #self.__factory = tipo_banco
        try:
            str_conexao = "dbname='%s' user='%s' host='%s' password='%s'" % ("desenvolvimento", "postgres", "localhost", "postgres")
            # PostgreSQL
            if (tipo_banco == self.__POSTGRESQL):
                con = psycopg2.connect(str_conexao)
            # SQLite
            if (tipo_banco == self.__SQLITE):
                str_conexao = "'%s'" % (os.path.join(os.path.dirname(os.path.abspath(__file__)),"banco.db"))
                con = sqlite3.connect(str_conexao)
            #print "BD-CONEXAO ABERTA!"
            return con
        
        except Exception as excecao:
            print excecao
            self.log.logger.critical('Erro na conexao com banco de dados.', exc_info=True)
            
