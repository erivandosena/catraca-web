#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from tipo import Tipo
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TipoDAO(object):
    
    log = Logs()

    def __init__(self):
        super(TipoDAO, self).__init__()
        self.__erro = None
        self.__con = None
        self.__factory = None
        self.__fecha = None
    
    @property
    def aviso(self):
        return self.__aviso

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
            self.__aviso = str(e)
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
        finally:
            pass
        
    def busca(self, *arg):
        obj = Tipo()
        list = []
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT tipo_id, tipo_nome, tipo_vlr_credito FROM tipo WHERE tipo_id = " + str(id)
        elif id is None:
            sql = "SELECT tipo_id, tipo_nome, tipo_vlr_credito FROM tipo"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
                        obj.valor = dados[2]
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela tipo.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM tipo WHERE tipo_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE tipo SET " +\
                              "tipo_nome = '" + str(obj.nome) + "', " +\
                              "tipo_vlr_credito = " + str(obj.valor) +\
                              " WHERE "\
                              "tipo_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO tipo("\
                              "tipo_nome, "\
                              "tipo_vlr_credito) VALUES ('" +\
                              obj.nome + "', " +\
                              str(obj.valor) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.__con.commit()
                    self.__aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.__aviso = msg
                return False
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela tipo.', exc_info=True)
            return False
        finally:
            pass
        