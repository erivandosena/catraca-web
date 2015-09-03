#!/usr/bin/env python
# -*- coding: latin-1 -*-


import os
import socket
import locale
import datetime
from catraca.dao.registro import Registro
from catraca.dao.registrodao import RegistroDAO
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.catracadao import CatracaDAO
from catraca.dao.finalidadedao import FinalidadeDAO

import requests
import json


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production



socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect(('unilab.edu.br', 0))
IP = '%s' % (socket.getsockname()[0])

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    print 'Iniciando os testes tabela registro...'
    
    registro = Registro()
    registro_dao = RegistroDAO()
    cartao_dao = CartaoDAO()

    registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    registro.giro = 1
    registro.cartao = cartao_dao.busca(4)
    registro.valor = registro.cartao.perfil.tipo.valor
    
    if registro_dao.conexao_status():
         print "conexao_status: "+ str(registro_dao.conexao_status())

    url = 'http://10.5.1.8:8888/api/tipo/inserir'


    payload = {'some': 'data'}
    
    dados = {"tipos": [{"tipo_id":9,"tipo_nome":"Administrador","tipo_vlr_credito":"0.00"},{"tipo_id":29,"tipo_nome":"alan","tipo_vlr_credito":"7.00"},{"tipo_id":13,"tipo_nome":"Catraca","tipo_vlr_credito":"4.00"},{"tipo_id":28,"tipo_nome":"erivando","tipo_vlr_credito":"2.00"},{"tipo_id":1,"tipo_nome":"Estudante","tipo_vlr_credito":"1.10"},{"tipo_id":30,"tipo_nome":"eu","tipo_vlr_credito":"0.00"},{"tipo_id":15,"tipo_nome":"Lab","tipo_vlr_credito":"1.99"},{"tipo_id":16,"tipo_nome":"Liberdade","tipo_vlr_credito":"89.69"},{"tipo_id":8,"tipo_nome":"Operador","tipo_vlr_credito":"0.00"},{"tipo_id":17,"tipo_nome":"Palmares","tipo_vlr_credito":"789.96"},{"tipo_id":2,"tipo_nome":"Professor","tipo_vlr_credito":"2.20"},{"tipo_id":27,"tipo_nome":"REBECA","tipo_vlr_credito":"999.00"},{"tipo_id":14,"tipo_nome":"ru","tipo_vlr_credito":"0.09"},{"tipo_id":3,"tipo_nome":"Tecnico","tipo_vlr_credito":"1.60"},{"tipo_id":19,"tipo_nome":"test","tipo_vlr_credito":"4.99"},{"tipo_id":22,"tipo_nome":"teste","tipo_vlr_credito":"242424.00"},{"tipo_id":12,"tipo_nome":"Teste","tipo_vlr_credito":"2.30"},{"tipo_id":10,"tipo_nome":"Teste","tipo_vlr_credito":"1.99"},{"tipo_id":11,"tipo_nome":"Tutor","tipo_vlr_credito":"1.50"},{"tipo_id":21,"tipo_nome":"UNILAB","tipo_vlr_credito":"2015.00"},{"tipo_id":4,"tipo_nome":"Visitante","tipo_vlr_credito":"4.00"}]}

    r = requests.post(url, auth=('teste', 'teste'), data=json.dumps(dados))

    url = 'http://10.5.1.8:8888/api/tipo/listar'
    r = requests.get(url, auth=('teste', 'teste'))
    print r.status_code
    print r.headers['content-type']
    print r.text
    
    
    """
    if not registro_dao.mantem(registro,False):
        raise Exception(registro_dao.aviso)
    else:
        print registro_dao.aviso
    """

    print 62 * "="
    print '======################### RELATORIO ####################======'
    print 62 * "="
    

    for registro in registro_dao.busca():
        cartao = cartao_dao.busca(registro[4])
        print str(registro[1]) +" "\
        + str(registro[2]) +" "\
        + str(registro[3]) +" "\
        + str(cartao.numero) +" "\
        + str(cartao.perfil.nome) +" "\
        + str(cartao.perfil.tipo.nome)
    print 62 * "="
