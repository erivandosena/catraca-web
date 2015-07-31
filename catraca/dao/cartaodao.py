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

#         try:
#             conexao = ConexaoFactory()
#             self.__con = conexao.getConexao(1) #use 1=PostgreSQL 2=MySQL 3=SQLite
#             self.__factory = conexao.getFactory()
#         except Exception, e:
#             self.__erro = str(e)

    def abre_conexao(self):
        try:
            conexao = ConexaoFactory()
            self.__con = conexao.getConexao(1) #use 1=PostgreSQL 2=MySQL 3=SQLite
            self.__factory = conexao.getFactory()
            return self.__con.cursor()
        except Exception, e:
            self.__erro = str(e)
 
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
            obj.setId(dados[0])
            obj.setNumero(dados[1])
            obj.setCreditos(dados[2])
            obj.setValor(dados[3])
            obj.setTipo(dados[4])
            obj.setData(dados[5])    
            return obj    
        except Exception, e:
            self.__erro = str(e)
        finally:
            pass
#             self.__con.close()
#             print "Conexão finalizada.(Select)"
#             self.log.logger.debug('Conexão com o Bd finalizada.')
            

    # Insert
    def insere(self, obj):
        sql = "INSERT INTO cartao("\
              "cart_numero, "\
              "cart_qtd_creditos, "\
              "cart_vlr_credito, "\
              "cart_tipo, "\
              "cart_dt_acesso) VALUES (" +\
              str(obj.getNumero()) + ", " +\
              str(obj.getCreditos()) + ", " +\
              str(obj.getValor()) + ", " +\
              str(obj.getTipo()) + ", " +\
              str(obj.getData()) + ")"
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False

    # Update
    def altera(self, obj):
       sql = "UPDATE cartao SET " +\
             "cart_numero = " + str(obj.getNumero()) + ", " +\
             "cart_qtd_creditos = " + str(obj.getCreditos()) + ", " +\
             "cart_vlr_credito = " + str(obj.getValor()) + ", " +\
             "cart_tipo = " + str(obj.getTipo()) + ", " +\
             "cart_dt_acesso = " + str(obj.getData()) +\
             " WHERE "\
             "cart_id = " + str(obj.getId())
       try:
           cursor = self.abre_conexao()#self.__con.cursor()
           cursor.execute(sql)
           #self.__con.commit()
           return True
       except Exception, e:
           self.__erro = str(e)
           return False
       finally:
           pass
#            self.__con.close()
#            print "Conexão finalizada.(Update)"
#            self.log.logger.debug('Conexão com o Bd finalizada.')
    
    # Delete
    def exclui(self, obj):
        sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.getId())
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False

    def getErro(self):
        return self.__erro
    
    def getCommit(self):
        return self.__con.commit()
    
    def getRollback(self):
        return self.__con.rollback()
    
    def getFecha(self):
        return self.__con.close()
    
#     def __del__(self):
#             print "Conexão finalizada."
#             self.log.logger.debug('Conexão com o Bd finalizada.')
#             del self
#     
