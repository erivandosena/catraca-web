#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.isencao import Isencao


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class IsencaoDAO(ConexaoGenerica):

    def __init__(self):
        super(IsencaoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = Isencao()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT isen_id, isen_inicio, isen_fim, cart_id FROM isencao WHERE isen_id = " + str(id)
        elif id is None:
            sql = "SELECT isen_id, isen_inicio, isen_fim, cart_id FROM isencao ORDER BY isen_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.inicio = dados[1]
                        obj.fim = dados[2]
                        obj.cartao = self.busca_por_cartao(obj)
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
            self.log.logger.error('Erro ao realizar SELECT na tabela isencao.', exc_info=True)
        finally:
            pass
        
    def busca_por_cartao(self, obj):
        return CartaoDAO().busca(obj.id)
        
    def busca_por_isencao(self, obj):
        return CartaoDAO().busca_por_numero(obj.numero)
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO isencao("\
                        "isen_id, "\
                        "isen_inicio, "\
                        "isen_fim, "\
                        "cart_id) VALUES (" +\
                        str(obj.id) + ", " +\
                        str(obj.inicio) + ", " +\
                        str(obj.fim) + ", " +\
                        str(obj.cartao) + ")"
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
            self.log.logger.error('Erro realizando INSERT na tabela isencao.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    sql = "DELETE FROM isencao WHERE isen_id = " + str(obj.id)
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE isencao SET " +\
                          "isen_inicio = " + str(obj.inicio) + ", " +\
                          "isen_fim = " + str(obj.fim) + ", " +\
                          "cart_id = " + str(obj.cartao.id) +\
                          " WHERE "\
                          "cart_id = " + str(obj.id)
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
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela isencao.', exc_info=True)
            return False
        finally:
            pass
        