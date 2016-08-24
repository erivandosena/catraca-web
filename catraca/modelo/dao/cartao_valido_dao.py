#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.logs import Logs
from catraca.util import Util
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.cartao_valido import CartaoValido
# from catraca.modelo.dao.tipo_dao import TipoDAO
# from catraca.modelo.dao.vinculo_dao import VinculoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoValidoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(CartaoValidoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca_cartao_valido(self, numero):
        sql = "SELECT "\
            "cartao.cart_creditos as creditos, "\
            "vinculo.vinc_descricao as descricao, "\
            "vinculo.vinc_fim as fim, "\
            "cartao.cart_id as id, "\
            "vinculo.vinc_inicio as inicio, "\
            "SUBSTR(TRIM(usuario.usua_nome), 0, 16) || '.' as nome, "\
            "cartao.cart_numero as numero, "\
            "vinculo.vinc_refeicoes as refeicoes, "\
            "tipo.tipo_id as tipo, "\
            "tipo.tipo_valor as valor, "\
            "vinculo.vinc_id as vinculo "\
            "FROM cartao "\
            "INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id "\
            "INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id "\
            "INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id "\
            "WHERE cartao.cart_numero = %s"
        return self.seleciona(CartaoValido, sql, numero)
        
#     def busca_cartao_valido(self, numero, data=None):
#         obj = CartaoValido()
#         if data is None:
#             data = Util().obtem_datahora_postgresql()
#         sql = "SELECT cartao.cart_id, cartao.cart_numero, cartao.cart_creditos, "\
#             "tipo.tipo_valor, vinculo.vinc_refeicoes, tipo.tipo_id, vinculo.vinc_id, "\
#             "vinculo.vinc_descricao, SUBSTR(TRIM(usuario.usua_nome), 0, 16) || '.' as usua_nome "\
#             "FROM cartao "\
#             "INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id "\
#             "INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id "\
#             "INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id "\
#             "WHERE ('"+str(data)+"' BETWEEN vinculo.vinc_inicio AND vinculo.vinc_fim) AND "\
#             "(cartao.cart_numero = '"+str(numero)+"')"
#         print "=" * 100
#         print sql 
#         print "=" * 100
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 dados = cursor.fetchone()
#                 if dados:
#                     obj.id = dados[0]
#                     obj.numero = dados[1]
#                     obj.creditos = dados[2]
#                     obj.valor = dados[3]
#                     obj.refeicoes = dados[4]
#                     obj.tipo = dados[5]
#                     obj.vinculo = dados[6]
# #                     obj.tipo = self.busca_por_tipo(obj)
# #                     obj.vinculo = self.busca_por_vinculo(obj)
#                     obj.descricao = dados[7]
#                     obj.nome = dados[8]
#                     return obj
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[cartao] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
        
#     def busca_por_tipo(self, obj):
#         print TipoDAO().busca(obj.id)
#         return TipoDAO().busca(obj.id)
#     
#     def busca_por_vinculo(self, obj):
#         print VinculoDAO().busca(obj.id)
#         return VinculoDAO().busca(obj.id)
    