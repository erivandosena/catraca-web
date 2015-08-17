#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Catraca(object):

    def __init__(self):
        super(Catraca, self).__init__()
        self.__catr_id = None
        self.__catr_ip = None
        self.__catr_localizacao = None
        self.__catr_tempo_giro = None
        self.__catr_operacao = None
        self.__turno = None
        self.__giro = None
        self.__mensagem = None

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
    def localizacao(self):
        return self.__catr_localizacao
    
    @localizacao.setter
    def localizacao(self, valor):
        self.__catr_localizacao = valor
 
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
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, obj):
        self.__turno = obj
 
    @property
    def giro(self):
        return self.__giro
    
    @giro.setter
    def giro(self, obj):
        self.__giro = obj
        
    @property
    def mensagem(self):
        return self.__mensagem
    
    @mensagem.setter
    def mensagem(self, obj):
        self.__mensagem = obj
        
        