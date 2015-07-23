#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.catraca import Catraca
from catraca.dao.catracadao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela catraca...'
    
    # teste (insert)
    catraca = Catraca()
    # teste (update)
    catraca_dao = CatracaDAO()
    # teste (select)
    ##catraca = catraca_dao.busca(42)
    catraca.setIp("10.5.2.253")
    catraca.setLocal("RU Liberdade")
    catraca.setTempo(5)
    catraca.setMensagem("SEJA BEM-VINDO!")
    catraca.setSentido(1)

    if catraca.getId():
        if catraca_dao.altera(catraca):
            print "Alterado com sucesso!"
        else:
            print "Erro ao alterar:"
            print catraca_dao.getErro()
    else:
        if catraca_dao.insere(catraca):
            print "Inserido com sucesso!"
        else:
            print "Erro ao inserir:"
            print catraca_dao.getErro()
    
    """
    # teste excluir
    catraca_dao = CatracaDAO()
    catraca = catraca_dao.busca(41)
    print catraca.getId()
    print catraca.getIp()
    if catraca_dao.exclui(catraca):
        print "Excluido com sucesso!"
    else:
        print aspberry_dao.getErro()
    """
