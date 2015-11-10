#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.controle.restful.relogio import Relogio
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.recursos.catraca_json import CatracaJson


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleRestful(Relogio, threading.Thread):
    
    log = Logs()
    util = Util()
    catraca_dao = CatracaDAO()

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
            # verifica se existe catraca cadastrada
            if self.catraca_dao.busca_por_ip(self.util.obtem_ip()) is None:
                print " PASSOU ==>>>> if self.catraca_dao.busca_por_ip(self.util.obtem_ip()) is None:"
                CatracaJson().catraca_get()
            periodo = self.periodo
            print periodo
            print self.hora_atual
            sleep(self.intervalo) # delay de 1 segundo
            