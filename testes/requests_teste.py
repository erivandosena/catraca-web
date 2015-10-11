#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pprint
import socket
import locale
import datetime
# from catraca.dao.registro import Registro
# from catraca.dao.registrodao import RegistroDAO
# from catraca.dao.cartaodao import CartaoDAO
# from catraca.dao.catracadao import CatracaDAO
# from catraca.dao.finalidadedao import FinalidadeDAO
# from catraca.dao.tipodao import TipoDAO
import requests
import json
from catraca.visao.restful.tabela_registro import TabelaRegistro

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production



socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect(('unilab.edu.br', 0))
IP = '%s' % (socket.getsockname()[0])

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    print 'Iniciando os testes restful'
    
    t_registro = TabelaRegistro()
    
    t_registro.registro_get()
    
    
#     registro = Registro()
#     registro_dao = RegistroDAO()
#     cartao_dao = CartaoDAO()
# 
#     registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#     registro.giro = 1
#     registro.cartao = cartao_dao.busca(4)
#     registro.valor = registro.cartao.perfil.tipo.valor
#     
#     if registro_dao.conexao_status():
#          print "conexao_status: "+ str(registro_dao.conexao_status())
#          
# 
#     def lista_tipos(lista):
#         ilista=[]
#         count = 0
#         for item in lista:
#             i = {
#                 #'id':item[0],
#                 "tipo_nome":item[1],
#                 "tipo_vlr_credito":float(item[2])
#             }
#             count += 1
#             post_tipo(i)
#             print i
#             print "inserindo.." + str(count)
#             
#     
#     tipo_dao = TipoDAO()
#     
# 
#     def post_tipo(tipo):
#         url = 'http://10.5.0.15:27289/api/tipo/inserir'
#         #dados = {"tipo_nome":"Teste requests","tipo_vlr_credito":"9.91"}
#         header = {'Content-type': 'application/json'}
#         r = requests.post(url, auth=('teste', 'teste'), headers=header, data=json.dumps(tipo))
# 
#     
#     lista_tipos(tipo_dao.busca())
# 
# 
#     url = 'http://10.5.0.15:27289/api/tipo/listar'
#     r = requests.get(url, auth=('teste', 'teste'))
#     print r.status_code
#     print r.headers['content-type']
#     #print r.text
#     pprint.pprint(r.text)
#     
#     
#     """
#     if not registro_dao.mantem(registro,False):
#         raise Exception(registro_dao.aviso)
#     else:
#         print registro_dao.aviso
#    """

#     print 62 * "="
#     print '======################### RELATORIO ####################======'
#     print 62 * "="
#     
# 
#     for registro in registro_dao.busca():
#         cartao = cartao_dao.busca(registro[4])
#         print str(registro[1]) +" "\
#         + str(registro[2]) +" "\
#         + str(registro[3]) +" "\
#         + str(cartao.numero) +" "\
#         + str(cartao.perfil.nome) +" "\
#         + str(cartao.perfil.tipo.nome)
#     print 62 * "="
