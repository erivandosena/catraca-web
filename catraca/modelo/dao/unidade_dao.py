#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.unidade import Unidade


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(UnidadeDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "unid_id as id, "\
                "unid_nome as nome "\
                "FROM unidade WHERE "\
                "unid_id = %s"
        else:
            sql = "SELECT "\
                "unid_id as id, "\
                "unid_nome as nome "\
                "FROM unidade ORDER BY unid_id"
        return self.seleciona(Unidade, sql, arg)
    
    def insere(self, obj):
        sql = "INSERT INTO unidade "\
            "("\
            "unid_id, "\
            "unid_nome "\
            ") VALUES ("\
            "%s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE unidade SET "\
            "unid_nome = %s "\
            "WHERE unid_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM unidade"
        if obj:
            sql = str(sql) + " WHERE unid_id = %s"
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
            
        