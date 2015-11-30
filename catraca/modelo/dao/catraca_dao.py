#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.catraca import Catraca


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
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "catr_nome "\
                  "FROM catraca WHERE "\
                  "catr_id = " + str(id)
        elif id is None:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "catr_nome "\
                  "FROM catraca ORDER BY catr_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.ip = dados[1]
                        obj.tempo = dados[2]
                        obj.operacao = dados[3]
                        obj.nome = dados[4]
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
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def busca_por_ip(self, ip):
        obj = Catraca()
        sql = "SELECT catr_id, "\
              "catr_ip, "\
              "catr_tempo_giro, "\
              "catr_operacao, "\
              "catr_nome "\
              "FROM catraca WHERE "\
              "catr_ip = '" + str(ip) + "'"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.ip = dados[1]
                    obj.tempo = dados[2]
                    obj.operacao = dados[3]
                    obj.nome = dados[4]
                    return obj
                else:
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO catraca("\
                    "catr_id, "\
                    "catr_ip, "\
                    "catr_tempo_giro, "\
                    "catr_operacao, "\
                    "catr_nome) VALUES (" +\
                    str(obj.id) + ", '" +\
                    str(obj.ip) + "', " +\
                    str(obj.tempo) + ", " +\
                    str(obj.operacao) + ", '" +\
                    str(obj.nome) + "')"
                self.aviso = "[catraca] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return False
            else:
                self.aviso = "[catraca] inexistente!"
                return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[catraca] Erro realizando INSERT.', exc_info=True)
#             return False
        finally:
            pass   
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM catraca WHERE catr_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM catraca"
                    self.aviso = "[catraca] Excluido com sucesso!"
                else:
                    sql = "UPDATE catraca SET " +\
                        "catr_ip = '" + str(obj.ip) + "', " +\
                        "catr_tempo_giro = " + str(obj.tempo) + ", " +\
                        "catr_operacao = " + str(obj.operacao) + ", " +\
                        "catr_nome = '" + str(obj.nome) +\
                        "' WHERE "\
                        "catr_id = " + str(obj.id)
                    self.aviso = "[catraca] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[catraca] inexistente!"
                return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[catraca] Erro realizando UPDATE/DELETE.', exc_info=True)
#             return False
        finally:
            pass
        