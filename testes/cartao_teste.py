#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.perfildao import PerfilDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela cartao...'

    cartao = Cartao()
    cartao_dao = CartaoDAO()
    perfil_dao = PerfilDAO()

    cartao.numero = 3995148316
    cartao.creditos = 10
    cartao.perfil = perfil_dao.busca_perfil(5)

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
            


