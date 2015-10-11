#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.custo_refeicao import CustoRefeicao


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CustoRefeicaoDAO(ConexaoGenerica):
    
    def __init__(self):
        super(CustoRefeicaoDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self, *arg):
        pass
        
    def mantem(self, obj, delete):
        pass
    