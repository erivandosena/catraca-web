#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.unidade import Unidade


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class UnidadeDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(UnidadeDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "unid_id as id, "\
                    "unid_nome as nome "\
                    "FROM unidade WHERE "\
                    "unid_id = %s"
                return self.seleciona(Unidade, sql, arg)
            else:
                sql = "SELECT "\
                    "unid_id as id, "\
                    "unid_nome as nome "\
                    "FROM unidade ORDER BY unid_id"
                return self.seleciona(Unidade, sql)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO unidade "\
            "("\
            "unid_id, "\
            "unid_nome "\
            ") VALUES ("\
            "%s, %s)"
        try:
            return self.inclui(Unidade, sql, obj)
        finally:
            self.fecha_conexao()
    
    def atualiza(self, obj):
        sql = "UPDATE unidade SET "\
            "unid_nome = %s "\
            "WHERE unid_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM unidade"
        if obj:
            sql = str(sql) + " WHERE unid_id = %s"
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
                