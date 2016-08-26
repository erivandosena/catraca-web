#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class ConexaoGenerica(ConexaoFactory):
    
    log = Logs()
    
    def __init__(self):
        super(ConexaoGenerica, self).__init__()
        ConexaoFactory.__init__(self)
#         self.__aviso = None
        self.__con = None
#         self.__factory = None
        self.__fecha = None
#         self.__extras = None
#         self.__extensoes = None
        
#     def aviso(self):
#         return self.__aviso
    
    def commit(self):
        return self.__con.commit()
    
    def rollback(self):
        return self.__con.rollback()
    
    def fecha_conexao(self):
        #print "BD-CONEXAO FECHADA!"
        self.__con.close()
        
#     @property
#     def extras(self):
#         return self.__extras
#     
#     @extras.setter
#     def extras(self, extra):
#         self.__extras = extra
#         
#     @property
#     def extensoes(self):
#         return self.__extensoes
#     
#     @extensoes.setter
#     def extensoes(self, extensao):
#         self.__extensoes = extensao
        
    def abre_conexao(self):
        try:
#             conexao_factory = ConexaoFactory()
#             self.extras = conexao_factory.extras
#             self.extensoes = conexao_factory.extensoes
#             self.daata_error = self.DataError
#             self.programming_error = self.ProgrammingError
#             self.operational_error = self.OperationalError
#             self.__factory = conexao_factory.factory
#             self.__con = conexao_factory.conexao(1) #use 1=PostgreSQL 2=MySQL 3=SQLite
            self.__con = self.conexao(1) #use 1=PostgreSQL 2=SQLite
            self.__con.autocommit=False
            self.__con.set_client_encoding('UTF8')
            return self.__con
        
        except Exception, e:
            print e
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
#             self.__aviso = str(e)
        
    def fecha_todas_conexoes(self):
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                sql = "SELECT pg_terminate_backend(procpid) FROM pg_stat_get_activity(NULL::integer) WHERE datid=(SELECT oid from pg_database where datname = 'desenvolvimento');"
                cursor.execute(sql)
        except Exception, e: 
            print e
        