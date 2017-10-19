#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from catraca.controle.raspberrypi.pinos import PinoControle


rpi = PinoControle()
D0 = rpi.ler(17)['gpio']
D1 = rpi.ler(27)['gpio']
bits = ''
numero_cartao = None

def zero(self):
    global bits
    bits = bits + '0'

def um(self):
    global bits
    bits = bits + '1'

def obtem_numero_cartao_rfid():
    id = None
    try:
        rpi.evento_rising_ou_falling(D0, zero)
        rpi.evento_rising_ou_falling(D1, um)
        while True:
            if bits:
                print bits
                id = int(str(bits), 2)
                if (len(bits) == 32) and (len(str(id)) == 10):
                    self.numero_cartao = id
                    return numero_cartao
                else:
                    id = None
                    return id
            else:
                return id
    except Exception as excecao:
        print excecao
    finally:
        bits = ''
        
def main():
    while True:
        print obtem_numero_cartao_rfid()
        sleep(1)


# import os
# import pprint
# import socket
# import locale
# import datetime
# # from catraca.dao.registro import Registro
# # from catraca.dao.registrodao import RegistroDAO
# # from catraca.dao.cartaodao import CartaoDAO
# # from catraca.dao.catracadao import CatracaDAO
# # from catraca.dao.finalidadedao import FinalidadeDAO
# # from catraca.dao.tipodao import TipoDAO
# import requests
# import json
# from catraca.controle.recursos.tipo_json import TipoJson
# from catraca.controle.recursos.turno_json import TurnoJson
# from catraca.controle.recursos.catraca_json import CatracaJson
# from catraca.controle.recursos.giro_json import GiroJson
# from catraca.controle.recursos.unidade_json import UnidadeJson
# from catraca.controle.recursos.custo_refeicao_json import CustoRefeicaoJson
# from catraca.controle.recursos.usuario_json import UsuarioJson
# from catraca.controle.recursos.mensagem_json import MensagemJson
# from catraca.controle.recursos.cartao_json import CartaoJson
# from catraca.controle.recursos.vinculo_json import VinculoJson
# from catraca.controle.recursos.isencao_json import IsencaoJson
# from catraca.controle.recursos.unidade_turno_json import UnidadeTurnoJson
# from catraca.controle.recursos.catraca_unidade_json import CatracaUnidadeJson
# from catraca.controle.recursos.registro_json import RegistroJson
# from catraca.util import Util
# 
# 
# from catraca.modelo.dao.catraca_dao import CatracaDAO
# from catraca.modelo.dao.turno_dao import TurnoDAO
# 
# __author__ = "Erivando Sena"
# __copyright__ = "Copyright 2015, Unilab"
# __email__ = "erivandoramos@unilab.edu.br"
# __status__ = "Prototype" # Prototype | Development | Production
# 
# 
# 
# socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.connect(('unilab.edu.br', 0))
# IP = '%s' % (socket.getsockname()[0])
# 
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
# 
# def main():
#     
#     pass
#     
#     
#     """
#     print 'Iniciando os testes restful'
# 
#     print "===" * 10 + " TIPO " + "===" * 10
#     tipo_json = TipoJson()
#     tipo_json.tipo_get()
#     
#     print "===" * 10 + " TURNO " + "===" * 10
#     turno_json = TurnoJson()
#     turno_json.turno_get()
#     
#     print "===" * 10 + " UNIDADE " + "===" * 10
#     unidade_json = UnidadeJson()
#     unidade_json.unidade_get()
#     
#     print "===" * 10 + " CUSTO-REFEIÇÃO " + "===" * 10
#     custo_refeicao_json = CustoRefeicaoJson()
#     custo_refeicao_json.custo_refeicao_get()
#     
#     print "===" * 10 + " USUÁRIO " + "===" * 10
#     usuario_json = UsuarioJson()
#     usuario_json.usuario_get()
# 
#     print "===" * 10 + " CATRACA " + "===" * 10
#     catraca_json = CatracaJson()
#     catraca_json.catraca_get()
#     
#     print "===" * 10 + " GIRO " + "===" * 10
#     giro_json = GiroJson()
#     giro_json.giro_get()
#     
#     print "===" * 10 + " MENSAGEM " + "===" * 10
#     mensagem_json = MensagemJson()
#     mensagem_json.mensagem_get()
#     
#     print "===" * 10 + " CARTAO " + "===" * 10
#     cartao_json = CartaoJson()
#     cartao_json.cartao_get()
#     
#     print "===" * 10 + " VÍNCULO " + "===" * 10
#     vinculo_json = VinculoJson()
#     vinculo_json.vinculo_get()
#     
#     print "===" * 10 + " ISENÇÃO " + "===" * 10
#     isencao_json = IsencaoJson()
#     isencao_json.isencao_get()
#     
#     print "===" * 10 + " UNIDADE-TURNO " + "===" * 10
#     unidade_turno_json = UnidadeTurnoJson()
#     unidade_turno_json.unidade_turno_get()
#     
#     print "===" * 10 + " CATRACA-UNIDADE " + "===" * 10
#     catraca_unidade_json = CatracaUnidadeJson()
#     catraca_unidade_json.catraca_unidade_get()
# 
#     print "===" * 10 + " REGISTRO " + "===" * 10
#     registro_json = RegistroJson()
#     registro_json.registro_get()
#     """
# 
# 
# #     registro = Registro()
# #     registro_dao = RegistroDAO()
# #     cartao_dao = CartaoDAO()
# # 
# #     registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
# #     registro.giro = 1
# #     registro.cartao = cartao_dao.busca(4)
# #     registro.valor = registro.cartao.perfil.tipo.valor
# #     
# #     if registro_dao.conexao_status():
# #          print "conexao_status: "+ str(registro_dao.conexao_status())
# #          
# # 
# #     def lista_tipos(lista):
# #         ilista=[]
# #         count = 0
# #         for item in lista:
# #             i = {
# #                 #'id':item[0],
# #                 "tipo_nome":item[1],
# #                 "tipo_vlr_credito":float(item[2])
# #             }
# #             count += 1
# #             post_tipo(i)
# #             print i
# #             print "inserindo.." + str(count)
# #             
# #     
# #     tipo_dao = TipoDAO()
# #     
# # 
# #     def post_tipo(tipo):
# #         url = 'http://10.5.0.15:27289/api/tipo/inserir'
# #         #dados = {"tipo_nome":"Teste requests","tipo_vlr_credito":"9.91"}
# #         header = {'Content-type': 'application/json'}
# #         r = requests.post(url, auth=('teste', 'teste'), headers=header, data=json.dumps(tipo))
# # 
# #     
# #     lista_tipos(tipo_dao.busca())
# # 
# # 
# #     url = 'http://10.5.0.15:27289/api/tipo/listar'
# #     r = requests.get(url, auth=('teste', 'teste'))
# #     print r.status_code
# #     print r.headers['content-type']
# #     #print r.text
# #     pprint.pprint(r.text)
# #     
# #     
# #     """
# #     if not registro_dao.mantem(registro,False):
# #         raise Exception(registro_dao.aviso)
# #     else:
# #         print registro_dao.aviso
# #    """
# 
# #     print 62 * "="
# #     print '======################### RELATORIO ####################======'
# #     print 62 * "="
# #     
# # 
# #     for registro in registro_dao.busca():
# #         cartao = cartao_dao.busca(registro[4])
# #         print str(registro[1]) +" "\
# #         + str(registro[2]) +" "\
# #         + str(registro[3]) +" "\
# #         + str(cartao.numero) +" "\
# #         + str(cartao.perfil.nome) +" "\
# #         + str(cartao.perfil.tipo.nome)
# #     print 62 * "="
