#!/usr/bin/env python
# -*- coding: latin-1 -*-

import json
from operator import itemgetter
from collections import OrderedDict

from typing import TypeVar
from typing import Generic
from typing import Sequence
from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dados.conexao_generica import ConexaoGenerica




__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


T = TypeVar('T')


class DAOGenerico(ConexaoGenerica, Generic[T]):
    
    log = Logs()
    
    def __init__(self):
        super(DAOGenerico, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def seleciona(self, T , sql, *arg):
        obj = T()
        #colunas = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict')).keys()
        try:
            with closing(self.abre_conexao().cursor('cursor_unique_name', cursor_factory=self.extras.DictCursor)) as cursor:
                cursor.execute(sql, arg)
                if [argumento for argumento in arg if argumento]:
                    dados = cursor.fetchone()
                    cursor.query
                    if dados:
                        for (campo, valor) in zip((nom[0] for nom in cursor.description), [val for val in dados]):
                            setattr(obj, campo, valor)
                        return obj
                else:
                    lista = cursor.fetchall()
                    cursor.query
                    if lista != []:
                        return lista
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def inclui(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            if obj:
                with closing(self.abre_conexao().cursor()) as cursor:
                    colunas = dict((name, getattr(obj, name)) for name in obj.__dict__).keys()
                    valores = dict((name, getattr(obj, name)) for name in obj.__dict__)
                    lista_ordenada = self.ordem_customizada(sorted(colunas))
                    lista_valores = lista_ordenada(valores)
                    cursor.execute(sql, lista_valores.values())
                    #print cursor.query
                    #self.commit()
                    self.aviso = "Inserido com sucesso!"
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def altera(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            if obj:
                with closing(self.abre_conexao().cursor()) as cursor:
                    colunas = dict((name, getattr(obj, name)) for name in obj.__dict__).keys()
                    valores = dict((name, getattr(obj, name)) for name in obj.__dict__)
                    lista_ordenada = self.ordem_customizada(sorted(colunas))
                    lista_valores = lista_ordenada(valores)
                    cursor.execute(sql, lista_valores.values())
                    print cursor.query
                    #self.commit()
                    self.aviso = "Alterado com sucesso!"
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def deleta(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                if obj:
                    cursor.execute(sql, (obj.id,))
                    print cursor.query
                else:
                    cursor.execute(sql)
                    print cursor.query
                #self.commit()
                self.aviso = "Deletado com sucesso!"
                return True
#         else:
#             self.aviso = "Objeto inexistente!"
#             return False
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
#     def altera_deleta(self, sql, boleano, *arg):
#         obj = [a for a in arg][0]
#         try:
#             if obj or boleano:
#                 if boleano:
#                     if obj is None:
#                         self.deleta(sql)
#                     else:
#                         self.deleta(sql, obj)
#                     return True
#                 else:
#                     self.altera(sql)
#                     return True
#             else:
#                 return False
#         except Exception as excecao:
#             self.log.logger.error(exc_info=True)
            
#     def atualiza_exclui(self, obj, delete):
#         try:
#             if obj or delete:
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     if delete:
#                         if obj is None:
#                             sql_delete = 'DELETE FROM catraca'
#                             cursor.execute(sql_delete)
#                         else:
#                             sql_delete = sql_delete +' WHERE catr_id = %s'
#                             cursor.execute(sql_delete, (obj.id))
#                         self.commit()
#                         self.aviso = "[catraca] Excluido com sucesso!"
#                         return True
#                     else:
#                         sql_update = 'UPDATE catraca SET catr_ip = %s, ' +\
#                               'catr_tempo_giro = %s, ' +\
#                               'catr_operacao = %s, ' +\
#                               'catr_nome = %s, ' +\
#                               'catr_mac_lan = %s, ' +\
#                               'catr_mac_wlan = %s, ' +\
#                               'catr_interface_rede = %s ' +\
#                               'WHERE catr_id = %s'
#                         cursor.execute(sql_update, (obj.ip, 
#                                                     obj.tempo,
#                                                     obj.operacao,
#                                                     obj.nome,
#                                                     obj.maclan,
#                                                     obj.macwlan,
#                                                     obj.interface,
#                                                     obj.id)
#                                        )
#                         self.commit()
#                         self.aviso = "[catraca] Alterado com sucesso!"
#                         return True
#             else:
#                 self.aviso = "[catraca] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[catraca] Erro realizando UPDATE/DELETE.', exc_info=True)
#             return False
#         finally:
#             pass
    
    def ordem_customizada(self, ordens):
        """
        Classificar em uma ordem especificada qualquer dicionário aninhado em uma estrutura complexa.
        Especialmente útil para classificar um arquivo JSON em uma ordem significativa.
        args :
            ordens: Uma lista de listas de chaves na ordem desejada.
        retorna:
            Um novo objeto com qualquer dict aninhada classificadas em conformidade.
        """
        ordens = [{k: -i for (i, k) in enumerate(reversed(order), 1)} for order in ordens]
        try:
            def process(stuff):
                if isinstance(stuff, dict):
                    l = [(k, process(v)) for (k, v) in stuff.iteritems()]
                    keys = set(stuff)
                    for order in ordens:
                        if keys.issubset(order) or keys.issuperset(order):
                            return OrderedDict(sorted(l, key=lambda x: order.get(x[0], 0)))
                    return OrderedDict(sorted(l))
                if isinstance(stuff, list):
                    return [process(x) for x in stuff]
                return stuff
            return process
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            