#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.entidades.catraca import Catraca


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CatracaJson(ServidorRestful):
    
    log = Logs()
    catraca_dao = CatracaDAO()
    
    def __init__(self, ):
        super(CatracaJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def catraca_get(self):
        url = self.obter_servidor() + "catraca/jcatraca"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
        print "Código: " + str(r.status_code)
        dados  = json.loads(r.text)
        
        for item in dados["catracas"]:
            obj = self.dict_obj(item)
            if obj.id:
                lista = self.catraca_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.nome)
                    self.catraca_dao.insere(obj)
                    print self.catraca_dao.aviso
                else:
                    print "existe - update " + str(obj.nome)
                    self.catraca_dao.atualiza_exclui(obj, False)
                    print self.catraca_dao.aviso
        
    def dict_obj(self, formato_json):
        catraca = Catraca()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "catr_id":
                catraca.id = self.dict_obj(formato_json[item])
            if item == "catr_ip":
                catraca.ip = self.dict_obj(formato_json[item])
            if item == "catr_tempo_giro":
                catraca.tempo = self.dict_obj(formato_json[item])
            if item == "catr_operacao":
                catraca.operacao = self.dict_obj(formato_json[item])
            if item == "catr_nome":
                catraca.nome = self.dict_obj(formato_json[item]).encode('utf-8')
                
        return catraca
    