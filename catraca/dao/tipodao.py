#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from tipo import Tipo


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TipoDAO(ConexaoGenerica):

    def __init__(self):
        super(TipoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
    
    def busca(self, *arg):
        obj = Tipo()
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
            self.aviso = str(e)
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
                    self.commit()
                    self.aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela tipo.', exc_info=True)
            return False
        finally:
            pass
        