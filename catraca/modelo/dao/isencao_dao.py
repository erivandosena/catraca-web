#!/usr/bin/env python
# -*- coding: latin-1 -*-


# from contextlib import closing
from catraca.logs import Logs
from catraca.util import Util
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.entidades.isencao import Isencao
# from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.dao_generico import DAOGenerico


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class IsencaoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(IsencaoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "isen_inicio as inicio, "\
                "isen_fim as fim, "\
                "isen_id as id, "\
                "cart_id as cartao "\
                "FROM isencao WHERE "\
                "isen_id = %s"
        else:
            sql = "SELECT "\
                "isen_inicio as inicio, "\
                "isen_fim as fim, "\
                "isen_id as id, "\
                "cart_id as cartao "\
                "FROM isencao ORDER BY isen_id"
        return self.seleciona(Isencao, sql, arg)
    
    def busca_isencao(self, numero_cartao=None, data=None):
        data_atual = Util().obtem_datahora_postgresql() if data is None else data
        sql = "SELECT "\
            "isencao.isen_inicio as inicio, "\
            "isencao.isen_fim as fim, "\
            "cartao.cart_id as cartao "\
            "FROM cartao "\
            "INNER JOIN isencao ON isencao.cart_id = cartao.cart_id "\
            "WHERE "\
            "cartao.cart_numero = %s AND (%s "\
            "BETWEEN  "\
            "isencao.isen_inicio AND isencao.isen_fim)"
        return self.seleciona(Isencao, sql, numero_cartao, str(data_atual))
    
#     def busca_por_isencao(self, obj):
#         return CartaoDAO().busca_por_numero(obj.numero)
    
#     def busca_isencao(self, numero_cartao=None, data=None):
#         obj = Isencao()
#         if data is None:
#             data = Util().obtem_datahora_postgresql()
#         sql = "SELECT isencao.isen_inicio, isencao.isen_fim, cartao.cart_id FROM cartao "\
#         "INNER JOIN isencao ON isencao.cart_id = cartao.cart_id WHERE cartao.cart_numero = '"+str(numero_cartao)+"' AND ('"+str(data)+"' "\
#         "BETWEEN isencao.isen_inicio AND isencao.isen_fim)" 
#         print "=" * 100
#         print sql
#         print "=" * 100
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 dados = cursor.fetchone()
#                 if dados is not None:
#                     obj.inicio = dados[0]
#                     obj.fim = dados[1]
#                     obj.cartao = self.busca_por_cartao(obj)
#                     return obj
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[isencao] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass

    def insere(self, obj):
        sql = "INSERT INTO isencao "\
            "("\
            "cart_id, "\
            "isen_fim, "\
            "isen_id, "\
            "isen_inicio "\
            ") VALUES ("\
            "%s, %s, %s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE isencao SET "\
            "cart_id = %s, "\
            "isen_fim = %s, "\
            "isen_inicio = %s "\
            "WHERE isen_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM isencao"
        if obj:
            sql = str(sql) + " WHERE isen_id = %s"
        return self.deleta(sql, obj)
    
    def atualiza_exclui(self, obj, boleano):
        if obj or boleano:
            if boleano:
                if obj is None:
                    return self.exclui()
                else:
                    self.exclui(obj)
            else:
                return self.atualiza(obj)
            
        
#     def busca(self, *arg):
#         obj = Isencao()
#         id = None
#         for i in arg:
#             id = i
#         if id:
#             sql = "SELECT isen_id, isen_inicio, isen_fim, cart_id FROM isencao WHERE isen_id = " + str(id)
#         elif id is None:
#             sql = "SELECT isen_id, isen_inicio, isen_fim, cart_id FROM isencao ORDER BY isen_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados is not None:
#                         obj.id = dados[0]
#                         obj.inicio = dados[1]
#                         obj.fim = dados[2]
#                         obj.cartao = dados[3]
#                         return obj
#                     else:
#                         return None
#                 elif id is None:
#                     list = cursor.fetchall()
#                     if list != []:
#                         return list
#                     else:
#                         return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[isencao] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
# #     def busca_por_cartao(self, obj):
# #         return CartaoDAO().busca(obj.id)
#         
#     def busca_por_isencao(self, obj):
#         return CartaoDAO().busca_por_numero(obj.numero)
#     
#     def busca_isencao(self, numero_cartao=None, data=None):
#         obj = Isencao()
#         if data is None:
#             data = Util().obtem_datahora_postgresql()
#         sql = "SELECT isencao.isen_inicio, isencao.isen_fim, cartao.cart_id FROM cartao "\
#         "INNER JOIN isencao ON isencao.cart_id = cartao.cart_id WHERE cartao.cart_numero = '"+str(numero_cartao)+"' AND ('"+str(data)+"' "\
#         "BETWEEN isencao.isen_inicio AND isencao.isen_fim)" 
#         print "=" * 100
#         print sql
#         print "=" * 100
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 dados = cursor.fetchone()
#                 if dados is not None:
#                     obj.inicio = dados[0]
#                     obj.fim = dados[1]
#                     obj.cartao = self.busca_por_cartao(obj)
#                     return obj
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[isencao] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
#     def insere(self, obj):
#         try:
#             if obj:
#                 sql = "INSERT INTO isencao("\
#                         "isen_id, "\
#                         "isen_inicio, "\
#                         "isen_fim, "\
#                         "cart_id) VALUES (" +\
#                         str(obj.id) + ", '" +\
#                         str(obj.inicio) + "', '" +\
#                         str(obj.fim) + "', " +\
#                         str(obj.cartao) + ")"
#                 self.aviso = "[isencao] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[isencao] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[isencao] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
#         
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM isencao WHERE isen_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM isencao"
#                     self.aviso = "[isencao] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE isencao SET " +\
#                           "isen_inicio = '" + str(obj.inicio) + "', " +\
#                           "isen_fim = '" + str(obj.fim) + "', " +\
#                           "cart_id = " + str(obj.cartao) +\
#                           " WHERE "\
#                           "isen_id = " + str(obj.id)
#                     self.aviso = "[isencao] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[isencao] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[isencao] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
#         