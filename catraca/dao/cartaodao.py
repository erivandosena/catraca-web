#!/usr/bin/env python
# -*- coding: latin-1 -*-

from cartao import Cartao
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
    
#         try:
#             conexao = ConexaoFactory()
#             self.__con = conexao.getConexao(1) #use 1=PostgreSQL 2=MySQL 3=SQLite
#             self.__factory = conexao.getFactory()
#         except Exception, e:
#             self.__erro = str(e)

    def abre_conexao(self):
        try:
            conexao_bd = ConexaoFactory()
            self.__con = conexao_bd.conexao = 1 #use 1=PostgreSQL 2=MySQL 3=SQLite
            self.__factory = conexao_bd.factory
            return self.__con.cursor()
        except Exception, e:
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
            self.__erro = str(e)
        finally:
            pass
 
    # Select por codigo ou id do cartao
    def busca_id(self, id):
        obj = Cartao()
        sql = "SELECT cart_id, "\
              "cart_numero, "\
              "cart_qtd_creditos, "\
              "cart_vlr_credito, "\
              "cart_tipo, "\
              "cart_dt_acesso "\
              "FROM cartao WHERE "\
              "cart_id = " + str(id) +\
              " OR cart_numero = " + str(id)
        try:
            cursor = self.abre_conexao()#self.__con.cursor()
            cursor.execute(sql)
            dados = cursor.fetchone()
            # Carrega objeto
            obj.id = dados[0]
            obj.numero = dados[1]
            obj.creditos = dados[2]
            obj.valor = dados[3]
            obj.tipo = dados[4]
            obj.data = dados[5]    
            return obj    
        except Exception, e:
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
            self.__erro = str(e)
        finally:
            pass

    # Insert
    def insere(self, obj):
        sql = "INSERT INTO cartao("\
              "cart_numero, "\
              "cart_qtd_creditos, "\
              "cart_vlr_credito, "\
              "cart_tipo, "\
              "cart_dt_acesso) VALUES (" +\
              str(obj.numero) + ", " +\
              str(obj.creditos) + ", " +\
              str(obj.valor) + ", " +\
              str(obj.tipo) + ", " +\
              str(obj.data) + ")"
        try:
            #cursor = self.__con.cursor()
            cursor = self.abre_conexao()
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
             "cart_vlr_credito = " + str(obj.valor) + ", " +\
             "cart_tipo = " + str(obj.tipo) + ", " +\
             "cart_dt_acesso = " + str(obj.data) +\
             " WHERE "\
             "cart_id = " + str(obj.id)
       try:
           cursor = self.abre_conexao()#self.__con.cursor()
           cursor.execute(sql)
           #self.__con.commit()
           return True
       except Exception, e:
           self.log.logger.error('Erro ao realizar UPDATE na tabela cartao.', exc_info=True)
           self.__erro = str(e)
           return False
       finally:
           pass
    
    # Delete
    def exclui(self, obj):
        sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
        try:
            #cursor = self.__con.cursor()
            cursor = self.abre_conexao()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar DELETE na tabela cartao.', exc_info=True)
            self.__erro = str(e)
            return False
        
    