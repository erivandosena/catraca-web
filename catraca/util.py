#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pwd
import time
import socket
import locale
import calendar
import datetime
import subprocess
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
    hora_stop = None
    
    def __init__(self):
        super(Util, self).__init__()
        
    def obtem_ip(self):
        exibe = False
        ip = None
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.settimeout(2)
            s.connect(('unilab.edu.br',0))
            ip = '%s' % ( s.getsockname()[0] )
            #return ip
        except Exception as excecao:
            exibe = True
            self.aviso.exibir_estatus_catraca(None)
            print "Erro obtendo unilab.edu.br"
            self.log.logger.error('Erro obtendo conexao!', exc_info=True)
        finally:
            if exibe:
                from catraca.visao.interface.aviso import Aviso
                Aviso().exibir_estatus_catraca(ip)
            s.close()
            return ip
        
    def obtem_nome_sistema(self):
        return os.name
    
    def obtem_nome_rpi(self):
        return socket.gethostname()
    
    def obtem_nome_root_rpi(self):
        return pwd.getpwuid(os.getuid())[0]
    
    def obtem_path(self, arquivo):
        return "%s" % (os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo))
        
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
            
    def beep_buzzer_delay(self, frequencia, intensidade, quantidade_beep, delay_beep):
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
    
    def obtem_data_formatada(self):
        return datetime.datetime.now().strftime("%d/%m/%Y")
    
    def obtem_datahora_display(self):
        return datetime.datetime.now().strftime('%d/%m/%Y %H:%M') # %d/%B/%Y
    
    def obtem_datahora_postgresql(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     
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
    
    def reinicia_raspberrypi(self):
        terminal = 'sudo reboot'
        subprocess.call(terminal.split())
        
    def desliga_raspberrypi(self):
        terminal = 'sudo shutdown -h now'
        subprocess.call(terminal.split())
        
    def obtem_tempo_decorrido(self, minutos):
        if self.hora_stop is None:
            self.hora_stop = self.util.obtem_datahora()
            hora_start = self.hora_stop
            self.hora_stop += datetime.timedelta(minutes=minutos)
            
            print "====start=====> " + str( hora_start.strftime('%H:%M:%S'))
            print "====stop======> " + str( self.hora_stop.strftime('%H:%M:%S'))
        
        if  self.util.obtem_datahora() >= self.hora_stop:
            self.hora_stop = None
            return False
        else:
            return True
        
    def subtrai_minuto(self, hora, minutos):
        print hora.strftime('%H:%M:%S')
        hora_prevista = datetime.datetime.strptime(hora.strftime('%H:%M:%S'),'%H:%M:%S') - datetime.timedelta(minutes=minutos)
        print hora_prevista.time()
        return hora_prevista.time()
    
    def converte_ip_para_long(self, ip):
        ip2int = lambda ip: reduce(lambda a, b: (a << 8) + b, map(int, ip.split('.')), 0)
        return ip2int(ip)
    
    def converte_long_para_ip(self, long):
        int2ip = lambda long: '.'.join([str(nlong >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])
        return int2ip(long)
    
    def obtem_cpu_temp(self):
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return str(float(cpu_temp)/1000.0) #(Fahrenheit) 1000.0 * 9/5 + 32

#         tempFile = open("/sys/class/thermal/thermal_zone0/temp")
#         cpuTemp0 = tempFile.read()
#         cpuTemp1 = float(cpuTemp0)/1000.0
#         cpuTemp2 = float(cpuTemp0)/100
#         cpuTempM = (cpuTemp2 % cpuTemp1)
#         return str(cpuTemp1)+"."+str(cpuTempM)
    
    def obtem_cpu_speed(self):
        tempFile = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
        cpu_speed = tempFile.read()
        tempFile.close()
        return str(float(cpu_speed)/1000)

    
        