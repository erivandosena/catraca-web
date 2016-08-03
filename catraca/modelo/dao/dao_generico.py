#!/usr/bin/env python
# -*- coding: latin-1 -*-


import inspect
from typing import TypeVar
from typing import Generic
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
        
    def seleciona(self, T, sql, *arg):
        obj = T()
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                dic = {}
                argumentos = []
                for a in arg:
                    argumentos.append(str(a))
                print argumentos
                cursor.execute(sql, argumentos)
                if arg:
                    linhas = cursor.fetchone()
                    print cursor.query
                    colunas = [coluna[0] for coluna in cursor.description]
                    dic = dict(zip(colunas, linhas))
                    if linhas:
                        for coluna in sorted(dic):
                            setattr(obj, coluna, dic[coluna])
                        return obj
                else:
                    linhas = cursor.fetchall()
                    #print cursor.query
                    if linhas != []:
                        listas = []
                        for linha in linhas:
                            colunas = [coluna[0] for coluna in cursor.description]
                            dic.update(zip(colunas, linha))
                            lista = []
                            for linha in sorted(dic):
                                lista.append(dic[linha])
                            listas.append(lista)
                        return listas
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def inclui(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            if obj:
                with closing(self.abre_conexao().cursor()) as cursor:

                    atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                    colunas = [m[0] for m in atributos if '_' not in m[0]]
                    valores = [m[1] for m in atributos if '_' not in m[0]]
                    dic = dict(zip(colunas[0::1], valores[0::1]))
                    lista_ordenada = []
                    for linha in sorted(dic):
                        lista_ordenada.append(dic[linha])
                    
                    print lista_ordenada
                    
                    cursor.execute(sql, lista_ordenada)
                    print cursor.query
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

                    atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                    colunas = [m[0] for m in atributos if '_' not in m[0]]
                    valores = [m[1] for m in atributos if '_' not in m[0]]
                    dic = dict(zip(colunas[0::1], valores[0::1]))
                    dic.pop('id')
                    lista_ordenada = []
                    for linha in sorted(dic):
                        lista_ordenada.append(dic[linha])
                    lista_ordenada.append(obj.id)
                    
                    print lista_ordenada

                    cursor.execute(sql, lista_ordenada)
                    print cursor.query
                    if obj.__class__.__name__ != "Cartao":
                        print obj.__class__.__name__
                        #self.commit()
                    else:
                        print "Favor realizar commit de " + str(obj.__class__.__name__)
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
                self.commit()
                self.aviso = "Deletado com sucesso!"
                return True
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            