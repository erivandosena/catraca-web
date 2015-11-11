#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
<<<<<<< HEAD
from catraca.util import Util
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.turno import Turno
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.recursos.catraca_json import CatracaJson
=======
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.turno import Turno

>>>>>>> remotes/origin/web_backend

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TurnoDAO(ConexaoGenerica):
<<<<<<< HEAD
    
    util = Util()
=======
>>>>>>> remotes/origin/web_backend

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
<<<<<<< HEAD
                   "FROM turno ORDER BY turn_id"
=======
                   "FROM turno"
>>>>>>> remotes/origin/web_backend
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
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela turno.', exc_info=True)
        finally:
            pass
        
<<<<<<< HEAD
    def busca_por_catraca(self, obj, hora_atual):
        if obj:
            print "passou >>> if obj:"
            sql = "SELECT turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno "\
                    "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
                    "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
                    "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
                    "WHERE catraca.catr_ip = '"+str(obj.ip)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
        else:
            print "passou >>> else: ip = self.util.obtem_ip()"
            ip = self.util.obtem_ip()
            sql = "SELECT turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno "\
                    "INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id "\
                    "INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id "\
                    "INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id "\
                    "WHERE catraca.catr_ip = '"+str(ip)+"' "\
                    "AND turno.turn_hora_inicio <= '" + str(hora_atual) +"' "\
                    "AND turno.turn_hora_fim >= '" + str(hora_atual) + "'"
 
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                list = cursor.fetchone()
                if list != []:
                    return list
                else:
                    return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela turno.', exc_info=True)
        finally:
            pass
        
    def obtem_catraca(self):
#         catraca = CatracaDAO().busca_por_ip(self.util.obtem_ip())
#         if catraca:
#             print " PASSOU ==>>>> catraca"
#             return catraca
#         else:
#             print " PASSOU ==>>>> else: CatracaJson().catraca_get()"
#             CatracaJson().catraca_get()
#             catraca = CatracaDAO().busca_por_ip(self.util.obtem_ip())
        return CatracaDAO().busca_por_ip(self.util.obtem_ip())
        
        
    def obtem_turno(self):
        turno = self.busca_por_catraca(self.obtem_catraca(), self.util.obtem_hora())
        print "select no BD!"
        if turno:      
            return turno
        else:
            return None
   
=======
>>>>>>> remotes/origin/web_backend
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
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.__aviso = str(e)
<<<<<<< HEAD
            self.log.logger.error('Erro realizando INSERT na tabela turno.', exc_info=True)
=======
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela turno.', exc_info=True)
>>>>>>> remotes/origin/web_backend
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
<<<<<<< HEAD
                    if obj.id:
                        sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM turno"
                    self.aviso = "Excluido com sucesso!"
=======
                    sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
>>>>>>> remotes/origin/web_backend
                else:
                    sql = "UPDATE turno SET " +\
                          "turn_hora_inicio = '" + str(obj.inicio) + "', " +\
                          "turn_hora_fim = '" + str(obj.fim) + "', " +\
                          "turn_descricao = '" + str(obj.descricao) +\
                          "' WHERE "\
                          "turn_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.__aviso = str(e)
<<<<<<< HEAD
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela turno.', exc_info=True)
=======
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela turno.', exc_info=True)
>>>>>>> remotes/origin/web_backend
            return False
        finally:
            pass
        