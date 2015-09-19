#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
from threading import Thread
from catraca.logs import Logs
from catraca.dispositivos.registro_cliente import RegistroCliente


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ClienteRestFul(Thread):
    
    log = Logs()

    def __init__(self):
        super(ClienteRestFul, self).__init__()
        Thread.__init__(self)
        self.name = 'Thread Cliente RESTFul'

    def run(self):
        print "%s Rodando... " % self.name
        registro = RegistroCliente()
        sleep(13000)
        lista = registro.obtem_registros()
        if lista is not []:
            registro.post()
            self.log.logger.info('POST do Registro no servidor')
        