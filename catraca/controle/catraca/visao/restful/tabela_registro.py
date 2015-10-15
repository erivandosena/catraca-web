#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import threading
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TabelaRegistro(ServidorRestful):
    
    log = Logs()
    registro_dao = RegistroDAO()
    
    def __init__(self, ):
        super(TabelaRegistro, self).__init__()
        ServidorRestful.__init__(self)
        
    def registro_get(self):
        url = self.obter_servidor() + "registro/tregistro"
        print url
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=('teste', 'teste'), headers=header)
        print "Código: " + str(r.status_code)
        print "\n"

        data  = json.loads(r.text)
        for item in data["registros"]:
            obj = self.dict_obj(item)

            if obj.id:
                obj.id = None
                print obj.id
                print obj.data
                print obj.pago
                print obj.custo
                print obj.cartao
                print obj.turno
                print obj.catraca
        
                self.registro_dao.mantem(obj,False)
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
    