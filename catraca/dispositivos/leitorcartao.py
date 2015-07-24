#!/usr/bin/env python
# -*- coding: latin-1 -*-

import locale
from time import sleep
from datetime import datetime
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dao.cartaodao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dispositivos.display import Display
from catraca.dispositivos.solenoide import Solenoide
from catraca.dispositivos.pictograma import Pictograma
from catraca.dispositivos.sensoroptico import SensorOptico



__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(object):
    
    log = Logs()
    display = Display()
    solenoide = Solenoide()
    cartao_dao = CartaoDAO()
    pictograma = Pictograma()
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
        self.display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
        try:
            self.rpi.evento_falling(self.D0, self.zero)
            self.rpi.evento_falling(self.D1, self.um)
            while True:
                sleep(0.5)
                if len(self.bits) == 32:
                    sleep(0.1)
                    ID = int(str(self.bits), 2)
                    self.bits = ''
                    self.valida_cartao(ID)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.log.logger.error('Erro obtendo binario: '+str(self.bits))
                    self.bits = ''
                    self.display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",1,True,False)
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception, e:
            self.log.logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            self.display.mensagem("   Bem-vindo!\nAPROXIME CARTAO",0,True,False)

    def valida_cartao(self, id_cartao):
        try:
            cartao = Cartao()
            cartao = self.busca_id_cartao(id_cartao)
            creditos = cartao.getCreditos()
            
            if (cartao == None) or (len(str(id_cartao)) <> 10):
                self.log.logger.error('Cartao com ID incorreto.')
                self.display.mensagem("  Por favor...\nREPITA OPERACAO",0,True,False)
                return None
            else:
                if (cartao.getNumero() <> id_cartao):
                    self.log.logger.info('Cartao invalido! (Nao cadastrado) ID:'+ str(id_cartao))
                    self.display.mensagem(" ID: "+str(id_cartao)+"\nNAO CADASTRADO!",3,False,False)
                    self.display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
                    return None
                elif (creditos == 0):
                    self.log.logger.info('Cartao sem credito! ID:'+ str(id_cartao))
                    self.display.mensagem(" ID: "+str(id_cartao)+"\n SALDO NEGATIVO!",3,False,False)
                    self.display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
                    return None
                else:
                    self.log.logger.debug('Cartao valido! ID:'+ str(id_cartao))
                    self.display.mensagem(" ID: "+str(id_cartao)+"\n SALDO "+str(locale.currency(cartao.getValor()*creditos)).replace(".",","),1,False,False)
                    self.display.mensagem("     ACESSO\n    LIBERADO!",1,False,False)
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
                    CONTA_ACESSO = 0
                    giro = SensorOptico()
                    while True:
                        if giro.registra_giro(6000):
                            self.log.logger.info('Girou a catraca.')
                            self.debita_cartao(creditos, cartao)
                            break
                        else:
                            self.log.logger.info('Nao girou a catraca.')
                            self.cartao_dao.getRollback()
                            break
                    return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro validando ID do cartao.', exc_info=True)
        finally:
            self.solenoide.ativa_solenoide(1,0)
            self.pictograma.seta_esquerda(0)
            self.pictograma.xis(0)
            self.display.mensagem("   Bem-vindo!\nAPROXIME CARTAO",0,True,False)
        
    def busca_id_cartao(self, id):
        cartao = self.cartao_dao.busca_id(id)
        return cartao
    
    def debita_cartao(self, creditos, cartao):
        try:
            saldo_creditos = creditos - 1
            cartao.setCreditos(saldo_creditos)
            #cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))
            cartao.setData("'"+str(cartao.getData())+"'")
            if self.cartao_dao.altera(cartao):
                self.cartao_dao.getCommit()
                self.log.logger.info('Cartao alterado com sucesso.')
            else:
                self.log.logger.error('Erro ao alterar cartao. '+cartao_dao.getErro())
                self.cartao_dao.getRollback()
        except SystemExit, KeyboardInterrupt:
            raise
        except DatabaseError:
            self.cartao_dao.getRollback()
            self.log.logger.critical('Erro ao salvar informacao no banco de dados.', exc_info=True)
        except Exception:
            self.log.logger.critical('Erro realizando operacao de debito no cartao.', exc_info=True)
        finally:
            pass