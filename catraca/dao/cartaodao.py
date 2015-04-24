#!/usr/bin/env python
# -*- coding: latin-1 -*-

from cartao import Cartao
from conexao import ConexaoFactory


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CartaoDAO(object):

    def __init__(self):
        super(CartaoDAO, self).__init__()
        self.__erro = None
        self.__con = None
        self.__factory = None

        try:
            # Em .getConexao(?) use: 1 p/(PostgreSQL) 2 p/(MySQL) 3 p/(SQLite)
            conexao = ConexaoFactory()
            self.__con = conexao.getConexao(1)
            self.__factory = conexao.getFactory()
        except Exception, e:
            self.__erro = str(e)
 
    # Select
    def busca_cartao(self, id):
        cartao = Cartao()
        sql = "SELECT cart_id, cart_numero, cart_qtd_creditos, cart_vlr_credito, cart_tipo FROM cartao WHERE cart_id = " + str(id)
        try:
            cursor = self.__con.cursor()
            cursor.execute(sql)
            dados = cursor.fetchone()
            # Carrega objeto
            cartao.setId(dados[0])
            cartao.setNumero(dados[1])
            cartao.setCreditos(dados[2])
            cartao.setValor(dados[3])
            cartao.setTipo(dados[4])        
        except Exception, e:
            self.__erro = str(e)
        return cartao
 
    # Insert
    def insere_cartao(self, cartao):
        sql = "INSERT INTO cartao(cart_numero, cart_qtd_creditos, cart_vlr_credito, cart_tipo) VALUES (" + \
              str(cartao.getNumero()) + ", " + \
              str(cartao.getCreditos()) + ", " + \
              str(cartao.getValor()) + ", " + \
              str(cartao.getTipo()) + ")"
        #sql = "INSERT INTO cartao VALUES ("+\
              #str(cartao.getNumero())+","+\
              #str(cartao.getCreditos())+","+\
              #str(cartao.getValor())+","+\
              #str(cartao.getTipo())+")"
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False
    # Update
    def altera_cartao(self, cartao):
       sql = "UPDATE cartao SET " + \
             "cart_id = " + cartao.getId() + ", " + \
             "cart_numero = '" + cartao.getNumero() + "', " + \
             "cart_qtd_creditos = '" + cartao.getCreditos() + "', " + \
             "cart_vlr_credito = " + str(cartao.getValor()).replace(",",".") + \
	     "cart_tipo = '" + cartao.getTipo() + "', " + \
             " WHERE cart_id = " + cartao.getId()
       try:
           cursor=self.__con.cursor()
           cursor.execute(sql)
           self.__con.commit()
           return True
       except Exception, e:
           self.__erro = str(e)
           return False
    
    # Delete
    def exclui_cartao(self, cartao):
        sql = "DELETE FROM cartao WHERE cart_id = " + cartao.getId()
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False

    def getErro(self):
        return self.__erro
