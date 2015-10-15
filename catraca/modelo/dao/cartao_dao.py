#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.dao.tipo_dao import TipoDAO


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
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
                "WHERE cart_id = " + str(id)
        elif id is None:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
                        obj.tipo = TipoDAO().busca(dados[3])
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
        
    def busca_por_numero(self, *arg):
        obj = Cartao()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
                  "WHERE cart_numero = " + str(id)
        elif id is None:
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
                        obj.tipo = TipoDAO().busca(dados[3])
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
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO cartao("\
                        "cart_id, "\
                        "cart_numero, "\
                        "cart_creditos, "\
                        "tipo_id) VALUES (" +\
                        str(obj.id) + ", " +\
                        str(obj.numero) + ", " +\
                        str(obj.creditos) + ", " +\
                        str(obj.tipo) + ")"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE cartao SET " +\
                          "cart_numero = " + str(obj.numero) + ", " +\
                          "cart_creditos = " + str(obj.creditos) + ", " +\
                          "tipo_id = " + str(obj.tipo) +\
                          " WHERE "\
                          "cart_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela cartao.', exc_info=True)
            return False
        finally:
            pass
        