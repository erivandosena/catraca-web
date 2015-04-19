#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import yaml
from catraca.gpio import PinosGPIO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


PINOS_YML = os.path.join(os.path.dirname(os.path.abspath(__file__)),"pinos.yml")


class PinoControle(PinosGPIO):

    def __init__(self):
        super(PinoControle, self).__init__()
        self.carrega_yaml()

    def carrega_yaml(self):
        with open(PINOS_YML) as file_data:
            self.pins = yaml.safe_load(file_data)

    def pino_response(self, numero, config):
        output = {
            'nome': config.get('nome'),
            'gpio': numero,
            'modo': config.get('modo'),
            'estado': self.gpio.input(numero) # 1 if config.get('modo') == 'OUT' else 0
        }
        resistor = config.get('resistor')
        if resistor:
            output['resistor'] = resistor
        #inicial = config.get('inicial')
        #if inicial:
        #    output['inicial'] = inicial
        evento = config.get('evento')
        if evento:
            output['evento'] = evento
        ressalto = config.get('ressalto')
        if ressalto:
            output['ressalto'] = ressalto
        return output

    def configura(self, numero, valor):
        pino_numero = int(numero)
        try:
            self.pins[pino_numero]
            self.gpio.setup(pino_numero, valor)
            return self.pins[pino_numero]['modo']
        except KeyError:
            return None
        except Exception:
            self.gpio.cleanup()

    def atualiza(self, numero, valor):
        pino_numero = int(numero)
        try:
            self.pins[pino_numero]
            self.gpio.output(pino_numero, valor)
            estado = self.gpio.input(pino_numero)
            if estado:
                return True
            else:
                return False
        except KeyError:
            return None
        except Exception:
            self.gpio.cleanup()

    def ler(self, numero):
        pino_numero = int(numero)
        try:
            pino_config = self.pins[pino_numero]
            if pino_config['modo'] == 'OUT':
                self.gpio.setup(pino_config['gpio'], False)
            if pino_config['modo'] == 'IN':
                self.gpio.setup(pino_config['gpio'], True, pull_up_down= self.gpio.PUD_UP if pino_config['resistor'] == 'PUD_UP' else self.gpio.PUD_DOWN)
            return self.pino_response(pino_numero, pino_config)
        except KeyError:
            return None
        except Exception:
            self.gpio.cleanup()

    def ler_todos(self):
        results = []
        try:
            for pino_numero, pino_config in self.pins.items():
                if pino_config['modo'] == 'OUT':
                    self.gpio.setup(pino_config['gpio'], False)
                if pino_config['modo'] == 'IN':
                    self.gpio.setup(pino_config['gpio'], True, pull_up_down= self.gpio.PUD_UP if pino_config['resistor'] == 'PUD_UP' else self.gpio.PUD_DOWN)
                data = self.pino_response(pino_numero, pino_config)
                results.append(data)
            return results
        except KeyError:
            return None
        except Exception:
            self.gpio.cleanup()
