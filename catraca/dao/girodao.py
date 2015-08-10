#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from giro import Giro
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class GiroDAO(object):
    
    log = Logs()

    def __init__(self):
        super(GiroDAO, self).__init__()
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
            self.__erro = str(e)
            self.log.logger.critical('Erro abrindo conexao com o banco de dados.', exc_info=True)
        finally:
            pass
        
    def busca_giro(self, id):
        obj = Giro()
        sql = "SELECT giro_id, "\
              "giro_giros_horario, "\
              "giro_giros_antihorario, "\
              "giro_data_giro "\
              "FROM giro WHERE "\
              "giro_id = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.horario = dados[1]    
                    obj.antihorario = dados[2]
                    obj.data = dados[3]    
                    return obj  
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela giro.', exc_info=True)
        finally:
            pass

    def busca(self, id):
        obj = Giro()
        sql = "SELECT giro_id, "\
              "giro_giros_horario, "\
              "giro_giros_antihorario, "\
              "giro_data_giro "\
              "FROM giro WHERE "\
              "firo_id = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.horario = dados[1]    
                    obj.antihorario = dados[2]
                    obj.data = dados[3]    
                    return obj  
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela giro.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO giro("\
              "giro_giros_horario, "\
              "giro_giros_antihorario, "\
              "giro_data_giro) VALUES (" +\
              str(obj.horario) + ", " +\
              str(obj.antihorario) + ", " +\
              str(obj.data) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar INSERT na tabela giro.', exc_info=True)
            return False
        finally:
            pass

    def altera(self, obj):
       sql = "UPDATE giro SET " +\
             "giro_giros_horario = " + str(obj.horario) + ", " +\
             "giro_giros_antihorario = " + str(obj.antihorario) + ", " +\
             "giro_data_giro = " + str(obj.data) +\
             " WHERE "\
             "giro_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                return True
       except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar UPDATE na tabela giro.', exc_info=True)
            return False
       finally:
           pass
    
    def exclui(self, obj):
        sql = "DELETE FROM tipo WHERE giro_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela giro.', exc_info=True)
            return False
        finally:
           pass
       
        