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
import RPi.GPIO as GPIO

__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, Unilab"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Protótipo"


def DesativaSolenoide1():
    GPIO.output(19,True) ## Turn on GPIO pin 35
    time.sleep(2);
    GPIO.output(19,False)
    time.sleep(4);
    GPIO.output(19,True)
    time.sleep(2);
    GPIO.output(19,False)
    
def DesativaSolenoide2():
    GPIO.output(26,True) ## Turn on GPIO pin 37
    time.sleep(10);
    #GPIO.output(26,False)
    #time.sleep(4);
    #GPIO.output(26,True)
    #time.sleep(2);
    GPIO.output(26,False)

def main():
    """Bloco principal do programa.
    """

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) ## Use board pin numbering
    GPIO.setup(19, GPIO.OUT) ## Setup GPIO Pin 35 to OUT
    GPIO.setup(26, GPIO.OUT) ## Setup GPIO Pin 37 to OUT

    #DesativaSolenoide1()
    DesativaSolenoide2()

    GPIO.cleanup()

if __name__ == '__main__':
    main()
