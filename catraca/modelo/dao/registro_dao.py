#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroDAO(ConexaoGenerica):

    def __init__(self):
        super(RegistroDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_data, "\
              "regi_valor_pago, "\
              "regi_valor_custo, "\
              "cart_id, "\
              "turn_id, "\
              "catr_id "\
              "FROM registro ORDER BY regi_data DESC"
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
            self.log.logger.error('Erro ao realizar SELECT na tabela tipo.', exc_info=True)
        finally:
            pass
  
    def busca_por_cartao(self, obj):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_data, "\
              "regi_valor_pago, "\
              "regi_valor_custo, "\
              "cart_id, "\
              "turn_id, "\
              "catr_id "\
              "FROM registro WHERE "\
              "cart_id = " + str(obj.id) +\
              " ORDER BY regi_data DESC"
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
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass
        
    def busca_por_turno(self, obj):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_data, "\
              "regi_valor_pago, "\
              "regi_valor_custo, "\
              "cart_id, "\
              "turn_id, "\
              "catr_id "\
              "FROM registro WHERE "\
              "turn_id = " + str(obj.id) +\
              " ORDER BY regi_data DESC"
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
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass
        
    def busca_por_catraca(self, obj):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_data, "\
              "regi_valor_pago, "\
              "regi_valor_custo, "\
              "cart_id, "\
              "turn_id, "\
              "catr_id "\
              "FROM registro WHERE "\
              "turn_id = " + str(obj.id) +\
              " ORDER BY regi_data DESC"
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
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass
        
    def busca_por_periodo(self, data_ini, data_fim):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_data, "\
              "regi_valor_pago, "\
              "regi_valor_custo, "\
              "cart_id, "\
              "turn_id, "\
              "catr_id "\
              "FROM registro WHERE "\
              "regi_data BETWEEN " + str(data_ini) +\
              " AND " + str(data_fim) +\
              " ORDER BY regi_data DESC"
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
            self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass
        
    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM registro WHERE regi_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE registro SET " +\
                              "regi_data = '" + str(obj.data) + "', " +\
                              "regi_valor_pago = " + str(obj.pago) + ", " +\
                              "regi_valor_custo = " + str(obj.custo) + ", " +\
                              "cart_id = " + str(obj.cartao.id) + ", " +\
                              "turn_id = " + str(obj.turno.id) + ", " +\
                              "catr_id = " + str(obj.catraca.id) +\
                              " WHERE "\
                              "regi_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO registro("\
                              "regi_data, "\
                              "regi_valor_pago, "\
                              "regi_valor_custo, "\
                              "cart_id, "\
                              "turn_id, "\
                              "catr_id) VALUES ('" +\
                              str(obj.data) + "', " +\
                              str(obj.pago) + ", " +\
                              str(obj.custo) + ", " +\
                              str(obj.cartao.id) + ", " +\
                              str(obj.turno.id) + ", " +\
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
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela registro.', exc_info=True)
            return False
        finally:
            pass
        