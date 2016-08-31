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
from catraca.modelo.dao.custo_unidade_dao import CustoUnidadeDAO
from catraca.visao.interface.rede import Rede


from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson

from catraca.modelo.dao.registro_offline_dao import RegistroOfflineDAO
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
    rede = Rede()

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
        #Relogio.catraca = self.catraca_dao.busca_por_nome(self.util.obtem_nome_rpi())
        Relogio.catraca = self.obtem_catraca()
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
            #remoto
            print "print self.lote_off = " +str(self.lote_off)
            while self.lote_off:
                self.atualiza_remoto()
            else:
                catraca = Rede.interface_ativa[0]
                print "[ACESSO REMOTO] "+ str(catraca)
                return catraca
                #return self.obtem_dependencias_remotas(catraca)
        else:
            #local
            self.lote_off = True
            catraca = self.catraca_dao.busca_por_nome(self.util.obtem_nome_rpi())
            print "[ACESSO LOCAL] "+ str(catraca)
            return self.obtem_dependencias_locais(catraca)
        
    def obtem_dependencias_locais(self, catraca):
        if catraca is None or \
        UnidadeDAO().busca() is None or \
        CatracaUnidadeDAO().busca() is None or \
        TurnoDAO().busca() is None or \
        UnidadeTurnoDAO().busca() is None or \
        CustoRefeicaoDAO().busca() is None or \
        CustoUnidadeDAO().busca() is None or \
        TipoDAO().busca() is None or \
        CartaoDAO().busca() is None or \
        UsuarioDAO().busca() is None or \
        VinculoDAO().busca() is None or \
        IsencaoDAO().busca() is None or \
        MensagemDAO().busca() is None:
            return self.obtem_dependencias_remotas(catraca)
        else:
            return catraca
        
    def obtem_dependencias_remotas(self, catraca):
        print "not self.obtendo_recurso : " +str(not self.obtendo_recurso)
        if not self.obtendo_recurso:
            
            if self.rede.isAlive():
                self.rede.join()
            
            #catraca
            if self.recursos_restful.catraca_json.catraca_get() is None:
                self.aviso.exibir_catraca_nao_cadastrada()
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
            #custo-refeicao
            elif self.recursos_restful.custo_refeicao_json.custo_refeicao_get() is None:
                self.aviso.exibir_custo_refeicao_nao_cadastrado()
            #custo-unidade
            elif self.recursos_restful.custo_unidade_json.custo_unidade_get() is None:
                self.aviso.exibir_custo_unidade_nao_cadastrado()
#             else:
#                 return catraca

            if not self.rede.isAlive():
                self.rede = Rede()
                self.rede.start()

        return catraca
            
    def obtem_turno(self):
        if Relogio.catraca:
            if Rede.status:
                #remoto
                turno_ativo = self.recursos_restful.turno_json.turno_funcionamento_get()
            else:
                #local
                turno_ativo = self.turno_dao.obtem_turno(Relogio.catraca, self.hora)
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
                registro_dao = RegistroOfflineDAO()
                registros =  registro_dao.busca_por_periodo( str(self.util.obtem_data()) +" " + str(turno[3]) , str(self.util.obtem_data()) +" " + str(turno[1]))
                if registros:
                    registro = None
                    #registro_dao = RegistroOfflineDAO()
                    for item in registros:
                        registro = registro_dao.busca(item[4])
                        #registro aqui
                        print "#registro aqui"
                        # insere registro remoto
                        if RegistroJson().objeto_json(registro) == 200:
                            print ">>> Registro inserido no remoto com sucesso!"
                            if Relogio.catraca.financeiro:
                                cartao_dao = CartaoDAO()
                                cartao = cartao_dao.busca_cartao(item[0])
                                if cartao:
                                    #cartao aqui
                                    print "#cartao aqui"
                                    #saldo_creditos = cartao.creditos - cartao.valor
                                    cartao.creditos = (cartao.creditos - cartao.valor)
                                    if cartao_dao.atualiza_exclui(cartao, False):
                                        print cartao_dao.aviso
                                    # atualiza cartao remoto
                                    if CartaoJson().objeto_json(cartao) == 200:
                                        print ">>> Cartao atualizado no remoto com sucesso!"
                                        if registro_dao.atualiza_exclui(registro, True):
                                            print registro_dao.aviso
                                        #self.lote_off = False
                                    else:
                                        print ">>> Erro ao atualizar cartao no remoto!"
                            else:
                                print ">>> Financeiro não ativo, cartao sem atualização de credito!"
                                if registro_dao.atualiza_exclui(registro, True):
                                    print registro_dao.aviso
                                #self.lote_off = False
                        else:
                            print ">>> Erro ao inserir registro no remoto!"
                            #self.lote_off = True
                            
                    print ">>> Finalizou envio de registros e cartoes."
                    self.lote_off = False
                else:
                    print ">>> Sem registos nos turnos."
                    self.lote_off = False
                    