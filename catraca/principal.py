#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import time
from datetime import datetime
from threading import Thread
from catraca.pinos import PinoControle
from dispositivos import display
from dispositivos import leitor
from dispositivos import sensor
from dispositivos import painel_leds
#from persistencia.cartao import ModeloCartao

now = datetime.now()

def main():
    print 'Iniciando...'
    print 'Sistema Operacional: '+ os.name
    #display.display("Iniciando...",os.name.upper(),2,2)
    #display.display("Catraca","ON-LINE",2,2)
    #display.display(str(now.day)+"/"+str(now.month)+"/"+str(now.year), str(now.hour)+":"+str(now.minute)+":"+str(now.second),2,4)
    #cartao = ModeloCartao()
    #linhas = cartao.selecionar()
    #import pprint
    #print '===================================='
    #pprint.pprint(linhas)
    #linhas = cartao.atualizar(100, 1)
    #import pprint
    #print '===================================='
    #pprint.pprint(linhas)
    #multithread()

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
        print 'Threads finalizadas'

