#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
#from time import sleep
# from catraca.util import Util
# from catraca.logs import Logs
# from catraca.visao.interface.aviso import Aviso
# from catraca.modelo.dao.turno_dao import TurnoDAO
# from catraca.modelo.dao.catraca_dao import CatracaDAO
# from catraca.controle.restful.recursos_restful import RecursosRestful
from catraca.controle.restful.controle_generico import ControleGenerico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleApi(ControleGenerico):
    
    contador = 14
    alarme = True
    
    def __init__(self):
        super(ControleApi, self).__init__()
        ControleGenerico.__init__(self)
        self.__periodo_ativo = None
        self.__turno_ativo = None
        self.__catraca_local = None
        self.hora_atual = self.util.obtem_hora()

    @property
    def periodo(self):
        self.hora_atual = self.util.obtem_hora()
        self.__periodo_ativo = self.obtem_periodo()
        #print "obteve PERIODO"
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
        if self.contador >= 15:
            return self.obtem_turno_valido()
            
    def obtem_turno_valido(self):
        self.turno = self.turno_dao.obtem_turno(self.catraca, self.hora_atual)
        self.contador = 0
        if self.turno:
            self.hora_inicio = datetime.datetime.strptime(str(self.turno[1]),'%H:%M:%S').time()
            self.hora_fim = datetime.datetime.strptime(str(self.turno[2]),'%H:%M:%S').time()
            return self.turno
        else:
            self.alarme = True
            return None

    def obtem_periodo(self):
        # verifica se existe catraca cadastrada
        if self.catraca_dao.busca_por_ip(self.util.obtem_ip()) is None:
            self.aviso.exibir_catraca_nao_cadastrada()
            self.recursos_restful.obtem_recursos(True)
            self.aviso.exibir_aguarda_cartao()
        self.obtem_turno()
        if self.turno:
            if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                return True
            else:
                self.turno = None
                return False
        else:
            return False