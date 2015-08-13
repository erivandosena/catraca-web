#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from cartao import Cartao
from perfil import Perfil
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoDAO(object):
    
    log = Logs()

    def __init__(self):
        super(CartaoDAO, self).__init__()
        self.__erro = None
        self.__con = None
        self.__factory = None
        self.__fecha = None
        
    @property
    def erro(self):
        return self.__erro

    @property
    def commit(self):
        return self.__con.commit()

    @property
    def rollback(self):
        return self.__con.rollback()

    @property
    def fecha_conexao(self):
        return self.__con.close()

    @property
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
            self.__erro = str(e)
        finally:
            pass
 
    # Select
    def busca_cartao(self, id):
        obj = Cartao()
        sql = "SELECT cart_id, "\
              "cart_numero, "\
              "cart_qtd_creditos, "\
              "perf_id "\
              "FROM cartao WHERE "\
              "cart_id = " + str(id) +\
              " OR cart_numero = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                # Carrega objeto
                if dados:
                    obj.id = dados[0]
                    obj.numero = dados[1]
                    obj.creditos = dados[2] 
                    obj.perfil = Perfil().busca_perfil(dados[3])
                    return obj
                else:
                    return None
        except Exception, e:
            #if self.conexao_status:
            #    self.fecha_conexao
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass

    # Insert
    def insere(self, obj):
        sql = "INSERT INTO cartao("\
              "cart_numero, "\
              "cart_qtd_creditos, "\
              "perf_id) VALUES (" +\
              str(obj.numero) + ", " +\
              str(obj.creditos) + ", " +\
              str(obj.perfil) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                #cursor = self.__con.cursor()
                #cursor = self.abre_conexao()
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela cartao.', exc_info=True)
            self.__erro = str(e)
            return False

    # Update
    def altera(self, obj):
       sql = "UPDATE cartao SET " +\
             "cart_numero = " + str(obj.numero) + ", " +\
             "cart_qtd_creditos = " + str(obj.creditos) + ", " +\
             "perf_id = " + str(obj.perfil) +\
             " WHERE "\
             "cart_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                #self.__con.commit()
                return True
       except Exception, e:
           self.__erro = str(e)
           self.log.logger.error('Erro ao realizar UPDATE na tabela cartao.', exc_info=True)
           return False
       finally:
           pass
    
    # Delete
    def exclui(self, obj):
        sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                #cursor = self.__con.cursor()
                #cursor = self.abre_conexao()
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela cartao.', exc_info=True)
            return False
        finally:
            pass
        
    