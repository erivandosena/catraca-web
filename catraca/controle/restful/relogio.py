#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from multiprocessing import Process
import datetime
from time import sleep
from catraca.controle.restful.controle_api import ControleApi

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(ControleApi, threading.Thread):
    
    contador_status_recursos = 15

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        ControleApi.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Relogio'
        self.__hora_atual = self.util.obtem_hora()
#         self.__data_atual = self.util.obtem_data_formatada()
#         self.__data_hora_atual = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
#         self.__status = False
#         thread = threading.Thread(group=None, target=self.run(), name=None, args=(), kwargs={})
#         thread.daemon = False
#         thread.start()

    @property
    def hora(self):
        return self.__hora_atual
     
    @hora.setter
    def hora(self, valor):
        self.__hora_atual = valor
#     
#     @property
#     def data(self):
#         return self.__data_atual
#     
#     @data.setter
#     def data(self, valor):
#         self.__data_atual = valor
#     
#     @property
#     def datahora(self):
#         return self.__data_hora_atual
#     
#     @datahora.setter
#     def datahora(self, valor):
#         self.__data_hora_atual = valor
    
#     @property
#     def status(self):
#         return self.__status
# 
#     @status.setter
#     def status(self, valor):
#         self.__status = valor
        
    def run(self):
        print "%s. Rodando... " % self.name
        self.aviso.exibir_datahora(self.util.obtem_datahora_display())
        self.aviso.exibir_aguarda_cartao()
        
        while True:
            self.hora = self.util.obtem_hora()
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
#             self.data = self.util.obtem_data_formatada()

            print self.hora

            if (str(self.hora) == "06:00:00") or (str(self.hora) == "12:00:00") or (str(self.hora) == "18:00:00"): # and self.turno is None:
                self.aviso.exibir_saldacao(self.aviso.saldacao())
                self.aviso.exibir_aguarda_cartao()
                
            #global contador
            self.contador += 1
            print self.contador
            
            if self.obtem_catraca():
                if self.contador == 5:
                    self.contador = 0;
                    self.periodo
                    #if self.periodo:
            #global turno_valido
            #self.turno_valido = self.turno
            
            #print ">>> relogio >> " + str(self.turno_valido)
            
            #print self.turno_valido
            
            #if self.contador == 5:
            #if self.obtem_status():
 
            self.executa_controle_recursos()
            
            sleep(self.intervalo)
            
#     def obtem_status(self):
#         self.status = self.periodo
#         return self.status
            
    def executa_controle_recursos(self):
        while True:
            self.contador_status_recursos += 1
            print self.contador_status_recursos
            if not self.alarme:
                if self.contador_status_recursos >= 30:
                    self.obtem_recurso_servidor(False, True, False)
            else:
                if self.contador_status_recursos >= 1800:
                    self.obtem_recurso_servidor(False, True, True)
            break
            
    def obtem_recurso_servidor(self, display=False, mantem_tabela=False, limpa_tabela=False):
        self.contador_status_recursos = 0
        self.recursos_restful.obtem_recursos(display, mantem_tabela, limpa_tabela)
        