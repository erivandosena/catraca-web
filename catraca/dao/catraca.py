#!/usr/bin/env python
# -*- coding: latin-1 -*-

from giro import Giro

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Catraca(object):

    def __init__(self):
        super(Catraca, self).__init__()
        self.__catr_id = None
        self.__catr_local = None
        self.__catr_tempo_giro = None
        self.__catr_sentido_giro = None
        self.__catr_hora_inicio_almoco = None
        self.__catr_hora_fim_almoco = None
        self.__catr_hora_inicio_janta = None
        self.__catr_hora_fim_janta = None
        self.__giro = Giro()

    @property
    def id(self):
        return self.__catr_id
    
    @id.setter
    def id(self, valor):
        self.__catr_id = valor
 
    @property
    def local(self):
        return self.__catr_local
    
    @local.setter
    def local(self, valor):
        self.__catr_local = valor
 
    @property
    def tempo(self):
        return self.__catr_tempo_giro
    
    @tempo.setter
    def tempo(self, valor):
        self.__catr_tempo_giro = valor
 
    @property
    def sentido(self):
        return self.__catr_sentido_giro
    
    @sentido.setter
    def sentido(self, valor):
        self.__catr_sentido_giro = valor
 
    @property
    def inicio_almoco(self):
        return self.__catr_hora_inicio_almoco
    
    @inicio_almoco.setter
    def inicio_almoco(self, valor):
        self.__catr_hora_inicio_almoco = valor
 
    @property
    def fim_almoco(self):
        return self.__catr_hora_fim_almoco
    
    @fim_almoco.setter
    def fim_almoco(self, valor):
        self.__catr_hora_fim_almoco = valor
 
    @property
    def inicio_janta(self):
        return self.__catr_hora_inicio_janta
    
    @inicio_janta.setter
    def inicio_janta(self, valor):
        self.__catr_hora_inicio_janta = valor
 
    @property
    def fim_janta(self):
        return self.__catr_hora_fim_janta
    
    @fim_janta.setter
    def fim_janta(self, valor):
        self.__catr_hora_fim_janta = valor
 
    @property
    def giro(self):
        return self.__giro
    
    @giro.setter
    def giro(self, obj):
        self.__giro = obj
        