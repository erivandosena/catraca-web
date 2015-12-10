#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import threading
from time import sleep
#from catraca.controle.restful.controle_api import ControleApi
from catraca.controle.restful.controle_generico import ControleGenerico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(ControleGenerico, threading.Thread):
    
    catraca = None
    turno = None
    periodo = False
    contador = 4

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        ControleGenerico.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Relogio'
        self.status = True
        
    def run(self):
        print "%s. Rodando... " % self.name
        self.aviso.exibir_datahora(self.util.obtem_datahora_display())
        self.aviso.exibir_aguarda_cartao()
        
        while True:
            self.hora_atul = self.util.obtem_hora()
            self.hora = self.hora_atul
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")

            print self.datahora
            
            if (str(self.hora) == "06:00:00") or (str(self.hora) == "12:00:00") or (str(self.hora) == "18:00:00"):
                self.aviso.exibir_saldacao(self.aviso.saldacao())
                self.aviso.exibir_aguarda_cartao()
                
            self.contador += 1
            if self.contador == 5:
                self.contador = 0
                Relogio.catraca = self.obtem_catraca()
                Relogio.turno = self.obtem_turno()
                self.aviso.exibir_aguarda_cartao()
                
            print "periodo --------<RELOGIO>------ "+str(Relogio.periodo)
            sleep(self.intervalo)
            
    def obtem_catraca(self):
        #catraca
        if self.recursos_restful.catraca_json.catraca_get() is None:
            self.aviso.exibir_catraca_nao_cadastrada()
            self.recursos_restful.obtem_catraca(True, True, False)
        #unidade
        elif self.recursos_restful.unidade_json.unidade_get() is None:
            self.aviso.exibir_unidade_nao_cadastrada()
        #catraca-unidade
        elif self.recursos_restful.catraca_unidade_json.catraca_unidade_get() is None:
            self.aviso.exibir_catraca_unidade_nao_cadastrada()
        #turno
        elif self.recursos_restful.turno_json.turno_get() is None:
            self.aviso.exibir_turno_nao_cadastrado()
        #unidade-turno
        elif self.recursos_restful.unidade_turno_json.unidade_turno_get() is None:
            self.aviso.exibir_unidade_turno_nao_cadastrada()
        else:
            return self.turno_dao.obtem_catraca()
        
    def obtem_turno(self):
        if self.catraca:
            #remoto
            turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
            if turno_ativo is None:
                #local
                turno_ativo = self.turno_dao.obtem_turno(self.catraca, self.hora)
            if turno_ativo:
                Relogio.hora_inicio = datetime.datetime.strptime(str(turno_ativo.inicio),'%H:%M:%S').time()
                Relogio.hora_fim = datetime.datetime.strptime(str(turno_ativo.fim),'%H:%M:%S').time()
                # Inicia turno
                if self.status:
                    self.status = False
                    Relogio.periodo = True
                    self.aviso.exibir_turno_atual(turno_ativo.descricao)
                    self.util.beep_buzzer(855, .5, 1)
                    print "Turno >> INICIADO!"
#                 if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
#                     Relogio.periodo = True
#                 else:
#                     Relogio.periodo = False
                return turno_ativo
            else:
                # Finaliza turno
                if not self.status:
                    self.status = True
                    Relogio.periodo = False
                    self.aviso.exibir_horario_invalido()
                    self.util.beep_buzzer(855, .5, 1)
                    print "Turno >> FINALIZADO!"
                return None
        else:
            return None
        