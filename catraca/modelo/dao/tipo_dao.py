#!/usr/bin/env python
# -*- coding: utf-8 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.tipo import Tipo


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TipoDAO(ConexaoGenerica):
    
    log = Logs()

    def __init__(self):
        super(TipoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
    
    def busca(self, *arg):
        obj = Tipo()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT tipo_id, tipo_nome, tipo_valor FROM tipo WHERE tipo_id = " + str(id)
        else:
            sql = "SELECT tipo_id, tipo_nome, tipo_valor FROM tipo ORDER BY tipo_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados:
                        obj.id = dados[0]
                        obj.nome = dados[1]
                        obj.valor = dados[2]
                        return obj
                    else:
                        return None
                else:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[tipo] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO tipo("\
                        "tipo_id, "\
                        "tipo_nome, "\
                        "tipo_valor) VALUES (" +\
                        str(obj.id) + ", '" +\
                        str(obj.nome) + "', '" +\
                        str(obj.valor) + "')"
                self.aviso = "[tipo] Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[tipo] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[tipo] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                if delete:
                    if obj:
                        sql = "DELETE FROM tipo WHERE tipo_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM tipo"
                    self.aviso = "[tipo] Excluido com sucesso!"
                else:
                    sql = "UPDATE tipo SET " +\
                          "tipo_nome = '" + str(obj.nome) + "', " +\
                          "tipo_valor = '" + str(obj.valor) +\
                          "' WHERE "\
                          "tipo_id = " + str(obj.id)
                    self.aviso = "[tipo] Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "[tipo] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[tipo] Erro realizando DELETE/UPDATE.', exc_info=True)
            return False
        finally:
            pass
        
        
        