#!/usr/bin/env python
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


class Sensores(Thread):

    placa = configuracao.pinos_rpi()
    BAIXO = configuracao.pino_baixo()
    ALTO = configuracao.pino_alto()

    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        self.sensor_1 = self.placa.pins[19]
        self.sensor_2 = self.placa.pins[21]
        self.sensor_1.mode = configuracao.pino_entrada()
        self.sensor_2.mode = configuracao.pino_entrada()

    def run(self):
        print self.nome + " iniciados"
        ler_sensores(self)

def ler_sensores(self):
    try:       
        while True:
            if (self.sensor_1.state == self.BAIXO) & (self.sensor_2.state == self.BAIXO):
                sys.stdout.write("Catraca aguardando GIRO <- ou -> \n")
                sys.stdout.flush()
            else:
                if self.sensor_1.state == self.ALTO:
                    print("GIRANDO... A CATRACA NO SENTIDO HORARIO ->")
                if self.sensor_2.state == self.ALTO:
                    print("GIRANDO... A CATRACA NO SENTIDO ANTIHORARIO <-")

    except KeyboardInterrupt:
        print '\nInterrupido manualmente' # pass
    #except Exception:
    #    print '\nErro geral [Sensores].'
    finally:
        display.display("Catraca","OFFLINE",2,0)
        configuracao.limpa_pinos()
        print 'Sensor finalizado'



