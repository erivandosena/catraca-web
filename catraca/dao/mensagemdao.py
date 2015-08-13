#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class MensagemDAO(object):
    
    log = Logs()

    def __init__(self):
        super(MensagemDAO, self).__init__()
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

    def busca_mensagem(self):
        obj = Mensagem()
        sql = "SELECT mens_id, mens_inicializacao, mens_saldacao, mens_aguardacartao, "\
        "mens_erroleitor, mens_bloqueioacesso, mens_liberaacesso, mens_semcredito, "\
        "mens_semcadastro, mens_cartaoinvalido, mens_turnoinvalido, mens_datainvalida, "\
        "mens_cartaoutilizado, mens_institucional1, mens_institucional2, "\
        "mens_institucional3, mens_institucional4 FROM mensagem"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.msg_id = dados[1]
                    obj.msg_inicializacao = dados[2]
                    obj.msg_saldacao = dados[3]
                    obj.msg_aguardacartao = dados[4]
                    obj.msg_erroleitor = dados[5]
                    obj.msg_bloqueioacesso = dados[6]
                    obj.msg_liberaacesso = dados[7]
                    obj.msg_semcredito = dados[8]
                    obj.msg_semcadastro = dados[9]
                    obj.msg_cartaoinvalido = dados[10]
                    obj.msg_turnoinvalido = dados[11]
                    obj.msg_datainvalida = dados[12]
                    obj.msg_cartaoutilizado = dados[13]
                    obj.msg_institucional1 = dados[14]
                    obj.msg_institucional2 = dados[15]
                    obj.msg_institucional3 = dados[16]
                    obj.msg_institucional4 = dados[17]
                    return obj
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela mensagem.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO mensagem("\
              "mens_inicializacao, "\
              "mens_saldacao, "\
              "mens_aguardacartao, "\
              "mens_erroleitor, "\
              "mens_bloqueioacesso, "\
              "mens_liberaacesso, "\
              "mens_semcredito, "\
              "mens_semcadastro, "\
              "mens_cartaoinvalido, "\
              "mens_turnoinvalido, "\
              "mens_datainvalida, "\
              "mens_cartaoutilizado, "\
              "mens_institucional1, "\
              "mens_institucional2, "\
              "mens_institucional3, "\
              "mens_institucional4) VALUES (" +\
              str(obj.msg_inicializacao) + ", " +\
              str(obj.msg_saldacao) + ", " +\
              str(obj.msg_aguardacartao) + ", " +\
              str(obj.msg_erroleitor) + ", " +\
              str(obj.msg_bloqueioacesso) + ", " +\
              str(obj.msg_liberaacesso) + ", " +\
              str(obj.msg_semcredito) + ", " +\
              str(obj.msg_semcadastro) + ", " +\
              str(obj.msg_cartaoinvalido) + ", " +\
              str(obj.msg_turnoinvalido) + ", " +\
              str(obj.msg_datainvalida) + ", " +\
              str(obj.msg_cartaoutilizado) + ", " +\
              str(obj.msg_institucional1) + ", " +\
              str(obj.msg_institucional2) + ", " +\
              str(obj.msg_institucional3) + ", " +\
              str(obj.msg_institucional4) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela mensagem.', exc_info=True)
            self.__erro = str(e)
            return False

    def altera(self, obj):
       sql = "UPDATE mensagem SET " +\
            "mens_inicializacao = " + str(obj.msg_inicializacao) + ", " +\
            "mens_saldacao = " + str(obj.msg_saldacao) + ", " +\
            "mens_aguardacartao = " + str(obj.msg_aguardacartao) + ", " +\
            "mens_erroleitor = " + str(obj.msg_erroleitor) + ", " +\
            "mens_bloqueioacesso = " + str(obj.msg_bloqueioacesso) + ", " +\
            "mens_liberaacesso = " + str(obj.msg_liberaacesso) + ", " +\
            "mens_semcredito = " + str(obj.msg_semcredito) + ", " +\
            "mens_semcadastro = " + str(obj.msg_semcadastro) + ", " +\
            "mens_cartaoinvalido = " + str(obj.msg_cartaoinvalido) + ", " +\
            "mens_turnoinvalido = " + str(obj.msg_turnoinvalido) + ", " +\
            "mens_datainvalida = " + str(obj.msg_datainvalida) + ", " +\
            "mens_cartaoutilizado = " + str(obj.msg_cartaoutilizado) + ", " +\
            "mens_institucional1 = " + str(obj.msg_institucional1) + ", " +\
            "mens_institucional2 = " + str(obj.msg_institucional2) + ", " +\
            "mens_institucional3 = " + str(obj.msg_institucional3) + ", " +\
            "mens_institucional4 = " + str(obj.msg_institucional4) +\
            " WHERE "\
            "mens_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                return True
       except Exception, e:
           self.__erro = str(e)
           self.log.logger.error('Erro ao realizar UPDATE na tabela mensagem.', exc_info=True)
           return False
       finally:
           pass
    
    def exclui(self, obj):
        sql = "DELETE FROM mensagem WHERE mens_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela mensagem.', exc_info=True)
            return False
        finally:
            pass
        
    