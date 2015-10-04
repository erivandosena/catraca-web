#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import threading
from time import sleep
from catraca.logs import Logs
from catraca.restful.servidor_restful import ServidorRestful
from catraca.restful.registro_restful import RegistroRestful


#from catraca.restful.registro_cliente import RegistroCliente
__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ClienteRestful(threading.Thread):
    
    log = Logs()
    registro_restful = RegistroRestful()

    def __init__(self, intervalo=10):
        super(ClienteRestful, self).__init__()
        threading.Thread.__init__(self)
        self.name = 'Thread Cliente RESTFul'
        self.intervalo = intervalo
        thread = threading.Thread(group=None, target=self.processa, args=())
        thread.daemon = True # Daemonize thread
        thread.start()
        print "%s. Rodando... " % self.name

#     def run(self):
#         pass
            
    def processa(self):
        while True:
            print 'faço algo'
            registro = self.registro_restful.obtem_registro(9)
            print self.registro_restful.objeto_para_json(registro)
            sleep(self.intervalo)
            break


        