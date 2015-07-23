#!/usr/bin/env python
# -*- coding: latin-1 -*-

import locale
from time import sleep
from threading import Thread
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos import display
from catraca.dispositivos import painel_leds
from catraca.dao.cartaodao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.dispositivos.sensor_optico import SensorOptico
from catraca.dispositivos import solenoide
from catraca.dispositivos.leitorcartao import LeitorCartao

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Acesso(Thread):
    def __init__(self):
        super(Acesso, self).__init__()

    def run(self):
        self.ler_cartao()
        
    def ler_cartao(self):
        try:
            LeitorCartao().ler()
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            Logs().logger.error('Erro iniciando leitura do cartao.', exc_info=True)
        finally:
            pass
            