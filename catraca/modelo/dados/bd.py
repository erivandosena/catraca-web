#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Bd(ConexaoGenerica):

    def __init__(self):
        super(Bd, self).__init__()
        ConexaoGenerica.__init__(self)
        
    def verifica_bd(self):
        sql = "select count(*) as bd from pg_catalog.pg_database where datname = 'bd_teste';"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        print dados[0]
                        return obj
                    else:
                        return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT no pg_catalog', exc_info=True)
        finally:
            pass