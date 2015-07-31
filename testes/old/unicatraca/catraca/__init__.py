#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from flask import Flask 
from dispositivos import sensor

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Universidade da Integração Internacional da Lusofonia Afro-Brasileira" 
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production 

app = Flask(__name__)
app.config.from_object('config.Config')


from routes import bootstrap 
bootstrap.init_app(app)

import catraca.routes

sensor.ativaChaveOptica1
