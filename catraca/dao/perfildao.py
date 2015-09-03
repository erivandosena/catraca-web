#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from perfil import Perfil
from tipodao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class PerfilDAO(ConexaoGenerica):

    def __init__(self):
        super(PerfilDAO, self).__init__()
        ConexaoGenerica.__init__(self)

        
    def busca(self, *arg):
        obj = Perfil()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT perf_id, "\
                  "perf_nome, "\
                  "perf_email, "\
                  "perf_tel, "\
                  "perf_datanascimento, "\
                  "tipo_id "\
                  "FROM perfil WHERE "\
                  "perf_id = " + str(id)
        elif id is None:
            sql = "SELECT perf_id, "\
                  "perf_nome, "\
                  "perf_email, "\
                  "perf_tel, "\
                  "perf_datanascimento, "\
                  "tipo_id "\
                  "FROM perfil"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
                        obj.email = dados[2]
                        obj.telefone = dados[3]
                        obj.nascimento = dados[4] 
                        obj.tipo = TipoDAO().busca(dados[5])
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
            self.log.logger.error('Erro ao realizar SELECT na tabela perfil.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM perfil WHERE perf_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE perfil SET " +\
                              "perf_nome = '" + str(obj.nome) + "', " +\
                              "perf_email = '" + str(obj.email) + "', " +\
                              "perf_tel = '" + str(obj.telefone) + "', " +\
                              "perf_datanascimento = '" + str(obj.nascimento) + "', " +\
                              "tipo_id = " + str(obj.tipo.id) +\
                              " WHERE "\
                              "perf_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO perfil("\
                              "perf_nome, "\
                              "perf_email, "\
                              "perf_tel, "\
                              "perf_datanascimento, "\
                              "tipo_id) VALUES ('" +\
                              str(obj.nome) + "', '" +\
                              str(obj.email) + "', '" +\
                              str(obj.telefone) + "', '" +\
                              str(obj.nascimento) + "', " +\
                              str(obj.tipo.id) + ")"
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
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela perfil.', exc_info=True)
            return False
        finally:
            pass
        
    
