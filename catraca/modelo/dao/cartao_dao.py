#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.cartao import Cartao


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class CartaoDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(CartaoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "cart_numero as numero, "\
                    "cart_creditos as creditos, "\
                    "cart_id as id, "\
                    "tipo_id as tipo "\
                    "FROM cartao WHERE "\
                    "cart_id = %s"
                return self.seleciona(Cartao, sql, arg)
            else:
                sql = "SELECT "\
                    "cart_numero as numero, "\
                    "cart_creditos as creditos, "\
                    "cart_id as id, "\
                    "tipo_id as tipo "\
                    "FROM cartao ORDER BY cart_id"
                return self.seleciona(Cartao, sql)
        finally:
            pass
        
    def busca_cartao(self, id):
        sql = "SELECT "\
            "cartao.cart_creditos as creditos, "\
            "cartao.cart_id as id, "\
            "cartao.cart_numero as numero, "\
            "tipo.tipo_valor as valor "\
            "FROM cartao "\
            "INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id "\
            "WHERE cartao.cart_id = %s"
        try:
            return self.seleciona(Cartao, sql, id)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO cartao "\
            "("\
            "cart_creditos, "\
            "cart_id, "\
            "cart_numero, "\
            "tipo_id "\
            ") VALUES ("\
            "%s, %s, %s, %s)"
        try:
            self.inclui(Cartao, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE cartao SET "\
            "cart_creditos = %s, "\
            "cart_numero = %s, "\
            "tipo_id = %s "\
            "WHERE cart_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM cartao"
        if obj:
            sql = str(sql) + " WHERE cart_id = %s"
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
                