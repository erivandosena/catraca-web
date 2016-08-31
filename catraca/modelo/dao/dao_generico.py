#!/usr/bin/env python
# -*- coding: latin-1 -*-


import inspect
from typing import TypeVar
from typing import Generic
#from contextlib import closing
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
        self.cursor = None
        
    def seleciona(self, T, sql, *arg):
        obj = T()
        self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        try:
            #with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:
            dic = {}
            argumentos = []
            for a in arg:
                argumentos.append(a)
            if len(arg) == 1:
                #print argumentos
                self.cursor.execute(sql, argumentos)
                linhas = self.cursor.fetchone()
                #print self.cursor.query
                if linhas:
                    colunas = [coluna[0] for coluna in self.cursor.description]
                    dic = dict(zip(colunas, linhas))
                    for coluna in sorted(dic):
                        setattr(obj, coluna, dic[coluna])
                    msg = self.cursor.statusmessage
                    if msg:
                        status = msg[len(msg)-1:len(msg)]
                        if status:
                            self.aviso = "Selecionado {0} com sucesso!".format(status)
                            return obj
                        else:
                            return None
                else:
                    return None
            else:
                #print argumentos
                self.cursor.execute(sql, argumentos)
                linhas = self.cursor.fetchall()
                print self.cursor.query
                if linhas != []:
                    listas = []
                    for linha in linhas:
                        colunas = [coluna[0] for coluna in self.cursor.description]
                        dic.update(zip(colunas, linha))
                        lista = []
                        for linha in sorted(dic):
                            lista.append(dic[linha])
                        listas.append(lista)
                    msg = self.cursor.statusmessage
                    if msg:
                        status = msg[len(msg)-1:len(msg)]
                        if status:
                            self.aviso = "Selecionado {0} com sucesso!".format(status)
                            return listas
                        else:
                            return []
                else:
                    return []
        except (self.data_error, self.programming_error, self.operational_error):
            self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
        finally:
            self.__fecha_conexoes(self.cursor)
            
    def inclui(self, T, sql, *arg):
        arg = [a for a in arg][0]
        obj = None
        lista = []
        classe = None
        if isinstance(arg, list):
            lista = arg
            print lista
        if isinstance(arg, T):
            obj = arg
            print obj
        atributos = []
        colunas = []
        valores = []
        lista_ordenada = []
        self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        try:
            if lista:
                atributos = inspect.getmembers(T(), lambda m:not(inspect.isroutine(m)))
                colunas = [m[0] for m in atributos if '_' not in m[0] and 'id' not in m[0]]
                valores = lista
                print colunas
                print valores
                dic = dict(zip(colunas[0::1], valores[0::1]))
                print dic
                for linha in sorted(dic):
                    lista_ordenada.append(dic[linha])
                #print lista_ordenada
            if obj:
                atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                colunas = [m[0] for m in atributos if '_' not in m[0]]
                valores = [m[1] for m in atributos if '_' not in m[0]]
                print colunas
                print valores
                dic = dict(zip(colunas[0::1], valores[0::1]))
                print dic
                for linha in sorted(dic):
                    lista_ordenada.append(dic[linha])
                #print lista_ordenada
            self.cursor.execute(sql, lista_ordenada)
            print self.cursor.query
            self.commit()
            if lista != [] or obj:
                msg = self.cursor.statusmessage
                if msg:
                    status = msg[len(msg)-1:len(msg)]
                    if status:
                        self.aviso = "Inserido {0} com sucesso!".format(status)
                        return True
                    else:
                        return False
            else:
                return False
        except (self.data_error, self.programming_error, self.operational_error):
            print "fez rollback (insert)"
            self.rollback()
            self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
        finally:
            self.__fecha_conexoes(self.cursor)
            
    def altera(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        try:
            if obj:
                #with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:
                atributos = inspect.getmembers(obj, lambda m:not(inspect.isroutine(m)))
                colunas = [m[0] for m in atributos if '_' not in m[0]]
                valores = [m[1] for m in atributos if '_' not in m[0]]
                dic = dict(zip(colunas[0::1], valores[0::1]))
                dic.pop('id')
                lista_ordenada = []
                for linha in sorted(dic):
                    lista_ordenada.append(dic[linha])
                lista_ordenada.append(obj.id)
                self.cursor.execute(sql, lista_ordenada)
                print self.cursor.query
                self.commit()
                msg = self.cursor.statusmessage
                if msg:
                    status = msg[len(msg)-1:len(msg)]
                    if status:
                        self.aviso = "Alterado {0} com sucesso!".format(status)
                        return True
                    else:
                        return False
            else:
                return False
        except (self.data_error, self.programming_error, self.operational_error):
            print "fez rollback (edit)"
            self.rollback()
            self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
        finally:
            self.__fecha_conexoes(self.cursor)
            
    def deleta(self, sql, *arg):
        obj = [a for a in arg][0] if arg else None
        self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        try:
            #with closing(self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)) as cursor:
            if obj:
                self.cursor.execute(sql, (obj.id,))
            else:
                self.cursor.execute(sql)
            print self.cursor.query
            self.commit()
            msg = self.cursor.statusmessage
            if msg:
                status = msg[len(msg)-1:len(msg)]
                if status:
                    self.aviso = "Deletado {0} com sucesso!".format(status)
                    return True
                else:
                    return False
        except (self.data_error, self.programming_error, self.operational_error):
            print "fez rollback (delete)"
            self.rollback()
            self.cursor = self.abre_conexao().cursor(cursor_factory=self.extras.DictCursor)
        except Exception as excecao:
            self.log.logger.error("ERRO: ", exc_info=True)
        finally:
            self.__fecha_conexoes(self.cursor)
            
    def __fecha_conexoes(self, cursor):
        if not self.cursor.closed:
            self.cursor.close()
            #print "CURSOR FECHADO!"
            self.fecha_conexao()
        