#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.finalidade import Finalidade
from catraca.dao.finalidadedao import FinalidadeDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


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
        