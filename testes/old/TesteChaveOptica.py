#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Uma descrição resumida sobre o documento.

Descrição detalhada sobre o documento.
"""

# Imports
import RPi.GPIO as GPIO

__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, ©"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "Copyright"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Protótipo"


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
