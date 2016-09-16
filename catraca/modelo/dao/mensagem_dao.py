#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.mensagem import Mensagem


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class MensagemDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(MensagemDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "catr_id as catraca, "\
                    "mens_id as id, "\
                    "mens_institucional1 as institucional1, "\
                    "mens_institucional2 as institucional2, "\
                    "mens_institucional3 as institucional3, "\
                    "mens_institucional4 as institucional4 "\
                    "FROM mensagem WHERE "\
                    "mens_id = %s"
                return self.seleciona(Mensagem, sql, arg)
            else:
                sql = "SELECT "\
                    "catr_id as catraca, "\
                    "mens_id as id, "\
                    "mens_institucional1 as institucional1, "\
                    "mens_institucional2 as institucional2, "\
                    "mens_institucional3 as institucional3, "\
                    "mens_institucional4 as institucional4 "\
                    "FROM mensagem ORDER BY mens_id"
                return self.seleciona(Mensagem, sql)
        finally:
            pass
        
    def busca_por_catraca(self, id):
        try:
            sql = "SELECT "\
                "mens_institucional1 as institucional1, "\
                "mens_institucional2 as institucional2, "\
                "mens_institucional3 as institucional3, "\
                "mens_institucional4 as institucional4 "\
                "FROM mensagem WHERE "\
                "catr_id = %s"
            return self.seleciona(Mensagem, sql, id)
        finally:
            pass
     
    def insere(self, obj):
        sql = "INSERT INTO mensagem "\
            "("\
            "catr_id, "\
            "mens_id, "\
            "mens_institucional1, "\
            "mens_institucional2, "\
            "mens_institucional3, "\
            "mens_institucional4 "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s)"
        try:
            return self.inclui(Mensagem, sql, obj)
        finally:
            pass
     
    def atualiza(self, obj):
        sql = "UPDATE mensagem SET "\
            "catr_id = %s, "\
            "mens_institucional1 = %s, "\
            "mens_institucional2 = %s, "\
            "mens_institucional3 = %s, "\
            "mens_institucional4 = %s "\
            "WHERE mens_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM mensagem"
        if obj:
            sql = str(sql) + " WHERE mens_id = %s"
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
            