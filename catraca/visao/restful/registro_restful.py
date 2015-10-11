#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import datetime
from datetime import datetime
from time import sleep
from catraca.dao.registrodao import RegistroDAO
from catraca.restful.servidor_restful import ServidorRestful
import collections

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RegistroRestful(ServidorRestful):
    
    registro_dao = RegistroDAO()
    
    def __init__(self):
        super(RegistroRestful, self).__init__()
        ServidorRestful.__init__(self)
        
    def lista_para_json(self, lista):
        #if lista != []:
        for item in lista:
            registro = {
                "regi_data":item[1],
                "regi_valor_pago":float(item[2]),
                "regi_valor_custo":float(item[3]),
                "cart_id":item[4],
                "turn_id":item[5],
                "catr_id":item[6]
            }
            self.post_registro(registro)
            #self.registro_dao.mantem(self.registro_dao.busca(item[0]),True)

    def objeto_para_json(self, obj):
        registro = {
            "regi_data":str(obj.data),
            "regi_valor_pago":str(obj.pago),
            "regi_valor_custo":str(obj.custo),
            "cart_id":str(obj.cartao.id),
            "turn_id":str(obj.turno.id),
            "catr_id":str(obj.catraca.id)
        }
        self.post_registro(registro)
            
    def post_registro(self, formato_json):
        url = self.obter_servidor() + "registro/insere"
        print url
        header = {'Content-type': 'application/json'}
        r = requests.post(url, auth=('teste', 'teste'), headers=header, data=json.dumps(formato_json))
        #print r.headers['content-type']
        #print r.headers
        print r.text
        print r.status_code
        #print 'requests.post: '+ str(formato_json)
        
    def obtem_registros(self):
        return self.registro_dao.busca()
    
    def obtem_registro(self, id):
            return self.registro_dao.busca(id)
    