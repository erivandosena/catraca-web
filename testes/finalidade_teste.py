#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.finalidade import Finalidade
from catraca.dao.finalidadedao import FinalidadeDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela finalidade...'
    
    finalidade = Finalidade()
    finalidade_dao = FinalidadeDAO()
    finalidade.nome = "teste" # Cafe, Almoco, Janta.

    finalidade = finalidade_dao.busca(4)

    finalidade_dao.mantem(finalidade,True)
    print finalidade_dao.aviso

    finalidade = finalidade_dao.busca()
    if finalidade:
        print 30 * "="
        for f in finalidade:
            print str(f[1])
    else:
        print "Tabela vazia!"
        