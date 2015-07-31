#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from catraca import app
from flask import render_template, request, flash, session, url_for, redirect
from flask_bootstrap import Bootstrap
#from dispositivos import sensor

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Universidade da Integração Internacional da Lusofonia Afro-Brasileira"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


bootstrap = Bootstrap()

@app.route('/') 
def home():
    return render_template('index.html') #'<h1>Raspberry Pi, ON!</h1>'

@app.route('/about')
def about():
    return 'Projeto Catracas utilizando um pequeno dispositivo open source chamado <a href="http://www.raspberrypi.org/" target="_blank">Raspberry Pi</a>. <a href="javascript:window.history.go(-1)">Voltar</a>'

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return 'Acesso não permitido. <a href="javascript:window.history.go(-1)">Voltar</a>'

@app.route('/signout')
def signout():
    return 'Não logado. <a href="javascript:window.history.go(-1)">Voltar</a>'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'Envio de formulário. <a href="javascript:window.history.go(-1)">Voltar</a>'

@app.route("/gpio")
def gpio():
    return 'Status dos pinos GPIO. <a href="javascript:window.history.go(-1)">Voltar</a>'

#def testa_sensor():
    print sensor.ativaChaveOptica1
