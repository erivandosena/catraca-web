#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from typing import TypeVar
from typing import Generic
from typing import Sequence
from catraca.logs import Logs
from catraca.modelo.dados.conexao import ConexaoFactory
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
        
        
    def buscar(self, T , sql, colunas, *arg):
        obj = T()
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                for i in arg:
                    id = i
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        i=0
                        for campos in colunas:
                            setattr(obj, campos, dados[i])
                            i+=1
                            
                        print obj.id
                        print obj.ip
                        print obj.tempo
                        print obj.operacao
                        print obj.nome
                        print obj.maclan
                        print obj.macwlan
                        print obj.interface

#                         obj.id = dados[0]
#                         obj.ip = dados[1]
#                         obj.tempo = dados[2]
#                         obj.operacao = dados[3]
#                         obj.nome = dados[4]
#                         obj.maclan = dados[5]
#                         obj.macwlan = dados[6]
#                         obj.interface = dados[7]

                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        print list
                        return list
                    else:
                        return None
        except Exception as excecao:
            self.aviso = "["+str(T.__name__)+"]Erro ao realizar SELECT."
            self.log.logger.error(self.aviso, exc_info=True)
        finally:
            pass
        

    def insere(self, obj):
        pass
    
    def atualiza_exclui(self, obj, delete):
        pass