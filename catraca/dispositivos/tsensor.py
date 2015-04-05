!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
from threading import Thread
from time import sleep, ctime, time
import pingo
from catraca import configuracao
from catraca.dispositivos import display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ThreadSensor(Thread):

    BAIXO = configuracao.pino_baixo()
    ALTO = configuracao.pino_alto()

    def __init__(self, nome, pino, modo, estado):
        Thread.__init__(self)
        self.nome = nome
        self.pino = pino
        self.modo = modo
        self.estado = estado

    def run(self):
        print self.nome + "Iniciado"
        ler_sensor(self)

def ler_sensor(self):
    try:
        while True:
            if self.estado == BAIXO:
                display.display("Aguardando GIRO","<- ou ->",2,0)
                sys.stdout.write("Aguardando GIRO <- ou ->")
                sys.stdout.flush()
            else:    
                if self.estado == ALTO:
                    display.display("GIRANDO...","HORARIO ->",2,0)
                    sys.stdout.write("GIRANDO... HORARIO ->")
                    sys.stdout.flush()

    except KeyboardInterrupt:
        print '\nInterrupido manualmente' # pass
    except Exception:
        print '\nErro geral [Sensores].'
    finally:
        #display.display("Catraca","OFFLINE",2,0)
        #configuracao.limpa_pinos()
        print 'Sensor finalizado'

def print_time(threadName, delay):
    while True:
        #if exitFlag:
        #    thread.exit()
        sleep(delay)
        print "%s: %s" % (threadName, ctime(time()))
        #counter -= 1

