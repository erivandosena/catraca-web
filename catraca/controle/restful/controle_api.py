#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from catraca.controle.restful.controle_generico import ControleGenerico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleApi(ControleGenerico):
    
    contador = 0
    alarme = True
    
    def __init__(self):
        super(ControleApi, self).__init__()
        ControleGenerico.__init__(self)
        self.__periodo_ativo = None
        self.__turno_ativo = None
        self.__catraca_local = None
        self.hora_atual = self.util.obtem_hora()
        self.datahora_atual = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")

    @property
    def periodo(self):
        #self.periodo = self.obtem_periodo()
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
    
    @classmethod
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
    
#     def obtem_catraca(self):
#         # verifica se existem CATRACA,TURNO,UNIDADE,CATRACA-UNIDADE,UNIDADE-TURNO, cadastrados
#         if self.recursos_restful.catraca_json.catraca_get() is None:
#             self.aviso.exibir_catraca_nao_cadastrada()
#             self.recursos_restful.obtem_catraca(True, True, False)
#             
#         elif self.recursos_restful.unidade_json.unidade_get() is None:
#             self.aviso.exibir_unidade_nao_cadastrada()
#              
#         elif self.recursos_restful.catraca_unidade_json.catraca_unidade_get() is None:
#             self.aviso.exibir_catraca_unidade_nao_cadastrada()
#              
#         elif self.recursos_restful.turno_json.turno_get() is None:
#             self.aviso.exibir_turno_nao_cadastrado()
#              
#         elif self.recursos_restful.unidade_turno_json.unidade_turno_get() is None:
#             self.aviso.exibir_unidade_turno_nao_cadastrada()
#             
#         else:
#             self.catraca = self.turno_dao.obtem_catraca()
#             return self.catraca
#         
#     def obtem_turno(self):
#         if self.obtem_catraca():
#             global alarme
#             #remoto
#             turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
#             if turno_ativo is None:
#                 #local
#                 turno_ativo = self.turno_dao.obtem_turno(self.catraca, self.hora)
#             if turno_ativo:
#                 self.hora_inicio = datetime.datetime.strptime(str(turno_ativo.inicio),'%H:%M:%S').time()
#                 self.hora_fim = datetime.datetime.strptime(str(turno_ativo.fim),'%H:%M:%S').time()
#                 self.turno = turno_ativo
#                 return self.turno
#             else:
#                 return None
#         else:
#             return None
#         
#     def obtem_periodo(self):
#             self.obtem_turno()
#             print "passou"
#             print self.turno
#             if self.turno:
#                 # Inicia turno
#                 if self.alarme:
#                     self.alarme = False
#                     self.aviso.exibir_turno_atual(self.turno.descricao)
#                     self.util.beep_buzzer(855, .5, 1)
#                     print "Turno INICIADO!"
#                     self.aviso.exibir_aguarda_cartao()
#                 if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
#                     return True
#                 else:
#                     self.turno = None
#                     return False
#             else:
#                 # Finaliza turno
#                 if not self.alarme:
#                     self.alarme = True
#                     self.aviso.exibir_horario_invalido()
#                     self.util.beep_buzzer(855, .5, 1)
#                     print "Turno ENCERRADO!"
#                     self.aviso.exibir_aguarda_cartao()
#                 return False