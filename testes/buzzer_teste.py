#!/usr/bin/env python
# -*- coding: latin-1 -*-

from multiprocessing import Process
from threading import Thread
import sys
import os
import time
import socket
import locale
import datetime
import subprocess
from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos.sensoroptico import SensorOptico
from catraca.dao.catracadao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect(('unilab.edu.br', 0))
IP = '%s' % (socket.getsockname()[0])

log = Logs()
rpi = PinoControle()
pino_buzzer = rpi.ler(21)['gpio']

sensor_optico = SensorOptico()
catraca_dao = CatracaDAO()

catraca = None
cronometro = 0

def main():
    print 'Iniciando os testes buzzer...'

    def buzzer(frequencia, intensidade):
        period = 1.0 / frequencia
        delay = period / 2.0
        cycles = int(intensidade * frequencia)
        retorno = False
        for i in range(cycles):
            rpi.atualiza(pino_buzzer, True)
            time.sleep(delay)
            rpi.atualiza(pino_buzzer, False)
            time.sleep(delay)
            retorno = True
        return retorno
    
        
    def beep_buzzer(frequencia, intensidade):
        while True:
            rpi.atualiza(pino_buzzer, True)
            buzzer(frequencia,intensidade)
            time.sleep(intensidade)
            rpi.atualiza(pino_buzzer, False)


    def obtem_catraca():
        return catraca_dao.busca_por_ip(IP)
    
    def ler_cartao(tempo):
        global catraca
        catraca = obtem_catraca()
        teste = '11101110000100010000010011101110'
        while True:
            sleep(1)
            if len(teste) == 32:
                while not ler_sensor(tempo):
                    teste = ''
                    break
            elif (len(teste) > 0) or (len(teste) > 32):
                print 'nao ler'
    
    def ler_sensor(tempo):
        finaliza_giro = True
        global cronometro
        while True:
            cronometro += 1
            print str(cronometro) + '/'+ str(tempo/1000)
            sensor_optico.registra_giro(tempo, cronometro, catraca)
#             if not cronometro == (tempo/1000):
#                 if sensor_optico.registra_giro(tempo, cronometro, catraca):
#                     finaliza_giro = True
#                 else:
#                     finaliza_giro = False
#                     print 'faço algo'
#                     break
#                 obtem_codigo('00')
#                 print 'no tempo'
#             else:
#                 finaliza_giro = False
#                 print 'fim de tempo'
#                 break
        else:
            finaliza_giro = False
            print 'fim do tempo'
                
        return finaliza_giro
        
#         detecta_giro = sensor_optico.registra_giro(6000, catraca)
#         print obtem_catraca().operacao
#         while True:  
#             #if sensor_optico.registra_giro(6000, obtem_catraca):
#             if detecta_giro:
#                 print str(detecta_giro) + ' girou' 
#             else:
#                 print str(detecta_giro) + ' não girou'


    def obtem_codigo(codigo):
        opcoes = {
                   '00' : sensor_optico.beep_buzzer(860, 1, 2),
                   '01' : '    Professor',
                   '10' : '     Tecnico',
                   '11' : '    Visitante',
        }
        return opcoes.get(codigo,False)
        
        
    ler_cartao(15000)


    #beep_buzzer(860, .8)

    #beep_pwm(15, 850)
    #rpi.atualiza(pino_buzzer, False)
    
    
            
#     def beep_pwm(ciclo, frequencia):
#         p = rpi.ler_pwm(pino_buzzer, frequencia)
#         p.start(ciclo) 
#         while True:
#             rpi.atualiza(pino_buzzer, False)
#             p.ChangeFrequency(frequencia)
#             time.sleep(5)    
    
    
#     while True:
#         print("Beeep...")
#         buzzer(860,.7)
#         time.sleep(.7)

            
    
#     #beep_buzzer(1/440)
#     p = rpi.ler_pwm(pino_buzzer, 50)
#     #p = GPIO.PWM(25, 50)
#     p.start(15) 
#     #p.ChangeDutyCycle(25) 
#     p.ChangeFrequency(50) 
#     scale=[262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524, 825, 850, 990, 995]
#     scale=[850]
#     beep = 25
#     while True:
#         # Percorrer cada valor PWM e jogÃ¡-lo no buzzer
#         a=0
#         while a < 1:
#             #p.ChangeDutyCycle(.1)
#             p.ChangeFrequency(scale[a])
#             print str(scale[a])
#             time.sleep(.8)
#             a=a+1
            
            
            
#             for dc in range(0, 101, 5):
#                 p.ChangeDutyCycle(dc)
#                 time.sleep(0.1)
#             for dc in range(100, -1, -5):
#                 p.ChangeDutyCycle(dc)
#                 time.sleep(0.1)

      
#     def loop_a():
#         while 1:
#             print("a")
#             buzzer(850,.8)
#           
#     def loop_b():
#         while 1:
#             print("b")
#             buzzer(850,.8)
#               
#     def loop_c():
#         while 1:
#             print("b")
#             buzzer(850,.8)
#   
#     try:
#           
#         Process(target=loop_a).start()
#         Process(target=loop_b).start()
# 
#       
#     finally:
#         rpi.atualiza(pino_buzzer, False)
#           
#     rpi.atualiza(pino_buzzer, False)


#     scale=[262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524, 990, 995]
#     scale = 780
#     a=0
#     while True:
#         #p.ChangeFrequency(scale[a])
#         scale = 825
#         print buzzer(scale,.8)
#         time.sleep(.8)
#         print str('Frequencia: '+ str(scale))
#         a+=1
        
         
    #rpi.atualiza(pino_buzzer, False)
    
     
#     time.sleep(.5)
#     Process(target=loop_b).start()
#   
#     while True:
#         print("Beeep...")
#         buzz(980,.2)
#         time.sleep(.5)


    
#     rpi.atualiza(pino_buzzer, True)

#     rpi.atualiza(pino_buzzer, False)
    
    
#     def loopA():
#         for i in range(10):
#             #Do task A
#             print 'A'
#             buzz(340,0.5)
#             
#     def loopB():
#         for i in range(10):
#             #Do task B
#             print 'B'
#             buzz(340,0.5)
#             
#     threadA = Thread(target = loopA())
#     threadB = Thread(target = loopB())
#     threadA.run()
#     threadB.run()
#     # Faz o trabalho indepedent de LoopA e LoopB
#     threadA.join()
#     threadB.join()
    
#     while True:    
#         buzz(340,0.5)

#     # Set-up a campainha como um PWM . Isso nos permite reproduzir diferentes tons em um pino GPIO
#     myPWM=rpi.ler_pwm(pino_buzzer, 1)
#     myPWM.start(1)
#  
#     # Definir os valores PWM necessÃ¡rio para reproduzir diferentes tons na campainha
#     scale=[262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 524]
#      
#     try:
#         while True:
#             # Percorrer cada valor PWM e jogÃ¡-lo no buzzer
#             a=0
#             while a < 13:
#                 print a
#                 myPWM.ChangeFrequency(scale[a])
#                 time.sleep(0.5)
#                 a=a+1
#     finally:
#         pass

#     def __del__():
#         print 'finalizou!'
#         rpi.atualiza(pino_buzzer, False)
