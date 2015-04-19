#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import time
from threading import Thread
from catraca.pinos import PinoControle
from dispositivos import display, leitor, sensor, painel_leds
from catraca import configuracao
from datetime import datetime

now = datetime.now()

def main():
    configuracao.desativa_avisos()
    print 'Iniciando...'
    print 'Sistema Operacional: '+ os.name
    #display.display("Iniciando...",os.name.upper(),2,2)
    #display.display("Catraca","ON-LINE",2,2)
    #display.display(str(now.day)+"/"+str(now.month)+"/"+str(now.year), str(now.hour)+":"+str(now.minute)+":"+str(now.second),2,4)
    multithread()
    #print painel_leds.leds_se(False)
    #pino = PinoControle()
    #print pino.ler(17)['gpio']
    #gpio = pino.gpio
    #print pino.pins
    #pino = pinos.pins[30]
    #pinos = pino.gpio
    #print pino.gpio.OUT
    #print pino.gpio.IN
    #print pino.gpio.PUD_UP
    #print pino.gpio.PUD_DOWN
    
    #pino.configura(30, False)
    #pino.atualiza(30, True)
    #print pino.ler(17)['estado']
    #time.sleep(3)
    #pino.atualiza(30, False)
    #print pino.ler(18)['estado']
    #print pino.ler_todos()

def multithread():
    #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
    try:
        ts = sensor.Sensor("Sensores")
        tl = leitor.Leitor("Leitor")
        tl.start()
        print tl.name + " iniciado"
        ts.start()
        print ts.name + " iniciado"

    except (SystemExit, KeyboardInterrupt):
        print '\nInterrompido manualmente'
    #except Exception:
    #    print '\nErro geral [Multithread].'
    finally:
        #configuracao.limpa_pinos()
        print 'Threads finalizadas'

