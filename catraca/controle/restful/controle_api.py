#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from catraca.controle.restful.controle_generico import ControleGenerico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleApi(ControleGenerico):
    
    contador = 0
    alarme = True
    
    def __init__(self):
        super(ControleApi, self).__init__()
        ControleGenerico.__init__(self)
        self.__periodo_ativo = None
        self.__turno_ativo = None
        self.__catraca_local = None
        self.hora_atual = self.util.obtem_hora()
        self.datahora_atual = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def periodo(self):
        #self.periodo = self.obtem_periodo()
        return self.__periodo_ativo
    
    @periodo.setter
    def periodo(self, valor):
        self.__periodo_ativo = valor
     
    @property
    def catraca(self):
        return self.__catraca_local
    
    @catraca.setter
    def catraca(self, valor):
        self.__catraca_local = valor

    @property
    def turno(self):
        return self.__turno_ativo
    
    @classmethod
    @turno.setter
    def turno(self, valor):
        self.__turno_ativo = valor
    
    @property
    def hora(self):
        return self.hora_atual
    
    @hora.setter
    def hora(self, valor):
        self.hora_atual = valor
    
    @property
    def datahora(self):
        return self.datahora_atual
    
    @datahora.setter
    def datahora(self, valor):
        self.datahora_atual = valor
        