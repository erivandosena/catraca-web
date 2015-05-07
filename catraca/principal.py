#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import socket
from datetime import datetime
from threading import Thread
#from catraca.pinos import PinoControle
from dispositivos import display
from dispositivos import leitor
#from dispositivos import sensor



now = datetime.now()

def main():
    print 'Iniciando...'
    print 'Sistema Operacional: '+ os.name
    display.mensagem("Iniciando...\n"+os.name.upper(),1,False,False)
    
    display.mensagem(datetime.now().strftime('%d de %B %Y \n    %H:%M:%S'),2,False,False)
    #display.mensagem(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n"+str(now.hour)+":"+str(now.minute)+":"+str(now.second),2,False,False)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    ip = ' IP %s' % ( s.getsockname()[0] )
    display.mensagem("Catraca 1 ONLINE\n"+ip,2,False,False)

    
    multithread()

def multithread():
    #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
    try:
        #ts = sensor.Sensor("Sensores")
        tl = leitor.Leitor("Leitor")
        tl.start()
        print tl.name + " iniciado"
        #ts.start()
        #print ts.name + " iniciado"

    except (SystemExit, KeyboardInterrupt):
        print '\nInterrompido manualmente'
    #except Exception:
    #    print '\nErro geral [Multithread].'
    finally:
        print 'Threads finalizadas'
