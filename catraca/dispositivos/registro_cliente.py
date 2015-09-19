#!/usr/bin/env python
# -*- coding: latin-1 -*-

import json
import requests
from time import sleep
from catraca.dao.registrodao import RegistroDAO
from catraca.dispositivos.servidor_restful import ServidorRestful


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RegistroCliente(ServidorRestful):
    
    registro_dao = RegistroDAO()
    
    def __init__(self):
        super(RegistroCliente, self).__init__()
        ServidorRestful.__init__(self)
        
    def formato_json(self, lista):
        ilista=[]
        for item in lista:
            registro = {
                "tipo_nome":item[1],
                "regi_datahora":item[2],
                "regi_giro":item[3],
                "regi_valor":float(item[4]),
                "cart_id":item[5]
            }
            self.post_registro(registro)
            self.registro_dao.mantem(self.registro_dao.busca(item[0]),True)
            
    def post_registro(self, json):
        url = self.obter_servidor() + "registro/inserir"
        header = {'Content-type': 'application/json'}
        requests.post(url, auth=('teste', 'teste'), headers=header, data=json.dumps(json))
        
    def obtem_registros(self):
        return self.registro_dao.busca()
                
    def post(self):
        self.formato_json(self.obtem_registros)
        