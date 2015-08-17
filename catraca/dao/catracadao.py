#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from catraca import Catraca
from turno import Turno
from giro import Giro
from mensagem import Mensagem
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(object):
    
    log = Logs()

    def __init__(self):
        super(CatracaDAO, self).__init__()
        self.__aviso = None
        self.__con = None
        self.__factory = None
        self.__fecha = None
        
    @property
    def erro(self):
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
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
            self.__aviso = str(e)
        finally:
            pass
        
    def busca(self, *arg):
        obj = Catraca()
        list = []
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_localizacao, "\
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "turn_id, "\
                  "giro_id, "\
                  "mens_id "\
                  "FROM catraca WHERE "\
                  "catr_id = " + str(id)           
        elif id is None:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_localizacao, "\
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "turn_id, "\
                  "giro_id, "\
                  "mens_id "\
                  "FROM catraca"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.ip = dados[1]
                        obj.localizacao = dados[2]
                        obj.tempo = dados[3]
                        obj.operacao = dados[4]
                        obj.turno = Turno().busca(dados[5])
                        obj.giro = Giro().busca(dados[6])
                        obj.mensagem = Mensagem().busca(dados[7]) 
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
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca.', exc_info=True)
        finally:
            pass
          
    """
    def busca_id(self, id):
        obj = Catraca()
        sql = "SELECT catr_id, "\
              "catr_ip, "\
              "catr_localizacao, "\
              "catr_tempo_giro, "\
              "catr_operacao, "\
              "turn_id, "\
              "giro_id "\
              "FROM catraca WHERE "\
              "catr_id = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.ip = dados[1]
                    obj.localizacao = dados[2]
                    obj.tempo = dados[3]
                    obj.operacao = dados[4]    
                    obj.turno = Turno().busca_turno(dados[5])  
                    obj.giro = Giro().busca_giro(dados[6])  
                    return obj
                else:
                    return None
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO catraca("\
              "catr_ip, "\
              "catr_localizacao, "\
              "catr_tempo_giro, "\
              "catr_operacao, "\
              "turn_id, "\
              "giro_id) VALUES (" +\
              str(obj.ip) + ", " +\
              str(obj.localizacao) + ", " +\
              str(obj.tempo) + ", " +\
              str(obj.operacao) + ", " +\
              str(obj.turno) + ", " +\
              str(obj.giro) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela catraca.', exc_info=True)
            self.__aviso = str(e)
            return False

    def altera(self, obj):
       sql = "UPDATE catraca SET " +\
             "catr_ip = " + str(obj.ip) + ", " +\
             "catr_localizacao = " + str(obj.localizacao) + ", " +\
             "catr_tempo_giro = " + str(obj.tempo) + ", " +\
             "catr_operacao = " + str(obj.operacao) + ", " +\
             "turn_id = " + str(obj.turno) + ", " +\
             "giro_id = " + str(obj.giro) +\
             " WHERE "\
             "catr_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
       except Exception, e:
           self.__aviso = str(e)
           self.log.logger.error('Erro ao realizar UPDATE na tabela catraca.', exc_info=True)
           return False
       finally:
           pass
    
    def exclui(self, obj):
        sql = "DELETE FROM catraca WHERE catr_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela catraca.', exc_info=True)
            return False
        finally:
            pass
    """
    
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM catraca WHERE catr_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE catraca SET " +\
                              "catr_ip = '" + str(obj.ip) + "', " +\
                              "catr_localizacao = '" + str(obj.localizacao) + "', " +\
                              "catr_tempo_giro = " + str(obj.tempo) + ", " +\
                              "catr_operacao = " + str(obj.operacao) + ", " +\
                              "turn_id = " + str(obj.turno) + ", " +\
                              "giro_id = " + str(obj.turno) + ", " +\
                              "mens_id = " + str(obj.mensagem) +\
                              " WHERE "\
                              "catr_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO catraca("\
                              "catr_ip, "\
                              "catr_localizacao, "\
                              "catr_tempo_giro, "\
                              "catr_operacao, "\
                              "turn_id, "\
                              "giro_id, "\
                              "mens_id) VALUES ('" +\
                              str(obj.ip) + "', '" +\
                              str(obj.localizacao) + "', " +\
                              str(obj.tempo) + ", " +\
                              str(obj.operacao) + ", " +\
                              str(obj.turno) + ", " +\
                              str(obj.giro) + ", " +\
                              str(obj.mensagem) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.__con.commit()
                    self.__aviso = msg
                    return False
            else:
                msg = "Objeto inexistente!"
                self.__aviso = msg
                return False
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela catraca.', exc_info=True)
            return False
        finally:
            pass
        