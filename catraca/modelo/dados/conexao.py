#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3
import urlparse
import psycopg2
#import mysql.connector
from contextlib import closing
from catraca.logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
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
        
    @property
    def erro_conexao(self):
        return self.__erroCon
    
    @property
    def factory(self):
        return self.__factory
    
    def conexao(self, tipo_banco):
        con = None
        self.__factory = tipo_banco
        try:
            #str_conexao = self.obtem_dns("desenvolvimento","postgres","localhost","postgres", tipo_banco)
            str_conexao = "dbname='%s' user='%s' host='%s' password='%s'" % ("desenvolvimento", "postgres", "localhost", "postgres")
            # PostgreSQL
            if (tipo_banco == self.__POSTGRESQL):
                try:
                    con = psycopg2.connect(str_conexao)
                except Exception as excecao:
                    self.__erroCon = str(excecao)
                    self.log.logger.critical('Erro na conexao com PostgreSQL.', exc_info=True)
                finally:
                    pass
            # MySQL
            if (tipo_banco == self.__MYSQL):
                str_conexao = "user='%s' password='%s' host='%s' database='%s'" % (usuario, senha, host, bd)
                try:
                    #con = mysql.connector.connect(str_conexao)
                    pass
                except Exception as excecao:
                    self.__erroCon = str(excecao)
                    self.log.logger.critical('Erro na conexao com MySQL.', exc_info=True)
                finally:
                    pass
            # SQLite
            if (tipo_banco == self.__SQLITE):
                str_conexao = "'%s'" % (os.path.join(os.path.dirname(os.path.abspath(__file__)),"banco.db"))
                try:
                    con = sqlite3.connect(str_conexao)
                except Exception, e:
                    self.__erroCon = str(e)
                    self.log.logger.critical('Erro na conexao com SQLite.', exc_info=True)
                finally:
                    pass
            return con
        except Exception as excecao:
            self.__erroCon = str(excecao)
            self.log.logger.critical('Erro na string de conexao com banco de dados.', exc_info=True)
        finally:
            pass
        
    #metodo destrutor
#     def __del__(self):
#         print "Conexão BD finalizada!"
#         del self
        