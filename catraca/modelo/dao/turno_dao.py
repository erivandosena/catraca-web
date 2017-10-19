#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.entidades.turno import Turno


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class TurnoDAO(DAOGenerico):
    
    log = Logs()
    util = Util()
    
    def __init__(self):
        super(TurnoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        try:
            if arg:
                sql = "SELECT "\
                    "turn_descricao as descricao, "\
                    "turn_hora_fim as fim, "\
                    "turn_id as id, "\
                    "turn_hora_inicio as inicio "\
                    "FROM turno WHERE "\
                    "turn_id = %s"
                return self.seleciona(Turno, sql, arg)
            else:
                sql = "SELECT "\
                    "turn_descricao as descricao, "\
                    "turn_hora_fim as fim, "\
                    "turn_id as id, "\
                    "turn_hora_inicio as inicio "\
                    "FROM turno ORDER BY turn_id"
                return self.seleciona(Turno, sql)
        finally:
            pass
    
    def busca_por_catraca(self, obj, hora_atual):
        nome = obj.nome if obj else self.util.obtem_nome_rpi().upper()
        sql = "SELECT DISTINCT "\
            "turno.turn_descricao as descricao, "\
            "turno.turn_hora_fim as fim, "\
            "turno.turn_id as id , "\
            "turno.turn_hora_inicio as inicio "\
            "FROM turno "\
            "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
            "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
            "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
            "WHERE "\
            "catraca.catr_nome = %s AND "\
            "turno.turn_hora_inicio <= %s "\
            "AND turno.turn_hora_fim >= %s"
        try:
            lista = self.seleciona(Turno, sql, nome, str(hora_atual), str(hora_atual))
            if lista:
                turno = Turno()
                for item in lista:
                    turno.descricao = item[0]
                    turno.fim = item[1]
                    turno.id = item[2]
                    turno.inicio = item[3]
                return turno
            else:
                return None
        finally:
            pass
    
    def obtem_turno(self, catraca=None, hora=None):
        turno = None
        try:
            if (catraca is None) or (hora is None):
                turno = self.busca_por_catraca( CatracaDAO().busca_por_ip(self.util.obtem_ip_por_interface()), self.util.obtem_hora() )
            else:
                turno = self.busca_por_catraca(catraca, hora)
            return turno
        finally:
            pass
    
    def insere(self, obj):
        sql = "INSERT INTO turno "\
            "("\
            "turn_descricao, "\
            "turn_hora_fim, "\
            "turn_id, "\
            "turn_hora_inicio "\
            ") VALUES ("\
            "%s, %s, %s, %s)"
        try:
            return self.inclui(Turno, sql, obj)
        finally:
            pass
    
    def atualiza(self, obj):
        sql = "UPDATE turno SET "\
            "turn_descricao = %s, "\
            "turn_hora_fim = %s, "\
            "turn_hora_inicio = %s "\
            "WHERE turn_id = %s"
        try:
            return self.altera(sql, obj)
        finally:
            pass
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM turno"
        if obj:
            sql = str(sql) + " WHERE turn_id = %s"
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
                