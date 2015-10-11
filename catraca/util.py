#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import socket
import locale
import calendar
import datetime
from time import sleep
from catraca.logs import Logs
from catraca.controle.raspberrypi.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Util(object):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    log = Logs()
    rpi = PinoControle()
    pino_buzzer = rpi.ler(21)['gpio']
    cronometro = 0

    def __init__(self):
        super(Util, self).__init__()
        
    def obtem_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('unilab.edu.br', 0))
        ip = '%s' % ( s.getsockname()[0] )
        return ip
        
    def buzzer(self, frequencia, intensidade):
        period = 1.0 / frequencia
        delay = period / 2.0
        cycles = int(intensidade * frequencia)
        retorno = False
        for i in range(cycles):
            self.rpi.atualiza(self.pino_buzzer, True)
            sleep(delay)
            self.rpi.atualiza(self.pino_buzzer, False)
            sleep(delay)
            retorno = True
        return retorno
    
    def beep_buzzer(self, frequencia, intensidade, quantidade_beep):
        while quantidade_beep > 0:
            self.rpi.atualiza(self.pino_buzzer, True)
            self.buzzer(frequencia, intensidade)
            print 'beeep!'
            sleep(intensidade)
            self.rpi.atualiza(self.pino_buzzer, False)
            quantidade_beep -= 1
            
    def emite_beep(self, frequencia, intensidade, quantidade_beep, delay_beep):
        self.cronometro += 1
        if self.cronometro/1000 == delay_beep:
            self.beep_buzzer(frequencia, intensidade, quantidade_beep)
            
    def obtem_hora(self):
        hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
        return hora_atual
    
    def obtem_data(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")
    
    def obtem_datahora(self):
        return datetime.datetime.now()
     
    def obtem_dia_util(self):
        dia_util = True
        weekday_count = 0
        cal = calendar.Calendar()
        data_atual = datetime.datetime.now()
        for week in cal.monthdayscalendar(data_atual.year, data_atual.month):
            for i, day in enumerate(week):
                if (day == 0) or (i >= 5):
                    if (day <> 0) and (day <> data_atual.day):
                        pass
                    if day == data_atual.day:
                        dia_util = False
                    continue
                if day == data_atual.day:
                    dia_util = True
                else:
                    pass
                weekday_count += 1
        return dia_util
        