#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import simplejson as json
# import hashlib
# import decimal
# import datetime
#from catraca.modelo.entidades.registro import Registro


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RegistroOffline(object):

    def __init__(self):
        super(RegistroOffline, self).__init__()
        #Registro.__init__(self)
#         self.__reof_id = None
#         self.__reof_data = None
#         self.__reof_valor_pago = None
#         self.__reof_valor_custo = None
#         self.__cartao = None
#         self.__catraca = None
#         self.__vinculo = None
#         
#     def __eq__(self, outro):
#         return self.hash_dict(self) == self.hash_dict(outro)
#     
#     def __ne__(self, outro):
#         return not self.__eq__(outro)
#     
#     def hash_dict(self, obj):
#         return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
#     
#     def json_encode(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             return str(obj)
#         if isinstance(obj, datetime.datetime):
#             return str(obj)
#         raise TypeError(repr(obj) + " nao JSON serializado")
#     
#     @property
#     def id(self):
#         return self.__reof_id
#     
#     @id.setter
#     def id(self, valor):
#         self.__reof_id = valor
#         
#     @property
#     def data(self):
#         return self.__reof_data
#     
#     @data.setter
#     def data(self, valor):
#         self.__reof_data = valor
#         
#     @property
#     def pago(self):
#         return self.__reof_valor_pago
#     
#     @pago.setter
#     def pago(self, valor):
#         self.__reof_valor_pago = valor
#         
#     @property
#     def custo(self):
#         return self.__reof_valor_custo
#     
#     @custo.setter
#     def custo(self, valor):
#         self.__reof_valor_custo = valor
#         
#     @property
#     def cartao(self):
#         return self.__cartao
# 
#     @cartao.setter
#     def cartao(self, obj):
#         self.__cartao = obj
#         
#     @property
#     def catraca(self):
#         return self.__catraca
# 
#     @catraca.setter
#     def catraca(self, obj):
#         self.__catraca = obj
#         
#     @property
#     def vinculo(self):
#         return self.__vinculo
# 
#     @vinculo.setter
#     def vinculo(self, obj):
#         self.__vinculo = obj
        