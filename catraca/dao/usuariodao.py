#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from usuario import Usuario
from tipo import Tipo
from conexao import ConexaoFactory
from .. logs import Logs


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UsuarioDAO(object):
    
    log = Logs()

    def __init__(self):
        super(UsuarioDAO, self).__init__()
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
        
    def busca_usuario(self, id):
        obj = Usuario()
        sql = "SELECT usua_id, "\
              "usua_nome, "\
              "usua_email, "\
              "usua_login, "\
              "usua_senha, "\
              "usua_nivel, "\
              "id_externo, "\
              "usua_num_doc, "\
              "tipo_id "\
              "FROM usuario WHERE "\
              "usua_id = " + str(id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.nome = dados[1]    
                    obj.email = dados[2]
                    obj.login = dados[3]    
                    obj.senha = dados[4]
                    obj.nivel = dados[5]    
                    obj.externo = dados[6]
                    obj.documento = dados[7]   
                    obj.tipo = Tipo().busca_tipo(dados[8])
                    return obj  
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela usuario.', exc_info=True)
        finally:
            pass
 
    def busca(self, valor):
        obj = Usuario()
        sql = "SELECT usua_id, "\
              "usua_nome, "\
              "usua_email, "\
              "usua_login, "\
              "usua_senha, "\
              "usua_nivel, "\
              "id_externo, "\
              "usua_num_doc, "\
              "tipo_id "\
              "FROM usuario WHERE "\
              "usua_nome = " + str(valor) +\
              " OR documento = " + str(valor)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.id = dados[0]
                    obj.nome = dados[1]    
                    obj.email = dados[2]
                    obj.login = dados[3]    
                    obj.senha = dados[4]
                    obj.nivel = dados[5]    
                    obj.externo = dados[6]
                    obj.documento = dados[7]   
                    obj.tipo = Tipo().busca_tipo(dados[8])
                    return obj  
                else:
                    return None
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela usuario.', exc_info=True)
        finally:
            pass

    def insere(self, obj):
        sql = "INSERT INTO usuario("\
              "usua_nome, "\
              "usua_email, "\
              "usua_login, "\
              "usua_senha, "\
              "usua_nivel, "\
              "id_externo, "\
              "usua_num_doc, "\
              "tipo_id) VALUES (" +\
              str(obj.nome) + ", " +\
              str(obj.email) + ", " +\
              str(obj.login) + ", " +\
              str(obj.senha) + ", " +\
              str(obj.nivel) + ", " +\
              str(obj.externo) + ", " +\
              str(obj.documento) + ", " +\
              str(obj.tipo) + ")"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar INSERT na tabela usuario.', exc_info=True)
            return False
        finally:
            pass

    def altera(self, obj):
       sql = "UPDATE usuario SET " +\
             "usua_nome = " + str(obj.nome) + ", " +\
             "usua_email = " + str(obj.email) + ", " +\
             "usua_login = " + str(obj.login) + ", " +\
             "usua_senha = " + str(obj.senha) + ", " +\
             "usua_nivel = " + str(obj.nivel) + ", " +\
             "id_externo = " + str(obj.externo) + ", " +\
             "usua_num_doc = " + str(obj.documento) + ", " +\
             "tipo_id = " + str(obj.tipo) +\
             " WHERE "\
             "usua_id = " + str(obj.id)
       try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                return True
       except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar UPDATE na tabela usuario.', exc_info=True)
            return False
       finally:
           pass
    
    def exclui(self, obj):
        sql = "DELETE FROM usuario WHERE usua_id = " + str(obj.id)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                self.__con.commit()
                return True
        except Exception, e:
            self.__erro = str(e)
            self.log.logger.error('Erro ao realizar DELETE na tabela usuario.', exc_info=True)
            return False
        finally:
           pass
       