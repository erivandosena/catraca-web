#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.giro import Giro
from catraca.dao.girodao import GiroDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela giro...'
    
    giro = Giro()
    giro_dao = GiroDAO()

    giro.horario = 1
    giro.antihorario = 0
    giro.data = datetime.datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")


    giro_dao.mantem(giro,False)
    print giro_dao.aviso
        
    print 30 * "="
    
    for giro in giro_dao.busca():
        print str(giro[1]) +" "+ str(giro[2]) +" "+ str(giro[3])