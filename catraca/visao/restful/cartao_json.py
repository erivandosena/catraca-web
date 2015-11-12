#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.entidades.cartao import Cartao


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CartaoJson(ServidorRestful):
    
    log = Logs()
    cartao_dao = CartaoDAO()
    
    def __init__(self, ):
        super(CartaoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def cartao_get(self):
        url = self.obter_servidor() + "cartao/jcartao"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
        print "Código: " + str(r.status_code)
        dados  = json.loads(r.text)
        
        for item in dados["cartoes"]:
            obj = self.dict_obj(item)
            if obj.id:
                lista = self.cartao_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.numero)
                    self.cartao_dao.insere(obj)
                    self.cartao_dao.commit()
                    print self.cartao_dao.aviso
                else:
                    print "existe - update " + str(obj.numero)
                    self.cartao_dao.atualiza_exclui(obj, False)
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
    