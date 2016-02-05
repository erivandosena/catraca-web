#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
from catraca.logs import Logs
from catraca.controle.raspberrypi.pinos import PinoControle


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Buzzer(object):

    log = Logs()
    rpi = PinoControle()
    x=0
    
    def __init__(self):
        super(Buzzer, self).__init__()
        self.pino_buzzer = self.rpi.ler(21)['gpio']

    def beeper(self, pitch, duration):
        if(pitch==0):
            sleep(duration)
            return
        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)
            
        for i in range(cycles):
            self.rpi.atualiza(self.pino_buzzer, True)
            sleep(delay)
            self.rpi.atualiza(self.pino_buzzer, False)
            sleep(delay)
            
    def play(self, tune=0):
        tune = int(tune)
        print "Reproduzindo o tom ", tune
        
        if(tune==1):
            pitches=[262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047]
            duration=0.1
            for p in pitches:
                self.beeper(p, duration)
                sleep(duration * 0.5)
                for p in reversed(pitches):
                    self.beeper(p, duration)
                    sleep(duration * 0.5)
    
        elif(tune==2):
            pitches=[262, 330, 392, 523, 1047]
            duration=[0.2, 0.2, 0.2, 0.2, 0.2, 0,5]
            for p in pitches:
                self.beeper(p, duration[self.x])
                sleep(duration[self.x] * 0.5)
                self.x+=1
                
        elif(tune==3):
            pitches=[392, 294, 0, 392, 294, 0, 392, 0, 392, 392, 392, 0, 1047, 262]
            duration=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.4]
            for p in pitches:
                self.beeper(p, duration[self.x])
                sleep(duration[self.x] * 0.5)
                self.x+=1
        
        elif(tune==4):
            pitches=[1047, 988, 659]
            duration=[0.1, 0.1, 0.2]
            for p in pitches:
                self.beeper(p, duration[self.x])
                sleep(duration[self.x] * 0.5)
                self.x+=1
        
        elif(tune==5):
            pitches=[1047, 988, 523]
            duration=[0.1, 0.1, 0.2]
            for p in pitches:
                self.beeper(p, duration[self.x])
                sleep(duration[self.x] * 0.5)
                self.x+=1
                
    def reproduzir(self, frequencia=523, duracao=0.1, repeticao=1):
        
        print "Reproduzindo..."
        print "Frequencia: ", frequencia
        print "Duracao: ", duracao
        print "Repeticao: ", repeticao
        
        pitches=[frequencia]
        duration=duracao
        while repeticao > 0:
            print repeticao
            for p in pitches:
                self.beeper(p, duration)
                sleep(duration * 0.5)
            repeticao -= 1
            
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name, "finalizado!"
        