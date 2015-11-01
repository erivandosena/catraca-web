#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroDAO(ConexaoGenerica):

    def __init__(self):
        super(RegistroDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Registro()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT regi_id, regi_data, regi_valor_pago, regi_valor_custo, " +\
            "cart_id, turn_id, catr_id FROM registro WHERE regi_id = " + str(id)
        elif id is None:
            sql = "SELECT regi_id, regi_data, regi_valor_pago, regi_valor_custo, " +\
            "cart_id, turn_id, catr_id FROM registro ORDER BY regi_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.data = dados[1]
                        obj.pago = dados[2]
                        obj.custo = dados[3]
                        obj.cartao = self.busca_por_cartao(obj)
                        obj.turno = self.busca_por_turno(obj)
                        obj.catraca = self.busca_por_catraca(obj)
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
            self.log.logger.error('Erro ao realizar SELECT na tabela cartao.', exc_info=True)
        finally:
            pass
  
    def busca_por_cartao(self, obj):
        return CartaoDAO().busca(obj.id)
        
    def busca_por_turno(self, obj):
        return TurnoDAO().busca(obj.id)
        
    def busca_por_catraca(self, obj):
        return CatracaDAO().busca(obj.id)
    
    def busca_por_periodo(self, data_ini, data_fim):
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
        
    def busca_utilizacao(self, data_ini, data_fim, id_cartao, limite):
        sql = "SELECT count(regi_id) FROM registro " +\
            "WHERE (regi_data BETWEEN '"+ str(data_ini) +"' AND '"+ str(data_fim) +"') AND " +\
            "(cart_id = "+str(id_cartao)+")" #+\
            #" ORDER BY 1 DESC LIMIT "+str(limite)+";"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
                obj = cursor.fetchone()
                if obj:
                    return obj
                else:
                    return None
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro ao realizar SELECT na tabela registro.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO registro("\
                      "regi_id, "\
                      "regi_data, "\
                      "regi_valor_pago, "\
                      "regi_valor_custo, "\
                      "cart_id, "\
                      "turn_id, "\
                      "catr_id) VALUES (" +\
                      str(obj.id) + ", '" +\
                      str(obj.data) + "', " +\
                      str(obj.pago) + ", " +\
                      str(obj.custo) + ", " +\
                      str(obj.cartao) + ", " +\
                      str(obj.turno) + ", " +\
                      str(obj.catraca) + ")"
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
            self.log.logger.error('Erro realizando INSERT na tabela registro.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    sql = "DELETE FROM registro WHERE regi_id = " + str(obj.id)
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE registro SET " +\
                          "regi_data = '" + str(obj.data) + "', " +\
                          "regi_valor_pago = " + str(obj.pago) + ", " +\
                          "regi_valor_custo = " + str(obj.custo) + ", " +\
                          "cart_id = " + str(obj.cartao) + ", " +\
                          "turn_id = " + str(obj.turno) + ", " +\
                          "catr_id = " + str(obj.catraca) +\
                          " WHERE "\
                          "regi_id = " + str(obj.id)
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
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela registro.', exc_info=True)
            return False
        finally:
            pass
        
#     def mantem(self, obj, delete):
#         try:
#             if obj is not None:
#                 if delete:
#                     sql = "DELETE FROM registro WHERE regi_id = " + str(obj.id)
#                     self.aviso = "Excluido com sucesso!"
#                 else:
#                     if obj.id:
#                         sql = "UPDATE registro SET " +\
#                               "regi_data = '" + str(obj.data) + "', " +\
#                               "regi_valor_pago = " + str(obj.pago) + ", " +\
#                               "regi_valor_custo = " + str(obj.custo) + ", " +\
#                               "cart_id = " + str(obj.cartao) + ", " +\
#                               "turn_id = " + str(obj.turno) + ", " +\
#                               "catr_id = " + str(obj.catraca) +\
#                               " WHERE "\
#                               "regi_id = " + str(obj.id)
#                         self.aviso = "Alterado com sucesso!"
#                     else:
#                         sql = "INSERT INTO registro("\
#                               "regi_data, "\
#                               "regi_valor_pago, "\
#                               "regi_valor_custo, "\
#                               "cart_id, "\
#                               "turn_id, "\
#                               "catr_id) VALUES ('" +\
#                               str(obj.data) + "', " +\
#                               str(obj.pago) + ", " +\
#                               str(obj.custo) + ", " +\
#                               str(obj.cartao) + ", " +\
#                               str(obj.turno) + ", " +\
#                               str(obj.catraca) + ")"
#                         self.aviso = "Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "Objeto inexistente!"
#                 return False
#         except Exception, e:
#             self.aviso = str(e)
#             self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela registro.', exc_info=True)
#             return False
#         finally:
#             pass
        