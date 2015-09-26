#!/usr/bin/env python
# -*- coding: latin-1 -*-


import json
import requests


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ServidorRestful(object):
    
    URL = 'http://10.5.1.8:8888/api/'

    def __init__(self):
        super(ServidorRestful, self).__init__()
        
    def obter_servidor(self):
        return self.URL
        