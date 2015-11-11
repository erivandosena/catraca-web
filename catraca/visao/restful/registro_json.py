#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RegistroJson(ServidorRestful):
    
    log = Logs()
    registro_dao = RegistroDAO()
    
    def __init__(self, ):
        super(RegistroJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def registro_get(self):
        url = self.obter_servidor() + "registro/jregistro"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
        print "Código: " + str(r.status_code)
        data  = json.loads(r.text)
        
        for item in data["registros"]:
            obj = self.dict_obj(item)

            if obj.id:
                lista = self.registro_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.data)
                    self.registro_dao.insere(obj)
                    print self.registro_dao.aviso
                else:
                    print "existe - update " + str(obj.data)
                    self.registro_dao.atualiza_exclui(obj, False)
                    print self.registro_dao.aviso
        
    def dict_obj(self, formato_json):
        registro = Registro()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "regi_id":
                registro.id = self.dict_obj(formato_json[item])
            if item == "regi_data":
                registro.data = self.dict_obj(formato_json[item])
            if item == "regi_valor_pago":
                registro.pago = self.dict_obj(formato_json[item])
            if item == "regi_valor_custo":
                registro.custo = self.dict_obj(formato_json[item])
            if item == "cart_id":
                registro.cartao = self.dict_obj(formato_json[item])
            if item == "turn_id":
                registro.turno = self.dict_obj(formato_json[item])
            if item == "catr_id":
                registro.catraca = self.dict_obj(formato_json[item])
                
        return registro
    