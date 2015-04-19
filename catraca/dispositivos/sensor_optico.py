#!/usr/bin/env python
# -*- coding: latin-1 -*-


#import pingo 
from time import sleep
from catraca.pinos import PinoControle
from catraca import configuracao 
from catraca.dispositivos import display, leitor_rfid, solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


#placa = configuracao.pinos_rpi()
rpi = PinoControle()
sensor_1 = rpi.ler(10)['gpio']#placa.pins[19]
sensor_2 = rpi.ler(9)['gpio']#placa.pins[21]
#sensor_1.mode = configuracao.pino_entrada()
#sensor_2.mode = configuracao.pino_entrada()
baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()


def ler_sensores():
    try:
        print rpi.ler(sensor_1)['estado']
        print baixo
        while True:
            #if (sensor_1.state == baixo) or (sensor_2.state == baixo):
            if (rpi.ler(sensor_1)['estado'] == baixo) or (rpi.ler(sensor_2)['estado'] == baixo):   
                if rpi.ler(sensor_1)['estado'] == alto:
                    ler_sensor_1()
                if rpi.ler(sensor_2)['estado'] == alto:
                    ler_sensor_2()
    except KeyboardInterrupt:
        print '\nInterrompido manualmente.' # pass
    #except Exception:
    #    print '\nErro geral [Sensores].'
    finally:
        display.display("Catraca","OFFLINE",2,0)
        #configuracao.limpa_pinos()
        print 'Sensor finalizado'

def ler_sensor_1():
    print str(leitor_rfid.verifica_acesso()) + ' SENSOR 1'
    while (rpi.ler(sensor_1)['estado'] == alto) and (leitor_rfid.verifica_acesso() == False):
        if rpi.ler(sensor_2)['estado'] == alto:
            solenoide.magnetiza_solenoide_2(baixo)
        solenoide.magnetiza_solenoide_1(alto)
    else:
        solenoide.magnetiza_solenoide_1(baixo)

def ler_sensor_2():
    print str(leitor_rfid.verifica_acesso()) + ' SENSOR 2'
    while (rpi.ler(sensor_2)['estado'] == alto) and (leitor_rfid.verifica_acesso() == False):
        if rpi.ler(sensor_1)['estado'] == alto:
            solenoide.magnetiza_solenoide_1(baixo)
        solenoide.magnetiza_solenoide_2(alto)
    else:
        solenoide.magnetiza_solenoide_2(baixo)

