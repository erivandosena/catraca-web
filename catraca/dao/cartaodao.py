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
            # Cria Conexão com o Factory Method Pattern
            # Pode ter uma classe para cada fonte de dados
            # Uni as três fontes aqui
            conexao = ConexaoFactory()
            self.__con = conexao.getConexao(3)
            self.__factory = conexao.getFactory()
        except Exception, e:
            self.__erro = str(e)
 
    # Metodo de Manipulação de dados
 
    def busca_cartao(self, id):
 
        # Cria instancia do objeto
        cartao = Cartao()
 
        # Define SQL
        sql = "SELECT cart_id, cart_numero, cart_qtd_creditos, cart_vlr_credito, cart_tipo FROM cartao WHERE cart_id = " + str(id)
 
        # Executa SQL
        try:
            cursor= self.__con.cursor()
            cursor.execute(sql)
            dados = cursor.fetchone()
        except Exception, e:
            self.__erro = str(e)
 
        # Alimenta objeto
        cartao.setId(dados[0])
        cartao.setNumero(dados[1])
        cartao.setCreditos(dados[2])
        cartao.setValor(dados[3])
        cartao.setTipo(dados[4])
 
        # Retorna Objeto
        return cartao
 
    def insere_cartao(self, cartao):

        sql = "INSERT INTO cartao VALUES (" + \
              cartao.getId() + ", '" + \
              cartao.getNumero() + "', '" + \
              cartao.getCreditos() + "', '" + \
			  str(cartao.getValor()).replace(",",".") + \
              cartao.getTipo() + ")"
        try:
             cursor=self.__con.cursor()
             cursor.execute(sql)
             self.__con.commit()
             return True
        except Exception, e:
            self.__erro = str(e)
            return False
 
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

