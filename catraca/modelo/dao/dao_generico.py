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
            with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:
                dic = {}
                argumentos = []
                for a in arg:
                    argumentos.append(a)
                print argumentos
                cursor.execute(sql, argumentos)
                if arg:
                    linhas = cursor.fetchone()
#                     print cursor.query
#                     colunas = [coluna[0] for coluna in cursor.description]
#                     print colunas, linhas
#                     dic = dict(zip(colunas, linhas))
#                     print dic
                    if linhas:
                        print cursor.query
                        colunas = [coluna[0] for coluna in cursor.description]
                        print colunas, linhas
                        dic = dict(zip(colunas, linhas))
                        print dic
                    
                        for coluna in sorted(dic):
                            setattr(obj, coluna, dic[coluna])
                        msg = cursor.statusmessage
                        status = msg[len(msg)-1:len(msg)]
                        if status:
                            self.aviso = "Selecionado {0} com sucesso!".format(status)
                            return obj
                        else:
                            return None
                    else:
                        return None
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
                        msg = cursor.statusmessage
                        status = msg[len(msg)-1:len(msg)]
                        if status:
                            self.aviso = "Selecionado {0} com sucesso!".format(status)
                            return listas
                        else:
                            return []
        except (self.DataError, self.ProgrammingError):
            self.rollback()
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def inclui(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            if obj:
                with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:

                    atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                    colunas = [m[0] for m in atributos if '_' not in m[0]]
                    valores = [m[1] for m in atributos if '_' not in m[0]]
                    dic = dict(zip(colunas[0::1], valores[0::1]))
                    lista_ordenada = []
                    for linha in sorted(dic):
                        print dic[linha]
                        lista_ordenada.append(dic[linha])
                    print "============================="
                    print sorted(dic)
                    print lista_ordenada
                    print sql
                    print "============================="
                    cursor.execute(sql, lista_ordenada)
                    print cursor.query
                    self.commit()
                    msg = cursor.statusmessage
                    status = msg[len(msg)-1:len(msg)]
                    if status:
                        self.aviso = "Inserido {0} com sucesso!".format(status)
                        return True
                    else:
                        return False
            else:
                return False
        except (self.DataError, self.ProgrammingError):
            self.rollback()
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def altera(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            if obj:
                with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:

                    atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                    colunas = [m[0] for m in atributos if '_' not in m[0]]
                    valores = [m[1] for m in atributos if '_' not in m[0]]
                    dic = dict(zip(colunas[0::1], valores[0::1]))
                    dic.pop('id')
                    lista_ordenada = []
                    for linha in sorted(dic):
                        lista_ordenada.append(dic[linha])
                    lista_ordenada.append(obj.id)
                    cursor.execute(sql, lista_ordenada)
                    print cursor.query
                    if obj.__class__.__name__ != "Cartao":
                        self.commit()
                        msg = cursor.statusmessage
                        status = msg[len(msg)-1:len(msg)]
                        if status:
                            self.aviso = "Alterado {0} com sucesso!".format(status)
                            return True
                        else:
                            return False
                    else:
                        self.aviso = "Favor realizar commit de {0} manualmente!".format(obj.__class__.__name__)
                        print self.aviso
            else:
                return False
        except (self.DataError, self.ProgrammingError):
            self.rollback()
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            
    def deleta(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        try:
            with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:
                if obj:
                    cursor.execute(sql, (obj.id,))
                    #print cursor.query
                else:
                    cursor.execute(sql)
                    #print cursor.query
                self.commit()
                msg = cursor.statusmessage
                status = msg[len(msg)-1:len(msg)]
                if status:
                    self.aviso = "Deletado {0} com sucesso!".format(status)
                    return True
                else:
                    return False
        except (self.DataError, self.ProgrammingError):
            self.rollback()
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
            