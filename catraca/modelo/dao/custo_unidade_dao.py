#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.custo_unidade import CustoUnidade


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class CustoUnidadeDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(CustoUnidadeDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "cure_id as custo, "\
                    "cuun_id as id, "\
                    "unid_id as unidade "\
                    "FROM custo_unidade WHERE "\
                    "cuun_id = %s"
                return self.seleciona(CustoUnidade, sql, arg)
            else:
                sql = "SELECT "\
                    "cure_id as custo, "\
                    "cuun_id as id, "\
                    "unid_id as unidade "\
                    "FROM custo_unidade ORDER BY cure_id"
                return self.seleciona(CustoUnidade, sql)
        finally:
            pass
        
#     def busca_custo(self):
#         try:
#             sql = "SELECT "\
#                 "cure_id as custo, "\
#                 "cuun_id as id, "\
#                 "unid_id as unidade "\
#                 "FROM custo_unidade ORDER BY cuun_id DESC LIMIT 1"
#             lista = self.seleciona(CustoUnidade, sql)
#             return lista[0][2] if lista else 0
#         finally:
#             pass
    
    def insere(self, obj):
        sql = "INSERT INTO custo_unidade "\
            "("\
            "cure_id, "\
            "cuun_id, "\
            "unid_id "\
            ") VALUES ("\
            "%s, %s, %s)"
        try:
            return self.inclui(CustoUnidade, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE custo_unidade SET "\
            "cure_id = %s, "\
            "unid_id = %s "\
            "WHERE cuun_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM custo_unidade"
        if obj:
            sql = str(sql) + " WHERE cuun_id = %s"
        try:
            return self.deleta(sql, obj)
        finally:
            pass
    
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
                