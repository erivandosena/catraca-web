#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from time import sleep
from catraca.util import Util
from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.turno_dao import TurnoDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(object):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    turno_dao = TurnoDAO()
    hora_atual = None
    hora_inicio = None
    hora_fim = None
    contador = 30
#     p1 = datetime.datetime.strptime('05:59:59','%H:%M:%S').time()
#     p2 = datetime.datetime.strptime('22:29:59','%H:%M:%S').time()
    
    def __init__(self):
        super(Relogio, self).__init__()
        self.__periodo_ativo = None
        self.__turno_ativo = None
        self.__catraca_local = None
        self.hora_atual = self.util.obtem_hora()

    @property
    def periodo(self):
        self.hora_atual = self.util.obtem_hora()
        self.__periodo_ativo = self.obtem_periodo()
        return self.__periodo_ativo
    
    @property
    def catraca(self):
        self.__catraca_local = self.turno_dao.obtem_catraca()
        return self.__catraca_local
        
    @property
    def turno(self):
        return self.__turno_ativo
 
    @turno.setter
    def turno(self, lista):
        self.__turno_ativo = lista

    def obtem_turno(self):
        self.contador += 1
#         if (self.hora_atual > self.p1) and (self.hora_atual < self.p2):
        if self.contador >= 30:
            print "passando... --> self.turno = self.turno_dao.obtem_turno() "
            #self.turno = self.turno_dao.obtem_turno()
            self.turno = self.turno_dao.obtem_turno(self.catraca, self.hora_atual)
            self.contador = 0
            if self.turno:
                self.hora_inicio = datetime.datetime.strptime(str(self.turno[1]),'%H:%M:%S').time()
                self.hora_fim = datetime.datetime.strptime(str(self.turno[2]),'%H:%M:%S').time()       
                return self.turno
            else:
                return None
#         else:
#             self.turno = None
#             return None

    def obtem_periodo(self):
        self.obtem_turno()
        if self.turno:
            if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):  
                print "turno ativo On "
                return True
            else:
                self.turno = None
                print "turno inativo Off "
                return False
        else:
#             if (self.hora_atual > self.p1) and (self.hora_atual < self.p2):
#                 print "ATENÇÃO: Nao existem Turnos cadastrados dentro do horario comercial para funcionamento da catraca!"
#             print "ATENÇÃO: Nao existem Turnos cadastrados para funcionamento da catraca!"
            return False
         