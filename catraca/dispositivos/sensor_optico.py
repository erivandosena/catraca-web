#!/usr/bin/env python
# -*- coding: latin-1 -*-


import pingo 
from time import sleep
from catraca import configuracao 
from catraca.dispositivos import display, leitor_rfid, solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


placa = configuracao.pinos_rpi()
sensor_1 = placa.pins[19]
sensor_2 = placa.pins[21]
sensor_1.mode = configuracao.pino_entrada()
sensor_2.mode = configuracao.pino_entrada()
baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()


def ler_sensores():
    try:
        while True:
            if (sensor_1.state == baixo) or (sensor_2.state == baixo):
                #print('Catraca aguardando GIRO <- ou ->')
                #else:    
                if sensor_1.state == alto:
                    ler_sensor_1()
                if sensor_2.state == alto:
                    ler_sensor_2()
    except KeyboardInterrupt:
        print '\nInterrompido manualmente.' # pass
    #except Exception:
    #    print '\nErro geral [Sensores].'
    finally:
        display.display("Catraca","OFFLINE",2,0)
        configuracao.limpa_pinos()
        print 'Sensor finalizado'

def ler_sensor_1(): 
    print('GIRANDO... A CATRACA NO SENTIDO HORARIO ->')
    #if (not leitor_rfid.libera_acesso()):
    if sensor_1.state == alto:
        if sensor_2.state == alto:
            solenoide.magnetiza_solenoide_2(False)
        solenoide.magnetiza_solenoide_1(True)
    else:
        solenoide.magnetiza_solenoide_1(False)

def ler_sensor_2():
    print('GIRANDO... A CATRACA NO SENTIDO ANTIHORARIO <-')
    #if (not leitor_rfid.libera_acesso()):
    if sensor_2.state == alto:
        if sensor_1.state == alto:
            solenoide.magnetiza_solenoide_1(False)
        solenoide.magnetiza_solenoide_2(True)
    else:
        solenoide.magnetiza_solenoide_2(False)

