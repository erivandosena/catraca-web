#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from cartao import Cartao
from perfildao import PerfilDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoDAO(ConexaoGenerica):

    def __init__(self):
        super(CartaoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Cartao()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT cart_id, "\
                  "cart_numero, "\
                  "cart_creditos, "\
                  "cart_data, "\
                  "perf_id "\
                  "FROM cartao WHERE "\
                  "cart_id = " + str(id) +\
                  " OR cart_numero = " + str(id)
        elif id is None:
            sql = "SELECT cart_id, "\
                  "cart_numero, "\
                  "cart_creditos, "\
                  "cart_data, "\
                  "perf_id "\
                  "FROM cartao"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
                        obj.data = dados[3]
                        obj.perfil = PerfilDAO().busca(dados[4])
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
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        print 
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE cartao SET " +\
                              "cart_numero = " + str(obj.numero) + ", " +\
                              "cart_creditos = " + str(obj.creditos) + ", " +\
                              "cart_data = '" + str(obj.data) + "', " +\
                              "perf_id = " + str(obj.perfil.id) +\
                              " WHERE "\
                              "cart_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO cartao("\
                              "cart_numero, "\
                              "cart_creditos, "\
                              "cart_data, "\
                              "perf_id) VALUES (" +\
                              str(obj.numero) + ", " +\
                              str(obj.creditos) + ", '" +\
                              str(obj.data) + "', " +\
                              str(obj.perfil.id) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    self.aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao.', exc_info=True)
            return False
        finally:
            pass
        