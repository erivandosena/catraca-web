#!/usr/bin/env python
# -*- coding: latin-1 -*-


# from contextlib import closing
from catraca.logs import Logs
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.usuario import Usuario


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UsuarioDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(UsuarioDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "usua_id as id, "\
                "usua_nome as nome, "\
                "usua_email as email, "\
                "usua_login as login, "\
                "usua_senha as senha, "\
                "usua_nivel as nivel "\
                "FROM usuario WHERE "\
                "usua_id = %s"
        else:
            sql = "SELECT "\
                "usua_id as id, "\
                "usua_nome as nome, "\
                "usua_email as email, "\
                "usua_login as login, "\
                "usua_senha as senha, "\
                "usua_nivel as nivel "\
                "FROM usuario ORDER BY usua_id"
        return self.seleciona(Usuario, sql, arg)
    
    def insere(self, obj):
        sql = "INSERT INTO usuario "\
            "("\
            "usua_email, "\
            "usua_id, "\
            "usua_login, "\
            "usua_nivel, "\
            "usua_nome, "\
            "usua_senha "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s)"
        return self.inclui(sql, obj)
     
    def atualiza(self, obj):
        sql = "UPDATE usuario SET "\
            "usua_email = %s, "\
            "usua_login = %s, "\
            "usua_nivel = %s, "\
            "usua_nome = %s, "\
            "usua_senha = %s "\
            "WHERE usua_id = %s"
        return self.altera(sql, obj)
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM usuario"
        if obj:
            sql = str(sql) + " WHERE usua_id = %s"
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
#         obj = Usuario()
#         id = None
#         for i in arg:
#             id = i
#         if id:
#             sql = "SELECT usua_id, "\
#                   "usua_nome, "\
#                   "usua_email, "\
#                   "usua_login, "\
#                   "usua_senha, "\
#                   "usua_nivel "\
#                   "FROM usuario WHERE "\
#                   "usua_id = " + str(id)
#         elif id is None:
#             sql = "SELECT usua_id, "\
#                   "usua_nome, "\
#                   "usua_email, "\
#                   "usua_login, "\
#                   "usua_senha, "\
#                   "usua_nivel "\
#                   "FROM usuario ORDER BY usua_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados is not None:
#                         obj.id = dados[0]
#                         obj.nome = dados[1]
#                         obj.email = dados[2]
#                         obj.login = dados[3]
#                         obj.senha = dados[4]
#                         obj.nivel = dados[5]
#                         return obj
#                     else:
#                         return None
#                 elif id is None:
#                     list = cursor.fetchall()
#                     if list != []:
#                         return list
#                     else:
#                         return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[usuario] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
#     def insere(self, obj):
#         try:
#             if obj:
#                 sql = "INSERT INTO usuario("\
#                       "usua_id, "\
#                       "usua_nome, "\
#                       "usua_email, "\
#                       "usua_login, "\
#                       "usua_senha, "\
#                       "usua_nivel) VALUES (" +\
#                       str(obj.id) + ", '" +\
#                       str(obj.nome) + "', '" +\
#                       str(obj.email) + "', '" +\
#                       str(obj.login) + "', '" +\
#                       str(obj.senha) + "', " +\
#                       str(obj.nivel) + ")"
#                 self.aviso = "[usuario] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[usuario] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[usuario] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
#         
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM usuario WHERE usua_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM usuario"
#                     self.aviso = "[usuario] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE usuario SET " +\
#                           "usua_nome = '" + str(obj.nome) + "', " +\
#                           "usua_email = '" + str(obj.email) + "', " +\
#                           "usua_login = '" + str(obj.login) + "', " +\
#                           "usua_senha = '" + str(obj.senha) + "', " +\
#                           "usua_nivel = " + str(obj.nivel) +\
#                           " WHERE "\
#                           "usua_id = " + str(obj.id)
#                     self.aviso = "[usuario] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[usuario] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[usuario] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
        