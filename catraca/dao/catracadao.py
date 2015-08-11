#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from catraca import Catraca
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(object):
    
    log = Logs()

    def __init__(self):
        super(CatracaDAO, self).__init__()
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
 
    def busca_id(self, local):
        obj = Catraca()
        sql = "SELECT catr_id, "\
              "catr_local, "\
              "catr_tempo_giro, "\
              "catr_sentido_trava_giro, "\
              "catr_hora_inicio_almoco, "\
              "catr_hora_fim_almoco, "\
              "catr_hora_inicio_janta, "\
              "catr_hora_fim_janta, "\
              "giro_id "\
              "FROM catraca WHERE "\
              "catr_local = " + str(local)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.local = dados[1]
                    obj.tempo = dados[2]
                    obj.sentido = dados[3]
                    obj.inicio_almoco = dados[4]    
                    obj.fim_almoco = dados[5]   
                    obj.inicio_janta = dados[6]
                    obj.fim_janta = dados[7]
                    obj.giro = Giro().busca_giro(dados[8])  
                    return obj
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO catraca("\
              "catr_local, "\
              "catr_tempo_giro, "\
              "catr_sentido_trava_giro, "\
              "catr_hora_inicio_almoco, "\
              "catr_hora_fim_almoco, "\
              "catr_hora_inicio_janta, "\
              "catr_hora_fim_janta, "\
              "giro_id) VALUES (" +\
              str(obj.local) + ", " +\
              str(obj.tempo) + ", " +\
              str(obj.sentido) + ", " +\
              str(obj.inicio_almoco) + ", " +\
              str(obj.fim_almoco) + ", " +\
              str(obj.inicio_janta) + ", " +\
              str(obj.fim_janta) + ", " +\
              str(obj.giro) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.log.logger.error('Erro ao realizar INSERT na tabela catraca.', exc_info=True)
            self.__erro = str(e)
            return False

    def altera(self, obj):
       sql = "UPDATE catraca SET " +\
             "catr_local = " + str(obj.local) + ", " +\
             "catr_tempo_giro = " + str(obj.tempo) + ", " +\
             "catr_sentido_trava_giro = " + str(obj.sentido) + ", " +\
             "catr_hora_inicio_almoco = " + str(obj.inicio_almoco) + ", " +\
             "catr_hora_fim_almoco = " + str(obj.fim_almoco) + ", " +\
             "catr_hora_inicio_janta = " + str(obj.inicio_janta) + ", " +\
             "catr_hora_fim_janta = " + str(obj.fim_janta) + ", " +\
             "giro_id = " + str(obj.giro) +\
             " WHERE "\
             "catr_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
       except Exception, e:
           self.__erro = str(e)
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
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela catraca.', exc_info=True)
            return False
        finally:
            pass
        
    