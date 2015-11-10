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
#     aviso = Aviso()
#     util = Util()
#     turno_dao = TurnoDAO()
#     catraca_dao = CatracaDAO()
    recursos_restful = RecursosRestful()
#     hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
#     hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
#     hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
#     turno_atual = None
    __periodo_ativo = None
    __turno_ativo = []
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
            if self.periodo:
                self.intervalo_recursos = 15
                self.obtem_recursos(self.intervalo_recursos)
            else:
                self.intervalo_recursos = 3600
                self.obtem_recursos(self.intervalo_recursos)

        sleep(self.intervalo)
            
    def obtem_recursos(self, intervalo_recursos):
        if intervalo_recursos == 15:
            print "dentro do horario de funcionamento"
            while True:
                if self.turno is None:
                    break
                print "##### obtendo RECURSOS ######"
                self.recursos_restful.obtem_recursos()
                sleep(self.intervalo_recursos)  
        elif intervalo_recursos == 3600:
            print "fora do horario de atendimento"
            while True: 
                if self.turno:
                    break
                print "##### obtendo RECURSOS ######"
                self.recursos_restful.obtem_recursos()
                sleep(self.intervalo_recursos)
                
    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora =  hora

    @property
    def datahora(self):
        return self.__data_hora
    
    @datahora.setter
    def datahora(self, data_hora):
        self.__data_hora = data_hora
        
    @property
    def periodo(self):
        return self.__periodo_ativo

    @periodo.setter
    def periodo(self, valor):
        self.__periodo_ativo = valor
        
    @property
    def turno(self):
        return self.__turno_ativo
 
    @turno.setter
    def turno(self, lista):
        self.__turno_ativo = lista
        