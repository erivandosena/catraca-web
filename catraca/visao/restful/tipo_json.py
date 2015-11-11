#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.tipo_dao import TipoDAO
from catraca.modelo.entidades.tipo import Tipo


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TipoJson(ServidorRestful):
    
    log = Logs()
    tipo_dao = TipoDAO()
    
    def __init__(self, ):
        super(TipoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def tipo_get(self):
        url = self.obter_servidor() + "tipo/jtipo"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
        print "Código: " + str(r.status_code)
        dados  = json.loads(r.text)
        
        for item in dados["tipos"]:
            obj = self.dict_obj(item)
            if obj.id:
                lista = self.tipo_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.nome)
                    self.tipo_dao.insere(obj)
                    print self.tipo_dao.aviso
                else:
                    print "existe - update " + str(obj.nome)
                    self.tipo_dao.atualiza_exclui(obj, False)
                    print self.tipo_dao.aviso
        
    def dict_obj(self, formato_json):
        tipo = Tipo()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "tipo_id":
                tipo.id = self.dict_obj(formato_json[item])
            if item == "tipo_nome":
                tipo.nome = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "tipo_valor":
                tipo.valor = self.dict_obj(formato_json[item])
                
        return tipo
    