#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.tipo import Tipo
from catraca.dao.tipodao import TipoDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


def main():
    print 'Iniciando os testes tabela tipo...'
    
    tipo = Tipo()
    tipo_dao = TipoDAO()
    tipo.nome = "teste" # Estudante(1,10), Professor(2,20), Tecnico(1,60), Visitante(4,00), Operador, Administrador.
    tipo.valor = 0.00

    tipo = tipo_dao.busca(7)

    tipo_dao.mantem(tipo,True)
    print tipo_dao.aviso
    
    print 30 * "="
    
    for tipo in tipo_dao.busca():
        print str(tipo[1]) +" "+ str(tipo[2])
        