#!/usr/bin/env python
# -*- coding: latin-1 -*-


# from contextlib import closing
from catraca.logs import Logs
# from catraca.modelo.dados.conexao import ConexaoFactory
# from catraca.modelo.dados.conexao_generica import ConexaoGenerica
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.mensagem import Mensagem
#from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class MensagemDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(MensagemDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "mens_id as id, "\
                "mens_institucional1 as institucional1, "\
                "mens_institucional2 as institucional2, "\
                "mens_institucional3 as institucional3, "\
                "mens_institucional4 as institucional4 "\
                "FROM mensagem WHERE "\
                "mens_id = %s"
        else:
            sql = "SELECT "\
                "mens_id as id, "\
                "mens_institucional1 as institucional1, "\
                "mens_institucional2 as institucional2, "\
                "mens_institucional3 as institucional3, "\
                "mens_institucional4 as institucional4 "\
                "FROM mensagem ORDER BY mens_id"
        return self.seleciona(Mensagem, sql, arg)
     
    def insere(self, obj):
        sql = "INSERT INTO mensagem "\
            "("\
            "mens_id, "\
            "mens_institucional1, "\
            "mens_institucional2, "\
            "mens_institucional3, "\
            "mens_institucional4 "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s)"
        return self.inclui(sql, obj)
     
    def atualiza(self, obj):
        sql = "UPDATE mensagem SET "\
            "mens_institucional1 = %s, "\
            "mens_institucional2 = %s, "\
            "mens_institucional3 = %s, "\
            "mens_institucional4 = %s "\
            "WHERE mens_id = %s"
        return self.altera(sql, obj)
     
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM mensagem"
        if obj:
            sql = str(sql) + " WHERE mens_id = %s"
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
#         obj = Mensagem()
#         id = None
#         for i in arg:
#             id = i
#         if id:
#             sql = "SELECT mens_id, mens_institucional1, mens_institucional2, "\
#             "mens_institucional3, mens_institucional4, catr_id FROM mensagem WHERE mens_id = " + str(id)
#         elif id is None:
#             sql = "SELECT mens_id, mens_institucional1, mens_institucional2, "\
#             "mens_institucional3, mens_institucional4, catr_id FROM mensagem ORDER BY mens_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 if id:
#                     dados = cursor.fetchone()
#                     if dados is not None:
#                         obj.id = dados[0]
#                         obj.institucional1 = dados[1]
#                         obj.institucional2 = dados[2]
#                         obj.institucional3 = dados[3]
#                         obj.institucional4 = dados[4]
#                         obj.catraca = dados[5]
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
#             self.log.logger.error('[mensagem] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
# #     def busca_por_catraca(self, obj):
# #         return CatracaDAO().busca(obj.id)        
#         
#     def obtem_mensagens(self, obj):
#         sql = "SELECT mens_id, mens_institucional1, mens_institucional2, "\
#         "mens_institucional3, mens_institucional4, catr_id FROM mensagem WHERE catr_id = " + str(obj.id)+ " ORDER BY mens_id"
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql)
#                 list = cursor.fetchall()
#                 if list != []:
#                     return list
#                 else:
#                     return None
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[mensagem] Erro ao realizar SELECT.', exc_info=True)
#         finally:
#             pass
#         
#     def insere(self, obj):
#         try:
#             if obj:
#                 sql = "INSERT INTO mensagem("\
#                     "mens_id, "\
#                     "mens_institucional1, "\
#                     "mens_institucional2, "\
#                     "mens_institucional3, "\
#                     "mens_institucional4, "\
#                     "catr_id) VALUES (" +\
#                     str(obj.id) + ", '" +\
#                     str(obj.institucional1) + "', '" +\
#                     str(obj.institucional2) + "', '" +\
#                     str(obj.institucional3) + "', '" +\
#                     str(obj.institucional4) + "', " +\
#                     str(obj.catraca) + ")"
#                 self.aviso = "[mensagem] Inserido com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[mensagem] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[mensagem] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass
# 
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 if delete:
#                     if obj:
#                         sql = "DELETE FROM mensagem WHERE mens_id = " + str(obj.id)
#                     else:
#                         sql = "DELETE FROM mensagem"
#                     self.aviso = "[mensagem] Excluido com sucesso!"
#                 else:
#                     sql = "UPDATE mensagem SET " +\
#                         "mens_institucional1 = '" + str(obj.institucional1) + "', " +\
#                         "mens_institucional2 = '" + str(obj.institucional2) + "', " +\
#                         "mens_institucional3 = '" + str(obj.institucional3) + "', " +\
#                         "mens_institucional4 = '" + str(obj.institucional4) + "', " +\
#                         "catr_id = " + str(obj.catraca) +\
#                         " WHERE "\
#                         "mens_id = " + str(obj.id)
#                     self.aviso = "[mensagem] Alterado com sucesso!"
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     cursor.execute(sql)
#                     self.commit()
#                     return True
#             else:
#                 self.aviso = "[mensagem] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[mensagem] Erro realizando DELETE/UPDATE.', exc_info=True)
#             return False
#         finally:
#             pass
        