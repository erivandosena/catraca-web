#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import threading
from time import sleep
from decimal import Decimal
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.unidade_dao import UnidadeDAO
from catraca.modelo.dao.catraca_unidade_dao import CatracaUnidadeDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.unidade_turno_dao import UnidadeTurnoDAO
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.dao.custo_unidade_dao import CustoUnidadeDAO
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.tipo_dao import TipoDAO
from catraca.modelo.dao.usuario_dao import UsuarioDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.dao.mensagem_dao import MensagemDAO
from catraca.modelo.dao.registro_offline_dao import RegistroOfflineDAO
from catraca.controle.api.rede import Rede
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.controle.recursos.recursos_restful import RecursosRestful
from catraca.controle.api.sincronizador import Sincronizador


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Gerenciador(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    rede = Rede()
    catraca_dao = CatracaDAO()
    recursos_restful = RecursosRestful()
    mensagem_dao = MensagemDAO()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    catraca = None
    turno = None
    periodo = False
    lote_off = False
    status = True
    uso_do_cartao = False
    uso_irregular = False
    
    def __init__(self, intervalo=1):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Gerenciador'
        
    def run(self):
        print "%s Rodando... " % self.name
        if not self.rede.isAlive():
            self.rede = Rede()
            self.rede.start()
        while not self._stopevent.isSet():
            
            Sincronizador.uso_do_cartao = Gerenciador.uso_do_cartao
            Gerenciador.periodo = Sincronizador.periodo
            Gerenciador.catraca = self.obtem_catraca()
            Gerenciador.turno = self.obtem_turno(Sincronizador.turno)
            Gerenciador.periodo = Sincronizador.periodo
            Gerenciador.hora_inicio = Sincronizador.hora_inicio
            Gerenciador.hora_fim = Sincronizador.hora_fim
                     
            self.executa_controle_recursos()
             
            if (datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() == datetime.datetime.strptime('00:00:00','%H:%M:%S').time()) or (datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() == datetime.datetime.strptime('12:00:00','%H:%M:%S').time()) or (datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() == datetime.datetime.strptime('18:00:00','%H:%M:%S').time()):
                self.aviso.exibir_saldacao(self.aviso.saldacao(), self.util.obtem_datahora_display())
                        
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
        
    def obtem_catraca(self):
        try:
            if Sincronizador.rede_status or Sincronizador.funcionamento:
                #remoto
                while self.lote_off:
                    self.atualiza_remoto()
                else:
                    return Sincronizador.catraca
            else:
                #local
                self.lote_off = True
                return self.obtem_dependencias_locais(Sincronizador.catraca)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
        
    def obtem_dependencias_locais(self, catraca):
        try:
            print "PROCURA NO LOCAL"
            #if catraca is None or \
            if UnidadeDAO().busca() is None or \
            CatracaUnidadeDAO().busca() is None or \
            TurnoDAO().busca() is None or \
            UnidadeTurnoDAO().busca() is None or \
            CustoRefeicaoDAO().busca() is None or \
            CustoUnidadeDAO().busca() is None or \
            TipoDAO().busca() is None or \
            UsuarioDAO().busca() is None or \
            CartaoDAO().busca() is None:
            #VinculoDAO().busca() is None:
            #IsencaoDAO().busca() is None or \
            #MensagemDAO().busca() is None:
                return self.obtem_dependencias_remotas(catraca)
            else:
                return catraca
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_dependencias_remotas(self, catraca):
        print "PROCURA NO REMOTO"
        try:
#             #catraca
#             if self.recursos_restful.catraca_json.catraca_get() is None:
#                 self.aviso.exibir_catraca_nao_cadastrada()
            #unidade
            if self.recursos_restful.unidade_json.unidade_get() is None:
                self.aviso.exibir_unidade_nao_cadastrada()
                return catraca
            #catraca-unidade
            elif self.recursos_restful.catraca_unidade_json.catraca_unidade_get() is None:
                self.aviso.exibir_catraca_unidade_nao_cadastrada()
                return catraca
            #turno
            elif self.recursos_restful.turno_json.turno_get() is None:
                self.aviso.exibir_turno_nao_cadastrado()
                return catraca
            #unidade-turno
            elif self.recursos_restful.unidade_turno_json.unidade_turno_get() is None:
                self.aviso.exibir_unidade_turno_nao_cadastrada()
                return catraca
            #custo-refeicao
            elif self.recursos_restful.custo_refeicao_json.custo_refeicao_get() is None:
                self.aviso.exibir_custo_refeicao_nao_cadastrado()
                return catraca
            elif self.recursos_restful.custo_unidade_json.custo_unidade_get() is None:
                self.aviso.exibir_custo_unidade_nao_cadastrado()
                return catraca
            #tipo
            elif self.recursos_restful.tipo_json.tipo_get() is None:
                self.aviso.exibir_tipo_nao_cadastrada()
                return catraca
            #usuario
            elif self.recursos_restful.usuario_json.usuario_get() is None:
                self.aviso.exibir_usuario_nao_cadastrado()
                return catraca
            #cartao
            elif self.recursos_restful.cartao_json.cartao_get() is None:
                self.aviso.exibir_cartao_nao_cadastrada()
                return catraca
            
            return catraca
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def obtem_turno(self, turno):
        try:
            turno_ativo = turno
            if turno_ativo:
                # Inicia turno
                if self.status:
                    # codigo aqui sera exibido apenas uma vez
                    self.status = False

                    self.aviso.exibir_turno_atual(turno_ativo.descricao)
                    self.util.beep_buzzer(855, .5, 1)
                    
                    self.aviso.exibir_aguarda_cartao()
                    
                    print "\nINICIO DE TURNO!\n"
                        
                return turno
            else:
                
                if not Gerenciador.uso_do_cartao:
                    self.exibe_mensagem_catraca(self.verifica_status)
                
                # Finaliza turno
                if not self.status:
                    # codigo aqui sera exibido apenas uma vez
                    self.status = True
                    
                    RecursosRestful.obtendo_recurso = False
                    
                    self.aviso.exibir_horario_invalido()
                    self.util.beep_buzzer(855, .5, 1)
                    
                    print "\nENCERRAMENTO DE TURNO!\n"

                return turno
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def atualiza_remoto(self):
        try:
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
                                if Gerenciador.catraca.financeiro:
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
            else:
                print ">>> Sem turnos."
                self.lote_off = False
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def executa_controle_recursos(self):
        try:
            if Gerenciador.catraca:
                if (Gerenciador.catraca.operacao == 1) or (Gerenciador.catraca.operacao == 2) or (Gerenciador.catraca.operacao == 3) or (Gerenciador.catraca.operacao == 4):
                    #if Gerenciador.periodo:
                    self.recursos_restful.obtem_recursos(Gerenciador.periodo)
                    if not Gerenciador.periodo:
                        if Sincronizador.rede_status:
                            if not self.lote_off:
                                if (datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() >= datetime.datetime.strptime('00:00:00','%H:%M:%S').time()) and (datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() <= datetime.datetime.strptime('00:00:30','%H:%M:%S').time()):
                                    self.util.beep_buzzer(855, .5, 1)
                                    
                                    if self.rede.isAlive():
                                        self.rede._stopevent.set()
        
                                    sleep(10)
                                    
                                    self.aviso.exibir_aguarda_sincronizacao()
                                    
                                    # realiza limpeza das tabelas locais
                                    print "\nLimpando... tabela local CATRACA"
                                    self.recursos_restful.obtem_catraca(True, False, True)
                                    print "Concluido!\n"
                                    print "\nLimpando... tabela local UNIDADE"
                                    self.recursos_restful.obtem_unidade(True, False, True)
                                    print "Concluido!\n"
                                    print "\nLimpando... tabela local TURNO"
                                    self.recursos_restful.obtem_turno(True, False, True)
                                    print "Concluido!\n"
                                    print "\nLimpando... tabela local TIPO"
                                    self.recursos_restful.obtem_tipo(True, False, True)
                                    print "Concluido!\n"
                                    print "\nLimpando... tabela local USUARIO"
                                    self.recursos_restful.obtem_usuario(True, False, True)
                                    print "Concluido!\n"
                                    print "\nLimpando... tabela local CUSTO-REFEICAO"
                                    self.recursos_restful.obtem_custo_refeicao(True, False, True)
                                    print "Concluido!\n"
                                    
                                    sleep(10)
                                    
                                    if not self.rede.isAlive():
                                        self.rede = Rede()
                                        self.rede.start()
                                        
                                    sleep(10)
                                    self.recursos_restful.obtem_recursos()
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def verifica_status(self):
        if Sincronizador.periodo or Gerenciador.uso_do_cartao or Gerenciador.uso_irregular:
            return False
        else:
            return True
            
    def exibe_mensagem_catraca(self, verifica_status):
        try:
            #self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 0, False, False, True)
            if Sincronizador.catraca:
                mensagens = self.mensagem_dao.busca_por_catraca(Sincronizador.catraca.id)
                lista = []
                if mensagens is not None:
                    if mensagens.institucional1:
                        lista.insert(len(lista), mensagens.institucional1)
                        #self.aviso.exibir_mensagem_institucional_fixa(mensagens.institucional1[0:16], "", 0, False, False, True)
                    if mensagens.institucional2:
                        lista.insert(len(lista), mensagens.institucional2)
                        self.aviso.exibir_mensagem_institucional_scroll(mensagens.institucional1[0:16], mensagens.institucional2, verifica_status, 0.4)
                    if mensagens.institucional3:
                        lista.insert(len(lista), mensagens.institucional3)
                        #self.aviso.exibir_mensagem_institucional_fixa(mensagens.institucional3[0:16], "", 0, False, False, True)
                    if mensagens.institucional4:
                        lista.insert(len(lista), mensagens.institucional4)
                        self.aviso.exibir_mensagem_institucional_scroll(mensagens.institucional3[0:16], mensagens.institucional4, verifica_status, 0.4)
#                         for msg in lista[:len(lista)-1]:
#                             self.aviso.exibir_mensagem_institucional_scroll(msg, 0.4)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            