#!/usr/bin/env python
# -*- coding: utf-8 -*-

<<<<<<< HEAD

=======
>>>>>>> remotes/origin/web_backend
from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.unidade_turno import UnidadeTurno
<<<<<<< HEAD
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.unidade_dao import UnidadeDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
=======


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
>>>>>>> remotes/origin/web_backend
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeTurnoDAO(ConexaoGenerica):
    
    def __init__(self):
        super(UnidadeTurnoDAO, self).__init__()
        ConexaoGenerica.__init__(self)
<<<<<<< HEAD
        
    def busca(self, *arg):
        obj = UnidadeTurno()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT untu_id, turn_id, unid_id FROM unidade_turno WHERE untu_id = " + str(id)
        elif id is None:
            sql = "SELECT untu_id, turn_id, unid_id FROM unidade_turno ORDER BY untu_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.turno = self.busca_por_turno(obj)
                        obj.unidade = self.busca_por_unidade(obj)
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela unidade_turno.', exc_info=True)
        finally:
            pass
        
    def busca_por_turno(self, obj):
        return TurnoDAO().busca(obj.id)
        
    def busca_por_unidade(self, obj):
        return UnidadeDAO().busca(obj.id)
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO unidade_turno("\
                    "untu_id, "\
                    "turn_id, "\
                    "unid_id) VALUES (" +\
                    str(obj.id) + ", " +\
                    str(obj.turno) + ", " +\
                    str(obj.unidade) + ")"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return False
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT na tabela unidade_turno.', exc_info=True)
            return False
        finally:
            pass   
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    if obj.id:
                        sql = "DELETE FROM unidade_turno WHERE untu_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM unidade_turno"
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE unidade_turno SET " +\
                        "turn_id = " + str(obj.turno) + ", " +\
                        "unid_id = " + str(obj.unidade) +\
                        " WHERE "\
                        "untu_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return False
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela unidade_turno.', exc_info=True)
            return False
        finally:
            pass
        
=======

    def busca(self, *arg):
        pass
        
    def mantem(self, obj, delete):
        pass
    
>>>>>>> remotes/origin/web_backend
