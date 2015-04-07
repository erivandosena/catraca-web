#!/usr/bin/env python
# -*- coding: latin-1 -*-

import pingo 
from time import sleep
from catraca import configuracao 
from catraca.dispositivos import display
from catraca.dispositivos import leitor
#from catraca.dispositivos import sensor

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


placa = configuracao.pinos_rpi()

solenoide_1 = placa.pins[23]
solenoide_2 = placa.pins[13]

solenoide_1.mode = configuracao.pino_saida()
solenoide_2.mode = configuracao.pino_saida()

baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()


def magnetiza_solenoides():
    try:  
        if sensor.ler_sensor_1():
            display.display("Solenoide 1","ATRACADO!",2,0)
            magnetiza_solenoide_1()
        elif sensor.ler_sensor_2():
            display.display("Solenoide 2","ATRACADO!",2,0)
            magnetiza_solenoide_2()
    except KeyboardInterrupt:
        print '\nInterrupido manualmente' # pass
    except Exception:
        print '\nErro geral [Solenoides].'
    finally:
        #display.display("Catraca","OFFLINE",2,0)
        #configuracao.limpa_pinos()
        print 'Solenoides finalizados.'


#def solenoides(): 
#    while (solenoide_1.state == baixo) & (solenoide_2.state == baixo):
#        print('Solenoides aguardando estado dos sensores.')


def magnetiza_solenoide_1(estado):
    #if solenoide_2.state == alto:
    #solenoide_1.state = alto
    #print('SOLENOIDE 1... Atracado!')
    #    return False
    #elif solenoide_2.state == baixo:
    #solenoide_2.state = baixo
    #print('SOLENOIDE 2... Desatracado!')
    #return True
    if estado == True:
        solenoide_1.state = alto
        print('SOLENOIDE 1... Atracado!')
    else:
        solenoide_1.state = baixo
        print('SOLENOIDE 1... Desatracado!')


def magnetiza_solenoide_2(estado):
    #if solenoide_1.state == alto:
    #solenoide_2.state = alto
    #print('SOLENOIDE 2... Atracado!')
    #    return False
    #elif solenoide_1.state == baixo:
    #solenoide_1.state = baixo
    #print('SOLENOIDE 1... Desatracado!')
    #    return True
    if estado == True:
        solenoide_2.state = alto
        print('SOLENOIDE 2... Atracado!')
    else:
        solenoide_2.state = baixo
        print('SOLENOIDE 2... Desatracado!')


