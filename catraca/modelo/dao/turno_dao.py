#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.util import Util
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.turno import Turno
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TurnoDAO(ConexaoGenerica):
    
    util = Util()
    catraca_dao = CatracaDAO()

    def __init__(self):
        super(TurnoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Turno()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT turn_id, "\
                   "turn_hora_inicio, "\
                   "turn_hora_fim, "\
                   "turn_descricao "\
                   "FROM turno WHERE "\
                   "turn_id = " + str(id)
        elif id is None:
            sql = "SELECT turn_id, "\
                   "turn_hora_inicio, "\
                   "turn_hora_fim, "\
                   "turn_descricao "\
                   "FROM turno ORDER BY turn_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.inicio = dados[1]
                        obj.fim = dados[2]
                        obj.descricao = dados[3]
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[turno] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def busca_por_catraca(self, obj, hora_atual):
        if obj:
            sql = "SELECT turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno "\
                    "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
                    "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
                    "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
                    "WHERE catraca.catr_ip = '"+str(obj.ip)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
            print "=" * 100
            print sql
            print "=" * 100
        else:
            ip = self.util.obtem_ip()
            sql = "SELECT turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno "\
                    "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
                    "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
                    "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
                    "WHERE catraca.catr_ip = '"+str(ip)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
            print "=" * 100
            print sql
            print "=" * 100
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                obj = Turno()
                if dados:
                    obj.id = dados[0]
                    obj.inicio = dados[1]
                    obj.fim = dados[2]
                    obj.descricao = dados[3]
                    return obj
                else:
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[turno] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def obtem_turno(self, catraca=None, hora=None):
        turno = None
        if (catraca is None) or (hora is None):
            turno = self.busca_por_catraca(self.catraca_dao.obtem_catraca(), self.util.obtem_hora())
        else:
            turno = self.busca_por_catraca(catraca, hora)
        return turno

    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO turno("\
                        "turn_id, "\
                        "turn_hora_inicio, "\
                        "turn_hora_fim, "\
                        "turn_descricao) VALUES (" +\
                        str(obj.id) + ", '" +\
                        str(obj.inicio) + "', '" +\
                        str(obj.fim) + "', '" +\
                        str(obj.descricao) + "')"
                self.aviso = "[turno] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[turno] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[turno] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM turno"
                    self.aviso = "[turno] Excluido com sucesso!"
                else:
                    sql = "UPDATE turno SET " +\
                          "turn_hora_inicio = '" + str(obj.inicio) + "', " +\
                          "turn_hora_fim = '" + str(obj.fim) + "', " +\
                          "turn_descricao = '" + str(obj.descricao) +\
                          "' WHERE "\
                          "turn_id = " + str(obj.id)
                    self.aviso = "[turno] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[turno] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[turno] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        