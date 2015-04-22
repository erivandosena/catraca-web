#!/usr/bin/env python
# -*- coding: latin-1 -*-

from conexao import Conexao


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class ModeloCartao:

    def __init__(self):
        print

    def selecionar(self):
        try:
            con = Conexao() 
            sql = con.cur()
            sql.execute("SELECT cart_id, cart_numero, cart_qtd_creditos, cart_vlr_credito, cart_tipo FROM cartao")
            return sql.fetchall()
        except Exception, e:
            print 'Erro ao selecionar registro(s):'
            print e

    def atualizar(self, credito, id):
        try:
            con = Conexao()
            sql = con.cur() # UPDATE cartao SET cart_numero=?, cart_qtd_creditos=?, cart_vlr_credito=?, cart_tipo=? WHERE  cart_id=
            sql.execute("UPDATE cartao SET cart_qtd_creditos=%s WHERE cart_id=%s", (credito, id))
            return sql.commit()
        except Exception, e:
            #con.rollback()
            print 'Erro ao atualizar registro(s):'
            print e

    def __del__(self):
        del self
