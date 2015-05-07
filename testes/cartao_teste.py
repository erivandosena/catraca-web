#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from datetime import datetime
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR')


def main():
    print 'Iniciando os testes tabela cartao...'
    
    # teste (insert)
    cartao = Cartao()
    # teste (update)
    cartao_dao = CartaoDAO()
    # teste (select)
    ##cartao = cartao_dao.busca(42)
    cartao.setNumero(3995148318)
    cartao.setCreditos(10)
    cartao.setValor(4.00)
    cartao.setTipo(5) # 1=Estudante, 2=Docente, 3=Tecnico, 4=Terceirizado, 5=Visitante, 6=Administrador.
    cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))

    if cartao.getId():
        if cartao_dao.altera(cartao):
            print "Alterado com sucesso!"
        else:
            print "Erro ao alterar:"
            print cartao_dao.getErro()
    else:
        if cartao_dao.insere(cartao):
            print "Inserido com sucesso!"
        else:
            print "Erro ao inserir:"
            print cartao_dao.getErro()
    
    """
    # teste excluir
    cartao_dao = CartaoDAO()
    cartao = cartao_dao.busca(41)
    print cartao.getId()
    print cartao.getIp()
    if cartao_dao.exclui(cartao):
        print "Excluido com sucesso!"
    else:
        print aspberry_dao.getErro()
    """
