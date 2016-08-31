#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dao.dao_generico import DAOGenerico
#from catraca.modelo.entidades.registro_offline import RegistroOffline
from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroOfflineDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(RegistroOfflineDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "reof_id as id, "\
                    "reof_data as data, "\
                    "reof_valor_pago as pago, "\
                    "reof_valor_custo as custo, "\
                    "cart_id as cartao, "\
                    "catr_id as catraca, "\
                    "vinc_id as vinculo "\
                    "FROM registro_offline WHERE "\
                    "reof_id = %s"
                return self.seleciona(Registro, sql, arg)
            else:
                sql = "SELECT "\
                    "reof_id as id, "\
                    "reof_data as data, "\
                    "reof_valor_pago as pago, "\
                    "reof_valor_custo as custo, "\
                    "cart_id as cartao, "\
                    "catr_id as catraca, "\
                    "vinc_id as vinculo "\
                    "FROM registro_offline ORDER BY reof_id"
                return self.seleciona(Registro, sql)
        finally:
            pass
            
    def busca_utilizacao(self, hora_ini, hora_fim, cartao_id):
        data = Util().obtem_datahora()
        data_ini = str(data.strftime("%Y-%m-%d")) + " " + str(hora_ini)
        data_fim = str(data.strftime("%Y-%m-%d")) + " " + str(hora_fim)
        sql = "SELECT "\
            "COUNT(reof_data)"\
            "FROM registro_offline "\
            "WHERE "\
            "reof_data BETWEEN %s AND %s AND cart_id = %s"
        try:
            lista = self.seleciona(Registro, sql, data_ini, data_fim, cartao_id)
            return int(lista[0][0]) if lista else 0
         
        finally:
            pass
            
    def busca_por_periodo(self, data_ini, data_fim):
        sql = "SELECT "\
            "reof_id as id, "\
            "reof_data as data, "\
            "reof_valor_pago as pago, "\
            "reof_valor_custo as custo, "\
            "cart_id as cartao, "\
            "catr_id as catraca, "\
            "vinc_id as vinculo "\
            "FROM registro_offline WHERE "\
            "reof_data::timestamp::time BETWEEN %s AND %s"
        try:
            return self.seleciona(Registro, sql, data_ini, data_fim)
        finally:
            pass
            
#     def busca_ultimo_registro_offline(self):
#         sql = "SELECT MAX(reof_id) FROM registro_offline"
#         obj = self.seleciona(RegistroOffline, sql)
#         try:
#             return obj[0][0] if obj[0][0] else 0
#         finally:
#             #self.fecha_conexao()
#             pass
            
    def insere(self, obj):
        sql = "INSERT INTO registro_offline "\
            "("\
            "cart_id, "\
            "catr_id, "\
            "reof_valor_custo, "\
            "reof_data, "\
            "reof_valor_pago, "\
            "vinc_id "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s)"
        try:
            return self.inclui(Registro, sql, obj)
        finally:
            pass
     
    def atualiza(self, obj):
        sql = "UPDATE registro_offline SET "\
            "cart_id = %s, "\
            "catr_id = %s, "\
            "reof_valor_custo = %s, "\
            "reof_data = %s, "\
            "reof_valor_pago = %s, "\
            "vinc_id = %s "\
            "WHERE reof_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM registro_offline"
        if obj:
            sql = str(sql) + " WHERE reof_id = %s"
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
                