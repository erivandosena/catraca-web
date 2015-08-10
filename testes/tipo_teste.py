#!/usr/bin/env python
# -*- coding: latin-1 -*-


#from datetime import datetime
import locale
from catraca.dao.tipo import Tipo
from catraca.dao.tipodao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela tipo...'
    
    tipo = Tipo()
    tipo_dao = TipoDAO()

    # Estudante(1,10), Professor(2,20), Tecnico(1,60), Visitante(4,00), Operador, Administrador.
    tipo.nome = "'Administrador'"

    if tipo.id:
        if tipo_dao.altera(tipo):
            print "Alterado com sucesso!"
        else:
            print "Erro ao alterar:"
            print tipo_dao.erro
    else:
        if tipo_dao.insere(tipo):
            print "Inserido com sucesso!"
        else:
            print "Erro ao inserir:"
            print tipo_dao.erro
            
