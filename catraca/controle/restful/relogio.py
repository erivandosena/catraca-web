#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import datetime
from time import sleep
from catraca.controle.restful.controle_api import ControleApi

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(ControleApi, threading.Thread):
    
    contador_status_recursos = 90

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        ControleApi.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Relogio'
        self.__hora_atual = self.util.obtem_hora()
        self.__data_atual = self.util.obtem_data_formatada()
        self.__data_hora_atual = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
        self.__status = False
        
    def run(self):
        print "%s. Rodando... " % self.name
        self.aviso.exibir_datahora(self.util.obtem_datahora_display())
        self.aviso.exibir_aguarda_cartao()
        while True:
            self.hora = self.util.obtem_hora()
            self.data = self.util.obtem_data_formatada()
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")

            print self.datahora

            self.obtem_status()
            self.obtem_atualizacao_de_turno()
            #print self.contador
            #print self.alarme

            if (str(self.hora) == "06:00:00") or (str(self.hora) == "12:00:00") or (str(self.hora) == "18:00:00") and self.turno is None:
                self.aviso.exibir_saldacao(self.saldacao())
                self.aviso.exibir_aguarda_cartao()
                
            self.executa_controle_recursos()
            
            sleep(self.intervalo)
            
    @property
    def hora(self):
        return self.__hora_atual
    
    @property
    def data(self):
        return self.__data_atual
    
    @property
    def datahora(self):
        return self.__data_hora_atual
    
    @property
    def status(self):
        return self.__status
    
    @hora.setter
    def hora(self, valor):
        self.__hora_atual = valor
    
    @data.setter
    def data(self, valor):
        self.__data_atual = valor
    
    @datahora.setter
    def datahora(self, valor):
        self.__data_hora_atual = valor
        
    @status.setter
    def status(self, valor):
        self.__status = valor
        
    def saldacao(self):
        hora = int(self.util.obtem_datahora().strftime('%H'))
        periodo = 0
        if (hora >= 0 and hora < 12):
            periodo = 1
        if (hora >= 12 and hora <= 17):
            periodo = 2
        if (hora >= 18 and hora <= 23):
            periodo = 3
        opcoes = {
                   1 : 'Ola'.center(16) +'\n'+ 'Bom Dia!'.center(16),
                   2 : 'Ola'.center(16) +'\n'+ 'Boa Tarde!'.center(16),
                   3 : 'Ola'.center(16) +'\n'+ 'Boa Noite!'.center(16),

        }
        return opcoes.get(periodo, "Ola!".center(16) +"\n"+ self.util.obtem_data_formatada().center(16))
    
    def obtem_status(self):
        self.status = self.periodo
        return self.status
    
    def executa_controle_recursos(self):
        while True:
            
            #print "status do relogio:-> " + str(self.status)

            #print self.contador_status_recursos
            self.contador_status_recursos += 1
            if self.turno:
                #print "self.contador_status_recursos > 120"
                if self.contador_status_recursos >= 120:
                    self.obtem_recurso_servidor()
            else:
                #print "self.contador_status_recursos >= 3600"
                if self.contador_status_recursos >= 1800:
                    self.obtem_recurso_servidor(False, True)
            break
            
    def obtem_recurso_servidor(self, display=False, limpa_tabela=False):
        self.contador_status_recursos = 0
        self.recursos_restful.obtem_recursos(display, limpa_tabela)
        
    def obtem_atualizacao_de_turno(self):
        if self.turno:
            # Inicia turno
            if self.alarme:
                self.alarme = False
                self.aviso.exibir_turno_atual(self.turno[3])
                #self.util.beep_buzzer(855, .5, 1)
                #print "Turno INICIADO!"
                self.aviso.exibir_aguarda_cartao()
        # Finaliza turno
        else:
            if not self.alarme:
                self.alarme = True
                self.aviso.exibir_horario_invalido()
                #self.util.beep_buzzer(855, .5, 1)
                #print "Turno ENCERRADO!"
                self.aviso.exibir_aguarda_cartao()
        