#!/usr/bin/env python
# -*- coding: latin-1 -*-


#from datetime import datetime
import locale
from catraca.dao.tipo import Tipo
from catraca.dao.tipodao import TipoDAO
from catraca.dao.usuario import Usuario
from catraca.dao.usuariodao import UsuarioDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela usuario...'
    
    tipo = Tipo()
    tipo_dao = TipoDAO()
    
    usuario = Usuario()
    usuario_dao = UsuarioDAO()

    usuario.nome = "'ALAN CLEBER'"
    usuario.email = "'alan.cleber@unilab.edu.br'"
    usuario.login = "'acleber'"
    usuario.senha = "'acleber'"
    usuario.nivel = "'1'"
    usuario.externo = "'00001'"
    usuario.documento = "12345678912"
    usuario.tipo = tipo_dao.busca("'Estudante'").id
    

    if usuario.id:
        if usuario_dao.altera(usuario):
            print "Alterado com sucesso!"
        else:
            print "Erro ao alterar:"
            print usuario_dao.erro
    else:
        if usuario_dao.insere(usuario):
            print "Inserido com sucesso!"
        else:
            print "Erro ao inserir:"
            print usuario_dao.erro
            
