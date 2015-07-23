#!/usr/bin/env python
# -*- coding: latin-1 -*-

import locale
from time import sleep
from catraca.pinos import PinoControle
from catraca.dispositivos import display
from catraca.dispositivos import painel_leds
from catraca.dao.cartaodao import Cartao
from catraca.dao.cartaodao import CartaoDAO
#from catraca.dispositivos import sensor_optico
from catraca.dispositivos.sensor_optico import SensorOptico
from catraca.dispositivos import solenoide
from catraca.dispositivos.leitorcartao import LeitorCartao

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
D0 = rpi.ler(17)['gpio']
D1 = rpi.ler(27)['gpio']

baixo = rpi.baixo()
alto = rpi.alto()
bits = ''
numero_cartao = ''
conta_acesso = 0
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def zero(self):
    global bits
    bits = bits + '0'

def um(self):
    global bits
    bits = bits + '1' 

def ler_cartao():
    display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
    global bits
    global numero_cartao
    try:
        rpi.evento_falling(D0, zero)
        rpi.evento_falling(D1, um)
        while True:
            sleep(0.5)
            if len(bits) == 32:
                sleep(0.1)
                numero_cartao = int(str(bits), 2)
                valida_cartao(numero_cartao)
                bits = ''
            elif (len(bits) > 0) or (len(bits) > 32):
                bits = ''
                display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",0,True,False)
                
    except KeyboardInterrupt:
        print '\nInterrompido manualmente' # pass
    #except Exception:
        #print '\nErro geral [Leitor RFID].'
    finally:
        print 'Leitor RFID finalizado'


#def busca_cartao(id):
#    cartao_dao = CartaoDAO()
#    cartao = cartao_dao.busca(id)
#    return cartao

def busca_id_cartao(id):
    cartao_dao = CartaoDAO()
    cartao = cartao_dao.busca_id(id)
    return cartao

def cartao():
    lc = LeitorCartao()
    display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
    id_cartao = lc.ler()
    if id_cartao == None:
        display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",0,True,False)
    else:
        ler_cartao(id)


def valida_cartao(id_cartao):
    cartao = busca_id_cartao(id_cartao)
    creditos = cartao.getCreditos()
    
    if (cartao == None) or (len(str(id_cartao)) <> 10):
        display.mensagem("  Por favor...\nREPITA OPERACAO",0,True,False)
        return None
    else:
        if (cartao.getNumero() <> id_cartao):
            print 'Cartao invalido!'
            ACESSO = False
            display.mensagem(" ID: "+str(id_cartao)+"\nNAO CADASTRADO!",3,False,False)
            display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
            solenoide.ativa_solenoide(1,baixo)
            display.mensagem("    Bem-vindo!\nAPROXIME CARTAO",0,True,False)
            return None
        elif (creditos == 0):
            print 'Cartao sem credito!'
            ACESSO = False
            display.mensagem(" ID: "+str(id_cartao)+"\n SALDO NEGATIVO!",3,False,False)
            display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
            solenoide.ativa_solenoide(1,baixo)
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
            giro = SensorOptico()
            while True:
                if giro.registra_giro(6000):
                    print'GIROU A CATRACA'
                    solenoide.ativa_solenoide(1,baixo)
                    painel_leds.leds_se(0)
                    painel_leds.leds_x(0)
                    break
                else:
                    print 'NÃO GIROU A CATRACA' 
                    solenoide.ativa_solenoide(1,baixo)
                    painel_leds.leds_se(0)
                    painel_leds.leds_x(0)
                    break
            
            #saldo_creditos = creditos - CONTA_ACESSO
            cartao = Cartao()
            cartao_dao = CartaoDAO()
            #cartao.setCreditos(saldo_creditos)
            #if cartao_dao.altera(cartao):
            #    print "Alterado com sucesso!"
            #else:
            #    print "Erro ao alterar:"
            #    print cartao_dao.getErro()
            display.mensagem("   Bem-vindo!\nAPROXIME CARTAO",0,True,False)
            return None
