#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.util import Util
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.turno import Turno
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TurnoDAO(DAOGenerico):
    
    log = Logs()
    util = Util()
    #catraca_dao = CatracaDAO()

    def __init__(self):
        super(TurnoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
#     def busca(self, *arg):
#         arg = [a for a in arg][0] if arg else None
#         if arg:
#             sql = "SELECT "\
#                 "turn_descricao as descricao, "\
#                 "turn_hora_fim as interface, "\
#                 "turn_id as ip, "\
#                 "turn_hora_inicio as maclan "\
#                 "FROM catraca WHERE "\
#                 "catr_id = %s"
#         else:
#             sql = "SELECT "\
#                 "catr_id as id, "\
#                 "catr_interface_rede as interface, "\
#                 "catr_ip as ip, "\
#                 "catr_mac_lan as maclan, "\
#                 "catr_mac_wlan as macwlan, "\
#                 "catr_nome as nome, "\
#                 "catr_operacao as operacao, "\
#                 "catr_tempo_giro as tempo "\
#                 "FROM catraca ORDER BY 1"
#         return self.seleciona(Catraca, sql, arg)
        
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
                    "WHERE catraca.catr_nome = '"+str(obj.nome)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
        else:
            nome = self.util.obtem_nome_rpi().upper()
            sql = "SELECT turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno "\
                    "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
                    "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
                    "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
                    "WHERE catraca.catr_nome = '"+str(nome)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
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
            turno = self.busca_por_catraca( CatracaDAO().busca_por_ip(self.util.obtem_ip_por_interface()), self.util.obtem_hora() )
        else:
            turno = self.busca_por_catraca(catraca, hora)
        return turno
    
    def insere(self, obj):
        sql = "INSERT INTO turno "\
            "("\
            "turn_descricao, "\
            "turn_hora_fim, "\
            "turn_id, "\
            "turn_hora_inicio "\
            ") VALUES ("\
            "%s, %s, %s, %s)"
        return self.inclui(sql, obj)

#     def insere(self, obj):
#         try:
#             if obj:
#                 sql = "INSERT INTO turno("\
#                         "turn_id, "\
#                         "turn_hora_inicio, "\
#                         "turn_hora_fim, "\
#                         "turn_descricao) VALUES (" +\
#                         str(obj.id) + ", '" +\
#                         str(obj.inicio) + "', '" +\
#                         str(obj.fim) + "', '" +\
#                         str(obj.descricao) + "')"
#                 self.aviso = "[turno] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[turno] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[turno] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
        
    def atualiza(self, obj):
        sql = "UPDATE turno SET "\
            "turn_descricao = %s, "\
            "turn_hora_fim = %s, "\
            "turn_hora_inicio = %s "\
            "WHERE turn_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM turno"
        if obj:
            sql = str(sql) + " WHERE turn_id = %s"
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
        
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM turno"
#                     self.aviso = "[turno] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE turno SET " +\
#                           "turn_hora_inicio = '" + str(obj.inicio) + "', " +\
#                           "turn_hora_fim = '" + str(obj.fim) + "', " +\
#                           "turn_descricao = '" + str(obj.descricao) +\
#                           "' WHERE "\
#                           "turn_id = " + str(obj.id)
#                     self.aviso = "[turno] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[turno] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[turno] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
        