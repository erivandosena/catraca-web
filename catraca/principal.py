#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import time
from threading import Thread
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
    #multithread()
    print painel_leds.acende_senta_direira()

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

