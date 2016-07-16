#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import pwd
import time
import fcntl
import struct
import socket
import random
import locale
import calendar
import datetime

import codecs 
from tempfile import mkstemp
from shutil import move

from unicodedata import normalize

import subprocess
from time import sleep
from catraca.controle.dispositivos.buzzer import Buzzer
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Util(object):
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    buzzer = Buzzer()
    catraca_dao = CatracaDAO()
    
    cronometro = 0
    hora_stop = None
    
    def __init__(self):
        super(Util, self).__init__()
        
    def obtem_nome_sistema(self):
        return os.name
    
    def obtem_nome_rpi(self):
        return socket.gethostname()
    
    def obtem_nome_root_rpi(self):
        return pwd.getpwuid(os.getuid())[0]
    
    def obtem_path(self, arquivo):
        return "%s" % (os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo))
    
    def beep_buzzer(self, frequencia, intensidade, quantidade_beep):
        self.buzzer.reproduzir(frequencia, intensidade, quantidade_beep)
        
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
    
    def converte_data_string(self, data_hora):
        dh = datetime.strptime(data_hora, '%Y-%m-%d %H:%M:%S')
        return str(dh.strftime('%d/%m/%Y %H:%M'))
    
    def converte_ip_para_long(self, ip):
        try:
            ip2int = lambda ip: reduce(lambda a, b: (a << 8) + b, map(int, ip.split('.')), 0)
        except Exception as excecao:
            print excecao
            return ip2int("127.0.0.1")
        return ip2int(ip)
    
    def converte_long_para_ip(self, long):
        int2ip = lambda long: '.'.join([str(nlong >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])
        return int2ip(long)
    
    def obtem_cpu_temp(self):
        """Retorna a velocidade atual da CPU."""
        try:
            s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
            return str(float(s.split('=')[1][:-3]))
        except:
            return "0"
    
    def obtem_cpu_speed(self):
        tempFile = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
        try:
            cpu_speed = tempFile.read()
            return str(float(cpu_speed)/1000)
        except:
            return "0"
        finally:
            tempFile.close()
            
    def obtem_ram(self):
        """Retorna uma tupla (total de RAM, memória RAM disponível) em megabytes."""
        try:
            s = subprocess.check_output(["free","-m"])
            lines = s.split('\n')
            ram = (int(lines[1].split()[1]), int(lines[2].split()[3]))
            return str(ram[1])+'Mb de ('+str(ram[0])+'Mb)'
        except:
            return "0" 
        
    def obtem_process_count(self):
        """Retorna o número de processos."""
        try:
            s = subprocess.check_output(["ps","-e"])
            return str(len(s.split('\n')))
        except:
            return "0"
        
    def obtem_up_time(self):
        """Retorna uma tupla ( tempo de atividade, média de carga 5 min)."""
        try:
            s = subprocess.check_output(["uptime"])
            load_split = s.split('load average:')
            load_five = float(load_split[1].split(',')[1])
            up = load_split[0]
            up_pos = up.rfind(',',0,len(up)-4)
            up = up[:up_pos].split('up ')[1]
            up_stats = (up, load_five)
            return str(up_stats[0])
        except:
            return str(('', 0))
            
    def obtem_connections(self):
        """Retorna o número de conexões de rede."""
        try:
            s = subprocess.check_output(["netstat","-tun"])
            return str(len([x for x in s.split() if x == 'ESTABELECIDA']) or len([x for x in s.split() if x == 'ESTABLISHED']))
        except:
            return "0"
    
    def obtem_temperature(self):
        """Retorna a temperatura em grau celsius °C."""
        try:
            s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
            return str(float(s.split('=')[1][:-3]))
        except:
            return "0"
        
    def obtem_ip_por_interface(self, interface=None):
        exibe = False
        if interface is None:
            interface = self.catraca_dao.obtem_interface_rede(self.obtem_nome_rpi())
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', interface[:15]))[20:24])
            return ip
        except Exception as excecao:
            #print excecao
            ip = "127.0.0.1"
            exibe = True
            print "Erro ao obter ip!"
            return ip
        finally:
            pass
#             if exibe:
#                 from catraca.visao.interface.aviso import Aviso
#                 Aviso().exibir_estatus_catraca(ip)
                
    def obtem_MAC_por_interface(self, interface=None):
        mac = None
        if interface is None:
            interface = self.catraca_dao.obtem_interface_rede(self.obtem_nome_rpi())
        try:
            arquivo = "/sys/class/net/" + interface + "/address"
            if self.verifica_arquivo(arquivo):
                str = open(arquivo).read()
                mac = str[0:17]
            else:
                mac = "00:00:00:00:00:00"
        except Exception as excecao:
            print excecao
            mac = "00:00:00:00:00:00"
        return mac
        
    def altera_hostname(self, novo_nome):
        self.substitui_string_arquivo("/etc/hosts", self.obtem_nome_rpi(), novo_nome)
        self.substitui_string_arquivo("/etc/hostname", self.obtem_nome_rpi(), novo_nome)
        subprocess.call('/etc/init.d/hostname.sh')
        
    def substitui_string_arquivo(self, local_arquivo, str_atual, str_novo):
        with codecs.open(local_arquivo, 'r+', 'utf-8') as arq:
            content = arq.read()
            arq.seek(0)
            arq.truncate()
            arq.write(content.replace(str_atual, str_novo))
            
#     def remove_chr(self, old, to_remove):
#         new_string = old
#         for x in to_remove:
#             new_string = new_string.replace(x, '')
#         return new_string
    
    def substitui_espaco(self, texto):
        vogais = " "
        for espaco in vogais:
            texto = texto.replace(espaco, "_")
        return texto
    
    def remove_acentos_caracteres(self, texto, codif='utf-8'):
        return normalize('NFKD', texto.decode(codif)).encode('ASCII','ignore')
    
    def obtem_string_normalizada(self, str):
        return self.remove_acentos_caracteres( self.substitui_espaco(str) )
    
    def verifica_pasta(self, dir):
        if os.path.exists(dir):
            return True
        else:
            return False
    
    def verifica_arquivo(self, arq):
        if os.path.isfile(arq):
            return True
        else:
            return False