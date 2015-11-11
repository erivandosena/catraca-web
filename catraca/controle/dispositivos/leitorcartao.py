#!/usr/bin/env python
# -*- coding: utf-8 -*-

<<<<<<< HEAD
import csv
import locale
=======

import os
import time
import socket
import locale
import calendar
>>>>>>> remotes/origin/web_backend
import datetime
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide
from catraca.controle.dispositivos.pictograma import Pictograma
from catraca.controle.dispositivos.sensoroptico import SensorOptico
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.giro_dao import GiroDAO
from catraca.modelo.dao.registro_dao import RegistroDAO
<<<<<<< HEAD
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.entidades.registro_off import RegistroOff
from catraca.modelo.entidades.giro import Giro
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.controle.restful.recursos_restful import RecursosRestful
=======
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.entidades.giro import Giro
>>>>>>> remotes/origin/web_backend


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(object):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    log = Logs()
    util = Util()
    aviso = Aviso()
<<<<<<< HEAD
    rpi = PinoControle()
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    giro = Giro()
    cartao = Cartao()
    registro = Registro()
    giro_dao = GiroDAO()
    turno_dao = TurnoDAO()
    cartao_dao = CartaoDAO()
    catraca_dao = CatracaDAO()
    registro_dao = RegistroDAO()
    custo_refeicao_dado = CustoRefeicaoDAO()
    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    bits = '' #11101110000100010000010011101110
    numero_cartao = 0
    giro = []
    turno = []
    cartoes = []
    TURNO = []
    CARTAO = []
    CATRACA = None
    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    
    def __init__(self):
        super(LeitorCartao, self).__init__()
        self.aviso.exibir_aguarda_sincronizacao()
        #self.obtem_recursos_do_servidor()
        #self.obtem_catraca()
        #self.obtem_turno()
=======
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    
    rpi = PinoControle()
    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    
    bits = '' #11101110000100010000010011101110
    
    numero_cartao = 0

    cartao = Cartao()
    registro = Registro()
    
    cartao_dao = CartaoDAO()
    catraca_dao = CatracaDAO()
    turno_dao = TurnoDAO()
    registro_dao = RegistroDAO()
    giro_dao = GiroDAO()
    
    catraca = None
    cartao_ativo = None
    turno_atual = None
    
    turno = []
    cartoes = []
    giro = []
    
    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()

    def __init__(self):
        super(LeitorCartao, self).__init__()
        
        self.aviso.exibir_aguarda_sincronizacao()
        self.verifica_turnos()
        self.cartoes = self.verifica_cartoes()
        self.giro = self.giro_dao.busca(self.catraca.id)
>>>>>>> remotes/origin/web_backend
        self.aviso.exibir_aguarda_cartao()
    
    def zero(self, obj):
        self.bits = self.bits + '0'
    
    def um(self, obj):
        self.bits = self.bits + '1'
        
    def ler(self):
        try:            
            self.rpi.evento_falling(self.D0, self.zero)
            self.rpi.evento_falling(self.D1, self.um)
            while True:
                sleep(1)
                #self.bits = '11101110000100010000010011101110'
                if len(self.bits) == 32:
                    self.util.beep_buzzer(860, .1, 1)
                    self.aviso.exibir_aguarda_consulta()
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
                    self.numero_cartao = int(str(self.bits), 2)
                    self.bits = ''
<<<<<<< HEAD
                    csv = self.obtem_csv(self.numero_cartao)
                    if csv == "Reiniciar Catraca":
                        self.util.reinicia_raspberrypi()
                    if csv == "Desligar Catraca":
                        self.util.desliga_raspberrypi()
=======
>>>>>>> remotes/origin/web_backend
                    self.valida_cartao(self.numero_cartao)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.util.emite_beep(250, .1, 3, 0) #0 seg.
                    self.log.logger.error('Erro obtendo binario: '+str(self.bits))
                    self.numero_cartao = 0
                    self.bits = ''
                    self.aviso.exibir_erro_leitura_cartao()
                    self.aviso.exibir_aguarda_cartao()
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception, e:
            self.log.logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            self.bits = ''
            self.numero_cartao = 0
<<<<<<< HEAD

    def valida_cartao(self, id_cartao):
        self.hora_atual = self.util.obtem_hora()
=======
            self.aviso.exibir_aguarda_cartao()

    def valida_cartao(self, id_cartao):
        #self.aviso.exibir_aguarda_liberacao()
        self.hora_atual = self.obtem_hora()
>>>>>>> remotes/origin/web_backend
        try:
            ##############################################################
            ## VERIFICA SE HOUVE ATUALIZACAO NOS CARTOES DURANTE O TURNO
            ##############################################################
            self.cartoes = self.verifica_cartoes()
            """
            -> VERIFICACAO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
            if not self.dias_uteis():
                self.aviso.exibir_dia_invalido()
                self.aviso.exibir_acesso_bloqueado()
                return None
            """
            ##############################################################
            ## VERIFICA O HORARIO PARA FUNCIONAMENTO DO TURNO
            ##############################################################
            if not (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim))):
<<<<<<< HEAD
=======
                #self.util.beep_buzzer(750, .1, 2)
>>>>>>> remotes/origin/web_backend
                self.aviso.exibir_horario_invalido()
                self.util.emite_beep(250, .1, 3, 0) #0 seg.
                self.aviso.exibir_acesso_bloqueado()
                self.log.logger.info('Cartao apresentado fora do horario de atendimento ID:'+ str(id_cartao))
                ##############################################################
                ## VERIFICA ATUALIZACOES NO TURNO DE FUNCIONAMENTO
                ##############################################################
<<<<<<< HEAD
                self.obtem_catraca()
                self.obtem_turno()
=======
                self.verifica_turnos()
>>>>>>> remotes/origin/web_backend
                return None
            ##############################################################
            ## VERIFICA SE EXISTE TURNO NO HORARIO DE FUNCIONAMENTO
            ##############################################################            
            elif ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                pass
#             if not ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or self.turno_atual is None:
#                 self.aviso.exibir_turno_invalido()
#                 self.aviso.exibir_acesso_bloqueado()
#                 self.log.logger.info('Nao existe turno cadastrado para o horario.')
#                 return None
            ##############################################################
            ## VERIFICA SE O ID DO CARTAO E DIFERENTE DE 10 CARACTERES
            ##############################################################
            if (len(str(id_cartao)) <> 10):
                self.util.emite_beep(250, .1, 3, 0) #0 seg.
                self.aviso.exibir_erro_leitura_cartao()
                self.aviso.exibir_aguarda_cartao()
                self.log.logger.info('Cartao com ID incorreto:'+ str(id_cartao))
                return None
            ##############################################################
            ## VERIFICA SE O ID DO CARTAO POSSUI EXATOS 10 CARACTERES
            ##############################################################
            if (len(str(id_cartao)) == 10):
                ##############################################################
                ## CONSULTA SE O CARTAO ESTA CADASTRADO NO BANCO DE DADOS
                ##############################################################
<<<<<<< HEAD
                self.CARTAO = self.obtem_cartao(id_cartao)
                if self.CARTAO is []:
=======
                self.cartao_ativo = self.pesquisa_id(self.cartoes, id_cartao)
                if self.cartao_ativo is None:
>>>>>>> remotes/origin/web_backend
                    self.util.emite_beep(250, .1, 3, 0) #0 seg.
                    self.aviso.exibir_cartao_nao_cadastrado()
                    self.aviso.exibir_aguarda_cartao()
                    self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                    return None
                else:
                    ##############################################################
                    ## OBTEM AS INFORMACOES DO CARTAO CONSULTADO NO BANCO DE DADOS
                    ##############################################################
<<<<<<< HEAD
                    cartao_id = self.CARTAO[0]
                    cartao_numero = self.CARTAO[1]
                    cartao_total_creditos = self.CARTAO[2]
                    cartao_valor_tipo = self.CARTAO[3]
                    cartao_limite_utilizacao = self.CARTAO[4]
                    cartao_id_tipo = self.CARTAO[5]
                    #hora_ultimo_acesso = datetime.datetime.strptime(self.cartao_ativo[3].strftime('%H:%M:%S'),'%H:%M:%S').time()
                    #tipo = self.cartao_ativo[4]
                    
                    
#                     datasis = self.obtem_datahora()
#                     data_atual = datetime.datetime(
#                         day=datasis.day,
#                         month=datasis.month,
#                         year=datasis.year, 
#                     ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
#                     
#                     databd = datetime.datetime.strptime(self.cartao_ativo[3].strftime('%H:%M:%S'),'%H:%M:%S')
#                     data_ultimo_acesso = datetime.datetime(
#                         day=databd.day,
#                         month=databd.month,
#                         year=databd.year, 
#                     ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')
=======
                    creditos = self.cartao_ativo[2]
                    hora_ultimo_acesso = datetime.datetime.strptime(self.cartao_ativo[3].strftime('%H:%M:%S'),'%H:%M:%S').time()
                    tipo = self.cartao_ativo[4]
                    
                    datasis = self.obtem_datahora()
                    data_atual = datetime.datetime(
                        day=datasis.day,
                        month=datasis.month,
                        year=datasis.year, 
                    ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
                    
                    databd = datetime.datetime.strptime(self.cartao_ativo[3].strftime('%H:%M:%S'),'%H:%M:%S')
                    data_ultimo_acesso = datetime.datetime(
                        day=databd.day,
                        month=databd.month,
                        year=databd.year, 
                    ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')
>>>>>>> remotes/origin/web_backend
                    """
                    -> VERIFICACAO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
                    if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
                        if ((hora_ultimo_acesso >= p1_hora_inicio) and (hora_ultimo_acesso <= p1_hora_fim) and (data_ultimo_acesso == data_atual)):
                            self.aviso.exibir_cartao_utilizado()
                            self.aviso.exibir_acesso_bloqueado()
                            return None
                    """
                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                    ##############################################################
<<<<<<< HEAD
                    if (float(cartao_total_creditos) < float(cartao_valor_tipo)):
                        self.aviso.exibir_cartao_sem_saldo()
                        self.util.emite_beep(250, .1, 3, 0) #0 seg.
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Cartao sem credito ID:'+ str(cartao_numero))
                        return None
                    ##############################################################
                    ## VERIFICA O LIMITE PERMITIDO DE USO DO CARTAO DURANTE TURNO
                    ##############################################################
                    elif int(self.registro_dao.busca_utilizacao(str(self.util.obtem_data()) + " " + str(self.hora_inicio), str(self.util.obtem_data()) + " " + str(self.hora_fim), cartao_id)[0]) > int(cartao_limite_utilizacao):
                        print self.registro_dao.busca_utilizacao(str(self.util.obtem_data()) + " " + str(self.hora_inicio), str(self.util.obtem_data()) + " " + str(self.hora_fim), cartao_id)[0]
                        print self.util.obtem_data() + " " + str(self.hora_inicio)
                        print self.util.obtem_data() + " " + str(self.hora_fim)
                        #self.aviso.exibir_cartao_sem_saldo()
                        self.util.emite_beep(250, .1, 3, 0) #0 seg.
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Limite de uso por turno ID:'+ str(cartao_numero))
=======
                    if (creditos == 0):
                        self.aviso.exibir_cartao_sem_saldo()
                        self.util.emite_beep(250, .1, 3, 0) #0 seg.
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Cartao sem credito ID:'+ str(id_cartao))
>>>>>>> remotes/origin/web_backend
                        return None
                    else:
                        """
                        -> VERIFICACAO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
                        ##############################################################
                        ## EXIBE O SALDO DOS CREDITOS PARA O UTILIZADOR DO CARTAO
                        ##############################################################
                        saldo = str(locale.currency(cartao.perfil.tipo.valor*creditos)).replace(".",",")
                        self.aviso.exibir_cartao_valido(tipo, saldo)
                        self.log.logger.info('Saldo atual do cartao ID:'+ str(id_cartao) + ' - ' + saldo)
                        """
<<<<<<< HEAD
                        self.aviso.exibir_cartao_valido("  R$ "+str(float(cartao_total_creditos))+"")
                        ##############################################################
                        ## INICIA A OPERACAO DE DECREMENTO DE CREDITO DO CARTAO
                        ##############################################################
                        ##############################################################
                        ## VERIFICA SE O CARTAO POSSUI ISENCAO DE PAGAMENTO
                        ##############################################################
                        saldo_creditos = 0.00
                        if self.cartao_dao.busca_isencao():
                            self.log.logger.info('Cartao isento ID:'+ str(cartao_numero))
                            saldo_creditos = float(cartao_total_creditos)
                        else:
                            saldo_creditos = float(cartao_total_creditos) - float(cartao_valor_tipo)
                        self.cartao.numero = cartao_numero
                        self.cartao.creditos = saldo_creditos
                        self.cartao.tipo = cartao_id_tipo
                        #self.cartao.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
=======
                        self.aviso.exibir_cartao_valido("  R$ <TESTE>")
                        ##############################################################
                        ## INICIA A OPERACAO DE DECREMENTO DE CREDITO DO CARTAO
                        ##############################################################
                        self.cartao = self.obtem_cartao(id_cartao)
                        saldo_creditos = creditos - 1
                        self.cartao.creditos = saldo_creditos
                        self.cartao.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        if not self.cartao_dao.mantem(self.cartao,False):
                            self.log.logger.error('[Cartao] ' + self.cartao_dao.aviso)
                            raise Exception('Erro atualizando valores no cartao.')
                        else:
                            self.log.logger.info("[Cartao] " + self.cartao_dao.aviso)
>>>>>>> remotes/origin/web_backend
                        self.aviso.exibir_aguarda_liberacao()
                        ##############################################################
                        ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        self.desbroqueia_acesso()
                        ##############################################################
                        ## AGUARDA UTILIZADOR PASSAR NA CATRACA E REALIZAR O GIRO
                        ##############################################################
                        while True:
#                             print self.sensor_optico.registra_giro(self.catraca.tempo, self.catraca)
#                             print "%.2f" % round(self.sensor_optico.tempo_decorrido, 2)
#                             break
                            print self.sensor_optico.finaliza_giro
<<<<<<< HEAD
                            if self.sensor_optico.registra_giro(self.CATRACA.tempo, self.CATRACA):                                
                                self.log.logger.info('Utilizador REALIZOU GIRO na catraca.')
#                                 ############################################################
#                                  EFETIVA A OPERACAO DE DECREMENTO DE CREDITO DO CARTAO
#                                 ############################################################
                                ##############################################################
                                ## ENVIA ATUALIZACAO DE CREDITO DO CARTAO PARA O SERVIDOR REST
                                ##############################################################
                                if not CartaoJson().objeto_json(self.cartao):
                                    if not self.cartao_dao.mantem_cartao_off(self.cartao,False):
                                        self.log.logger.error('[Cartao Off] ' + self.cartao_dao.aviso)
                                        #raise Exception('Erro atualizando valores no cartao off.')
                                    else:
                                        self.log.logger.info("[Cartao Off] " + self.cartao_dao.aviso)
#                                 if self.cartao_dao.conexao_status():
#                                     self.cartao_dao.commit() # se girou, persiste no banco de dados.
#                                     self.log.logger.info('Cartao com alteracao comitada com sucesso.')
                                ##############################################################
                                ## REGISTRA INFORMACOES DA OPERACAO REALIZADA COM EXITO
                                ##############################################################
                                ##############################################################
                                ## ENVIA REGISTRO DE USO DO CARTAO PARA O SERVIDOR REST
                                ##############################################################
                                self.registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                self.registro.pago = cartao_valor_tipo
                                self.registro.custo = self.custo_refeicao_dado.busca().valor
                                self.registro.cartao = CartaoDAO().busca(cartao_id)
                                self.registro.turno = TurnoDAO().busca(TURNO[0])
                                self.registro.catraca = self.CATRACA
                                if not RegistroJson().objeto_json(self.registro):
                                    if not self.registro_dao.mantem_registro_off(self.registro,False):
                                        self.log.logger.error('[Registro Off] ' + self.registro_dao.aviso)
                                        #raise Exception('Erro atualizando valores no registro off.')
                                    else:
                                        self.log.logger.info("[Registro Off] " + self.registro_dao.aviso)
#                                 if self.turno_atual is not None:
#                                     self.registro.data = self.cartao.data
#                                     self.registro.giro = 1
#                                     self.registro.valor = self.cartao.perfil.tipo.valor
#                                     self.registro.cartao = self.cartao
#                                     self.registro.turno = self.turno_atual
#                                     if not self.registro_dao.mantem(self.registro,False):
#                                         self.log.logger.error('[Registro] ' + self.registro_dao.aviso)
#                                         #raise Exception('Erro inserindo valores no registro.')
#                                     else:
#                                         self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
                                ##############################################################
                                ## REGISTRA INFORMACOES DE GIRO REALIZADO NA CATRACA
                                ##############################################################   
                                ##############################################################
                                ## ENVIA REGISTRO DE GIRO DA CATRACA PARA O SERVIDOR REST
                                ##############################################################
                                self.giro.horario = 1 if self.CATRACA.operacao == 1 else 0
                                self.giro.antihorario = 1 if self.CATRACA.operacao == 2 else 0
                                self.giro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                self.giro.catraca = self.CATRACA
                                if not RegistroJson().objeto_json(self.registro):
                                    if not self.registro_dao.mantem_registro_off(self.registro,False):
                                        self.log.logger.error('[Giro Off] ' + self.registro_dao.aviso)
                                        #raise Exception('Erro atualizando valores no giro off.')
                                    else:
                                        self.log.logger.info("[Giro Off] " + self.registro_dao.aviso)                 
#                                 giro.horario = 1 if self.catraca.operacao == 1 else 0
#                                 giro.antihorario = 1 if self.catraca.operacao == 2 else 0
#                                 giro.tempo = "%.1f" % round(self.sensor_optico.tempo_decorrido, 2) #self.sensor_optico.tempo_decorrido
#                                 giro.data = self.cartao.data
#                                 giro.catraca = self.catraca
#                                 if not self.giro_dao.mantem(giro,False):
#                                     self.log.logger.error('[Giro] ' + self.giro_dao.aviso)
#                                     raise Exception('Erro inserindo valores no giro.')
#                                 else:
#                                     self.log.logger.info('[Giro] ' + self.giro_dao.aviso)
                                break
                            else:
                                self.log.logger.info('Utilizador NAO realizou GIRO na catraca.')
                                self.cartao = None
                                self.registro = None
                                self.giro = None
                                ##############################################################
                                ## NAO CONFIRMA OPERACAO DE DECREMENTO DE CREDITO NO CARTAO
                                ##############################################################
#                                 if self.cartao_dao.conexao_status():
#                                     self.cartao_dao.rollback()
#                                     self.log.logger.info("Alteracao no cartao cancelada! (rollback)")
                                ##############################################################
                                ## REGISTRA INFORMACOES DA OPERACAO REALIZADA SEM EXITO
                                ##############################################################
#                                 if self.turno_atual is not None:
#                                     self.registro.data = self.cartao.data
#                                     self.registro.giro = 0
#                                     self.registro.valor = 0.00
#                                     self.registro.cartao = self.cartao
#                                     self.registro.turno = self.turno_atual
#                                     if not self.registro_dao.mantem(self.registro,False):
#                                         self.log.logger.error('[Registro] ' + self.registro_dao.aviso)
#                                         #raise Exception('Erro inserindo valores no registro.')
#                                     else:
#                                         self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
=======
                            if self.sensor_optico.registra_giro(self.catraca.tempo, self.catraca):                                
                                self.log.logger.info('Utilizador REALIZOU GIRO na catraca.')
                                ##############################################################
                                ## EFETIVA A OPERACAO DE DECREMENTO DE CREDITO DO CARTAO
                                ##############################################################
                                if self.cartao_dao.conexao_status():
                                    self.cartao_dao.commit() # se girou, persiste no banco de dados.
                                    self.log.logger.info('Cartao com alteracao comitada com sucesso.')
                                ##############################################################
                                ## REGISTRA INFORMACOES DA OPERACAO REALIZADA COM EXITO
                                ##############################################################
                                if self.turno_atual is not None:
                                    self.registro.data = self.cartao.data
                                    self.registro.giro = 1
                                    self.registro.valor = self.cartao.perfil.tipo.valor
                                    self.registro.cartao = self.cartao
                                    self.registro.turno = self.turno_atual
                                    if not self.registro_dao.mantem(self.registro,False):
                                        self.log.logger.error('[Registro] ' + self.registro_dao.aviso)
                                        #raise Exception('Erro inserindo valores no registro.')
                                    else:
                                        self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
                                ##############################################################
                                ## REGISTRA INFORMACOES DE GIRO REALIZADO NA CATRACA
                                ##############################################################                                
                                giro = Giro()
                                giro.horario = 1 if self.catraca.operacao == 1 else 0
                                giro.antihorario = 1 if self.catraca.operacao == 2 else 0
                                giro.tempo = "%.1f" % round(self.sensor_optico.tempo_decorrido, 2) #self.sensor_optico.tempo_decorrido
                                giro.data = self.cartao.data
                                giro.catraca = self.catraca
                                if not self.giro_dao.mantem(giro,False):
                                    self.log.logger.error('[Giro] ' + self.giro_dao.aviso)
                                    raise Exception('Erro inserindo valores no giro.')
                                else:
                                    self.log.logger.info('[Giro] ' + self.giro_dao.aviso)
                                break
                            else:
                                self.log.logger.info('Utilizador NAO realizou GIRO na catraca.')
                                ##############################################################
                                ## NAO CONFIRMA OPERACAO DE DECREMENTO DE CREDITO NO CARTAO
                                ##############################################################
                                if self.cartao_dao.conexao_status():
                                    self.cartao_dao.rollback()
                                    self.log.logger.info("Alteracao no cartao cancelada! (rollback)")
                                ##############################################################
                                ## REGISTRA INFORMACOES DA OPERACAO REALIZADA SEM EXITO
                                ##############################################################
                                if self.turno_atual is not None:
                                    self.registro.data = self.cartao.data
                                    self.registro.giro = 0
                                    self.registro.valor = 0.00
                                    self.registro.cartao = self.cartao
                                    self.registro.turno = self.turno_atual
                                    if not self.registro_dao.mantem(self.registro,False):
                                        self.log.logger.error('[Registro] ' + self.registro_dao.aviso)
                                        #raise Exception('Erro inserindo valores no registro.')
                                    else:
                                        self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
>>>>>>> remotes/origin/web_backend
                                break
                            print self.sensor_optico.finaliza_giro
                        ##############################################################
                        ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        self.broqueia_acesso()
                        ##############################################################
                        ## VERIFICA ATUALIZACOES NO TURNO DE FUNCIONAMENTO
                        ##############################################################
<<<<<<< HEAD
                        self.obtem_catraca()
                        self.obtem_turno()
                        UsuarioJson().usuario_get()
                        TipoJson().tipo_get()
                        CartaoJson().cartao_get()
                        VinculoJson().vinculo_get()
                        
=======
                        self.verifica_turnos()
>>>>>>> remotes/origin/web_backend
            else:
                ##############################################################
                ## CANCELA ACESSO PELA INVALIDADE DO ID DO CARTAO APRESENTADO
                ##############################################################
                return None
        except SystemExit, KeyboardInterrupt:
            raise
#         except Exception:
#             self.log.logger.error('Erro realizando operacoes de validacao no acesso.')
#             if self.cartao_dao.conexao_status():
#                 self.cartao_dao.rollback()
#                 self.log.logger.info("Alteracao no cartao cancelada! (rollback)")
        finally:
            self.bits = ''
            self.numero_cartao = 0
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.broqueia_acesso()
            ##############################################################
            ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
            ##############################################################
            self.aviso.exibir_aguarda_cartao()
            ##############################################################
            ## FECHA POSSIVEIS CONEXOES ABERTAS COM O BANCO DE DADOS
            ##############################################################
            if self.cartao_dao.conexao_status():
                self.cartao_dao.fecha_conexao()
                self.log.logger.debug('[Cartao] Conexao finalizada com o BD.')
            if self.registro_dao.conexao_status():
                self.registro_dao.fecha_conexao()
                self.log.logger.debug('[Registro] Conexao finalizada com o BD.')
            if self.giro_dao.conexao_status():
                self.giro_dao.fecha_conexao()
                self.log.logger.debug('[Giro] Conexao finalizada com o BD.')
<<<<<<< HEAD
                     
    def obtem_recursos_do_servidor(self):
        RecursosRestful().obtem_recursos()

    def obtem_catraca(self):
        IP = Util().obtem_ip()
        self.CATRACA = self.catraca_dao.busca_por_ip(IP)
               
    def obtem_turno(self):   
        self.TURNO = self.turno_dao.busca_por_catraca(self.CATRACA)
        if self.TURNO:
            self.TURNO.sort()
            for turno in self.TURNO:
                self.hora_atual = self.util.obtem_hora()
                self.hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
                self.hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
                if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                    return turno
                    break
            return None
    
    def obtem_cartao(self, numero):
        lista = self.cartao_dao.busca_cartao_valido(numero)
        self.CARTAO = lista
        return lista

#     def verifica_turnos(self):
#         self.catraca = self.obtem_catraca()
#         self.turno = self.obtem_turno(self.catraca)
#         self.turno_atual = self.turno_dao.busca(self.turno[0]) if self.turno != None else None #Op. ternario
    
    def broqueia_acesso(self):
        if self.CATRACA.operacao == 1:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.CATRACA.operacao == 2:
=======
                      
    def pesquisa_id(self, lista, id):
        resultado = None
        for cartao in lista:
            if cartao[1] == id:
                resultado = cartao
                return resultado
                break
        return resultado

    def obtem_turno(self, catraca):
        turnos = catraca.turnos
        turnos.sort()
        for turno in turnos:
            self.hora_atual = self.obtem_hora()
            self.hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
            self.hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
            if ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)):
                return turno
                break
        return None
    
    def obtem_cartao(self, id):
        try:
            cartao = self.cartao_dao.busca(id)
            return cartao
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro obtendo ID do cartao.', exc_info=True)
        finally:
            pass
    
    def obtem_cartoes(self):
        try:
            lista_cartoes = self.cartao_dao.busca()
            lista_cartoes.sort()
            return lista_cartoes
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro obtendo lista de cartoes', exc_info=True)
        finally:
            pass
        
    def obtem_catraca(self):
        return self.catraca_dao.busca_por_ip(self.obtem_ip())
    
    def obtem_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('unilab.edu.br', 0))
        ip = '%s' % ( s.getsockname()[0] )
        return ip
    
    def obtem_dia_util(self):
        dia_util = True
        weekday_count = 0
        cal = calendar.Calendar()
        data_atual = datetime.datetime.now()
        for week in cal.monthdayscalendar(data_atual.year, data_atual.month):
            for i, day in enumerate(week):
                if (day == 0) or (i >= 5):
                    if (day <> 0) and (day <> data_atual.day):
                        pass
                    if day == data_atual.day:
                        dia_util = False
                    continue
                if day == data_atual.day:
                    dia_util = True
                else:
                    pass
                weekday_count += 1
        return dia_util
    
    def obtem_hora(self):
        hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
        return hora_atual
    
    def obtem_data(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    def obtem_datahora(self):
        return datetime.datetime.now()
    
    def verifica_cartoes(self):
        return self.obtem_cartoes()
        
    def verifica_turnos(self):
        self.catraca = self.obtem_catraca()
        self.turno = self.obtem_turno(self.catraca)
        self.turno_atual = self.turno_dao.busca(self.turno[0]) if self.turno != None else None #Op. ternario
    
    def broqueia_acesso(self):
        if self.catraca.operacao == 1:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.catraca.operacao == 2:
>>>>>>> remotes/origin/web_backend
            self.solenoide.ativa_solenoide(2,0)
            self.pictograma.seta_direita(0)
            self.pictograma.xis(0)
        ##############################################################
        ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
        ##############################################################
        self.aviso.exibir_aguarda_cartao()
    
    def desbroqueia_acesso(self):
        self.util.beep_buzzer(950, .1, 2)
<<<<<<< HEAD
        if self.CATRACA.operacao == 1:
=======
        if self.catraca.operacao == 1:
>>>>>>> remotes/origin/web_backend
            self.solenoide.ativa_solenoide(1,1)
            self.pictograma.seta_esquerda(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
<<<<<<< HEAD
        if self.CATRACA.operacao == 2:
=======
        if self.catraca.operacao == 2:
>>>>>>> remotes/origin/web_backend
            self.solenoide.ativa_solenoide(2,1)
            self.pictograma.seta_direita(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
<<<<<<< HEAD
            
    def obtem_csv(self, numero_cartao):
        with open(Util().obtem_path('cartao.csv')) as csvfile:
            reader = csv.reader(csvfile)
            if reader:
                for row in reader:
                    if row[0] == str(numero_cartao):
                        print row[1]
                        return row[1]
                    
=======
            
>>>>>>> remotes/origin/web_backend
