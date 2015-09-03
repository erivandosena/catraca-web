#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from catraca import Catraca
from girodao import GiroDAO
from turnodao import TurnoDAO
from mensagemdao import MensagemDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(ConexaoGenerica):

    def __init__(self):
        super(CatracaDAO, self).__init__()
        ConexaoGenerica.__init__(self)
 
    def busca(self, *arg):
        obj = Catraca()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_localizacao, "\
                  "catr_tempo_giro, "\
                  "catr_operacao "\
                  "FROM catraca WHERE "\
                  "catr_id = " + str(id)
        elif id is None:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_localizacao, "\
                  "catr_tempo_giro, "\
                  "catr_operacao "\
                  "FROM catraca"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.ip = dados[1]
                        obj.localizacao = dados[2]
                        obj.tempo = dados[3]
                        obj.operacao = dados[4]
                        obj.giro = GiroDAO().busca_por_catraca(dados[0])
                        obj.turno = TurnoDAO().busca_por_catraca(dados[0])
                        obj.mensagem = MensagemDAO().busca_por_catraca(dados[0])
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
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca.', exc_info=True)
        finally:
            pass
        
    def busca_por_ip(self, ip):
        obj = Catraca()
        sql = "SELECT catr_id, "\
              "catr_ip, "\
              "catr_localizacao, "\
              "catr_tempo_giro, "\
              "catr_operacao "\
              "FROM catraca WHERE "\
              "catr_ip = '" + str(ip) + "'"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.ip = dados[1]
                    obj.localizacao = dados[2]
                    obj.tempo = dados[3]
                    obj.operacao = dados[4]
                    obj.giro = GiroDAO().busca_por_catraca(dados[0])
                    obj.turno = TurnoDAO().busca_por_catraca(dados[0])
                    obj.mensagem = MensagemDAO().busca_por_catraca(dados[0])
                    return obj
                else:
                    return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM catraca WHERE catr_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE catraca SET " +\
                              "catr_ip = '" + str(obj.ip) + "', " +\
                              "catr_localizacao = '" + str(obj.localizacao) + "', " +\
                              "catr_tempo_giro = " + str(obj.tempo) + ", " +\
                              "catr_operacao = " + str(obj.giro.operacao) +\
                              " WHERE "\
                              "catr_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO catraca("\
                              "catr_ip, "\
                              "catr_localizacao, "\
                              "catr_tempo_giro, "\
                              "catr_operacao) VALUES ('" +\
                              str(obj.ip) + "', '" +\
                              str(obj.localizacao) + "', " +\
                              str(obj.tempo) + ", " +\
                              str(obj.operacao) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    self.aviso = msg
                    return False
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela catraca.', exc_info=True)
            return False
        finally:
            pass
        