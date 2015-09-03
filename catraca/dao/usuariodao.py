#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from usuario import Usuario


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UsuarioDAO(ConexaoGenerica):
    
    #log = Logs()

    def __init__(self):
        super(UsuarioDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Usuario()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT usua_id, "\
                  "usua_nome, "\
                  "usua_email, "\
                  "usua_login, "\
                  "usua_senha, "\
                  "usua_nivel "\
                  "FROM usuario WHERE "\
                  "usua_id = " + str(id)
        elif id is None:
            sql = "SELECT usua_id, "\
                  "usua_nome, "\
                  "usua_email, "\
                  "usua_login, "\
                  "usua_senha, "\
                  "usua_nivel "\
                  "FROM usuario"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
                        obj.email = dados[2]
                        obj.login = dados[3]
                        obj.senha = dados[4]
                        obj.nivel = dados[5]
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
            self.log.logger.error('Erro ao realizar SELECT na tabela usuario.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM usuario WHERE usua_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE usuario SET " +\
                              "usua_nome = " + str(obj.nome) + ", " +\
                              "usua_email = " + str(obj.email) + ", " +\
                              "usua_login = " + str(obj.login) + ", " +\
                              "usua_senha = " + str(obj.senha) + ", " +\
                              "usua_nivel = " + str(obj.nivel) +\
                              " WHERE "\
                              "usua_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO usuario("\
                              "usua_nome, "\
                              "usua_email, "\
                              "usua_login, "\
                              "usua_senha "\
                              "usua_nivel) VALUES (" +\
                              str(obj.nome) + ", " +\
                              str(obj.email) + ", " +\
                              str(obj.login) + ", " +\
                              str(obj.senha) + ", " +\
                              str(obj.nivel) + ")"
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
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela usuario.', exc_info=True)
            return False
        finally:
            pass
        