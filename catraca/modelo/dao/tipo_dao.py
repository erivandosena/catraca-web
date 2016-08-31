#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.tipo import Tipo


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TipoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(TipoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "tipo_nome as nome, "\
                    "tipo_valor as valor, "\
                    "tipo_id as id "\
                    "FROM tipo WHERE "\
                    "tipo_id = %s"
                return self.seleciona(Tipo, sql, arg)
            else:
                sql = "SELECT "\
                    "tipo_nome as nome, "\
                    "tipo_valor as valor, "\
                    "tipo_id as id "\
                    "FROM tipo ORDER BY tipo_id"
                return self.seleciona(Tipo, sql)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO tipo "\
            "("\
            "tipo_id, "\
            "tipo_nome, "\
            "tipo_valor "\
            ") VALUES ("\
            "%s, %s, %s)"
        try:
            return self.inclui(Tipo, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE tipo SET "\
            "tipo_nome = %s, "\
            "tipo_valor = %s "\
            "WHERE tipo_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM tipo"
        if obj:
            sql = str(sql) + " WHERE tipo_id = %s"
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
                