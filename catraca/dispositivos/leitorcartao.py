#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
import locale
import calendar
#from datetime import datetime
import datetime
from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dao.cartaodao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dispositivos.aviso import Aviso
from catraca.dispositivos.solenoide import Solenoide
from catraca.dispositivos.pictograma import Pictograma
from catraca.dispositivos.sensoroptico import SensorOptico


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(object):
    
    log = Logs()
    aviso = Aviso()
    solenoide = Solenoide()
    cartao_dao = CartaoDAO()
    pictograma = Pictograma()
    giro = SensorOptico()
    
    rpi = PinoControle()
    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    bits = ''
    ID = ''
    
    def __init__(self):
        super(LeitorCartao, self).__init__()
      
    def zero(self, obj):
        self.bits = self.bits + '0'
    
    def um(self, obj):
        self.bits = self.bits + '1'

    def ler(self):
        status = False
        self.aviso.exibir_aguarda_cartao()
        try:
            self.rpi.evento_falling(self.D0, self.zero)
            self.rpi.evento_falling(self.D1, self.um)
            while True:
                sleep(0.5)
                if len(self.bits) == 32:
                    sleep(0.1)
                    ID = int(str(self.bits), 2)
                    status = True
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
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
            self.log.logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            self.aviso.exibir_aguarda_cartao()
            status = False
        return status

    def valida_cartao(self, id_cartao):
        try:
            cartao = Cartao()

            hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
            p1_hora_inicio = datetime.datetime.strptime('11:00:00','%H:%M:%S').time()
            p1_hora_fim = datetime.datetime.strptime('13:30:00','%H:%M:%S').time()
            p2_hora_inicio = datetime.datetime.strptime('17:30:00','%H:%M:%S').time()
            p2_hora_fim = datetime.datetime.strptime('19:00:00','%H:%M:%S').time()

            if not self.dias_uteis():
                self.aviso.exibir_dia_invalido
                self.aviso.exibir_acesso_bloqueado()
                return None
            if not (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim))):        
                self.aviso.exibir_horario_invalido()
                self.aviso.exibir_acesso_bloqueado()
                return None
            elif (len(str(id_cartao)) <> 10):
                self.log.logger.error('Cartao com ID incorreto:'+ str(id_cartao))
                self.aviso.exibir_erro_leitura_cartao()
                self.aviso.exibir_aguarda_cartao()
                return None
            elif (len(str(id_cartao)) == 10):
                cartao = self.busca_id_cartao(id_cartao)
                if (cartao == None):
                    self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                    self.aviso.exibir_cartao_nao_cadastrado()
                    self.aviso.exibir_aguarda_cartao()
                    return None
                else:
                    creditos = cartao.creditos
                    usuario_cartao = cartao.tipo
                    tipo = self.tipo_usuario(usuario_cartao)
                    
                    hora_ultimo_acesso = datetime.datetime.strptime(cartao.data.strftime('%H:%M:%S'),'%H:%M:%S').time()

                    datasis = datetime.datetime.now()
                    data_atual = datetime.datetime(
                        day=datasis.day,
                        month=datasis.month,
                        year=datasis.year, 
                    ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
                    
                    databd = cartao.data
                    data_ultimo_acesso = datetime.datetime(
                        day=databd.day,
                        month=databd.month,
                        year=databd.year, 
                    ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')

                    if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
                        if ((hora_ultimo_acesso >= p1_hora_inicio) and (hora_ultimo_acesso <= p1_hora_fim) and (data_ultimo_acesso == data_atual)):
                            self.aviso.exibir_cartao_utilizado1()
                            self.aviso.exibir_acesso_bloqueado()
                            return None    
                    if ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim)):
                        if ((hora_ultimo_acesso >= p2_hora_inicio) and (hora_ultimo_acesso <= p2_hora_fim) and (data_ultimo_acesso == data_atual)):
                            self.aviso.exibir_cartao_utilizado2()
                            self.aviso.exibir_acesso_bloqueado()
                            return None
                    if (creditos == 0):
                        self.log.logger.info('Cartao sem credito ID:'+ str(id_cartao))
                        self.aviso.exibir_cartao_sem_saldo(tipo)
                        self.aviso.exibir_acesso_bloqueado()
                        return None
                    else:
                        self.log.logger.debug('Cartao valido ID:'+ str(id_cartao))
                        saldo = str(locale.currency(cartao.valor*creditos)).replace(".",",")
                        self.aviso.exibir_cartao_valido(tipo, saldo)
                        self.aviso.exibir_acesso_liberado()
                        self.solenoide.ativa_solenoide(1,1)
                        self.pictograma.seta_esquerda(1)
                        self.pictograma.xis(1)
                        ##############################################################
                        # OPERACAO DE DECREMENTO DE CREDITO NO CARTAO
                        ##############################################################
                        saldo_creditos = creditos - 1
                        cartao.creditos = saldo_creditos
                        cartao.data = datetime.datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")
                        ##############################################################
                        if not self.cartao_dao.altera(cartao): # altera no banco de dados
                            self.log.logger.critical('Erro atualizando valores no cartao.')
                            raise Exception(self.cartao_dao.erro)
                        while True:
                            if self.giro.registra_giro(6000):
                                self.log.logger.info('Girou a catraca.')
                                if self.cartao_dao.conexao_status:
                                    self.cartao_dao.commit # persiste no banco de dados
                                    self.log.logger.info('Cartao alterado com sucesso.')
                                break
                            else:
                                self.log.logger.info('Nao girou a catraca.')
                                if self.cartao_dao.conexao_status:
                                    self.cartao_dao.rollback
                                break
            else:
                return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            if self.cartao_dao.conexao_status:
                self.cartao_dao.rollback
            self.log.logger.error('Erro validando ID do cartao.', exc_info=True)
        finally:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
            self.aviso.exibir_aguarda_cartao()
            if self.cartao_dao.conexao_status:
                self.cartao_dao.fecha_conexao
                self.log.logger.debug('[valida_cartao] Conexão finalizada com o BD.')

    def busca_id_cartao(self, id):
        try:
            cartao = self.cartao_dao.busca_id(id)
            return cartao
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro consultando ID do cartao.', exc_info=True)
        finally:
            pass

    def tipo_usuario(self, tipo):
        opcoes = {
                   1 : '    Estudante',
                   2 : '    Professor',
                   3 : '     Tecnico',
                   4 : '    Visitante',
                   5 : '    Operador',
                   6 : ' Administrador',
        }
        return opcoes.get(tipo, "  Desconhecido").upper()
    
    def dias_uteis(self):
        dia_util = True
        weekday_count = 0
        cal = calendar.Calendar()
        data_atual = datetime.datetime.now()
        for week in cal.monthdayscalendar(data_atual.year, data_atual.month):
            for i, day in enumerate(week):
                if (day == 0) or (i >= 5):
                    if (day <> 0) and (day <> data_atual.day):
                        #print str(day) + ' não é dia útil'
                        pass
                    if day == data_atual.day:
                        dia_util = False
                        #print str(day) + ' não é dia útil [HOJE]'
                    continue
                if day == data_atual.day:
                    dia_util = True
                    #print str(day) + ' é dia útil [HOJE]'
                else:
                    #print str(day) + ' é dia útil'
                    pass
                weekday_count += 1
        #print 'Total de dias uteis: '+str(weekday_count)
        return dia_util
    
    