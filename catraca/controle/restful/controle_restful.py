#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.logs import Logs
from catraca.controle.restful.relogio import Relogio


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleRestful(Relogio, threading.Thread):
    
    log = Logs()

    def __init__(self, intervalo=1):
        super(ControleRestful, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Controle RESTFul'
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True # Daemonize thread
        #thread.start()
        
    def run(self):
        print "%s. Rodando... " % self.name
        while True:
            self.periodo
            print self.hora_atual
            sleep(self.intervalo) # delay de 1 segundo
            