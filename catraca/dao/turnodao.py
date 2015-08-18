#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from turno import Turno
from conexaogenerica import ConexaoGenerica
#from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TurnoDAO(ConexaoGenerica):
    
    #log = Logs()

    def __init__(self):
        super(TurnoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
    """
        self.__aviso = None
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
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
            self.__aviso = str(e)
        finally:
            pass
    """
        
    def busca(self, *arg):
        obj = Turno()
        list = []
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT turn_id, "\
                   "turn_hora_inicio, "\
                   "turn_hora_fim, "\
                   "turn_data, "\
                   "turn_continuo "\
                   "FROM turno WHERE "\
                   "turn_id = " + str(id)
        elif id is None:
            sql = "SELECT turn_id, "\
                   "turn_hora_inicio, "\
                   "turn_hora_fim, "\
                   "turn_data, "\
                   "turn_continuo "\
                   "FROM turno"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.inicio = dados[1]
                        obj.fim = dados[2]
                        obj.data = dados[3]
                        obj.continuo = dados[4]
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
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela turno.', exc_info=True)
        finally:
            pass

    """
    def busca_turno(self, data1, data2):
        obj = Registro()
        sql = "SELECT turn_id, "\
              "turn_hora_inicio, "\
              "turn_hora_fim, "\
              "turn_data, "\
              "turn_continuo "\
              "FROM turno WHERE "\
              "turn_id = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.inicio = dados[1]
                    obj.fim = dados[2]
                    obj.data = dados[3]
                    obj.continuo = dados[4]
                    return obj
                else:
                    return None
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela turno.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO turno("\
              "turn_hora_inicio, "\
              "turn_hora_fim, "\
              "turn_data, "\
              "turn_continuo) VALUES (" +\
              str(obj.inicio) + ", " +\
              str(obj.fim) + ", " +\
              str(obj.data) + ", " +\
              str(obj.continuo) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela turno.', exc_info=True)
            self.__aviso = str(e)
            return False

    def altera(self, obj):
       sql = "UPDATE turno SET " +\
             "turn_hora_inicio = " + str(obj.inicio) + ", " +\
             "turn_hora_fim = " + str(obj.fim) + ", " +\
             "turn_data = " + str(obj.data) + ", " +\
             "turn_continuo = " + str(obj.continuo) +\
             " WHERE "\
             "turn_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                return True
       except Exception, e:
           self.__aviso = str(e)
           self.log.logger.error('Erro ao realizar UPDATE na tabela turno.', exc_info=True)
           return False
       finally:
           pass

    def exclui(self, obj):
        sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela turno.', exc_info=True)
            return False
        finally:
            pass
    """
    
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE turno SET " +\
                              "turn_hora_inicio = '" + str(obj.inicio) + "', " +\
                              "turn_hora_fim = '" + str(obj.fim) + "', " +\
                              "turn_data = '" + str(obj.data) + "', " +\
                              "turn_continuo = " + str(obj.continuo) +\
                              " WHERE "\
                              "turn_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO turno("\
                              "turn_hora_inicio, "\
                              "turn_hora_fim, "\
                              "turn_data, "\
                              "turn_continuo) VALUES ('" +\
                              str(obj.inicio) + "', '" +\
                              str(obj.fim) + "', " +\
                              str(obj.data) + ", " +\
                              str(obj.continuo) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    self.aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela turno.', exc_info=True)
            return False
        finally:
            pass
        
