#!/usr/bin/env python
# -*- coding: latin-1 -*-

import json
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
                    if dados:
                        for (campo, valor) in zip((nom[0] for nom in cursor.description), [val for val in dados]):
                            setattr(obj, campo, valor)
#                         print "\n======================="
#                         print obj.id
#                         print obj.ip
#                         print obj.tempo
#                         print obj.operacao
#                         print obj.nome
#                         print obj.maclan
#                         print obj.macwlan
#                         print obj.interface
#                         print "======================="
                        return obj
                else:
                    lista = cursor.fetchall()
                    if lista != []:
                        return lista
        except Exception as excecao:
            self.log.logger.error(T.__name__, exc_info=True)
            
    def inclui(self, T , sql, *arg):
        obj = T()
        obj = [o for o in arg if o]
        print obj
        print obj[0]
        
        if obj:
            print obj.id
            print obj.ip
            print obj.tempo
            print obj.operacao
            print obj.nome
            print obj.maclan
            print obj.macwlan
            print obj.interface
        
        
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql, arg)
                print cursor.query
#                 if [argumento for argumento in arg if argumento]:
#                     dados = cursor.fetchone()
#                     if dados:
#                         for (campo, valor) in zip((nom[0] for nom in cursor.description), [val for val in dados]):
#                             setattr(obj, campo, valor)
# #                         print "\n======================="
# #                         print obj.id
# #                         print obj.ip
# #                         print obj.tempo
# #                         print obj.operacao
# #                         print obj.nome
# #                         print obj.maclan
# #                         print obj.macwlan
# #                         print obj.interface
# #                         print "======================="
#                         return obj
#                 else:
#                     lista = cursor.fetchall()
#                     if lista != []:
#                         return lista
        except Exception as excecao:
            self.log.logger.error(T.__name__, exc_info=True)
        
        
#     def insere(self, obj):
#         try:
#             if obj:
#                 with closing(self.abre_conexao().cursor()) as cursor:
#                     sql_insert = 'INSERT INTO catraca(' +\
#                        'catr_id, ' +\
#                        'catr_ip, ' +\
#                        'catr_tempo_giro, ' +\
#                        'catr_operacao, ' +\
#                        'catr_nome, ' +\
#                        'catr_mac_lan, ' +\
#                        'catr_mac_wlan, ' +\
#                        'catr_interface_rede) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
#                     cursor.execute(sql_insert, (obj.id, 
#                                                 obj.ip,
#                                                 obj.tempo,
#                                                 obj.operacao,
#                                                 obj.nome,
#                                                 obj.maclan,
#                                                 obj.macwlan,
#                                                 obj.interface)
#                                    )
#                     self.commit()
#                     self.aviso = "[catraca] Inserido com sucesso!"
#                     return True
#             else:
#                 self.aviso = "[catraca] inexistente!"
#                 return False
#         except Exception as excecao:
#             self.aviso = str(excecao)
#             self.log.logger.error('[catraca] Erro realizando INSERT.', exc_info=True)
#             return False
#         finally:
#             pass   
        
#         obj = T()
#         obj = [argumento for argumento in arg if argumento][0]
#         dic1 = [i for i in T.__dict__ if i[:1] != '_' and i[:1] != 'hash_dict']
#         dic2 = [name for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict')]
#         #dic3 = [(name, getattr(obj, name)) for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict')]
#         dic3 = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict'))
        #print dic1
        #print dic2
#         print dic3.keys()
#         print dic3.values()
#         print ', '.join([i for i in dic3 if i[:1]])
        
        #print getattr(obj, 'nome')
#         nomes = ""
#         for nome in colunas:
#             nomes += str(getattr(obj, nome)(nome)+", ")
#         print nomes
        #''.join([str(hex(x)[2:4]).zfill(2) for x in backData[:-1][::-1]])
        #print [name for name in dir(obj) if not name.startswith('_')][1][2][3][4][5][6]
        #print dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict'))
#         i=0
#         for coluna in dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('_') and not name.startswith('hash_dict')).items():
#             print coluna
#             i+=1
        with closing(self.abre_conexao().cursor()) as cursor:
            pass
        
        
        
        return False
#         try:
#             with closing(self.abre_conexao().cursor()) as cursor:
#                 cursor.execute(sql, arg)
#                 if [argumento for argumento in arg if argumento]:
#                     dados = cursor.fetchone()
#                     if dados:
#                         i=0
#                         for nome in colunas:
#                             setattr(obj, nome, dados[i])
#                             i+=1
#                         return obj
#                 else:
#                     lista = cursor.fetchall()
#                     if lista != []:
#                         return lista
#         except Exception as excecao:
#             self.log.logger.error(T.__name__, exc_info=True)
    
    def atualiza_exclui(self, obj, delete):
        pass