#!/usr/bin/env python
# -*- coding: utf-8 -*-


import simplejson as json
import hashlib


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class UsuarioExterno(object):
    
    def __init__(self):
        self.__categoria = None
        self.__cpf_cnpj = None
        self.__email = None
        self.__id_categoria = None
        self.__id_usuario = None
        self.__identidade = None
        self.__login = None
        self.__matricula_disc = None
        self.__nivel_discente = None
        self.__nome = None
        self.__passaporte = None
        self.__siape = None
        self.__status_discente = None
        self.__status_servidor = None
        self.__tipo_usuario = None
         
    def __eq__(self, outro):
        return self.hash_dict(self) == self.hash_dict(outro)
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    def hash_dict(self, obj):
        return hashlib.sha1(json.dumps(obj.__dict__, use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')).hexdigest()
    
    @property
    def idusuario(self):
        return self.__id_usuario
    
    @idusuario.setter
    def idusuario(self, valor):
        self.__id_usuario = valor
        
    @property
    def idcategoria(self):
        return self.__id_categoria
    
    @idcategoria.setter
    def idcategoria(self, valor):
        self.__id_categoria = valor
        
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor
        
    @property
    def cpfcnpj(self):
        return self.__cpf_cnpj
    
    @cpfcnpj.setter
    def cpfcnpj(self, valor):
        self.__cpf_cnpj = valor
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        self.__email = valor
        
    @property
    def identidade(self):
        return self.__identidade
    
    @identidade.setter
    def identidade(self, valor):
        self.__identidade = valor
        
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, valor):
        self.__login = valor
        
    @property
    def matriculadisc(self):
        return self.__matricula_disc
    
    @matriculadisc.setter
    def matriculadisc(self, valor):
        self.__matricula_disc = valor
        
    @property
    def niveldiscente(self):
        return self.__nivel_discente
    
    @niveldiscente.setter
    def niveldiscente(self, valor):
        self.__nivel_discente = valor
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
         
    @property
    def passaporte(self):
        return self.__passaporte
    
    @passaporte.setter
    def passaporte(self, valor):
        self.__passaporte = valor
        
    @property
    def siape(self):
        return self.__siape
    
    @siape.setter
    def siape(self, valor):
        self.__siape = valor
        
    @property
    def statusdiscente(self):
        return self.__status_discente
    
    @statusdiscente.setter
    def statusdiscente(self, valor):
        self.__status_discente = valor
        
    @property
    def statusservidor(self):
        return self.__status_servidor
    
    @statusservidor.setter
    def statusservidor(self, valor):
        self.__status_servidor = valor
        
    @property
    def tipousuario(self):
        return self.__tipo_usuario
    
    @tipousuario.setter
    def tipousuario(self, valor):
        self.__tipo_usuario = valor
        