#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
import locale
from time import sleep
from datetime import datetime
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
    
    #hora_atual = datetime.now().strftime('%H:%M:%S')
    
    def __init__(self):
        super(LeitorCartao, self).__init__()
      
    def zero(self, obj):
        self.bits = self.bits + '0'
    
    def um(self, obj):
        self.bits = self.bits + '1'

    def ler(self):
        status = False
        self.aviso.exibir_aguarda_cartao()
        #self.mensagem.inicia_mensagem()
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
            print 'finaliza ler'
            self.aviso.exibir_aguarda_cartao()
            status = False
        return status

    def valida_cartao(self, id_cartao):
        #self.mensagem.finaliza_mensagem()
        try:
            cartao = Cartao()

            hora_atual = datetime.strptime(datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
            p1_hora_inicio = datetime.strptime('11:00:00','%H:%M:%S').time()
            p1_hora_fim = datetime.strptime('13:30:00','%H:%M:%S').time()
            p2_hora_inicio = datetime.strptime('17:30:00','%H:%M:%S').time()
            p2_hora_fim = datetime.strptime('19:00:00','%H:%M:%S').time()
            
            print str(hora_atual)
            print str(p1_hora_inicio)+' '+str(hora_atual < p1_hora_inicio)
            print str(p1_hora_fim)+' '+str(hora_atual > p1_hora_fim)
            print str(p2_hora_inicio)+' '+str(hora_atual < p2_hora_inicio)
            print str(p2_hora_fim)+' '+str(hora_atual > p2_hora_fim)
            
            print 50 * "="
            print '11:00:00 - 13:30:00 '+str(((hora_atual < p1_hora_inicio) and (hora_atual > p1_hora_fim)))
            print '17:30:00 - 19:00:00 '+str(((hora_atual < p2_hora_inicio) and (hora_atual > p2_hora_fim)))
            print 50 * "§"
            print '11:00:00 - 13:30:00 / 17:30:00 - 19:00:00 '+str( (((hora_atual < p1_hora_inicio) and (hora_atual > p1_hora_fim)) or ((hora_atual < p2_hora_inicio) and (hora_atual > p2_hora_fim))) )
            print '11:00:00 - 13:30:00 / 17:30:00 - 19:00:00 '+str( (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim))) )
            
            if not (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim))):        
                self.aviso.exibir_horario_invalido()
                self.aviso.exibir_acesso_bloqueado()
                print 'passou na validaoa de horario'
                return None
            elif (len(str(id_cartao)) <> 10):
                self.log.logger.error('Cartao com ID incorreto:'+ str(id_cartao))
                self.aviso.exibir_erro_leitura_cartao()
                self.aviso.exibir_aguarda_cartao()
                return None
            elif (len(str(id_cartao)) == 10):
                cartao = self.busca_id_cartao(id_cartao)
                #if (cartao == None) or (len(str(id_cartao)) <> 10):
                if (cartao == None):
                    self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                    self.aviso.exibir_cartao_nao_cadastrado()
                    self.aviso.exibir_aguarda_cartao()
                    return None
    #             elif (len(str(id_cartao)) <> 10):
    #                 self.log.logger.error('Cartao com ID incorreto:'+ str(id_cartao))
    #                 self.aviso.exibir_erro_leitura_cartao()
    #                 self.aviso.exibir_aguarda_cartao()
    #                 return None
                else:
                    creditos = cartao.creditos
                    usuario_cartao = cartao.tipo
                    tipo = self.tipo_usuario(usuario_cartao)
    #                 if (cartao.getNumero() <> id_cartao):
    #                     self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
    #                     self.aviso.exibir_cartao_nao_cadastrado()
    #                     self.aviso.exibir_acesso_bloqueado()
    #                     return None
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
                        """
                        while sensor_optico.ler_sensor(2):
                            solenoide.ativa_solenoide(2,alto)
                            print 'Sensor 2 = '+str(sensor_optico.ler_sensor(2))
                            print 'Ativa Solenoide 2'
                        else:
                            solenoide.ativa_solenoide(2,baixo)
                            print 'Sensor 2 = '+str(sensor_optico.ler_sensor(2))
                            print 'Desativa Solenoide 2'
                        """    
                        #CONTA_ACESSO = 0
                        #giro = SensorOptico()
                        
                        #self.debita_cartao(creditos, cartao)
                        ##############################################################
                        # OPERACAO DE DEBITO NO CARTAO
                        ##############################################################
                        saldo_creditos = creditos - 1
                        cartao.creditos = saldo_creditos
                        cartao.data = datetime.now().strftime("'%Y-%m-%d %H:%M:%S'")
                        ##############################################################
                        #cartao.setData("'"+str(cartao.getData())+"'")
                        if not self.cartao_dao.altera(cartao): # altera no banco de dados
                            self.log.logger.critical('Erro atualizando valores no cartao.')
                            raise Exception(self.cartao_dao.erro)
                        while True:
                            if self.giro.registra_giro(6000):
                                self.log.logger.info('Girou a catraca.')
                                self.cartao_dao.commit # persiste no banco de dados
                                self.log.logger.info('Cartao alterado com sucesso.')
    #                             self.cartao_dao.getFecha()
    #                             print "Conexão finalizada (c/ giro)"
    #                             self.log.logger.info('Conexão finalizada com o BD. (c/ giro)')
                                break
                            else:
                                self.log.logger.info('Nao girou a catraca.')
                                self.cartao_dao.rollback
    #                             self.cartao_dao.getFecha()
    #                             print "Conexão finalizada (s/ giro)"
    #                             self.log.logger.info('Conexão finalizada com o BD. (s/ giro)')
                                break
            else:
                return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.cartao_dao.rollback
            self.log.logger.error('Erro validando ID do cartao.', exc_info=True)
        finally:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
            self.aviso.exibir_aguarda_cartao()
            #self.mensagem.inicia_mensagem()
            if not self.cartao_dao.abre_conexao():
                print self.cartao_dao.fecha_conexao
                print "Conexão finalizada (Cartao update)"
                self.log.logger.debug('[Cartao Update] Conexão finalizada com o BD.')
            print 'finaliza valida_cartao'
        
    def busca_id_cartao(self, id):
        try:
            cartao = self.cartao_dao.busca_id(id)
            return cartao
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro consultando ID do cartao.', exc_info=True)
        finally:
            #pass
            print 'finaliza busca_id_cartao'
            #self.cartao_dao.fecha_conexao
            #print "Conexão finalizada (Cartao select)"
            #self.log.logger.debug('[Cartao Select] Conexão finalizada com o BD.')
            
#     def debita_cartao(self, creditos, cartao):
#         try:
#             saldo_creditos = creditos - 1
#             cartao.setCreditos(saldo_creditos)
#             #cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))
#             cartao.setData("'"+str(cartao.getData())+"'")
#             if not self.cartao_dao.altera(cartao): # altera no banco de dados
#                 raise Exception(self.cartao_dao.getErro())
#                 #self.cartao_dao.getErro()
# #                 self.log.logger.debug('Iniciando alteracao do cartao.')
# #             else:
# #                 self.log.logger.critical('Erro ao alterar cartao. '+cartao_dao.getErro())
# #                 self.cartao_dao.getRollback()
#         except SystemExit, KeyboardInterrupt:
#             raise
# #         except DatabaseError:
# #             self.cartao_dao.getRollback()
# #             self.log.logger.critical('Erro ao salvar informacao no banco de dados.', exc_info=True)
#         except Exception:
#             self.cartao_dao.getRollback()
#             self.log.logger.critical('Erro realizando operacao de debito no cartao.', exc_info=True)
#         finally:
#             #pass
# #             self.cartao_dao.getFecha()
# #             print "Conexão finalizada (Cartao)"
# #             self.log.logger.debug('Conexão (Cartao) com o Bd finalizada.')
#             print 'finaliza debita_cartao'
        
    def tipo_usuario(self, tipo):
        opcoes = {
                   1 : '    Estudante',
                   2 : '     Tecnico',
                   3 : '    Professor',
                   4 : '    Visitante',
                   5 : '    Operador',
                   6 : ' Administrador',
        }
        return opcoes.get(tipo, "  Desconhecido").upper()
    