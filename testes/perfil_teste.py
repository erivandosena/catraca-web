#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.dao.perfil import Perfil
from catraca.dao.perfildao import PerfilDAO
from catraca.dao.tipodao import TipoDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela perfil...'
    
    
    perfil = Perfil()
    perfil_dao = PerfilDAO()
    tipo_dao = TipoDAO()

    perfil.nome = "STEVEN JOBS"
    perfil.email = "teste1@teste.tw"
    perfil.telefone = "85987670600"
    perfil.nascimento = "02/1955"
    perfil.tipo = tipo_dao.busca_tipo(3)

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



