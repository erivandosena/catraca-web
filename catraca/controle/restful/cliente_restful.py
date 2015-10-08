#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import threading
import datetime
from time import sleep
from catraca.util import Util
from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.controle.restful.recursos_restful import RecursosRestful
from catraca.controle.recursos.turno_json import TurnoJson
from catraca.controle.recursos.catraca_json import CatracaJson

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ClienteRestful(threading.Thread):
    
    log = Logs()
    aviso = Aviso()
    util = Util()
    turno_dao = TurnoDAO()
    catraca_dao = CatracaDAO()
    recursos_restful = RecursosRestful()
    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    turno_atual = None
    
    __hora = None
    __data_hora = None
    
    intervalo_recursos = 0

    def __init__(self, intervalo=1):
        super(ClienteRestful, self).__init__()
        threading.Thread.__init__(self)
        self.name = 'Thread Cliente RESTFul'
        self.intervalo = intervalo
        thread = threading.Thread(group=None, target=self.processa, args=())
        thread.daemon = True # Daemonize thread
        #thread.start()
        print "%s. Rodando... " % self.name
        
    def run(self):
        self.processa()

    def processa(self):
        while True:
            self.hora_atual = self.hora_real
#             print self.hora_real
#             print self.data_hora_real

            #self.aviso.exibir_datahora(self.data_hora_real,0)
#             
#             print self.hora_atual
#             print self.hora_real
#             print self.hora_atual
# 
#             print self.turno_atual
#             print self.hora_atual
#             print self.hora_inicio
#             print self.hora_fim

#             if self.turno_atual is None:
#                 print "ler turno"
#                 self.turno_atual = self.obtem_turno_atual()
#             if not (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim))):
#                 self.intervalo_recursos = 60*60
#             else:
#                 self.intervalo_recursos = 10
#                 
#                    
#             while True:
#                 self.obtem_recursos(self.intervalo_recursos)
#                 print "verificando..."
#                 print self.hora_atual
#                 print self.hora_real
#                 if self.hora_atual != self.hora_real:
#                      
#                     if self.turno_atual is None:
#                         print "ler turno"
#                         self.turno_atual = self.obtem_turno_atual()
#                     if not (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim))):
#                         pass
#                     else:
#                         break
#    
#                 sleep(self.intervalo_recursos)
            sleep(self.intervalo)
            
    def obtem_recursos(self, intervalo_recursos):
        if intervalo_recursos == 10:
            print "dentro do horario de funcionamento"
            while True: 
                print "################################ TURNO EM FUNCIONAMENTO ################################"
                if self.obtem_turno_atual():
                    break
                sleep(self.intervalo)  
#             self.aviso.exibir_aguarda_cartao()
#             #self.util.emite_beep(250, .1, 3, 2) #0 seg.
#             self.recursos_restful.obtem_recursos()
#            print "########################### TURNO EM FUNCIONAMENTO ############################"
        elif intervalo_recursos == 60*60:
            print "fora do horario de atendimento"
            while True: 
                print "################################ FORA DE TURNO ################################"
                if self.obtem_turno_atual() is None:
                    break
                sleep(self.intervalo)  
#             self.aviso.exibir_aguarda_sincronizacao()
#             self.recursos_restful.obtem_recursos()
#             self.aviso.exibir_horario_invalido()
#           print "################################ FORA DE TURNO ################################"
            
    def obtem_catraca(self):
        catraca = self.catraca_dao.busca_por_ip(self.util.obtem_ip())
        if catraca is None:
            CatracaJson().catraca_get()
            catraca = self.obtem_catraca()
        return catraca
    
    def obtem_turno(self):
        return self.turno_dao.busca_por_catraca(self.obtem_catraca())
            
    def obtem_turno_atual(self):
        turnos = self.obtem_turno()
        if turnos is None:
            print " passou em turnos is None"
            TurnoJson().turno_get()
            turnos = self.obtem_turno()
        else:
            turnos.sort()
            print "passou em turnos.sort()"
            for turno in turnos:
                print "esta em for turno in turnos:"
                self.hora_atual = self.hora_real #self.util.obtem_hora()
                self.hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
                self.hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
                if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                    return turno
                          
    @property
    def hora_real(self):
        return self.__hora

    @hora_real.setter
    def hora_real(self, hora):
        self.__hora =  hora

    @property
    def data_hora_real(self):
        return self.__data_hora
    
    @data_hora_real.setter
    def data_hora_real(self, data_hora):
        self.__data_hora = data_hora