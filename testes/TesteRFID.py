#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Fornece uma leitura de números decimais de um cartão de aproximação.

O número em decimal obtido é convertido de binário para decimal cujo este
número deverá ser sempre igual a número ID do cartão RFID (Radio-Frequency
IDentification) de 13.56Mhz lido através do protocolo Wiegand por meio do
leitor de TAGs da marca HID mod. R-640X-300 iCLASS(2kbits, 16kbits, 32Kbits)
R10 Reader 6100.
"""

import time
#import RPi.GPIO as GPIO
from catraca.controle.raspberrypi.pinos import PinoControle

__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, ©"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Protótipo"


#green/data0 is pin 22
#white/data1 is pin 7

def main():

    pc = PinoControle()
    
    pc.gpio.setmode(pc.gpio.BCM)
    pc.gpio.setwarnings(False)
    
    D0 = pc.ler(17)['gpio']
    D1 = pc.ler(27)['gpio']
    
#     pc.gpio.setup(17, pc.gpio.IN)
#     pc.gpio.setup(27, pc.gpio.IN)
    
    bits = ''
    bits = '11101110000100010000010011101110'
    
    timeout = 5
    def one(channel):
        global bits
        if channel:
            bits += '1'
        
    def zero(channel):
        global bits
        if channel:
            bits += '0'
    
    pc.evento_falling(D0, one)
    pc.evento_falling(D1, zero)
    
    print "Present Card"
    while 1:
        if len(bits) == 32:
            print 25 * "-"
            print "32 Bit Mifare Card"
            print "Binary:",bits
            print "Decimal:",int(str(bits),2)
            print "Hex:",hex(int(str(bits),2))
            bits = '0'
            print 25 * "-"
            print 
            print "Present Card"
        