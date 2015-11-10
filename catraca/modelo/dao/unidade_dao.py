#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.unidade import Unidade


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class UnidadeDAO(ConexaoGenerica):
    
    def __init__(self):
        super(UnidadeDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self, *arg):
<<<<<<< HEAD
<<<<<<< HEAD
        obj = Unidade()
=======
        obj = Tipo()
>>>>>>> remotes/origin/web_backend
=======
        obj = Unidade()
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT unid_id, unid_nome FROM unidade WHERE unid_id = " + str(id)
        elif id is None:
<<<<<<< HEAD
<<<<<<< HEAD
            sql = "SELECT unid_id, unid_nome FROM unidade ORDER BY unid_id"
=======
            sql = "SELECT unid_id, unid_nome FROM unidade"
>>>>>>> remotes/origin/web_backend
=======
            sql = "SELECT unid_id, unid_nome FROM unidade ORDER BY unid_id"
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.nome = dados[1]
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
            self.log.logger.error('Erro ao realizar SELECT na tabela unidade.', exc_info=True)
        finally:
            pass
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO unidade(unid_id, unid_nome) VALUES (" + str(obj.id) + ",'" + str(obj.nome) + "')"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT na tabela unidade.', exc_info=True)
            return False
        finally:
            cursor.close()
            pass

    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    if obj.id:
                        sql = "DELETE FROM unidade WHERE unid_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM unidade"
                    self.aviso = "Excluido com sucesso!"
                else:
                    sql = "UPDATE unidade SET unid_nome = '" + str(obj.nome) + "' WHERE unid_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela unidade.', exc_info=True)
            return False
        finally:
            pass
<<<<<<< HEAD
        
=======

    def mantem(self, obj, delete):
        try:
            if obj is not None:
                if delete:
                    sql = "DELETE FROM unidade WHERE unid_id = " + str(obj.id)
                    msg = "Excluido com sucesso!"
                else:
                    if obj.id:
                        sql = "UPDATE unidade SET unid_nome = " + str(obj.nome) + " WHERE unid_id = " + str(obj.id)
                        msg = "Alterado com sucesso!"
                    else:
                        sql = "INSERT INTO unidade(unid_nome) VALUES (" + str(obj.nome) + ")"
                        msg = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    self.aviso = msg
                    return True
            else:
                msg = "Objeto inexistente!"
                self.aviso = msg
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT/UPDATE/DELETE na tabela unidade.', exc_info=True)
            return False
        finally:
            pass
>>>>>>> remotes/origin/web_backend
=======
        
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
