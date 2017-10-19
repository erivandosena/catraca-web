#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.dao.perfil import Perfil
from catraca.dao.perfildao import PerfilDAO
from catraca.dao.tipodao import TipoDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


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

    perfil = perfil_dao.busca(0)
    perfil.nome

    perfil_dao.mantem(perfil,False)
    print tipo_dao.aviso
        
    print 30 * "="
    
    for perfil in perfil_dao.busca():
        print str(perfil[1]) +" "+ str(perfil[2])

