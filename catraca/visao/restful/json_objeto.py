#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from catraca.modelo.entidades.registro import Registro

__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class JsonObjeto(object):
    
    def __init__(self, **kwargs):
        super(JsonObjeto, self).__init__()
        #Registro.__init__(self)
        
        obj = self.dict_obj(kwargs)
        
        print obj.id
        print obj.data
        print obj.pago
        print obj.custo
        print obj.cartao
        print obj.turno
        print obj.catraca
        
        
    def dict_obj(self, formato_json):
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        
        #campos_objeto = [self.regi_id, self.regi_data, self.regi_valor_pago, self.regi_valor_custo, self.cart_id, self.turn_id, self.catr_id]

        registro = Registro()
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
             
#             print registro.id
#             print registro.data
#             print registro.pago
#             print registro.custo
#             print registro.cartao
#             print registro.turno
#             print registro.catraca

                
#             regi_id = "__regi_id"
#             regi_data = "__regi_data"
#             regi_valor_pago = "__regi_valor_pago"
#             regi_valor_custo = "__regi_valor_custo"
#             cart_id = "__cart_id"
#             turn_id = "__turn_id"
#             catr_id = "__catr_id"
            
            
#             campo_json = ''.join(["__", item])
#             objeto = self.compara_nomes(campos_objeto, campo_json, self.dict_obj(formato_json[item]))
        return registro
        
        
    def compara_nomes(self, lista, nome_campo, valor_campo):
        for i in range(len(lista)):
            if nome_campo == lista[i]:
                print str(lista[i]) + " : " + str(valor_campo)
                return lista[i]







# #         self.__dict__.update(kwargs)
# #         
#         print self.dict_obj(kwargs)
#         
#     def dict_obj(self, formato_json):
#         if isinstance(formato_json, list):
#             formato_json = [self.dict_obj(x) for x in formato_json]
#         if not isinstance(formato_json, dict):
#             return formato_json
#         registro = Registro()
#         for item in formato_json:
#             print 'item: ' + str( item)
#             #registro.__dict__[item] = self.dict_obj(formato_json[item])
#             print 'registro.__dict__[item]: ' + str( self.dict_obj(formato_json[item]) )
#             
#             registro.id = self.dict_obj(formato_json[item])
# #         class C(object):
# #             pass
# #         obj = C()
# #         for item in d_json:
# #             obj.__dict__[item] = self.dict_obj(d_json[item])
#         #print registro.regi_data
#         return registro