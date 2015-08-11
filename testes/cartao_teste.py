#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.usuario import Usuario
from catraca.dao.usuariodao import UsuarioDAO
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela cartao...'
    
    usuario = Usuario()
    usuario_dao = UsuarioDAO()
    
    cartao = Cartao()
    cartao_dao = CartaoDAO()

    cartao.numero = 3995295262
    cartao.creditos = 10
    cartao.valor = 1.10
    cartao.data = datetime.datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")
    cartao.usuario = usuario_dao.busca("'12345678912'").id
    

    if cartao.id:
        if cartao_dao.altera(usuario):
            print "Alterado com sucesso!"
        else:
            print "Erro ao alterar:"
            print cartao_dao.erro
    else:
        if cartao_dao.insere(usuario):
            print "Inserido com sucesso!"
        else:
            print "Erro ao inserir:"
            print cartao_dao.erro
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # teste (insert)
    cartao = Cartao()
    # teste (update)
    cartao_dao = CartaoDAO()
    # teste (select)
    ##cartao = cartao_dao.busca(42)
    cartao.setNumero(3995295262)
    cartao.setCreditos(0)
    cartao.setValor(0.00)
    cartao.setTipo(6) # 1=Estudante(1,10), 2=Tecnico(1,60), 3=Professor(2,20), 4=Visitante(4,00) 5=Operador, 6=Administrador.
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
