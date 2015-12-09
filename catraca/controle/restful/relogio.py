#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from multiprocessing import Process
import datetime
from time import sleep
#from catraca.controle.restful.controle_api import ControleApi
from catraca.controle.restful.controle_generico import ControleGenerico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(ControleGenerico, threading.Thread):
    
    contador_status_recursos = 15
    contador = 0
    alarme = True
    turno_ativo = None
    catraca_ativa = None

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        
        ControleGenerico.__init__(self)

        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Relogio'
        self.__hora_atual = self.util.obtem_hora()
        
        self.__periodo_ativo = None
        self.__turno_ativo = None
        self.__catraca_local = None
        self.hora_atual = self.util.obtem_hora()
        self.datahora_atual = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
        
    @property
    def hora(self):
        return self.__hora_atual
     
    @hora.setter
    def hora(self, valor):
        self.__hora_atual = valor

    @property
    def periodo(self):
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

    def run(self):
        print "%s. Rodando... " % self.name
        self.aviso.exibir_datahora(self.util.obtem_datahora_display())
        self.aviso.exibir_aguarda_cartao()
        
        while True:
            self.hora = self.util.obtem_hora()
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")

            print self.hora

            if (str(self.hora) == "06:00:00") or (str(self.hora) == "12:00:00") or (str(self.hora) == "18:00:00"): # and self.turno is None:
                self.aviso.exibir_saldacao(self.aviso.saldacao())
                self.aviso.exibir_aguarda_cartao()

            self.contador += 1
            print self.contador
            
            Relogio.alarme = self.alarme

            if self.obtem_catraca():
                if self.contador == 5:
                    self.contador = 0;
                    self.obtem_periodo()
            
            #self.executa_controle_recursos()
            sleep(self.intervalo)
            
    def obtem_catraca(self):
        # verifica se existem CATRACA,TURNO,UNIDADE,CATRACA-UNIDADE,UNIDADE-TURNO, cadastrados
        if self.recursos_restful.catraca_json.catraca_get() is None:
            self.aviso.exibir_catraca_nao_cadastrada()
            self.recursos_restful.obtem_catraca(True, True, False)
            
        elif self.recursos_restful.unidade_json.unidade_get() is None:
            self.aviso.exibir_unidade_nao_cadastrada()
             
        elif self.recursos_restful.catraca_unidade_json.catraca_unidade_get() is None:
            self.aviso.exibir_catraca_unidade_nao_cadastrada()
             
        elif self.recursos_restful.turno_json.turno_get() is None:
            self.aviso.exibir_turno_nao_cadastrado()
             
        elif self.recursos_restful.unidade_turno_json.unidade_turno_get() is None:
            self.aviso.exibir_unidade_turno_nao_cadastrada()
            
        else:
            self.catraca = self.turno_dao.obtem_catraca()
            Relogio.catraca_ativa = self.catraca
            return self.catraca
        
    def obtem_turno(self):
        if self.obtem_catraca():
            #remoto
            turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
            if turno_ativo is None:
                #local
                print turno_ativo
                turno_ativo = self.turno_dao.obtem_turno(self.catraca, self.hora)
            if turno_ativo:
                self.hora_inicio = datetime.datetime.strptime(str(turno_ativo.inicio),'%H:%M:%S').time()
                self.hora_fim = datetime.datetime.strptime(str(turno_ativo.fim),'%H:%M:%S').time()
                self.turno = turno_ativo
                return self.turno
            else:
                return None
        else:
            return None
        
    def obtem_periodo(self):
            Relogio.turno_ativo = self.obtem_turno()
            if self.turno:
                # Inicia turno
                if self.alarme:
                    self.alarme = False
                    self.aviso.exibir_turno_atual(self.turno.descricao)
                    self.util.beep_buzzer(855, .5, 1)
                    print "Turno INICIADO!"
                    self.aviso.exibir_aguarda_cartao()
                if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                    return True
                else:
                    self.turno = None
                    return False
            else:
                # Finaliza turno
                if not self.alarme:
                    self.alarme = True
                    self.aviso.exibir_horario_invalido()
                    self.util.beep_buzzer(855, .5, 1)
                    print "Turno ENCERRADO!"
                    self.aviso.exibir_aguarda_cartao()
                return False

#     def executa_controle_recursos(self):
#         while True:
#             self.contador_status_recursos += 1
#             print self.contador_status_recursos
#             #print self.alarme 
#             
#             if not self.alarme:
#                 if self.contador_status_recursos >= 30:
#                     self.obtem_recurso_servidor(False, True, False)
#             else:
#                 if self.contador_status_recursos >= 1800:
#                     self.obtem_recurso_servidor(False, True, True)
#             break
#             
#     def obtem_recurso_servidor(self, display=False, mantem_tabela=False, limpa_tabela=False):
#         self.contador_status_recursos = 0
#         self.recursos_restful.obtem_recursos(display, mantem_tabela, limpa_tabela)
        