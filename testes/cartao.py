#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pprint
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def pesquisar(id):
    cartao = Cartao()
    pesquisar = CartaoDAO()
 
    try:
        cartao = pesquisar.busca_cartao(id)
    except ValueError:
        print pesquisar.getErro()
    # Exibe dados
    pprint.pprint(cartao.getId())
    pprint.pprint(cartao.getNumero())
    pprint.pprint(cartao.getCreditos())
    pprint.pprint(cartao.getValor())
    pprint.pprint(cartao.getTipo())
    print '-------------------------'
 
def inserir(numero,creditos,valor,tipo):
    cartao = Cartao()
    #cartao.setId(id)
    cartao.setNumero(numero)
    cartao.setCreditos(creditos)
    cartao.setValor(valor)
    cartao.setTipo(tipo)

    inserir = CartaoDAO()
    resultado = inserir.insere_cartao(cartao)

    if (resultado):
        print "Dados inseridos com suscesso!"
    else:
        print "Erro:"
        print inserir.getErro()
 
def alterar(id,numero,creditos,valor,tipo):
    cartao = Cartao()
    cartao.setId(id)
    cartao.setNumero(numero)
    cartao.setCreditos(creditos)
    cartao.setValor(valor)
    cartao.setTipo(tipo)

    alterar = CartaoDAO()
    resultado = alterar.altera_cartao(cartao)

    if (resultado):
        print "Dados alterados com suscesso!"
    else:
        print "Erro:"
	print alterar.getErro()
 
def excluir(id):
    cartao = Cartao()
    cartao.setId(id)
    #cartao.setNumero(numero)
    #cartao.setCreditos(creditos)
    #cartao.setValor(valor)
    #cartao.setTipo(tipo)

    apagar = CartaoDAO()
    resultado = apagar.exclui_cartao(cartao)

    if (resultado):
        print "Dados excluidos com suscesso!"
    else:
        print "Erro:"
	print apagar.getErro()
	
def main():
    print 'Iniciando os testes...'
    pesquisar(1)

    inserir(9999999999, 8, 6.90, 3)

    pesquisar(8)
    #teste_cartao.pesquisar()
    #teste_cartao.alterar(3, 6666666666, 19, 1.50, 3)
    #teste_cartao.excluir(4)
    
