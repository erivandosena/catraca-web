#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
from catraca.logs import Logs


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class MensagemCondicao(object):
    
    log = Logs()
    
    def __init__(self):
        super(MensagemCondicao, self).__init__()
        
    def __init__(self, seconds=10):
        self.run_time = seconds
        self.start_time = time.time()
        
    @property
    def condition(self):
        return time.time()-self.start_time < self.run_time