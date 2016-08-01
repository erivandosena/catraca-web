#!/usr/bin/env python
# -*- coding: latin-1 -*-


import simplejson as json
from typing import TypeVar
from typing import Generic
from collections import OrderedDict
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
                    print colunas
                    valores = dict((name, getattr(obj, name)) for name in obj.__dict__)
                    lista_ordenada = self.ordem_customizada(sorted(colunas))
                    lista_valores = lista_ordenada(valores)
                    cursor.execute(sql, lista_valores.values())
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
        print obj.id
        try:
            if obj:
                with closing(self.abre_conexao().cursor()) as cursor:
                    colunas = dict((name, getattr(obj, name)) for name in obj.__dict__).keys()
                    valores = dict((name, getattr(obj, name)) for name in obj.__dict__)
                    lista_ordenada = self.ordem_customizada(sorted(colunas))
                    lista_valores = lista_ordenada(valores)
                    lista_valores = lista_valores.values()[1:len(lista_valores.values())]
                    lista_valores.append(obj.id)
                    cursor.execute(sql, lista_valores)
                    print cursor.query
                    if obj.__class__.__name__ != "Cartao":
                        print obj.__class__.__name__
                        #self.commit()
                    else:
                        print "Favor realizar commit do " + str(obj.__class__.__name__)
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
            
            