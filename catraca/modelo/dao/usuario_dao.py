#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.usuario import Usuario


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UsuarioDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(UsuarioDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "usua_email as email, "\
                    "usua_id as id, "\
                    "id_base_externa as idexterno, "\
                    "usua_login as login, "\
                    "usua_nivel as nivel, "\
                    "usua_nome as nome, "\
                    "usua_senha as senha "\
                    "FROM usuario WHERE "\
                    "usua_id = %s"
                return self.seleciona(Usuario, sql, arg)
            else:
                sql = "SELECT "\
                    "usua_email as email, "\
                    "usua_id as id, "\
                    "id_base_externa as idexterno, "\
                    "usua_login as login, "\
                    "usua_nivel as nivel, "\
                    "usua_nome as nome, "\
                    "usua_senha as senha "\
                    "FROM usuario ORDER BY usua_id"
                return self.seleciona(Usuario, sql)
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO usuario "\
            "("\
            "usua_email, "\
            "usua_id, "\
            "id_base_externa, "\
            "usua_login, "\
            "usua_nivel, "\
            "usua_nome, "\
            "usua_senha "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s, %s)"
        try:
            return self.inclui(Usuario, sql, obj)
        finally:
            pass
     
    def atualiza(self, obj):
        sql = "UPDATE usuario SET "\
            "usua_email = %s, "\
            "id_base_externa = %s, "\
            "usua_login = %s, "\
            "usua_nivel = %s, "\
            "usua_nome = %s, "\
            "usua_senha = %s "\
            "WHERE usua_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM usuario"
        if obj:
            sql = str(sql) + " WHERE usua_id = %s"
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
                