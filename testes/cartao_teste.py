#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.perfil import Perfil
from catraca.dao.perfildao import PerfilDAO
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela cartao...'
    
    perfil = Perfil()
    perfil_dao = PerfilDAO()
    
    cartao = Cartao()
    cartao_dao = CartaoDAO()

    cartao.numero = 3995148318
    cartao.creditos = 10
    cartao.perfil = perfil_dao.busca_perfil(2).id

    if cartao.id:
        if cartao_dao.altera(cartao):
            print "Alterado com sucesso!"
        else:
            print cartao_dao.erro
    else:
        if cartao_dao.insere(cartao):
            print "Inserido com sucesso!"
        else:
            print cartao_dao.erro
    

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
 
 #   cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))


