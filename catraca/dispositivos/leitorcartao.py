#!/usr/bin/env python
# -*- coding: latin-1 -*-


import calendar
import datetime
import locale
import os
import socket
from time import sleep
import time

from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.catracadao import CatracaDAO
from catraca.dao.turnodao import TurnoDAO
from catraca.dao.finalidadedao import FinalidadeDAO
from catraca.dao.registro import Registro
from catraca.dao.registrodao import RegistroDAO
from catraca.dispositivos.aviso import Aviso
from catraca.dispositivos.pictograma import Pictograma
from catraca.dispositivos.sensoroptico import SensorOptico
from catraca.dispositivos.solenoide import Solenoide
from catraca.logs import Logs
from catraca.pinos import PinoControle


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
    giro = SensorOptico()
    
    rpi = PinoControle()
    D0 = rpi.ler(17)['gpio']
    D1 = rpi.ler(27)['gpio']
    
    bits = ''
    ID = ''
    #conta_turnos = 0
    
    catraca_dao = CatracaDAO()
    turno_dao = TurnoDAO()
    cartao_dao = CartaoDAO()
    registro_dao = RegistroDAO()
    
    cartao = Cartao()
    registro = Registro()

    catraca = None
    turnos = []
    turno_valido = False
    turno_atual = None
    cartoes = []

    def __init__(self):
        super(LeitorCartao, self).__init__()
        self.catraca = self.catraca_dao.busca_por_ip(self.obtem_ip())
        self.turnos = self.catraca.turno
        
        self.cartoes = self.lista_cartoes()
        #self.ids = self.lista_id_cartoes()
        
        for turno in self.turnos:
            #self.conta_turnos += 1
            hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
            hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
            hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
    
            if ((hora_atual >= hora_inicio) and (hora_atual <= hora_fim)):
                self.turno_atual = self.turno_dao.busca(turno[0])
                #finalidade_turno = FinalidadeDAO().busca(turno[3]).nome
                #print "Turno encontrado entre:" +str(p1_hora_inicio)+" "+str(p1_hora_fim)+ " -> " + finalidade_turno
                turno_valido = True
                break
        
    def obtem_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('unilab.edu.br', 0))
        ip = '%s' % ( s.getsockname()[0] )
        return ip
      
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
                    ID = int(str(self.bits), 2)
                    status = True
                    self.log.logger.info('Binario obtido corretamente: '+str(self.bits))
                    self.bits = ''
                    self.aviso.exibir_aguarda_liberacao()
                    self.valida_cartao(ID)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.log.logger.error('Erro obtendo binario: '+str(self.bits))
                    self.bits = ''
                    self.aviso.exibir_erro_leitura_cartao()
                    self.aviso.exibir_aguarda_cartao()
        except SystemExit, KeyboardInterrupt:
            self.bits = ''
            raise
        except Exception, e:
            status = False
            self.log.logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            self.aviso.exibir_aguarda_cartao()
            self.bits = ''
            status = False
        return status

    def valida_cartao(self, id_cartao):
        try:
            idcartao = 0
            creditocartao = 0.00
            #cartao = Cartao()
            #registro = Registro()
            #registro_dao = RegistroDAO()
            #catraca = self.catraca_dao.busca_por_ip(self.obtem_ip())
            #turnos = self.catraca.turno
            #turno_atual = None
            
            #self.aviso.exibir_aguarda_liberacao()
            
            hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
            hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
            hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()

            """
            -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE PARA TESTES
            if not self.dias_uteis():
                self.aviso.exibir_dia_invalido()
                self.aviso.exibir_acesso_bloqueado()
                return None
            """
#             for turno in self.turnos:
#                 #self.conta_turnos += 1
#                 hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
#                 hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
#         
#                 if ((hora_atual >= hora_inicio) and (hora_atual <= hora_fim)):
#                     turno_atual = TurnoDAO().busca(turno[0])
#                     #finalidade_turno = FinalidadeDAO().busca(turno[3]).nome
#                     #print "Turno encontrado entre:" +str(p1_hora_inicio)+" "+str(p1_hora_fim)+ " -> " + finalidade_turno
#                     break
            if turno_valido:
                print "Turno encontrado entre:" +str(hora_inicio)+" "+str(hora_fim)
                
            if not (((hora_atual >= hora_inicio) and (hora_atual <= hora_fim)) or ((hora_atual >= hora_inicio) and (hora_atual <= hora_fim))):
                #print "Fora do horario!"
                self.aviso.exibir_horario_invalido()
                self.aviso.exibir_acesso_bloqueado()
                return None
            elif ((hora_atual >= hora_inicio) and (hora_atual <= hora_fim)):
                #print "Turno liberado entre:" +str(p1_hora_inicio)+" "+str(p1_hora_fim)
                #print "*****faco coisas apartir daqui!*****"
                pass
            if (len(str(id_cartao)) <> 10):
                self.log.logger.error('Cartao com ID incorreto:'+ str(id_cartao))
                self.aviso.exibir_erro_leitura_cartao()
                self.aviso.exibir_aguarda_cartao()
                return None
            elif (len(str(id_cartao)) == 10):
                #self.cartao = self.busca_id_cartao(id_cartao)
                
                 
                for cartao in self.lista_cartoes():
                    if cartao[1] == id_cartao:
                        idcartao = cartao[1]
                        creditocartao = cartao[2] 
                        break
                        
                        
                if len(idcartao) == 0:
                    return None
#                 if (self.cartao == None):
#                     self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
#                     self.aviso.exibir_cartao_nao_cadastrado()
#                     self.aviso.exibir_aguarda_cartao()
#                     return None
#                 if self.lista_cartoes.index(id_cartao):
#                     self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
#                     self.aviso.exibir_cartao_nao_cadastrado()
#                     self.aviso.exibir_aguarda_cartao()
#                     return None
                else:
                    #creditos = self.cartao.creditos
                    creditos = creditocartao
                    #tipo = self.cartao.perfil.nome
                    hora_ultimo_acesso = datetime.datetime.strptime(self.cartao.data.strftime('%H:%M:%S'),'%H:%M:%S').time()
                    
                    datasis = datetime.datetime.now()
                    data_atual = datetime.datetime(
                        day=datasis.day,
                        month=datasis.month,
                        year=datasis.year, 
                    ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
                    
                    databd = self.cartao.data
                    data_ultimo_acesso = datetime.datetime(
                        day=databd.day,
                        month=databd.month,
                        year=databd.year, 
                    ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')

                    """
                    -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE PARA TESTES
                    if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
                        if ((hora_ultimo_acesso >= p1_hora_inicio) and (hora_ultimo_acesso <= p1_hora_fim) and (data_ultimo_acesso == data_atual)):
                            self.aviso.exibir_cartao_utilizado()
                            self.aviso.exibir_acesso_bloqueado()
                            return None
                    """
                    if (creditos == 0):
                        self.log.logger.info('Cartao sem credito ID:'+ str(id_cartao))
                        #self.aviso.exibir_cartao_sem_saldo(tipo)
                        self.aviso.exibir_acesso_bloqueado()
                        return None
                    else:
                        """
                        -> VERIFICAÇÃO DESATIVADA TEMPORARIAMENTE PARA TESTES
                        self.log.logger.debug('Cartao valido ID:'+ str(id_cartao))
                        saldo = str(locale.currency(cartao.perfil.tipo.valor*creditos)).replace(".",",")
                        self.aviso.exibir_cartao_valido(tipo, saldo)
                        """
                        #self.aviso.exibir_acesso_liberado()
                        #self.aviso.exibir_aguarda_liberacao()
                        
                        if self.catraca.operacao == 1:
                            self.solenoide.ativa_solenoide(1,1)
                            self.pictograma.seta_esquerda(1)
                            self.pictograma.xis(1)
                        if self.catraca.operacao == 2:
                            self.solenoide.ativa_solenoide(2,1)
                            self.pictograma.seta_direita(1)
                            self.pictograma.xis(1)
                            
                        self.cartao = self.busca_id_cartao(idcartao)
                        
                        self.aviso.exibir_acesso_liberado()
                        ##############################################################
                        ## OPERACAO DE DECREMENTO DE CREDITO NO CARTAO
                        ##############################################################
                        saldo_creditos = creditos - 1
                        self.cartao.creditos = saldo_creditos
                        self.cartao.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        ##############################################################
                        if not self.cartao_dao.mantem(self.cartao,False):
                            raise Exception('Erro atualizando valores no cartao.'+ self.cartao_dao.aviso)
                        else:
                            self.log.logger.info("[Cartao] "+self.cartao_dao.aviso)
                        while True:
                            #sleep(0.99)
                            if self.giro.registra_giro(self.catraca.tempo):
                                self.log.logger.info('Girou a catraca.')
                                if self.cartao_dao.conexao_status():
                                    self.cartao_dao.commit() # se girou, persiste no banco de dados
                                    self.log.logger.info('Cartao com alteracao comitado com sucesso.')

                                self.registro.data = self.cartao.data
                                self.registro.giro = 1
                                self.registro.valor = self.cartao.perfil.tipo.valor
                                self.registro.cartao = self.cartao
                                self.registro.turno = turno_atual
                                if not self.registro_dao.mantem(self.registro,False):
                                    raise Exception('Erro inserindo valores no registro:\n'+ self.registro_dao.aviso)
                                else:
                                    self.log.logger.info("[Registro] "+self.registro_dao.aviso)
                                break
                            else:
                                self.log.logger.info('Nao girou a catraca.')
                                
                                if self.cartao_dao.conexao_status():
                                    self.cartao_dao.rollback()
                                    self.log.logger.info("Alteracao no cartao cancelada!(rollback)")
                                
                                self.registro.giro = 0
                                self.registro.valor = 0.00
                                self.registro.data = self.cartao.data
                                self.registro.cartao = self.cartao
                                self.registro.turno = turno_atual
                                if not self.registro_dao.mantem(self.registro,False):
                                    raise Exception('Erro inserindo valores no registro:\n'+ self.registro_dao.aviso)
                                else:
                                    self.log.logger.info("[Registro] "+ self.registro_dao.aviso)
                                break
            else:
                return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            if self.cartao_dao.conexao_status():
                self.cartao_dao.rollback()
                self.log.logger.info("Alteracao no cartao cancelada!(rollback)")
            #self.log.logger.error('Erro validando ID do cartao:\n'+ self.cartao_dao.aviso)
        finally:
            if self.catraca.operacao == 1:
                self.solenoide.ativa_solenoide(1,0)
                self.pictograma.seta_esquerda(0)
                self.pictograma.xis(0)
            if self.catraca.operacao == 2:
                self.solenoide.ativa_solenoide(2,0)
                self.pictograma.seta_direita(0)
                self.pictograma.xis(0)
                
            self.aviso.exibir_aguarda_cartao()

            if self.registro_dao.conexao_status():
                self.registro_dao.fecha_conexao()
                self.log.logger.debug('[registro] Conexão finalizada com o BD.')
            
            if self.cartao_dao.conexao_status():
                self.cartao_dao.fecha_conexao()
                self.log.logger.debug('[cartao] Conexão finalizada com o BD.')
            
            self.aviso.exibir_aguarda_cartao()

    def busca_id_cartao(self, id):
        try:
            cartao = self.cartao_dao.busca(id)
            return cartao
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro consultando ID do cartao.', exc_info=True)
        finally:
            pass
        
    def lista_cartoes(self):
        #lista = []
        try:
            cartoes = self.cartao_dao.busca()
#             for id in cartoes:
#                 lista.append(id[1])
            return cartoes
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro consultando ID.', exc_info=True)
        finally:
            pass
    
    def dias_uteis(self):
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
    
    