#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Giro(object):

    def __init__(self):
        super(Giro, self).__init__()
        self.__giro_id = None
        self.__giro_giros_horario = 0
        self.__giro_giros_antihorario = 0
        self.__giro_data_giro = None
        self.__catraca = None

    @property
    def id(self):
        return self.__giro_id
    
    @id.setter
    def id(self, valor):
        self.__giro_id = valor
    
    @property
    def horario(self):
        return self.__giro_giros_horario
    
    @horario.setter
    def horario(self, valor):
        self.__giro_giros_horario = valor
    
    @property
    def antihorario(self):
        return self.__giro_giros_antihorario
    
    @antihorario.setter
    def antihorario(self, valor):
        self.__giro_giros_antihorario = valor
    
    @property
    def data(self):
        return self.__giro_data_giro
    
    @data.setter
    def data(self, valor):
        self.__giro_data_giro = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, obj):
        self.__catraca = obj
        