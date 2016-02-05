#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.logs import Logs
from catraca.util import Util

from catraca.visao.interface.aviso import Aviso


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class VerificaRede(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    
    def __init__(self, intervalo=1):
        super(VerificaRede, self).__init__()
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Verifica Rede.'
        
    def run(self):
        print "%s Rodando... " % self.name
        while True:
            if not self.obtem_status():
                print "rede"
                self.aviso.exibir_estatus_catraca(None)
            else:
                status = self.util.obtem_ip()
                if status:
                    self.aviso.exibir_estatus_catraca(status)
                break
        sleep(self.intervalo)
    
    def obtem_status(self):
        if self.util.obtem_ip():
            return True
        else:
            return False