#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from catraca.dao.catraca import Catraca
from catraca.dao.catracadao import CatracaDAO
from catraca.dao.giro import Giro
from catraca.dao.girodao import GiroDAO
from catraca.dao.turno import Turno
from catraca.dao.turnodao import TurnoDAO
from catraca.dao.mensagem import Mensagem
from catraca.dao.mensagemdao import MensagemDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela catraca...'
    
    
    catraca = Catraca()
    catraca_dao = CatracaDAO()
    giro_dao = GiroDAO()
    turno_dao = TurnoDAO()
    mensagem_dao = MensagemDAO()

    catraca.ip = "10.5.2.253"
    catraca.localizacao = "RU Liberdade"
    catraca.tempo = 6000
    catraca.operacao = 1
    catraca.turno = turno_dao.busca(1).id
    catraca.giro = giro_dao.busca(1).id
    catraca.mensagem = mensagem_dao.busca(1).id

    cat = catraca_dao.busca()
    if cat is not None:
        print "Nao e possivel inserir, somente alterar!"
    else:
        catraca_dao.mantem(catraca,False)
        print catraca_dao.aviso
        
    print 30 * "="
    
    for catraca in catraca_dao.busca():
        print str(catraca[1]) +" "+ str(catraca[2]) +" "+ str(catraca[3]) +" "+ str(catraca[4])+" "+ str(catraca[5]) +" "+ str(catraca[6]) +" "+ str(catraca[6])
