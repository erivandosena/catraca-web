#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.cartao_valido import CartaoValido

__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CartaoJson(ServidorRestful):
    
    log = Logs()
    cartao_dao = CartaoDAO()
    
    def __init__(self):
        super(CartaoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def cartao_get(self, mantem_tabela=False, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "cartao/jcartao"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                #print "Status HTTP: " + str(r.status_code)
                
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["cartoes"]
                    if LISTA_JSON != []:
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                if mantem_tabela:
                                    self.mantem_tabela_local(obj, limpa_tabela)
                        return lista
                    else:
                        self.atualiza_exclui(None, True)
                        return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json cartao', exc_info=True)
        finally:
            pass
        
    def cartao_valido_get(self, numero_cartao):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "cartao/jcartao/" + str(numero_cartao)
                print url
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Status HTTP: " + str(r.status_code)
                
                print r.text

                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["cartao"]
                    if LISTA_JSON != []:
                        for item in LISTA_JSON:
                            obj = self.dict_obj_cartao_valido(item)
                            if obj:
                                return obj
                            else:
                                return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json cartao', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.cartao_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
        
    def atualiza_exclui(self, obj, boleano):
        self.cartao_dao.atualiza_exclui(obj, boleano)
        self.cartao_dao.commit()
        print self.cartao_dao.aviso
        
    def insere(self, obj):
        self.cartao_dao.insere(obj)
        self.cartao_dao.commit()
        print self.cartao_dao.aviso
        
    def dict_obj(self, formato_json):
        cartao = Cartao()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "cart_id":
                cartao.id = self.dict_obj(formato_json[item])
            if item == "cart_numero":
                cartao.numero = self.dict_obj(formato_json[item])
            if item == "cart_creditos":
                cartao.creditos = self.dict_obj(formato_json[item])
            if item == "tipo_id":
                cartao.tipo = self.dict_obj(formato_json[item])
        return cartao

    def dict_obj_cartao_valido(self, formato_json):
        cartao = CartaoValido()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj_cartao_valido(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "cart_id":
                cartao.id = self.dict_obj_cartao_valido(formato_json[item])
            if item == "cart_numero":
                cartao.numero = self.dict_obj_cartao_valido(formato_json[item])
            if item == "cart_creditos":
                cartao.creditos = self.dict_obj_cartao_valido(formato_json[item])
            if item == "tipo_valor":
                cartao.valor = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_refeicoes":
                cartao.refeicoes = self.dict_obj_cartao_valido(formato_json[item])
            if item == "tipo_id":
                cartao.tipo = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_id":
                cartao.vinculo = self.dict_obj_cartao_valido(formato_json[item])
        return cartao
    
    def lista_json(self, lista):
        if lista:
            for item in lista:
                cartao = {
                    "cart_numero":item[1],
                    "cart_creditos":float(item[2]),
                    "tipo_id":item[3]
                }
                self.cartao_put(cartao, item[0])
                #self.registro_dao.mantem(self.registro_dao.busca(item[0]),True)
                
    def objeto_json(self, obj):
        if obj:
            cartao = {
                "cart_numero":obj.numero,
                "cart_creditos":float(obj.creditos),
                "tipo_id":obj.tipo
            }
            return self.cartao_put(cartao, obj.id)
            
    def cartao_put(self, formato_json, id):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "cartao/atualiza/"+ str(id)
                print url
                header = {'Content-type': 'application/json'}
                r = requests.put(url, auth=(self.usuario, self.senha), headers=header, data=json.dumps(formato_json))
                print r.text
                print r.status_code
                return True
            else:
                return False
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro enviando json cartao.', exc_info=True)
        finally:
            pass
        