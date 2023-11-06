#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.catraca_unidade import CatracaUnidade


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class CatracaUnidadeDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(CatracaUnidadeDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "catr_id as catraca, "\
                    "unid_id as unidade, "\
                    "caun_id as id "\
                    "FROM catraca_unidade WHERE "\
                    "caun_id = %s"
                return self.seleciona(CatracaUnidade, sql, arg)
            else:
                sql = "SELECT "\
                    "catr_id as catraca, "\
                    "unid_id as unidade, "\
                    "caun_id as id "\
                    "FROM catraca_unidade ORDER BY caun_id"
                return self.seleciona(CatracaUnidade, sql)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO catraca_unidade "\
            "("\
            "catr_id, "\
            "caun_id, "\
            "unid_id "\
            ") VALUES ("\
            "%s, %s, %s)"
        try:
            return self.inclui(CatracaUnidade, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE catraca_unidade SET "\
            "catr_id = %s, "\
            "unid_id = %s "\
            "WHERE caun_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM catraca_unidade"
        if obj:
            sql = str(sql) + " WHERE caun_id = %s"
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
                