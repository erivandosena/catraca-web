#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import threading
from time import sleep
from decimal import Decimal
from catraca.util import Util
from catraca.controle.restful.controle_generico import ControleGenerico
from catraca.modelo.dao.unidade_dao import UnidadeDAO
from catraca.modelo.dao.catraca_unidade_dao import CatracaUnidadeDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.unidade_turno_dao import UnidadeTurnoDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.visao.interface.rede import Rede


from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson

from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.dao.cartao_dao import CartaoDAO



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
    lote_off = False

    def __init__(self, intervalo=1):
        super(Relogio, self).__init__()
        ControleGenerico.__init__(self)
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Relogio'
        self.status = True
        
    def run(self):
        print "%s Rodando... " % self.name
        self.catraca = self.catraca_dao.busca_por_nome(self.util.obtem_nome_rpi())
        while not self._stopevent.isSet():
            self.hora_atul = self.util.obtem_hora()
            Relogio.hora = self.hora_atul
            self.datahora = self.util.obtem_datahora().strftime("%d/%m/%Y %H:%M:%S")
            if (datetime.datetime.strptime(str(self.hora),'%H:%M:%S').time() == datetime.datetime.strptime('06:00:00','%H:%M:%S').time()) or (datetime.datetime.strptime(str(self.hora),'%H:%M:%S').time() == datetime.datetime.strptime('12:00:00','%H:%M:%S').time()) or (datetime.datetime.strptime(str(self.hora),'%H:%M:%S').time() == datetime.datetime.strptime('18:00:00','%H:%M:%S').time()):
                self.aviso.exibir_saldacao(self.aviso.saldacao(), self.util.obtem_datahora_display())
            self.contador += 1
            if self.contador == 10:
                self.contador = 0
                Relogio.catraca = self.obtem_catraca()
                if Relogio.catraca:
                    if not Relogio.catraca.operacao == 5 or not Relogio.catraca.operacao <= 0 or not Relogio.catraca.operacao >= 6:
                        Relogio.turno = self.obtem_turno()

            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
            
    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)
            
    def obtem_catraca(self):
        if Rede.status:
            
            print self.lote_off
            while self.lote_off:
                self.atualiza_remoto()
            else:
                catraca = Rede.interface_ativa[0]
                print "[ACESSO REMOTO] "+ str(catraca)
                return self.obtem_dependencias_remotas(catraca)
        else:
            #local
            self.lote_off = True
            catraca = self.catraca_dao.busca_por_nome(self.util.obtem_nome_rpi())
            print "[ACESSO LOCAL] "+ str(catraca)
            return self.obtem_dependencias_locais(catraca)

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
        if not self.obtendo_recurso:
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
        return catraca
            
    def obtem_turno(self):
        if self.catraca:
            if Rede.status:
                #remoto
                turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
            else:
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
        
    def atualiza_remoto(self):
        turnos = TurnoDAO().busca()
        if turnos:
            for turno in turnos:
                registros =  RegistroDAO().busca_por_periodo( str(self.util.obtem_data()) +" " + str(turno[3]) , str(self.util.obtem_data()) +" " + str(turno[1]))
                if registros:
                    for registro in registros:
                        #registro aqui
                        print "#registro aqui"
                        # insere registro remoto
                        if RegistroJson().objeto_json(registro) == 200:
                            print "Registro inserido no remoto com sucesso!"
                            cartao = CartaoDAO().busca(registro[4])
                            if cartao:
                                #cartao aqui
                                print "#cartao aqui"
                                saldo_creditos = cartao.creditos - cartao.tipo.valor
                                cartao.creditos = saldo_creditos
                                print CartaoDAO().atualiza_exclui(cartao, False).aviso
                                # atualiza cartao remoto
                                if CartaoJson().objeto_json(cartao) == 200:
                                    print "Cartao atualizado no remoto com sucesso!"
                                    print RegistroDAO().atualiza_exclui(registro, True).aviso
                                    self.lote_off = False
                                else:
                                    print "Erro ao atualizar cartao no remoto!"
                        else:
                            print "Erro ao inserir registro no remoto!"
                else:
                    print "Sem registos nos turnos."
                    self.lote_off = False
                    