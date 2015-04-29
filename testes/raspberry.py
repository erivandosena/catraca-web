#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pprint
from catraca.dao.cartao import Cartao
from catraca.dao.raspberry import Raspberry
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.raspberrydao import RaspberryDAO
from datetime import datetime
import locale
import time

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR')


def main():
    print 'Iniciando os testes raspberry...'
    """
    # teste (insert)
    raspberry = Raspberry()
    # teste (update)
    raspberry_dao = RaspberryDAO()
    # teste (select)
    ##raspberry = raspberry_dao.busca(42)
    raspberry.setIp("10.5.2.253")
    raspberry.setLocal("RU Liberdade")
    raspberry.setTempo(10)
    raspberry.setMensagem("SEJA BEM-VINDO!")
    raspberry.setSentido(2)

    if raspberry.getId():
        if raspberry_dao.altera(raspberry):
            print "Alterado com sucesso!"
            raspberry = raspberry_dao.busca(raspberry.getIp())
        else:
            print "Erro ao alterar:"
            print raspberry_dao.getErro()
    else:
        if raspberry_dao.insere(raspberry):
            print "Inserido com sucesso!"
            raspberry = raspberry_dao.busca(raspberry.getIp())
        else:
            print "Erro ao inserir:"
            print raspberry_dao.getErro()
    """
    """
    # teste excluir
    raspberry_dao = RaspberryDAO()
    raspberry = raspberry_dao.busca(41)
    print raspberry.getId()
    print raspberry.getIp()
    if raspberry_dao.exclui(raspberry):
        print "Excluido com sucesso!"
    else:
        print aspberry_dao.getErro()
    """
