#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pprint
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production

class TesteCartao(object):

    #def __init__(self, id, numero, creditos, valor, tipo):
    def __init__(self):
        super(TesteCartao, self).__init__()
        #self.id = id
        #self.numero = numero
        #self.creditos = creditos
        #self.valor = valor
        #self.tipo = tipo

    def pesquisar(self):
 
        cartao = Cartao()
        pesquisar = CartaoDAO()
 
        try:
            cartao = pesquisar.busca_cartao(self.id)
        except ValueError:
            print pesquisar.getErro()
 
        # Exibe dados
        pprint.pprint(0, str(cartao.getId()))
        pprint.pprint(0, cartao.getNumero())
        pprint.pprint(0, cartao.getCreditos())
        pprint.pprint(0, str(cartao.getValor()))
        pprint.pprint(0, cartao.getTipo())
 
    def inserir(self):
 
        cartao = Cartao()

        #cartao.setId(self.id)
        cartao.setNumero(self.numero)
        cartao.setCreditos(self.creditos)
        cartao.setValor(self.valor)
        cartao.setTipo(self.tipo)
 
        inserir = CartaoDAO()
 
        # realiza a trasferencia de objetos
        resultado = inserir.insere_cartao(cartao)
 
        if (resultado):
            print "Dados inseridos com suscesso!"
        else:
            print "Erro:"
			print inserir.getErro()
 
    def alterar(self):

        cartao = Cartao()
 
        cartao.setId(self.id)
        cartao.setNumero(self.numero)
        cartao.setCreditos(self.creditos)
        cartao.setValor(self.valor)
        cartao.setTipo(self.tipo)
 
        alterar = CartaoDAO()

        resultado = alterar.altera_cartao(cartao)

        if (resultado):
            print "Dados alterados com suscesso!"
        else:
            print "Erro:"
			print alterar.getErro()
 
    def excluir(self):
 
        cartao = Cartao()

        cartao.setId(self.id)
        cartao.setNumero(self.numero)
        cartao.setCreditos(self.creditos)
        cartao.setValor(self.valor)
        cartao.setTipo(self.tipo)
 
        apagar = CartaoDAO()

        resultado = apagar.exclui_cartao(cartao)
 
        if (resultado):
            print "Dados excluidos com suscesso!"
        else:
            print "Erro:"
			print apagar.getErro()
	
def main():
    print 'Iniciando os testes...'
	#teste_cartao = TesteCartao(1, 1111111111, 19, 1.50, 2)
    teste_cartao = TesteCartao()
    teste_cartao.pesquisar(5)
    #teste_cartao.inserir(1111111111, 19, 1.50, 2)
    #teste_cartao.alterar(3, 6666666666, 19, 1.50, 3)
    #teste_cartao.excluir(4)
	
	