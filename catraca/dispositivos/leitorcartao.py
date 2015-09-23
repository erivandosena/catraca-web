#!/usr/bin/env python
# -*- coding: latin-1 -*-


import os
import time
import socket
import locale
import calendar
import datetime
from time import sleep
from catraca.logs import Logs
from catraca.dispositivos.aviso import Aviso
from catraca.dispositivos.pictograma import Pictograma
from catraca.dispositivos.sensoroptico import SensorOptico
from catraca.dispositivos.solenoide import Solenoide
from catraca.pinos import PinoControle
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.catracadao import CatracaDAO
from catraca.dao.turnodao import TurnoDAO
from catraca.dao.girodao import GiroDAO
from catraca.dao.registrodao import RegistroDAO
from catraca.dao.cartao import Cartao
from catraca.dao.registro import Registro
from catraca.dao.giro import Giro



__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(object):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    log = Logs()
    aviso = Aviso()
    solenoide = Solenoide()
    pictograma = Pictograma()
    sensor_optico = SensorOptico()
    rpi = PinoControle()
    
    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    
    bits = '' #11101110000100010000010011101110
    ID = ''

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
        
        #self.catraca = self.obtem_catraca()
        #self.turno = self.obtem_turno(self.catraca)
        self.verifica_turnos()
        
        self.turno_atual = self.turno_dao.busca(self.turno[0]) if self.turno != None else None #Op. ternario
        self.cartoes = self.verifica_cartoes()
        self.giro = self.giro_dao.busca(self.catraca.id)
        self.aviso.exibir_aguarda_cartao()
    
    def zero(self, obj):
        self.bits = self.bits + '0'
    
    def um(self, obj):
        self.bits = self.bits + '1'
        
    def ler(self):
        status = False
        try:            
            self.rpi.evento_falling(self.D0, self.zero)
            self.rpi.evento_falling(self.D1, self.um)
            while True:
                sleep(1)
                if len(self.bits) == 32:
                    #os.system('mpg321 -q -g 50 audio/Censor_B-Josh-8135_hifi.mp3 &') #http://www.flashkit.com/soundfx/Electronic/Beeps
                    self.aviso.exibir_aguarda_consulta()
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
                    ID = int(str(self.bits), 2)
                    status = True
                    self.bits = ''                    
                    self.valida_cartao(ID)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.log.logger.error('Erro obtendo binario: '+str(self.bits))
                    self.bits = ''
                    self.aviso.exibir_erro_leitura_cartao()
                    self.aviso.exibir_aguarda_cartao()
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception, e:
            status = False
            self.log.logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            self.bits = ''
            self.aviso.exibir_aguarda_cartao()
        return status

    def valida_cartao(self, id_cartao):
        #self.aviso.exibir_aguarda_liberacao()
        self.hora_atual = self.obtem_hora()
        try:
            ##############################################################
            ## VERIFICA SE HOUVE ATUALIZACAO NOS CARTOES DURANTE O TURNO
            ##############################################################
            self.cartoes = self.verifica_cartoes()
            """
            -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
            if not self.dias_uteis():
                self.aviso.exibir_dia_invalido()
                self.aviso.exibir_acesso_bloqueado()
                return None
            """
            ##############################################################
            ## VERIFICA O HORARIO PARA FUNCIONAMENTO DO TURNO
            ##############################################################
            if not (((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim)) or ((self.hora_atual >= self.hora_inicio) and (self.hora_atual <= self.hora_fim))):
                self.aviso.exibir_horario_invalido()
                self.aviso.exibir_acesso_bloqueado()
                self.log.logger.info('Cartao apresentado fora do horario de atendimento ID:'+ str(id_cartao))
                ##############################################################
                ## VERIFICA ATUALIZACOES NO TURNO DE FUNCIONAMENTO
                ##############################################################
                self.verifica_turnos()
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
                self.cartao_ativo = self.pesquisa_id(self.cartoes, id_cartao)
                if self.cartao_ativo is None:
                    self.aviso.exibir_cartao_nao_cadastrado()
                    self.aviso.exibir_aguarda_cartao()
                    self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                    return None
                else:
                    ##############################################################
                    ## OBTEM AS INFORMACOES DO CARTAO CONSULTADO NO BANCO DE DADOS
                    ##############################################################
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
                    """
                    -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
                    if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
                        if ((hora_ultimo_acesso >= p1_hora_inicio) and (hora_ultimo_acesso <= p1_hora_fim) and (data_ultimo_acesso == data_atual)):
                            self.aviso.exibir_cartao_utilizado()
                            self.aviso.exibir_acesso_bloqueado()
                            return None
                    """
                    ##############################################################
                    ## VERIFICA SE O CARTAO POSSUI CREDITO(S) PARA UTILIZACAO
                    ##############################################################
                    if (creditos == 0):
                        self.aviso.exibir_cartao_sem_saldo()
                        self.aviso.exibir_acesso_bloqueado()
                        self.log.logger.error('Cartao sem credito ID:'+ str(id_cartao))
                        return None
                    else:
                        """
                        -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE DURANTE OS TESTES
                        ##############################################################
                        ## EXIBE O SALDO DOS CREDITOS PARA O UTILIZADOR DO CARTAO
                        ##############################################################
                        saldo = str(locale.currency(cartao.perfil.tipo.valor*creditos)).replace(".",",")
                        self.aviso.exibir_cartao_valido(tipo, saldo)
                        self.log.logger.info('Saldo atual do cartao ID:'+ str(id_cartao) + ' - ' + saldo)
                        """
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
                        self.aviso.exibir_aguarda_liberacao()
                        ##############################################################
                        ## LIBERA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        self.desbroqueia_acesso()                        
                        ##############################################################
                        ## AGUARDA UTILIZADOR PASSAR NA CATRACA E REALIZAR O GIRO
                        ##############################################################
                        while True:
                            if not self.sensor_optico.registra_giro(self.catraca.tempo):                                
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
                                        raise Exception('Erro inserindo valores no registro.')
                                    else:
                                        self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
                                ##############################################################
                                ## REGISTRA INFORMACOES DE GIRO REALIZADO NA CATRACA
                                ##############################################################                                
                                giro = Giro()
                                giro.horario = 1 if self.catraca.operacao == 1 else 0
                                giro.antihorario = 1 if self.catraca.operacao == 2 else 0
                                giro.tempo = self.sensor_optico.tempo_decorrido
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
                                        raise Exception('Erro inserindo valores no registro.')
                                    else:
                                        self.log.logger.info('[Registro] ' + self.registro_dao.aviso)
                                break
                        ##############################################################
                        ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
                        ##############################################################
                        self.broqueia_acesso()
                        ##############################################################
                        ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
                        ##############################################################
                        self.aviso.exibir_aguarda_cartao()
                        ##############################################################
                        ## VERIFICA ATUALIZACOES NO TURNO DE FUNCIONAMENTO
                        ##############################################################
                        self.verifica_turnos()
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
            ##############################################################
            ## BLOQUEIA O ACESSO E SINALIZA O MESMO AO UTILIZADOR
            ##############################################################
            self.broqueia_acesso()
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
    
    def desbroqueia_acesso(self):
        if self.catraca.operacao == 1:
            self.solenoide.ativa_solenoide(1,1)
            self.pictograma.seta_esquerda(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado()
        if self.catraca.operacao == 2:
            self.solenoide.ativa_solenoide(2,1)
            self.pictograma.seta_direita(1)
            self.pictograma.xis(1)
            self.aviso.exibir_acesso_liberado() 
    
    def broqueia_acesso(self):
        if self.catraca.operacao == 1:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
        if self.catraca.operacao == 2:
            self.solenoide.ativa_solenoide(2,0)
            self.pictograma.seta_direita(0)
            self.pictograma.xis(0)
        ##############################################################
        ## EXIBE MENSAGEM NO DISPLAY AO UTILIZADOR DO PROXIMO ACESSO
        ##############################################################
        self.aviso.exibir_aguarda_cartao()
    