#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.entidades.isencao import Isencao
from catraca.modelo.dao.dao_generico import DAOGenerico


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class IsencaoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(IsencaoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "isen_inicio as inicio, "\
                    "isen_fim as fim, "\
                    "isen_id as id, "\
                    "cart_id as cartao "\
                    "FROM isencao WHERE "\
                    "isen_id = %s"
                return self.seleciona(Isencao, sql, arg)
            else:
                sql = "SELECT "\
                    "isen_inicio as inicio, "\
                    "isen_fim as fim, "\
                    "isen_id as id, "\
                    "cart_id as cartao "\
                    "FROM isencao ORDER BY isen_id"
                return self.seleciona(Isencao, sql)
        finally:
            pass
    
    def busca_isencao(self, numero_cartao=None, data=None):
        data_atual = Util().obtem_datahora_postgresql() if data is None else data
        sql = "SELECT "\
            "isencao.isen_inicio as inicio, "\
            "isencao.isen_fim as fim, "\
            "cartao.cart_id as cartao "\
            "FROM cartao "\
            "INNER JOIN isencao ON isencao.cart_id = cartao.cart_id "\
            "WHERE "\
            "cartao.cart_numero = %s AND (%s "\
            "BETWEEN  "\
            "isencao.isen_inicio AND isencao.isen_fim)"
        try:
            return self.seleciona(Isencao, sql, numero_cartao, str(data_atual))
        finally:
            pass
        
    def insere(self, obj):
        sql = "INSERT INTO isencao "\
            "("\
            "cart_id, "\
            "isen_fim, "\
            "isen_id, "\
            "isen_inicio "\
            ") VALUES ("\
            "%s, %s, %s, %s)"
        try:
            return self.inclui(Isencao, sql, obj)
        finally:
            self.fecha_conexao()
    
    def atualiza(self, obj):
        sql = "UPDATE isencao SET "\
            "cart_id = %s, "\
            "isen_fim = %s, "\
            "isen_inicio = %s "\
            "WHERE isen_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM isencao"
        if obj:
            sql = str(sql) + " WHERE isen_id = %s"
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
            