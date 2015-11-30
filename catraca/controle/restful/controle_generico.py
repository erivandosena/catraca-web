#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from catraca.util import Util
from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.restful.recursos_restful import RecursosRestful


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ControleGenerico(object):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    
    turno_dao = TurnoDAO()
    catraca_dao = CatracaDAO()
    
    recursos_restful = RecursosRestful()

    hora_atual = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    
    def __init__(self):
        super(ControleGenerico, self).__init__()
        self.hora_atual = self.util.obtem_hora()
        