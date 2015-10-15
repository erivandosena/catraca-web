#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.logs import Logs

__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class ConexaoGenerica(object):
    
    log = Logs()

    def __init__(self):
        super(ConexaoGenerica, self).__init__()
        self.__aviso = None
        self.__con = None
        self.__factory = None
        self.__fecha = None

    def aviso(self):
        return self.__aviso

    def commit(self):
        return self.__con.commit()

    def rollback(self):
        return self.__con.rollback()

    def fecha_conexao(self):
        return self.__con.close()

    def conexao_status(self):
        if self.__con is not None:
            if self.__con.closed:
                return False
            else:
                return True
        else:
            return False

    def abre_conexao(self):
        try:
            conexao_factory = ConexaoFactory()
            self.__con = conexao_factory.conexao(1) #use 1=PostgreSQL 2=MySQL 3=SQLite
            self.__con.autocommit = False
            self.__factory = conexao_factory.factory
            return self.__con
        except Exception, e:
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
            self.__aviso = str(e)
        finally:
            pass
        