#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle 
from catraca.dispositivos import display, leitor_rfid, solenoide, painel_leds


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


rpi = PinoControle()
sensor_1 = rpi.ler(10)['gpio']
sensor_2 = rpi.ler(9)['gpio']
baixo = rpi.baixo()
alto = rpi.alto()


def ler_sensores():
    try:
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
        painel_leds.leds_x(True)
    else:
        solenoide.magnetiza_solenoide_1(baixo)
        painel_leds.leds_x(False)
        while leitor_rfid.verifica_acesso():
            painel_leds.leds_sd(True)
        else:
            painel_leds.leds_sd(False)

def ler_sensor_2():
    print str(leitor_rfid.verifica_acesso()) + ' SENSOR 2'
    while (rpi.ler(sensor_2)['estado'] == alto) and (leitor_rfid.verifica_acesso() == False):
        if rpi.ler(sensor_1)['estado'] == alto:
            solenoide.magnetiza_solenoide_1(baixo)
        solenoide.magnetiza_solenoide_2(alto)
        painel_leds.leds_x(True)
    else:
        solenoide.magnetiza_solenoide_2(baixo)
        painel_leds.leds_x(False)
        while leitor_rfid.verifica_acesso():
            painel_leds.leds_se(True)
        else:
            painel_leds.leds_se(False)

