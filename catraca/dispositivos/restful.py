#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
from threading import Thread
from catraca.logs import Logs
from catraca.restful.servidor import app


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RestFul(Thread):
    
    log = Logs()

    def __init__(self):
        super(RestFul, self).__init__()
        Thread.__init__(self)
        self.name = 'Thread RESTFul'

    def run(self):
        print "%s Rodando... " % self.name
        app.run(host='10.5.2.253', port=27289)
        
