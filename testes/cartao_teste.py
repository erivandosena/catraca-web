#!/usr/bin/env python
# -*- coding: utf-8 -*-

from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.registro_dao import RegistroDAO

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"

def main():
    print 'Iniciando os testes tabela cartao...'
    
    # Estudante = 1 | Tecnico = 2 | Professor = 3 | Visitante = 4


    print "=" * 20 + " Cartao ativo"
    
    cartao_dao = CartaoDAO()
    obj = cartao_dao.busca_cartao_valido("1234567890")
    if obj:
        print obj[0]
        print obj[1]
        print obj[2]
        print obj[3]
        print obj[4]
    else:
        print obj
        
    print "=" * 20 + " Limite de uso"
        
    registro_dao = RegistroDAO()
    obj = registro_dao.busca_utilizacao("2015-10-16 11:00:00","2015-10-16 13:30:00", 1, 1)
    if obj:
        print obj[0]
    else:
        print obj
        
    print "=" * 20 + " Isencao"
    
    cartao_dao = CartaoDAO()
    obj = cartao_dao.busca_isencao()
    if obj:
        print obj[0]
        print obj[1]
    else:
        print obj
     
    
#     if cartao.id:
#         if cartao_dao.altera(cartao):
#             print "Alterado com sucesso!"
#         else:
#             print cartao_dao.erro
#     else:
#         if cartao_dao.insere(cartao):
#             print "Inserido com sucesso!"
#         else:
#             print cartao_dao.erro
            


