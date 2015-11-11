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
<<<<<<< HEAD
                  "giro_id = " + str(id)
=======
                  "giro_id = " + str(id) +\
                  " ORDER BY giro_data_giros DESC"
>>>>>>> remotes/origin/web_backend
        elif id is None:
            sql = "SELECT giro_id, "\
                  "giro_giros_horario, "\
                  "giro_giros_antihorario, "\
                  "giro_data_giros, "\
                  "catr_id "\
<<<<<<< HEAD
                  "FROM giro ORDER BY giro_id"
=======
                  "FROM giro ORDER BY giro_data_giros DESC"
>>>>>>> remotes/origin/web_backend
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
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela giro.', exc_info=True)
        finally:
            pass
        
<<<<<<< HEAD
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
=======
    def busca_por_catraca(self, id):
        sql = "SELECT giro_id, "\
              "giro_giros_horario, "\
              "giro_giros_antihorario, "\
              "giro_data_giros, "\
              "catr_id "\
              "FROM giro WHERE "\
              "catr_id = " + str(id) +\
              " ORDER BY giro_data_giros DESC"
>>>>>>> remotes/origin/web_backend
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
<<<<<<< HEAD
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
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
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT na tabela giro.', exc_info=True)
            return False
        finally:
            pass
          
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    if obj.id:
                        sql = "DELETE FROM giro WHERE giro_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM giro"
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE giro SET " +\
                        "giro_giros_horario = " + str(obj.horario) + ", " +\
                        "giro_giros_antihorario = " + str(obj.antihorario) + ", " +\
                        "giro_data_giros = '" + str(obj.data) + "', " +\
                        "catr_id = " + str(obj.catraca.id) +\
                        " WHERE "\
                        "giro_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela giro.', exc_info=True)
            return False
        finally:
            pass
        
    def mantem_giro_off(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM giro_off WHERE giof_id = " + str(obj.id)
                    self.aviso = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE giro_off SET " +\
                            "giof_giros_horario = " + str(obj.horario) + ", " +\
                            "giof_giros_antihorario = " + str(obj.antihorario) + ", " +\
                            "giof_data_giros = '" + str(obj.data) + "', " +\
                            "catr_id = " + str(obj.catraca.id) +\
                            " WHERE "\
                            "giof_id = " + str(obj.id)
                        self.aviso = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO giro_off("\
                            "giof_giros_horario, "\
                            "giof_giros_antihorario, "\
                            "giof_data_giros, catr_id) VALUES (" +\
                            str(obj.horario) + ", " +\
                            str(obj.antihorario) + ", '" +\
                            str(obj.data) + "', " +\
                            str(obj.catraca.id) + ")"
                        self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela giro_off.', exc_info=True)
=======
            self.log.logger.error('Erro ao realizar SELECT na tabela giro.', exc_info=True)
        finally:
            pass
          
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM tipo WHERE giro_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE giro SET " +\
                              "giro_giros_horario = " + str(obj.horario) + ", " +\
                              "giro_giros_antihorario = " + str(obj.antihorario) + ", " +\
                              "giro_tempo_realizado = " + str(obj.tempo) + ", " +\
                              "giro_data_giro = '" + str(obj.data) + "', " +\
                              "catr_id = " + str(obj.catraca.id) +\
                              " WHERE "\
                              "giro_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO giro("\
                              "giro_giros_horario, "\
                              "giro_giros_antihorario, "\
                              "giro_tempo_realizado, "\
                              "giro_data_giro, catr_id) VALUES (" +\
                              str(obj.horario) + ", " +\
                              str(obj.antihorario) + ", " +\
                              str(obj.tempo) + ", '" +\
                              str(obj.data) + "', " +\
                              str(obj.catraca.id) + ")"
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
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela giro.', exc_info=True)
>>>>>>> remotes/origin/web_backend
            return False
        finally:
            pass
        