#!/usr/bin/env python
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
# -*- coding: utf-8 -*-

from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.registro_dao import RegistroDAO
<<<<<<< HEAD
=======
# -*- coding: latin-1 -*-

import datetime
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.perfildao import PerfilDAO
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


def main():
    print 'Iniciando os testes tabela cartao...'
    
    # Estudante = 1 | Tecnico = 2 | Professor = 3 | Visitante = 4

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4

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
     
    
<<<<<<< HEAD
=======
    cartao = Cartao()
    cartao_dao = CartaoDAO()
    perfil_dao = PerfilDAO()

    cartao.numero = 3994078862
    cartao.creditos = 1000
    cartao.perfil = perfil_dao.busca(4)
    cartao.data = datetime.datetime.strptime("1939-01-01 00:00:00","%Y-%m-%d %H:%M:%S")
    
    
    if not cartao_dao.mantem(cartao,False):
        raise Exception(cartao_dao.aviso)
    else:
        cartao_dao.commit()
        print cartao_dao.aviso

>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
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
            


