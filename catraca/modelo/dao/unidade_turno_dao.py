#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.unidade_turno import UnidadeTurno


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class UnidadeTurnoDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(UnidadeTurnoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "turn_id as turno, "\
                    "unid_id as unidade, "\
                    "untu_id as id "\
                    "FROM unidade_turno WHERE "\
                    "untu_id = %s"
                return self.seleciona(UnidadeTurno, sql, arg)
            else:
                sql = "SELECT "\
                    "turn_id as turno, "\
                    "unid_id as unidade, "\
                    "untu_id as id "\
                    "FROM unidade_turno ORDER BY untu_id"
                return self.seleciona(UnidadeTurno, sql)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO unidade_turno "\
            "("\
            "untu_id, "\
            "turn_id, "\
            "unid_id "\
            ") VALUES ("\
            "%s, %s, %s)"
        try:
            return self.inclui(UnidadeTurno, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE unidade_turno SET "\
            "turn_id = %s, "\
            "unid_id = %s "\
            "WHERE untu_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM unidade_turno"
        if obj:
            sql = str(sql) + " WHERE untu_id = %s"
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
                