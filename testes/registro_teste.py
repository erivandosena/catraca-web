#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.registro import Registro
from catraca.dao.registrodao import RegistroDAO
from catraca.dao.cartaodao import CartaoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    print 'Iniciando os testes tabela registro...'
    
    registro = Registro()
    registro_dao = RegistroDAO()
    cartao_dao = CartaoDAO()

    registro.data = datetime.datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")
    registro.giro = 1
    registro.cartao = cartao_dao.busca_cartao(6)
    registro.valor = registro.cartao.perfil.tipo.valor

#     print registro.cartao.perfil.tipo.nome
#     print registro.cartao.perfil.nome
#     print registro.cartao.numero
#     print locale.currency(registro.valor).format()
    
    if registro.id:
        if registro_dao.altera(registro):
            print "Alterado com sucesso!"
        else:
            print registro_dao.erro
    else:
        if registro_dao.insere(registro):
            print "Inserido com sucesso!"
        else:
            print registro_dao.erro
            