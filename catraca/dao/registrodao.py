#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from cartaodao import CartaoDAO
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroDAO(object):
    
    log = Logs()

    def __init__(self):
        super(RegistroDAO, self).__init__()
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

    def busca_registro_periodo(self, data1, data2):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_datahora, "\
              "regi_giro, "\
              "regi_valor, "\
              "cart_id "\
              "FROM registro WHERE "\
              "regi_datahora BETWEEN " + str(data1) +\
              " AND " + str(data2) +\
              " ORDER BY regi_datahora DESC"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.data = dados[1]
                    obj.giro = dados[2]
                    obj.valor = dados[3]
                    obj.cartao = CartaoDAO().busca_cartao(dados[4])
                    return obj
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO registro("\
              "regi_datahora, "\
              "regi_giro, "\
              "regi_valor, "\
              "cart_id) VALUES (" +\
              str(obj.data) + ", " +\
              str(obj.giro) + ", " +\
              str(obj.valor) + ", " +\
              str(obj.cartao.id) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela registro.', exc_info=True)
            self.__erro = str(e)
            return False

    def altera(self, obj):
       sql = "UPDATE registro SET " +\
             "regi_datahora = " + str(obj.data) + ", " +\
             "regi_giro = " + str(obj.giro) + ", " +\
             "regi_valor = " + str(obj.valor) + ", " +\
             "cart_id = " + str(obj.cartao.id) +\
             " WHERE "\
             "regi_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                return True
       except Exception, e:
           self.__erro = str(e)
           self.log.logger.error('Erro ao realizar UPDATE na tabela registro.', exc_info=True)
           return False
       finally:
           pass

    def exclui(self, obj):
        sql = "DELETE FROM registro WHERE regi_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela registro.', exc_info=True)
            return False
        finally:
            pass
        