#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.logs import Logs


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class ConexaoGenerica(ConexaoFactory):
    
    log = Logs()
    
    def __init__(self):
        super(ConexaoGenerica, self).__init__()
        ConexaoFactory.__init__(self)
        self.__con = None
        self.__fecha = None

    def commit(self):
        return self.__con.commit()
    
    def rollback(self):
        return self.__con.rollback()
    
    def fecha_conexao(self):
        #print "BD-CONEXAO FECHADA!"
        if not self.__con.closed:
            self.__con.close()
        
    def abre_conexao(self):
        try:
            self.__con = self.conexao(1) #use 1=PostgreSQL 2=SQLite
            self.__con.autocommit=False
            self.__con.set_client_encoding('UTF8')
            return self.__con
        
        except Exception, e:
            print e
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
            