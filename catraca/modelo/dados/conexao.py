#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pwd
import socket
import sqlite3
import urlparse
import psycopg2
#import mysql.connector
from contextlib import closing
from catraca.logs import Logs
from catraca.util import Util


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
            str_conexao = self.obtem_dns("bd_teste","postgres","localhost","postgres", tipo_banco)
            # PostgreSQL
            if (tipo_banco == self.__POSTGRESQL):
                try:
                    con = psycopg2.connect(str_conexao)
                except Exception, e:
                    self.__erroCon = str(e)
                    self.log.logger.critical('Erro na conexao com PostgreSQL.', exc_info=True)
                finally:
                    pass
            # MySQL
            if (tipo_banco == self.__MYSQL):
                #str_conexao = "user='%s', password='%s', host='%s', database='%s'" % (usuario, senha, localhost, banco)
                try:
                    #con = mysql.connector.connect(str_conexao)
                    pass
                except Exception, e:
                    self.__erroCon = str(e)
                    self.log.logger.critical('Erro na conexao com MySQL.', exc_info=True)
                finally:
                    pass
            # SQLite
            if (tipo_banco == self.__SQLITE):
                #str_conexao = "'%s'" % (os.path.join(os.path.dirname(os.path.abspath(__file__)),"banco.db"))
                try:
                    con = sqlite3.connect(str_conexao)
                except Exception, e:
                    self.__erroCon = str(e)
                    self.log.logger.critical('Erro na conexao com SQLite.', exc_info=True)
                finally:
                    pass
            return con
        except Exception, e:
            self.__erroCon = str(e)
            self.log.logger.critical('Erro na string de conexao com banco de dados.', exc_info=True)
        finally:
            pass
        
    def obtem_dns(self, bd = None, usuario = None, host = None, senha = None, tipo_banco = 1):
        try:
            if bd == None:
                bd = socket.gethostname()
            if usuario == None:
                usuario = pwd.getpwuid(os.getuid())[0]
            if host == None:
                host = Util().obtem_ip()
            if senha == None:
                senha = 'postgres'
            if tipo_banco == 1:
                dns = "dbname='%s' user='%s' host='%s' password='%s'" % (bd, usuario, host, senha)
            elif tipo_banco == 2:
                dns = "user='%s' password='%s' host='%s' database='%s'" % (usuario, senha, host, bd)
            elif tipo_banco == 3:
                dns = "'%s'" % (os.path.join(os.path.dirname(os.path.abspath(__file__)), str(bd)+".db"))
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao obter string de conexao.', exc_info=True)
        finally:
            return dns
        