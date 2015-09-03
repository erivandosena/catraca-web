#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from turno import Turno
from finalidadedao import FinalidadeDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TurnoDAO(ConexaoGenerica):

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
                   "fina_id, "\
                   "catr_id "\
                   "FROM turno WHERE "\
                   "turn_id = " + str(id)
        elif id is None:
            sql = "SELECT turn_id, "\
                   "turn_hora_inicio, "\
                   "turn_hora_fim, "\
                   "fina_id, "\
                   "catr_id "\
                   "FROM turno"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.inicio = dados[1]
                        obj.fim = dados[2]
                        obj.finalidade = FinalidadeDAO().busca(dados[3])
                        obj.catraca = dados[4]
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
        
    def busca_por_catraca(self, catraca):
        obj = Turno()
        sql = "SELECT turn_id, "\
               "turn_hora_inicio, "\
               "turn_hora_fim, "\
               "fina_id, "\
               "catr_id "\
               "FROM turno WHERE "\
               "catr_id = " + str(catraca)
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
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
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM turno WHERE turn_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE turno SET " +\
                              "turn_hora_inicio = '" + str(obj.inicio) + "', " +\
                              "turn_hora_fim = '" + str(obj.fim) + "', " +\
                              "fina_id = " + str(obj.finalidade.id) +\
                              " WHERE "\
                              "turn_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO turno("\
                              "turn_hora_inicio, "\
                              "turn_hora_fim, "\
                              "fina_id) VALUES ('" +\
                              str(obj.inicio) + "', '" +\
                              str(obj.fim) + "', " +\
                              str(obj.data) + ", " +\
                              str(obj.finalidade.id) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    self.aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.__aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela turno.', exc_info=True)
            return False
        finally:
            pass
        