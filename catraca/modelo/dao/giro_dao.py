#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.giro import Giro
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class GiroDAO(ConexaoGenerica):

    def __init__(self):
        super(GiroDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Giro()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT giro_id, "\
                  "giro_giros_horario, "\
                  "giro_giros_antihorario, "\
                  "giro_data_giros, "\
                  "catr_id "\
                  "FROM giro WHERE "\
                  "giro_id = " + str(id)
        elif id is None:
            sql = "SELECT giro_id, "\
                  "giro_giros_horario, "\
                  "giro_giros_antihorario, "\
                  "giro_data_giros, "\
                  "catr_id "\
                  "FROM giro ORDER BY giro_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.horario = dados[1]
                        obj.antihorario = dados[2]
                        obj.data = dados[3]
                        obj.catraca = CatracaDAO().busca(dados[4])
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
            self.log.logger.error('[giro] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def busca_por_catraca(self, obj):
        return CatracaDAO().busca(obj.id)
    
    def busca_por_periodo(self, data_ini, data_fim, catraca):
        sql = "SELECT giro_id, "\
            "giro_giros_horario, "\
            "giro_giros_antihorario, "\
            "giro_data_giros, "\
            "catr_id "\
            "FROM giro WHERE "\
            "giro_data_giros BETWEEN " + str(data_ini) +\
            " AND " + str(data_fim) +\
            " AND catr_id = " + str(catraca.id) +\
            " ORDER BY giro_data_giros DESC"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                list = cursor.fetchall()
                if list != []:
                    return list
                else:
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[giro] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO giro("\
                    "giro_id, "\
                    "giro_giros_horario, "\
                    "giro_giros_antihorario, "\
                    "giro_data_giros, catr_id) VALUES (" +\
                    str(obj.id) + ", " +\
                    str(obj.horario) + ", " +\
                    str(obj.antihorario) + ", '" +\
                    str(obj.data) + "', " +\
                    str(obj.catraca.id) + ")"
                self.aviso = "[giro] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[giro] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[giro] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass
          
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM giro WHERE giro_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM giro"
                    self.aviso = "[giro] Excluido com sucesso!"
                else:
                    sql = "UPDATE giro SET " +\
                        "giro_giros_horario = " + str(obj.horario) + ", " +\
                        "giro_giros_antihorario = " + str(obj.antihorario) + ", " +\
                        "giro_data_giros = '" + str(obj.data) + "', " +\
                        "catr_id = " + str(obj.catraca.id) +\
                        " WHERE "\
                        "giro_id = " + str(obj.id)
                    self.aviso = "[giro] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[giro] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[giro] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        
    def mantem_giro_off(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM giro_off WHERE giof_id = " + str(obj.id)
                    self.aviso = "[giro-off] Excluido com sucesso!"
                else:
                    if obj:
                        sql = "UPDATE giro_off SET " +\
                            "giof_giros_horario = " + str(obj.horario) + ", " +\
                            "giof_giros_antihorario = " + str(obj.antihorario) + ", " +\
                            "giof_data_giros = '" + str(obj.data) + "', " +\
                            "catr_id = " + str(obj.catraca.id) +\
                            " WHERE "\
                            "giof_id = " + str(obj.id)
                        self.aviso = "[giro-off] Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO giro_off("\
                            "giof_giros_horario, "\
                            "giof_giros_antihorario, "\
                            "giof_data_giros, catr_id) VALUES (" +\
                            str(obj.horario) + ", " +\
                            str(obj.antihorario) + ", '" +\
                            str(obj.data) + "', " +\
                            str(obj.catraca.id) + ")"
                        self.aviso = "[giro-off] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[giro-off] Erro realizando INSERT/UPDATE/DELETE.', exc_info=True)
            return False
        finally:
            pass
        