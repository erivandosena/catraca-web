#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from contextlib import closing
from catraca.logs import Logs
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.tipo import Tipo


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class TipoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(TipoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "tipo_nome as nome, "\
                "tipo_valor as valor, "\
                "tipo_id as id "\
                "FROM tipo WHERE "\
                "tipo_id = %s"
        else:
            sql = "SELECT "\
                "tipo_nome as nome, "\
                "tipo_valor as valor, "\
                "tipo_id as id "\
                "FROM tipo ORDER BY tipo_id"
        return self.seleciona(Tipo, sql, arg)
    
    def insere(self, obj):
        sql = "INSERT INTO tipo "\
            "("\
            "tipo_id, "\
            "tipo_nome, "\
            "tipo_valor "\
            ") VALUES ("\
            "%s, %s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE tipo SET "\
            "tipo_nome = %s, "\
            "tipo_valor = %s "\
            "WHERE tipo_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM tipo"
        if obj:
            sql = str(sql) + " WHERE tipo_id = %s"
        return self.deleta(sql, obj)
    
    def atualiza_exclui(self, obj, boleano):
        if obj or boleano:
            if boleano:
                if obj is None:
                    return self.exclui()
                else:
                    self.exclui(obj)
            else:
                return self.atualiza(obj)
    
#     def busca(self, *arg):
#         obj = Tipo()
#         id = None
#         for i in arg:
#             id = i
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 if id:
#                     sql_select = 'SELECT tipo_id, tipo_nome, tipo_valor FROM tipo WHERE tipo_id = %s'
#                     cursor.execute(sql_select % str(id))
#                 else:
#                     sql_select = 'SELECT tipo_id, tipo_nome, tipo_valor FROM tipo ORDER BY tipo_id'
#                     cursor.execute(sql_select)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados:
#                         obj.id = dados[0]
#                         obj.nome = dados[1]
#                         obj.valor = dados[2]
#                         return obj
#                     else:
#                         return None
#                 else:
#                     list = cursor.fetchall()
#                     if list != []:
#                         return list
#                     else:
#                         return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[tipo] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
#     def insere(self, obj):
#         try:
#             if obj:
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     sql_insert = 'INSERT INTO tipo(tipo_id, tipo_nome, tipo_valor) VALUES (%s, %s, %s)'
#                     cursor.execute(sql_insert, (obj.id, obj.nome, obj.valor))
#                     self.commit()
#                     self.aviso = "[tipo] Inserido com sucesso!"
#                     return True
#             else:
#                 self.aviso = "[tipo] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[tipo] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
#         
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     if delete:
#                         if obj is None:
#                             sql_delete = 'DELETE FROM tipo'
#                             cursor.execute(sql_delete)
#                         else:
#                             sql_delete = sql_delete +' WHERE tipo_id = %s'
#                             cursor.execute(sql_delete, (obj.id))
#                         self.aviso = "[tipo] Excluido com sucesso!"
#                         self.commit()
#                         return True
#                     else:
#                         sql_update = 'UPDATE tipo SET tipo_nome = %s, tipo_valor = %s WHERE tipo_id = %s'
#                         cursor.execute(sql_update, (obj.nome, obj.valor, obj.id))
#                         self.commit()
#                         self.aviso = "[tipo] Alterado com sucesso!"
#                         return True
#             else:
#                 self.aviso = "[tipo] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[tipo] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
#         