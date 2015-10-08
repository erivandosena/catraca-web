#!/usr/bin/env python
# -*- coding: utf-8 -*-


import Queue
import threading
import datetime
from time import sleep
from catraca.util import Util
from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.restful.cliente_restful import ClienteRestful


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    turno_dao = TurnoDAO()
    catraca_dao = CatracaDAO()
    
    __periodo_ativo = None
    __hora_sistema = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    __datahora_display = datetime.datetime.now().strftime('%d/%B/%Y\n    %H:%M:%S')
    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    turno_ativo = None
    
    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        self.__hora_sistema = self.util.obtem_hora()
        self.__datahora_display = self.util.obtem_hora()
        threading.Thread.__init__(self)
        self.name = 'Thread Relogio'
        self.intervalo = intervalo
        
        self.queue = Queue.Queue()
        self.parent_thread = threading.current_thread() 
        self._stop = threading.Event()
        
        thread = threading.Thread(group=None, target=self.processa, args=())
        thread.daemon = True # Daemonize thread
        #thread.start()
        print "%s. Rodando... " % self.name
        
    def run(self):
        self.processa()
        
    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
        
    def processa(self):
        cliente_restful = ClienteRestful()
        cliente_restful.start()
        while True:
            #self.aviso.exibir_datahora(self.data_hora_display,0)  
            # atualiza variaveis com hora do sistema
            self.hora = self.util.obtem_hora()
            self.data_hora_display = self.util.obtem_datahora_display()
            # atualiza thread com hora atual
            cliente_restful.hora_real = self.hora
            #cliente_restful.data_hora_real = self.data_hora_display
            
            self.periodo = self.obtem_periodo()
            print self.periodo
            
            sleep(self.intervalo)
              
    @property
    def periodo(self):
        return self.__periodo_ativo

    @periodo.setter
    def periodo(self, valor):
        self.__periodo_ativo = valor
    
    @property
    def hora(self):
        return self.__hora_sistema

    @hora.setter
    def hora(self, hora):
        self.__hora_sistema = hora

    @property
    def data_hora_display(self):
        return self.__datahora_display
    
    @data_hora_display.setter
    def data_hora_display(self, datahora):
        self.__datahora_display = datahora
        
    def obtem_catraca(self):
        return self.catraca_dao.busca_por_ip(self.util.obtem_ip())
    
    def obtem_turno(self):
        self.turno_ativo = self.turno_dao.busca_por_catraca(self.obtem_catraca(), self.hora)
        print "nova consulta no turno!"
        if self.turno_ativo:
            self.hora_inicio = datetime.datetime.strptime(str(self.turno_ativo[1]),'%H:%M:%S').time()
            self.hora_fim = datetime.datetime.strptime(str(self.turno_ativo[2]),'%H:%M:%S').time()       
            print self.turno_ativo      
            return self.turno_ativo
        else:
            self.turno_ativo = None
            
    def obtem_periodo(self):
        self.hora_atual = self.hora
        if (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or (self.turno_ativo is None)):
            if self.turno_ativo:
                return True
            else:
                self.obtem_turno()
                return True
        else:
            return False
#                     if not (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim))):
#                         return False
#                     else:
#                         return True
                
#     def obtem_periodo(self):
#         if not (((self.hora >= self.hora_inicio) and (self.hora <= self.hora_fim)) or ((self.hora >= self.hora_inicio) and (self.hora <= self.hora_fim))):
#             return False
#         else:
#             return True