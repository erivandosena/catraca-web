#!/usr/bin/env python
# -*- coding: latin-1 -*-

import datetime
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.perfildao import PerfilDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela cartao...'
    
    # Estudante = 1 | Tecnico = 2 | Professor = 3 | Visitante = 4

    cartao = Cartao()
    cartao_dao = CartaoDAO()
    perfil_dao = PerfilDAO()

    cartao.numero = 3994078862
    cartao.creditos = 1000
    cartao.perfil = perfil_dao.busca(4)
    cartao.data = datetime.datetime.strptime("1939-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    
    
    if not cartao_dao.mantem(cartao,False):
        raise Exception(cartao_dao.aviso)
    else:
        cartao_dao.commit()
        print cartao_dao.aviso

#     if cartao.id:
#         if cartao_dao.altera(cartao):
#             print "Alterado com sucesso!"
#         else:
#             print cartao_dao.erro
#     else:
#         if cartao_dao.insere(cartao):
#             print "Inserido com sucesso!"
#         else:
#             print cartao_dao.erro
            


