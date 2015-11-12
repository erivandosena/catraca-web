#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
import datetime
from catraca.dao.mensagem import Mensagem
from catraca.dao.mensagemdao import MensagemDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def main():
    print 'Iniciando os testes tabela mensagem...'
    
    mensagem = Mensagem()
    mensagem_dao = MensagemDAO()

    mensagem.msg_inicializacao = "Iniciando..."
    mensagem.msg_saldacao = "   BEM-VINDO!"
    mensagem.msg_aguardacartao = "   APROXIME\n   SEU CARTAO"
    mensagem.msg_erroleitor = "APROXIME CARTAO\n  NOVAMENTE..."
    mensagem.msg_bloqueioacesso = "     ACESSO\n   BLOQUEADO!"
    mensagem.msg_liberaacesso = "     ACESSO\n    LIBERADO!"
    mensagem.msg_semcredito = "     CARTAO\n   SEM SALDO!"
    mensagem.msg_semcadastro = "     CARTAO\n NAO CADASTRADO!"
    mensagem.msg_cartaoinvalido = "     CARTAO\n  INVALIDO!"
    mensagem.msg_turnoinvalido = "FORA DO HORARIO\n DE ATENDIMENTO"
    mensagem.msg_datainvalida = "  DIA NAO UTIL\nPARA ATENDIMENTO"
    mensagem.msg_cartaoutilizado = "CARTAO JA USADO\nPARA 01 REFEICAO"
    mensagem.msg_institucional1 = "    UNILAB - Unilab.edu.br"
    mensagem.msg_institucional2 = "Desenvolvido por\n  DISUP | DTI"
    mensagem.msg_institucional3 = "      RU\n   Liberdade"
    mensagem.msg_institucional4 = "     BOM\n    APETITE!"

    mensagem = mensagem_dao.busca(4)

#     msg = mensagem_dao.busca()
#     if msg is not None:
#         print "Não é possivel inserir, somente alterar!"
#     else:
#         mensagem_dao.mantem(mensagem,False)
#         print mensagem_dao.aviso
        
    mensagem_dao.mantem(mensagem,True) 
    print mensagem_dao.aviso   
         
    print 30 * "="
    
    for mensagem in mensagem_dao.busca():
        print str(mensagem[1]) +" "+ str(mensagem[2]) +" "+ str(mensagem[3]) +" "+ str(mensagem[4])