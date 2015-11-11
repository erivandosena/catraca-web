#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.logs import Logs
from catraca.controle.restful.recursos_restful import RecursosRestful
from catraca.controle.restful.relogio import Relogio


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ClienteRestful(threading.Thread, Relogio):
    
    log = Logs()
    recursos_restful = RecursosRestful()
    intervalo_recursos = 15

    def __init__(self, intervalo=1.5):
        super(ClienteRestful, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Cliente RESTFul'
        thread = threading.Thread(target=self.run(), args=())
        thread.daemon = True # Daemonize thread
        #thread.start()
        
    def run(self):
        print "%s. Rodando... " % self.name
        while True:
            if self.periodo:
                print "intervalo_recursos = 15"
                self.intervalo_recursos = 15
                self.obtem_recursos(self.intervalo_recursos)
            else:
                print "intervalo_recursos = 3600"
                self.intervalo_recursos = 3600
                self.obtem_recursos(self.intervalo_recursos)
            sleep(self.intervalo)# delay de 1 segundo
            
    def obtem_recursos(self, intervalo_recursos):
        if intervalo_recursos == 15:
            print "dentro do horario de funcionamento"
            while True:
                if self.turno is None:
                    break
                print "##### obtendo RECURSOS ######"
                self.recursos_restful.obtem_recursos()
                sleep(self.intervalo_recursos)  
        elif intervalo_recursos == 3600:
            print "fora do horario de atendimento"
            while True: 
                if self.turno:
                    break
                print "##### obtendo RECURSOS ######"
                self.recursos_restful.obtem_recursos()
                sleep(self.intervalo_recursos)
                