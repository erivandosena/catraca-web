#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.vinculo import Vinculo


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
        try:
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
                return self.seleciona(Vinculo, sql, arg)
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
                return self.seleciona(Vinculo, sql)
        finally:
            pass
    
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
        try:
            return self.seleciona(Vinculo, sql, obj, str(data_ini), str(data_ini, data_fim))
        finally:
            pass
            
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
        try:
            return self.inclui(sql, obj)
        finally:
            pass
    
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
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM vinculo"
        if obj:
            sql = str(sql) + " WHERE vinc_id = %s"
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
                