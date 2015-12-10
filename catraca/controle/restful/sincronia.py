#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.controle.restful.relogio import Relogio


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Sincronia(Relogio):
    
    contador_status_recursos = 10

    def __init__(self, intervalo=1):
        super(Sincronia, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Sincronia'
        
    def run(self):
        print "%s. Rodando... " % self.name
        while True:
            print "periodo --------<SINCRONIA>------ "+str(Relogio.periodo)
            self.executa_controle_recursos()
            sleep(self.intervalo)

    def executa_controle_recursos(self):
        while True:
            self.contador_status_recursos += 1
            if Relogio.periodo:
                if self.contador_status_recursos >= 30:
                    self.obtem_recurso_servidor(False, True, False)
            else:
                if self.contador_status_recursos >= 1800:
                    self.obtem_recurso_servidor(False, True, True)
            break
            
    def obtem_recurso_servidor(self, display=False, mantem_tabela=False, limpa_tabela=False):
        self.contador_status_recursos = 0
        self.recursos_restful.obtem_recursos(display, mantem_tabela, limpa_tabela)
        