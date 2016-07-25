#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.entidades.unidade import Unidade


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeDAO(ConexaoGenerica):
    
    log = Logs()
    
    def __init__(self):
        super(UnidadeDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self, *arg):
        obj = Unidade()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT unid_id, unid_nome FROM unidade WHERE unid_id = " + str(id)
        elif id is None:
            sql = "SELECT unid_id, unid_nome FROM unidade ORDER BY unid_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
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
            self.log.logger.error('[unidade] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO unidade(unid_id, unid_nome) VALUES (" + str(obj.id) + ",'" + str(obj.nome) + "')"
                self.aviso = "[unidade] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[unidade] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[unidade] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            cursor.close()
            pass

    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM unidade WHERE unid_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM unidade"
                    self.aviso = "[unidade] Excluido com sucesso!"
                else:
                    sql = "UPDATE unidade SET unid_nome = '" + str(obj.nome) + "' WHERE unid_id = " + str(obj.id)
                    self.aviso = "[unidade] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[unidade] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[unidade] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        