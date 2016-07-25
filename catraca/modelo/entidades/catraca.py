#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib
import decimal


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Catraca(object):
    
    def __init__(self):
        super(Catraca, self).__init__()
        self.__catr_id = None
        self.__catr_ip = None
        self.__catr_tempo_giro = None
        self.__catr_operacao = None
        self.__catr_nome = None
        self.__catr_mac_lan = None
        self.__catr_mac_wlan = None
        self.__catr_interface_rede = None
        
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, default=self.json_encode_decimal, use_decimal=False, ensure_ascii=False, sort_keys=False, encoding='utf-8')).hexdigest()
    
    def json_encode_decimal(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        raise TypeError(repr(obj) + " nao JSON serializado")
    
    @property
    def id(self):
        return self.__catr_id
    
    @id.setter
    def id(self, valor):
        self.__catr_id = valor
    
    @property
    def ip(self):
        return self.__catr_ip
    
    @ip.setter
    def ip(self, valor):
        self.__catr_ip = valor
    
    @property
    def tempo(self):
        return self.__catr_tempo_giro
    
    @tempo.setter
    def tempo(self, valor):
        self.__catr_tempo_giro = valor
    
    @property
    def operacao(self):
        return self.__catr_operacao
    
    @operacao.setter
    def operacao(self, valor):
        self.__catr_operacao = valor
    
    @property
    def nome(self):
        return self.__catr_nome
    
    @nome.setter
    def nome(self, valor):
        self.__catr_nome = valor
        
    @property
    def maclan(self):
        return self.__catr_mac_lan
    
    @maclan.setter
    def maclan(self, valor):
        self.__catr_mac_lan = valor
    
    @property
    def macwlan(self):
        return self.__catr_mac_wlan
        
    @macwlan.setter
    def macwlan(self, valor):
        self.__catr_mac_wlan = valor
        
    @property
    def interface(self):
        return self.__catr_interface_rede
        
    @interface.setter
    def interface(self, valor):
        self.__catr_interface_rede = valor
        