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
    registro.cartao = cartao_dao.busca(4)
    registro.valor = registro.cartao.perfil.tipo.valor

#     print registro.cartao.perfil.tipo.nome
#     print registro.cartao.perfil.nome
#     print registro.cartao.numero
#     print locale.currency(registro.valor).format()

    #registro = registro_dao.busca(6)

    registro_dao.mantem(registro,False)
    print registro_dao.aviso
        
    print 30 * "="
    
    for registro in registro_dao.busca():
        print str(registro[1]) +" "+ str(registro[2]) +" "+ str(registro[3])  +" "+ str(registro[4])
        
            