#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pprint
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from datetime import datetime


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
    pprint.pprint(cartao.getData())
    print '-------------------------'
 
def inserir(numero,creditos,valor,tipo,data):
    cartao = Cartao()
    cartao.setNumero(numero)
    cartao.setCreditos(creditos)
    cartao.setValor(valor)
    cartao.setTipo(tipo)
    cartao.setData(data)

    inserir = CartaoDAO()
    resultado = inserir.insere_cartao(cartao)

    if (resultado):
        print "Dados inseridos com suscesso!"
    else:
        print "Erro:"
        print inserir.getErro()
 
def alterar(id,numero,creditos,valor,tipo,data):
    cartao = Cartao()
    cartao.setId(id)
    cartao.setNumero(numero)
    cartao.setCreditos(creditos)
    cartao.setValor(valor)
    cartao.setTipo(tipo)
    cartao.setData(data)

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

    apagar = CartaoDAO()
    resultado = apagar.exclui_cartao(cartao)

    if (resultado):
        print "Dados excluidos com suscesso!"
    else:
        print "Erro:"
	print apagar.getErro()
	
def main():
    print 'Iniciando os testes cartao...'
    """
    cartao_dao = CartaoDAO()
    cartao = cartao_dao.busca_cartao(1212121212)
    cartao_dao.busca_cartao(cartao.getNumero())
    #cartao.setNumero(1212121212)
    #cartao.setCreditos(44)
    #cartao.setValor(4.00)
    #cartao.setTipo(2)
    cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))
    print cartao_dao.altera_cartao(cartao)
    c =  cartao_dao.busca_cartao(cartao.getNumero())
    print c.getId()
    print c.getNumero()
    print c.getCreditos()
    import locale
    print locale.setlocale(locale.LC_ALL, 'pt_BR')
    print locale.currency(c.getValor()).format()
    print "R$ " + str(c.getValor()).replace(".",",")
    print c.getData().strftime("%d/%m/%Y %H:%M:%S")
    """
