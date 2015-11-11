#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.turno import Turno
from catraca.dao.turnodao import TurnoDAO
from catraca.dao.finalidadedao import FinalidadeDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela turno...'
    
    turno = Turno()
    turno_dao = TurnoDAO()

    turno.inicio = datetime.datetime.strptime('11:00:00','%H:%M:%S').time()
    turno.fim = datetime.datetime.strptime('13:30:00','%H:%M:%S').time()
    
    turno = turno_dao.busca(2)
    turno.inicio = datetime.datetime.strptime('17:30:00','%H:%M:%S').time()
    turno.fim = datetime.datetime.strptime('19:00:00','%H:%M:%S').time()
    turno.finalidade = FinalidadeDAO().busca(3).id
    

    turno_dao.mantem(turno,False)
    print turno_dao.aviso
        
    print 30 * "="
    
    for turno in turno_dao.busca():
        print str(turno[1]) +" "+ str(turno[2]) +" "+ str(FinalidadeDAO().busca(turno[3]).nome) 