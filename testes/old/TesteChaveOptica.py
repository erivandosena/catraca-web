#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Uma descrição resumida sobre o documento.

Descrição detalhada sobre o documento.
"""

# Imports
import RPi.GPIO as GPIO

__author__ = "erivando"
__copyright__ = "Copyright 2015, Unilab"
__credits__ = ["erivando", ""]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "erivando"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Desenvolvimento"


def main():
    """Bloco principal do programa.
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    #ativaChaveOptica1()
    ativaChaveOptica2()
    GPIO.cleanup()

def ativaChaveOptica1():
    while True:
        if (GPIO.input(6) == 0):
            print("Catraca aguardando giro")
            if (GPIO.input(6) == 1):
                print("GIROU A CATRACA")
                #exit(0)

def ativaChaveOptica2():
    while True:
        if (GPIO.input(13) == 0):
            print("Catraca aguardando giro")
            if (GPIO.input(13) == 1):
                print("GIROU A CATRACA")
                #exit(0)

if __name__ == '__main__':
    main()
