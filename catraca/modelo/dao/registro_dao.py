#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(RegistroDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "cart_id as cartao, "\
                    "catr_id as catraca, "\
                    "regi_valor_custo as custo, "\
                    "regi_data as data, "\
                    "regi_id as id, "\
                    "regi_valor_pago as pago, "\
                    "vinc_id as vinculo "\
                    "FROM registro WHERE "\
                    "regi_id = %s"
                return self.seleciona(Registro, sql, arg)
            else:
                sql = "SELECT "\
                    "cart_id as cartao, "\
                    "catr_id as catraca, "\
                    "regi_valor_custo as custo, "\
                    "regi_data as data, "\
                    "regi_id as id, "\
                    "regi_valor_pago as pago, "\
                    "vinc_id as vinculo "\
                    "FROM registro ORDER BY regi_id"
                return self.seleciona(Registro, sql)
        finally:
            pass
            
#     def busca_utilizacao(self, hora_ini, hora_fim, cartao_id):
#         data = Util().obtem_datahora()
#         data_ini = str(data.strftime("%Y-%m-%d")) + " " + str(hora_ini)
#         data_fim = str(data.strftime("%Y-%m-%d")) + " " + str(hora_fim)
#         sql = "SELECT "\
#             "COUNT(regi_data)"\
#             "FROM registro "\
#             "WHERE "\
#             "regi_data BETWEEN %s AND %s AND cart_id = %s"
#         try:
# #             obj = self.seleciona(Registro, sql, data_ini, data_fim, cartao_id)
# #             print obj.quantidade
# #             return int(obj.quantidade) if obj else None
#         
# #             lista = self.seleciona(Registro, sql, data_ini, data_fim, cartao_id)
# #             if lista:
# #                 registro = Registro()
# #                 for item in lista:
# #                     turno.descricao = item[0]
# #                     turno.fim = item[1]
# #                     turno.id = item[2]
# #                     turno.inicio = item[3]
# #                 return turno
# #             else:
# #                 return None
#             lista = self.seleciona(Registro, sql, data_ini, data_fim, cartao_id)
#             print lista
#             print lista[0][0]
#             return int(lista[0][0]) if lista else 0
#         
#         finally:
#             pass
            
#     def busca_por_periodo(self, data_ini, data_fim):
#         sql = "SELECT "\
#             "regi_id as id, "\
#             "regi_data as data, "\
#             "regi_valor_pago as pago, "\
#             "regi_valor_custo as custo, "\
#             "cart_id as cartao, "\
#             "catr_id as catraca, "\
#             "vinc_id as vinculo "\
#             "FROM registro WHERE "\
#             "regi_data::timestamp::time BETWEEN %s AND %s"
#         try:
#             return self.seleciona(Registro, sql, data_ini, data_fim)
#         finally:
#             pass
            
#     def busca_ultimo_registro(self):
#         sql = "SELECT MAX(regi_id) FROM registro"
#         obj = self.seleciona(Registro, sql)
#         try:
#             return obj[0][0] if obj[0][0] else 0
#         finally:
#             #self.fecha_conexao()
#             pass
            
    def insere(self, obj):
        sql = "INSERT INTO registro "\
            "("\
            "cart_id, "\
            "catr_id, "\
            "regi_valor_custo, "\
            "regi_data, "\
            "regi_id, "\
            "regi_valor_pago, "\
            "vinc_id "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s, %s)"
        try:
            return self.inclui(Registro, sql, obj)
        finally:
            pass
     
    def atualiza(self, obj):
        sql = "UPDATE registro SET "\
            "cart_id = %s, "\
            "catr_id = %s, "\
            "regi_valor_custo = %s, "\
            "regi_data = %s, "\
            "regi_valor_pago = %s, "\
            "vinc_id = %s "\
            "WHERE regi_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM registro"
        if obj:
            sql = str(sql) + " WHERE regi_id = %s"
        try:
            return self.deleta(sql, obj)
        finally:
            self.fecha_conexao()
     
    def atualiza_exclui(self, obj, boleano):
        if obj or boleano:
            try:
                if boleano:
                    if obj is None:
                        return self.exclui()
                    else:
                        self.exclui(obj)
                else:
                    return self.atualiza(obj)
            finally:
                pass
                