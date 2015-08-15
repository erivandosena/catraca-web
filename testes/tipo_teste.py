#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.tipo import Tipo
from catraca.dao.tipodao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela tipo...'
    
    tipo = Tipo()
    tipo_dao = TipoDAO()
    tipo.nome = "Visitante" # Estudante(1,10), Professor(2,20), Tecnico(1,60), Visitante(4,00), Operador, Administrador.
    tipo.valor = 4.00

    if tipo.id:
        if tipo_dao.altera(tipo):
            print "Alterado com sucesso!"
        else:
            print tipo_dao.erro
    else:
        if tipo_dao.insere(tipo):
            print "Inserido com sucesso!"
        else:
            print tipo_dao.erro

