#!/usr/bin/env python
# -*- coding: latin-1 -*-


import datetime
import threading
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.controle.api.rede import Rede
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.recursos.recursos_restful import RecursosRestful


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Sincronizador(threading.Thread):
    
    log = Logs()
    util = Util()
    recursos_restful = RecursosRestful()
    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    contador = 0
    status = True
    
    def __init__(self, intervalo=1):
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.__rede_interface = []
        self.__rede_status = False
        self.__catraca = None
        self.__turno = None
        self.__periodo = False
        self.__funcionamento = False
        self.__recursos = False
        self.__uso_do_cartao = False
        Sincronizador.hora = self.util.obtem_hora()
        Sincronizador.rede_interface = self.__rede_interface
        Sincronizador.rede_status = self.__rede_status
        Sincronizador.catraca = self.__catraca
        Sincronizador.turno = self.__turno
        Sincronizador.hora_inicio = self.hora_inicio
        Sincronizador.hora_fim = self.hora_fim
        Sincronizador.periodo = self.__periodo
        Sincronizador.funcionamento = self.__funcionamento
        Sincronizador.recursos = self.__recursos
        Sincronizador.uso_do_cartao = self.__uso_do_cartao
        self.name = 'Thread Atualizador.'
        
    @property
    def rede_status(self):
        return self.__rede_status
    
    @rede_status.setter
    def rede_status(self, valor):
        self.__rede_status = valor
        
    @property
    def rede_interface(self):
        return self.__rede_interface
    
    @rede_interface.setter
    def rede_interface(self, valor):
        self.__rede_interface = valor
        
    @property
    def catraca(self):
        return self.__catraca
    
    @catraca.setter
    def catraca(self, valor):
        self.__catraca = valor
        
    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, valor):
        self.__turno = valor
        
    @property
    def periodo(self):
        return self.__periodo
    
    @periodo.setter
    def periodo(self, valor):
        self.__periodo = valor
        
    @property
    def hora(self):
        return self.__hora_atual
    
    @hora.setter
    def hora(self, valor):
        self.__hora_atual = valor
    
    @property
    def datahora(self):
        return self.__datahora_atual
     
    @datahora.setter
    def datahora(self, valor):
        self.__datahora_atual = valor
        
    @property
    def funcionamento(self):
        return self.__funcionamento
     
    @funcionamento.setter
    def funcionamento(self, valor):
        self.__funcionamento = valor
        
    @property
    def recursos(self):
        return self.__recursos
     
    @recursos.setter
    def recursos(self, valor):
        self.__recursos = valor
        
    @property
    def uso_do_cartao(self):
        return self.__uso_do_cartao
     
    @uso_do_cartao.setter
    def uso_do_cartao(self, valor):
        self.__uso_do_cartao = valor
        
    def run(self):
        print "%s Rodando... " % self.name
        while True:    
            Sincronizador.hora = self.util.obtem_hora()
            Sincronizador.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
                
            self.obtem_atualizacao()

#             print "\nHora.........................................: " + str(Sincronizador.hora)
#             print "Rede Interface...............................: " + str(Sincronizador.rede_interface)
#             print "Rede Status..................................: " + str(Sincronizador.rede_status)
#             print "Catraca......................................: " + str(Sincronizador.catraca)
#             print "Turno........................................: " + str(Sincronizador.turno)
#             print "Perido(hora inicio)..........................: " + str(Sincronizador.hora_inicio)
#             print "Periodo(hora fim)............................: " + str(Sincronizador.hora_fim)
#             print "Periodo......................................: " + str(Sincronizador.periodo)
#             print "Funcionamento(online/offline)................: " + str(Sincronizador.funcionamento)
#             print "Recursos(obtendo)............................: " + str(Sincronizador.recursos)
#             print "Uso do cartao................................: " + str(Sincronizador.uso_do_cartao)
            
            sleep(self.intervalo)
        
    def obtem_atualizacao(self):
        try:
            Sincronizador.rede_status = Rede.status
            Sincronizador.rede_interface = Rede.interface_ativa
            self.contador += 1
            if self.contador == 5:
                self.contador = 0
                Sincronizador.catraca = self.obtem_catraca()
                if Sincronizador.catraca:
                    #if not Sincronizador.catraca.operacao == 5 or not Sincronizador.catraca.operacao <= 0 or not Sincronizador.catraca.operacao >= 6:
                    Sincronizador.turno = self.obtem_turno()
            Sincronizador.recursos = RecursosRestful.obtendo_recurso
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_catraca(self):
        try:
            catraca = Sincronizador.rede_interface[0] if Sincronizador.rede_interface else []
            if catraca:
                #remoto
                Sincronizador.funcionamento = True
                return catraca
            else:
                #local
                Sincronizador.funcionamento = False
                catraca = CatracaDAO().busca_por_nome(self.util.obtem_nome_rpi())
                Sincronizador.catraca = catraca
                return Sincronizador.catraca
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_turno(self):
        try:
            if Sincronizador.catraca:
                turno_ativo = None
                if Sincronizador.rede_status:
                    #remoto
                    turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
                else:
                    #local
                    turno_ativo = TurnoDAO().obtem_turno(Sincronizador.catraca, self.util.obtem_hora())
                if turno_ativo:
                    Sincronizador.hora_inicio = datetime.datetime.strptime(str(turno_ativo.inicio),'%H:%M:%S').time()
                    Sincronizador.hora_fim = datetime.datetime.strptime(str(turno_ativo.fim),'%H:%M:%S').time()
                    # Inicia turno
                    if self.status:
                        self.status = False
                        # codigo aqui sera exibido apenas uma vez
                        Sincronizador.periodo = True
                    return turno_ativo
                else:
                    # Finaliza turno
                    if not self.status:
                        self.status = True
                        # codigo aqui sera exibido apenas uma vez
                        Sincronizador.periodo = False
                    return turno_ativo
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            