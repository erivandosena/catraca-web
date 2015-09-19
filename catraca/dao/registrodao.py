#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from conexao import ConexaoFactory
from conexaogenerica import ConexaoGenerica
from registro import Registro
from cartaodao import CartaoDAO
from turnodao import TurnoDAO


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
            sql = "SELECT regi_id, "\
                  "regi_datahora, "\
                  "regi_giro, "\
                  "regi_valor, "\
                  "cart_id, "\
                  "turn_id "\
                  "FROM registro WHERE "\
                  "cart_id = " + str(id) +\
                  " ORDER BY regi_datahora DESC"
        elif id is None:
            sql = "SELECT regi_id, "\
                  "regi_datahora, "\
                  "regi_giro, "\
                  "regi_valor, "\
                  "cart_id, "\
                  "turn_id "\
                  "FROM registro ORDER BY regi_datahora DESC"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.data = dados[1]
                        obj.giro = dados[2]
                        obj.valor = dados[3]
                        obj.cartao = CartaoDAO().busca(dados[4])
                        obj.turno = TurnoDAO().busca(dados[5])
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
            self.log.logger.error('Erro ao realizar SELECT na tabela tipo.', exc_info=True)
        finally:
            pass
        

    def busca_por_periodo(self, data1, data2):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_datahora, "\
              "regi_giro, "\
              "regi_valor, "\
              "cart_id, "\
              "turn_id "\
              "FROM registro WHERE "\
              "regi_datahora BETWEEN " + str(data1) +\
              " AND " + str(data2) +\
              " ORDER BY regi_datahora DESC"
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
        
    def busca_por_cartao(self, cartao):
        obj = Registro()
        sql = "SELECT regi_id, "\
              "regi_datahora, "\
              "regi_giro, "\
              "regi_valor, "\
              "cart_id, "\
              "turn_id "\
              "FROM registro WHERE "\
              "cart_id = " + str(cartao)
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
                              "regi_datahora = '" + str(obj.data) + "', " +\
                              "regi_giro = " + str(obj.giro) + ", " +\
                              "regi_valor = " + str(obj.valor) + ", " +\
                              "cart_id = " + str(obj.cartao.id) + ", " +\
                              "turn_id = " + str(obj.turno.id) +\
                              " WHERE "\
                              "regi_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO registro("\
                              "regi_datahora, "\
                              "regi_giro, "\
                              "regi_valor, "\
                              "cart_id, "\
                              "turn_id) VALUES ('" +\
                              str(obj.data) + "', " +\
                              str(obj.giro) + ", " +\
                              str(obj.valor) + ", " +\
                              str(obj.cartao.id) + ", " +\
                              str(obj.turno.id) + ")"
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
        