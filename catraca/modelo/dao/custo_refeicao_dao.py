#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.custo_refeicao import CustoRefeicao


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoRefeicaoDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(CustoRefeicaoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "cure_valor as valor, "\
                "cure_data as data, "\
                "cure_id as id "\
                "FROM custo_refeicao WHERE "\
                "cure_id = %s"
        else:
            sql = "SELECT "\
                "cure_valor as valor, "\
                "cure_data as data, "\
                "cure_id as id "\
                "FROM custo_refeicao ORDER BY cure_id"
        return self.seleciona(CustoRefeicao, sql, arg)
    
    def insere(self, obj):
        sql = "INSERT INTO custo_refeicao "\
            "("\
            "cure_data, "\
            "cure_id, "\
            "cure_valor "\
            ") VALUES ("\
            "%s, %s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE custo_refeicao SET "\
            "cure_data = %s, "\
            "cure_valor = %s "\
            "WHERE cure_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM custo_refeicao"
        if obj:
            sql = str(sql) + " WHERE cure_id = %s"
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
            