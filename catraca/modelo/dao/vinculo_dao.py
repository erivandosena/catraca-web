#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.vinculo import Vinculo
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.usuario_dao import UsuarioDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class VinculoDAO(ConexaoGenerica):
    
    log = Logs()

    def __init__(self):
        super(VinculoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Vinculo()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
            "vinc_refeicoes, cart_id, usua_id FROM vinculo WHERE vinc_id = " + str(id)
        elif id is None:
            sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
            "vinc_refeicoes, cart_id, usua_id FROM vinculo ORDER BY vinc_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.avulso = dados[1]
                        obj.inicio = dados[2]
                        obj.fim = dados[3]
                        obj.descricao = dados[4]
                        obj.refeicoes = dados[5]
                        obj.cartao = dados[6]
                        obj.usuario = dados[7]
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
            self.log.logger.error('[vinculo] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
  
#     def busca_por_cartao(self, obj):
#         return CartaoDAO().busca(obj.id)
#         
#     def busca_por_usuario(self, obj):
#         return UsuarioDAO().busca(obj.id)
    
    def busca_por_periodo(self, data_ini, data_fim, cartao):
        sql = "SELECT vinc_id, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, "\
                "vinc_refeicoes, cart_id, usua_id FROM vinculo WHERE "\
                "regi_data BETWEEN " + str(data_ini) +\
                " AND " + str(data_fim) + " AND cart_id = "  + str(cartao.id) +\
                " ORDER BY vinc_inicio DESC"
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
            self.log.logger.error('[vinculo] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO vinculo("\
                      "vinc_id, "\
                      "vinc_avulso, "\
                      "vinc_inicio, "\
                      "vinc_fim, "\
                      "vinc_descricao, "\
                      "vinc_refeicoes, "\
                      "cart_id, "\
                      "usua_id) VALUES (" +\
                      str(obj.id) + ", " +\
                      str(obj.avulso) + ", '" +\
                      str(obj.inicio) + "', '" +\
                      str(obj.fim) + "', '" +\
                      str(obj.descricao) + "', " +\
                      str(obj.refeicoes) + ", " +\
                      str(obj.cartao) + ", " +\
                      str(obj.usuario) + ")"
                self.aviso = "[vinculo] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[vinculo] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[vinculo] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM vinculo WHERE vinc_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM vinculo"
                    self.aviso = "[vinculo] Excluido com sucesso!"
                else:
                    sql = "UPDATE vinculo SET " +\
                          "vinc_avulso = " + str(obj.avulso) + ", " +\
                          "vinc_inicio = '" + str(obj.inicio) + "', " +\
                          "vinc_fim = '" + str(obj.fim) + "', " +\
                          "vinc_descricao = '" + str(obj.descricao) + "', " +\
                          "vinc_refeicoes = " + str(obj.refeicoes) + ", " +\
                          "cart_id = " + str(obj.cartao) + ", " +\
                          "usua_id = " + str(obj.usuario) +\
                          " WHERE "\
                          "vinc_id = " + str(obj.id)
                    self.aviso = "[vinculo] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[vinculo] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[vinculo] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        
