#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
# from vinculo.modelo.dados.conexao import ConexaoFactory
# from vinculo.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.vinculo import Vinculo
# from vinculo.modelo.dao.cartao_dao import CartaoDAO
# from vinculo.modelo.dao.usuario_dao import UsuarioDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class VinculoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(VinculoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "vinc_id as id, "\
                "vinc_avulso as avulso, "\
                "vinc_inicio as inicio, "\
                "vinc_fim as fim, "\
                "vinc_descricao as descricao, "\
                "vinc_refeicoes as refeicoes, "\
                "cart_id as cartao, "\
                "usua_id as usuario "\
                "FROM vinculo WHERE "\
                "vinc_id = %s"
        else:
            sql = "SELECT "\
                "vinc_id as id, "\
                "vinc_avulso as avulso, "\
                "vinc_inicio as inicio, "\
                "vinc_fim as fim, "\
                "vinc_descricao as descricao, "\
                "vinc_refeicoes as refeicoes, "\
                "cart_id as cartao, "\
                "usua_id as usuario "\
                "FROM vinculo ORDER BY vinc_id"
        return self.seleciona(Vinculo, sql, arg)
    
    def busca_por_periodo(self, obj, data_ini, data_fim):
        sql = "SELECT "\
            "vinc_id as id, "\
            "vinc_avulso as avulso, "\
            "vinc_inicio as inicio, "\
            "vinc_fim as fim, "\
            "vinc_descricao as descricao, "\
            "vinc_refeicoes as refeicoes, "\
            "cart_id as cartao, "\
            "usua_id as usuario "\
            "FROM vinculo "\
            "WHERE "\
            "regi_data BETWEEN %s "\
            " AND %s AND cart_id = %s  "\
            " ORDER BY vinc_inicio DESC"
        return self.seleciona(Vinculo, sql, obj, str(data_ini), str(data_ini, data_fim))
        
#     def busca_por_periodo(self, data_ini, data_fim, cartao):
#         sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
#                 "vinc_refeicoes, cart_id, usua_id FROM vinculo WHERE "\
#                 "regi_data BETWEEN " + str(data_ini) +\
#                 " AND " + str(data_fim) + " AND cart_id = "  + str(cartao.id) +\
#                 " ORDER BY vinc_inicio DESC"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
#                     return list
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[vinculo] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
    
    def insere(self, obj):
        sql = "INSERT INTO vinculo "\
            "("\
            "vinc_avulso, "\
            "cart_id, "\
            "vinc_descricao, "\
            "vinc_fim, "\
            "vinc_id, "\
            "vinc_inicio, "\
            "vinc_refeicoes, "\
            "usua_id "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s, %s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE vinculo SET "\
            "vinc_avulso = %s, "\
            "cart_id = %s, "\
            "vinc_descricao = %s, "\
            "vinc_fim = %s, "\
            "vinc_inicio = %s, "\
            "vinc_refeicoes = %s, "\
            "usua_id = %s "\
            "WHERE vinc_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM vinculo"
        if obj:
            sql = str(sql) + " WHERE vinc_id = %s"
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
#         obj = Vinculo()
#         id = None
#         for i in arg:
#             id = i
#         if id:
#             sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
#             "vinc_refeicoes, cart_id, usua_id FROM vinculo WHERE vinc_id = " + str(id)
#         elif id is None:
#             sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
#             "vinc_refeicoes, cart_id, usua_id FROM vinculo ORDER BY vinc_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados is not None:
#                         obj.id = dados[0]
#                         obj.avulso = dados[1]
#                         obj.inicio = dados[2]
#                         obj.fim = dados[3]
#                         obj.descricao = dados[4]
#                         obj.refeicoes = dados[5]
#                         obj.cartao = dados[6]
#                         obj.usuario = dados[7]
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
#             self.log.logger.error('[vinculo] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#   
# #     def busca_por_cartao(self, obj):
# #         return CartaoDAO().busca(obj.id)
# #         
# #     def busca_por_usuario(self, obj):
# #         return UsuarioDAO().busca(obj.id)
#     
#     def busca_por_periodo(self, data_ini, data_fim, cartao):
#         sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
#                 "vinc_refeicoes, cart_id, usua_id FROM vinculo WHERE "\
#                 "regi_data BETWEEN " + str(data_ini) +\
#                 " AND " + str(data_fim) + " AND cart_id = "  + str(cartao.id) +\
#                 " ORDER BY vinc_inicio DESC"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
#                     return list
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[vinculo] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
#     def insere(self, obj):
#         try:
#             if obj:
#                 sql = "INSERT INTO vinculo("\
#                       "vinc_id, "\
#                       "vinc_avulso, "\
#                       "vinc_inicio, "\
#                       "vinc_fim, "\
#                       "vinc_descricao, "\
#                       "vinc_refeicoes, "\
#                       "cart_id, "\
#                       "usua_id) VALUES (" +\
#                       str(obj.id) + ", " +\
#                       str(obj.avulso) + ", '" +\
#                       str(obj.inicio) + "', '" +\
#                       str(obj.fim) + "', '" +\
#                       str(obj.descricao) + "', " +\
#                       str(obj.refeicoes) + ", " +\
#                       str(obj.cartao) + ", " +\
#                       str(obj.usuario) + ")"
#                 self.aviso = "[vinculo] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[vinculo] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[vinculo] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
#         
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM vinculo WHERE vinc_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM vinculo"
#                     self.aviso = "[vinculo] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE vinculo SET " +\
#                           "vinc_avulso = " + str(obj.avulso) + ", " +\
#                           "vinc_inicio = '" + str(obj.inicio) + "', " +\
#                           "vinc_fim = '" + str(obj.fim) + "', " +\
#                           "vinc_descricao = '" + str(obj.descricao) + "', " +\
#                           "vinc_refeicoes = " + str(obj.refeicoes) + ", " +\
#                           "cart_id = " + str(obj.cartao) + ", " +\
#                           "usua_id = " + str(obj.usuario) +\
#                           " WHERE "\
#                           "vinc_id = " + str(obj.id)
#                     self.aviso = "[vinculo] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[vinculo] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[vinculo] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
        
