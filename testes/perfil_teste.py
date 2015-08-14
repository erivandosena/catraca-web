#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.tipo import Tipo
from catraca.dao.tipodao import TipoDAO
from catraca.dao.perfil import Perfil
from catraca.dao.perfildao import PerfilDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela perfil...'
    
    tipo = Tipo()
    tipo_dao = TipoDAO()
    
    perfil = Perfil()
    perfil_dao = PerfilDAO()

    perfil.nome = "ADA LOVELACE"
    perfil.email = "teste4@teste.tw"
    perfil.telefone = "85999670877"
    perfil.nascimento = "09/1815"
    perfil.tipo = tipo_dao.busca_tipo(2).id


    if perfil.id:
        if perfil_dao.altera(perfil):
            print "Alterado com sucesso!"
        else:
            print perfil_dao.erro
    else:
        if perfil_dao.insere(perfil):
            print "Inserido com sucesso!"
        else:
            print perfil_dao.erro



