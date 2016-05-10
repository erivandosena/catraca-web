#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import threading
from time import sleep
from catraca.util import Util
from catraca.controle.restful.controle_generico import ControleGenerico
from catraca.modelo.dao.unidade_dao import UnidadeDAO
from catraca.modelo.dao.catraca_unidade_dao import CatracaUnidadeDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.unidade_turno_dao import UnidadeTurnoDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Relogio(ControleGenerico, threading.Thread):
    
    util = Util()
    catraca = None
    turno = None
    periodo = False
    contador = 4
    
#     unidade_dao = UnidadeDAO()
#     catraca_unidade_dao = CatracaUnidadeDAO()
#     turno_dao = TurnoDAO
#     unidade_turno_dao = UnidadeTurnoDAO()
#     custo_refeicao_dao = CustoRefeicaoDAO()

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        ControleGenerico.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Relogio'
        self.status = True
        self.rede = False
        self.catraca = self.recursos_restful.catraca_json.catraca_get()
        
    def run(self):
        print "%s. Rodando... " % self.name
        Relogio.catraca = self.catraca
        while True:
            self.hora_atul = self.util.obtem_hora()
            Relogio.hora = self.hora_atul
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
            if (self.hora == datetime.datetime.strptime('06:00:00','%H:%M:%S').time()) or (self.hora == datetime.datetime.strptime('12:00:00','%H:%M:%S').time()) or (self.hora == datetime.datetime.strptime('18:00:00','%H:%M:%S').time()):
                self.aviso.exibir_saldacao(self.aviso.saldacao(), self.util.obtem_datahora_display())
                #self.aviso.exibir_aguarda_cartao()
            self.contador += 1
            if self.contador == 10:
                self.contador = 0
                Relogio.catraca = self.obtem_catraca()
                if Relogio.catraca:
                    if not Relogio.catraca.operacao == 5 or not Relogio.catraca.operacao <= 0 or not Relogio.catraca.operacao >= 6:
                        Relogio.turno = self.obtem_turno()
            sleep(self.intervalo)
            
    def obtem_catraca(self):
        #remoto
        catraca = self.recursos_restful.catraca_json.catraca_get()
        if catraca is None:
            Relogio.rede = False
            if not self.turno:
                self.aviso.exibir_falha_rede()
            #local
            catraca = self.catraca_dao.busca_por_ip(self.util.obtem_ip_por_interface())
            if catraca is None:
                #catraca
                self.aviso.exibir_catraca_nao_cadastrada()
                self.recursos_restful.obtem_catraca(True, True, False)
                catraca = self.catraca_dao.busca_por_ip(self.util.obtem_ip_por_interface())
                if catraca:
                    return catraca
                else:
                    self.obtem_catraca()
            else:
                return self.obtem_dependencias_locais(catraca)
        else:
            Relogio.rede = True
            return self.obtem_dependencias_remotas(catraca)

    def obtem_dependencias_locais(self, catraca):
        #unidade
        if UnidadeDAO().busca() is None:
            self.aviso.exibir_unidade_nao_cadastrada()
        #catraca-unidade
        elif CatracaUnidadeDAO().busca() is None:
            self.aviso.exibir_catraca_unidade_nao_cadastrada()
        #turno
        elif TurnoDAO().busca() is None:
            self.aviso.exibir_turno_nao_cadastrado()
        #unidade-turno
        elif UnidadeTurnoDAO().busca() is None:
            self.aviso.exibir_unidade_turno_nao_cadastrada()
        #custo-refeicao
        elif CustoRefeicaoDAO().busca() is None:
            self.aviso.exibir_custo_refeicao_nao_cadastrado()
        else:
            return catraca
            
    def obtem_dependencias_remotas(self, catraca):
        #unidade
        if self.recursos_restful.unidade_json.unidade_get() is None:
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
        #custo-refeicao
        elif self.recursos_restful.custo_refeicao_json.custo_refeicao_get() is None:
            self.aviso.exibir_custo_refeicao_nao_cadastrado()
        else:
            return catraca
            
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
                    self.aviso.exibir_aguarda_cartao()
                    print "\nINICIO DE TURNO!\n"
                return turno_ativo
            else:
                # Finaliza turno
                if not self.status:
                    self.status = True
                    Relogio.periodo = False
                    self.aviso.exibir_horario_invalido()
                    self.util.beep_buzzer(855, .5, 1)
                    print "\nENCERRAMENTO DE TURNO!\n"
                return None
        else:
            return None
        