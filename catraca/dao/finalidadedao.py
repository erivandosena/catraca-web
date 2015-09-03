#!/usr/bin/env python
# -*- coding: latin-1 -*-

from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from finalidade import Finalidade


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class FinalidadeDAO(ConexaoGenerica):

    def __init__(self):
        super(FinalidadeDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self, *arg):
        obj = Finalidade()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT fina_id, fina_nome FROM finalidade WHERE fina_id = " + str(id)
        elif id is None:
            sql = "SELECT fina_id, fina_nome FROM finalidade"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
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
            self.log.logger.error('Erro ao realizar SELECT na tabela finalidade.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM finalidade WHERE fina_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE finalidade SET fina_nome = '"+str(obj.nome)+"' WHERE fina_id = "+str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO finalidade(fina_nome) VALUES ('" + obj.nome + "')"
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
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela finalidade.', exc_info=True)
            return False
        finally:
            pass
        