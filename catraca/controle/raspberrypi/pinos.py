#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import yaml
from catraca.controle.raspberrypi.gpio import PinosGPIO


__author__ = "Erivando Sena"
__copyright__ = "(C) Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


PINOS_YML = os.path.join(os.path.dirname(os.path.abspath(__file__)),"pinos.yml")


class PinoControle(PinosGPIO):

    def __init__(self):
        super(PinoControle, self).__init__()
        self.gpio.setmode(self.gpio.BCM)
        self.gpio.setwarnings(False)
        self.carrega_yaml()

    def carrega_yaml(self):
        try:
            with open(PINOS_YML) as file_data:
                self.pins = yaml.safe_load(file_data)
        except Exception as excecao:
            print excecao

    def pino_response(self, numero, config):
        try:
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
        except Exception as excecao:
            print excecao

    def configura(self, numero, valor):
        pino_habilitado = None
        pino_numero = int(numero)
        try:
            self.pins[pino_numero]
            self.gpio.setup(pino_numero, valor)
            pino_habilitado = self.pins[pino_numero]['modo']
        except Exception as excecao:
            print excecao
        finally:
            return pino_habilitado
            self.gpio.limpa()
            
    def atualiza(self, numero, valor):
        pino_numero = int(numero)
        try:
            self.pins[pino_numero]
            self.gpio.output(pino_numero, valor)
            estado = self.gpio.input(pino_numero)
            return estado
        except Exception as excecao:
            print excecao
            
    def estado(self, numero):
        pino_numero = int(numero)
        try:
            estado = self.gpio.input(pino_numero)
            return estado
        except Exception as excecao:
            print excecao
            
    def ler_pwm(self, numero, frequencia):
        pwm = self.gpio.PWM(numero, frequencia) 
        return pwm
        
    def ler(self, numero):
        pino_numero = int(numero)
        pino_habilitado = None
        try:
            pino_config = self.pins[pino_numero]
            if pino_config['modo'] == 'OUT':
                self.gpio.setup(pino_config['gpio'], self.gpio.OUT)
                print pino_config['nome']
            if pino_config['modo'] == 'IN':
                self.gpio.setup(pino_config['gpio'], self.gpio.IN, pull_up_down= self.gpio.PUD_UP if pino_config['resistor'] == 'PUD_UP' else self.gpio.PUD_DOWN)
                print pino_config['nome']
            pino_habilitado = self.pino_response(pino_numero, pino_config)
        except Exception as excecao:
            print excecao
        finally:
            return pino_habilitado  
            
    def ler_todos(self):
        resultados = []
        try:
            for pino_numero, pino_config in self.pins.items():
                if pino_config['modo'] == 'OUT':
                    self.gpio.setup(pino_config['gpio'], self.gpio.OUT)
                if pino_config['modo'] == 'IN':
                     self.gpio.setup(pino_config['gpio'], self.gpio.IN, pull_up_down= self.gpio.PUD_UP if pino_config['resistor'] == 'PUD_UP' else self.gpio.PUD_DOWN)
                pino_habilitado = self.pino_response(pino_numero, pino_config)
                resultados.append(pino_habilitado)
        except Exception as excecao:
            print excecao
        finally:
            return resultados
            
    def entrada(self):
        return self.gpio.IN

    def saida(self):
        return self.gpio.OUT

    def baixo(self):
        return self.gpio.LOW

    def alto(self):
        return self.gpio.HIGH

    def desativa_avisos(self):
        return self.gpio.setwarnings(False)

    def limpa(self):
        print "Limpa GPIO!"
        return self.gpio.cleanup()

    def entrada_up(self, num_pino):
        pino_habilitado = None
        try:
            pino_habilitado = self.gpio.setup(num_pino, self.gpio.IN, pull_up_down=self.gpio.PUD_UP)
        except Exception as excecao:
            print excecao
        finally:
            return pino_habilitado
            self.gpio.limpa()

    def entrada_down(self, num_pino):
        pino_habilitado = None
        try:
            pino_habilitado = self.gpio.setup(num_pino, self.gpio.IN, pull_up_down=self.gpio.PUD_DOWN)
        except Exception as excecao:
            print excecao
        finally:
            return pino_habilitado
            self.gpio.limpa()

    def evento_falling(self, num_pino, obj):
        try:
            return self.gpio.add_event_detect(num_pino, self.gpio.FALLING, callback=obj, bouncetime=1)
        except Exception as excecao:
            print excecao
            
    def evento_rising(self, num_pino, obj):
        try:
            return self.gpio.add_event_detect(num_pino, self.gpio.RISING, callback=obj, bouncetime=1)
        except Exception as excecao:
            print excecao
            
    def evento_both(self, num_pino, obj):
        try:
            return self.gpio.add_event_detect(num_pino, self.gpio.BOTH, callback=obj, bouncetime=1)
        except Exception as excecao:
            print excecao
            
    def __del__(self):
        self.limpa()
        