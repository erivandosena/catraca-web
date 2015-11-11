#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.catraca_unidade import CatracaUnidade
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.dao.unidade_dao import UnidadeDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaUnidadeDAO(ConexaoGenerica):
    
    def __init__(self):
        super(CatracaUnidadeDAO, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def busca(self, *arg):
        obj = CatracaUnidade()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT caun_id, catr_id, unid_id FROM catraca_unidade WHERE caun_id = " + str(id)
        elif id is None:
            sql = "SELECT caun_id, catr_id, unid_id FROM catraca_unidade ORDER BY caun_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.catraca = self.busca_por_catraca(obj)
                        obj.unidade = self.busca_por_unidade(obj)
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
            self.log.logger.error('Erro ao realizar SELECT na tabela catraca_unidade.', exc_info=True)
        finally:
            pass
        
    def busca_por_catraca(self, obj):
        return CatracaDAO().busca(obj.id)
        
    def busca_por_unidade(self, obj):
        return UnidadeDAO().busca(obj.id)
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO catraca_unidade("\
                    "caun_id, "\
                    "catr_id, "\
                    "unid_id) VALUES (" +\
                    str(obj.id) + ", " +\
                    str(obj.catraca) + ", " +\
                    str(obj.unidade) + ")"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return False
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT na tabela catraca_unidade.', exc_info=True)
            return False
        finally:
            pass   
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    if obj.id:
                        sql = "DELETE FROM catraca_unidade WHERE caun_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM catraca_unidade"
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE catraca_unidade SET " +\
                        "catr_id = " + str(obj.catraca) + ", " +\
                        "unid_id = " + str(obj.unidade) +\
                        " WHERE "\
                        "caun_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return False
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela catraca_unidade.', exc_info=True)
            return False
        finally:
            pass
        