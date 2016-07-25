#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.dao.tipo_dao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoDAO(ConexaoGenerica):
    
    log = Logs()

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
            sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao ORDER BY cart_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.numero = dados[1]
                        obj.creditos = dados[2]
                        obj.tipo = dados[3]
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[cartao] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass

#     def busca_por_tipo(self, id):
#         return TipoDAO().busca(id)
        
    def busca_por_numero(self, numero):
        obj = Cartao()
        sql = "SELECT cart_id, cart_numero, cart_creditos, tipo_id FROM cartao " +\
              "WHERE cart_numero = '" + str(numero) + "'"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.numero = dados[1]
                    obj.creditos = dados[2]
                    obj.tipo = self.busca_por_tipo(obj)
                    return obj
                else:
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[cartao] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                obj.numero = obj.numero.zfill(10)
                sql = "INSERT INTO cartao("\
                        "cart_id, "\
                        "cart_numero, "\
                        "cart_creditos, "\
                        "tipo_id) VALUES (" +\
                        str(obj.id) + ", '" +\
                        str(obj.numero) + "', " +\
                        str(obj.creditos) + ", " +\
                        str(obj.tipo) + ")"
                self.aviso = "[cartao] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "[cartao] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[cartao] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM cartao WHERE cart_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM cartao"
                    self.aviso = "[cartao] Excluido com sucesso!"
                else:
                    obj.numero = obj.numero.zfill(10)
                    sql = "UPDATE cartao SET " +\
                          "cart_numero = '" + str(obj.numero) + "', " +\
                          "cart_creditos = " + str(obj.creditos) + ", " +\
                          "tipo_id = " + str(obj.tipo) +\
                          " WHERE "\
                          "cart_id = " + str(obj.id)
                    self.aviso = "[cartao] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    #self.commit()
                    return True
            else:
                self.aviso = "[cartao] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[cartao] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        