#!/usr/bin/env python
# -*- coding: latin-1 -*-

import locale
from time import sleep
from datetime import datetime
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dao.cartaodao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dispositivos.sensor_optico import SensorOptico
from catraca.dispositivos import display
from catraca.dispositivos import painel_leds
from catraca.dispositivos import solenoide

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class LeitorCartao(object):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    bits = ''
    ID = ''
    
    def __init__(self):
        super(LeitorCartao, self).__init__()
      
    def zero(self, obj):
        #global bits
        self.bits = self.bits + '0'
    
    def um(self, obj):
        #global bits
        self.bits = self.bits + '1'

    def ler(self):
        display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
        try:
            rpi = PinoControle()
            D0 = rpi.ler(17)['gpio']
            D1 = rpi.ler(27)['gpio']
            rpi.evento_falling(D0, self.zero)
            rpi.evento_falling(D1, self.um)
            while True:
                sleep(0.5)
                if len(self.bits) == 32:
                    sleep(0.1)
                    ID = int(str(self.bits), 2)
                    self.bits = ''
                    self.valida_cartao(ID)
                elif (len(self.bits) > 0) or (len(self.bits) > 32):
                    self.bits = ''
                    display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",0,True,False)
                    #return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception, e:
            Logs().logger.error('Erro lendo cartao.', exc_info=True)
        finally:
            pass

    def valida_cartao(self, id_cartao):
        try:
            cartao = Cartao()
            cartao = self.busca_id_cartao(id_cartao)
            creditos = cartao.getCreditos()
            
            if (cartao == None) or (len(str(id_cartao)) <> 10):
                display.mensagem("  Por favor...\nREPITA OPERACAO",0,True,False)
                return None
            else:
                if (cartao.getNumero() <> id_cartao):
                    print 'Cartao invalido!'
                    display.mensagem(" ID: "+str(id_cartao)+"\nNAO CADASTRADO!",3,False,False)
                    display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
                    solenoide.ativa_solenoide(1,0)
                    display.mensagem("    Bem-vindo!\nAPROXIME CARTAO",0,True,False)
                    return None
                elif (creditos == 0):
                    print 'Cartao sem credito!'
                    display.mensagem(" ID: "+str(id_cartao)+"\n SALDO NEGATIVO!",3,False,False)
                    display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
                    solenoide.ativa_solenoide(1,0)
                    display.mensagem("   Bem-vindo!\nAPROXIME CARTAO",0,True,False)
                    return None
                else:
                    print 'Cartao Valido! ID:'+ str(id_cartao)
                    display.mensagem(" ID: "+str(id_cartao)+"\n SALDO "+str(locale.currency(cartao.getValor()*creditos)).replace(".",","),1,False,False)
                    display.mensagem("     ACESSO\n    LIBERADO!",1,False,False)
                    solenoide.ativa_solenoide(1,1)
                    painel_leds.leds_se(1)
                    painel_leds.leds_x(1)
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
                            print'GIROU A CATRACA'
                            CONTA_ACESSO = 1
                            solenoide.ativa_solenoide(1,0)
                            painel_leds.leds_se(0)
                            painel_leds.leds_x(0)
                            break
                        else:
                            print 'NÃO GIROU A CATRACA' 
                            solenoide.ativa_solenoide(1,0)
                            painel_leds.leds_se(0)
                            painel_leds.leds_x(0)
                            break
                    
                    saldo_creditos = creditos - CONTA_ACESSO
                    cartao_dao = CartaoDAO()
                    cartao.setCreditos(saldo_creditos)
                    cartao.setData(datetime.now().strftime("'%Y-%m-%d %H:%M:%S'"))
                    if cartao_dao.altera(cartao):
                        print "Alterado com sucesso!"
                    else:
                        print "Erro ao alterar:"
                        print cartao_dao.getErro()
                    display.mensagem("   Bem-vindo!\nAPROXIME CARTAO",0,True,False)
                    return None
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            Logs().logger.error('Erro validando ID do cartao.', exc_info=True)
        finally:
            pass
        
    def busca_id_cartao(self, id):
        cartao_dao = CartaoDAO()
        cartao = cartao_dao.busca_id(id)
        return cartao
        