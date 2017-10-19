#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Fornece uma leitura de números decimais de um cartão de aproximação.

O número em decimal obtido é convertido de binário para decimal cujo este
número deverá ser sempre igual a número ID do cartão RFID (Radio-Frequency
IDentification) de 13.56Mhz lido através do protocolo Wiegand por meio do
leitor de TAGs da marca HID mod. R-640X-300 iCLASS(2kbits, 16kbits, 32Kbits)
R10 Reader 6100.
"""

from time import sleep
from catraca.pinos import PinoControle
from catraca.dispositivos import display
from catraca.dao.cartaodao import CartaoDAO

__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, ©"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "Copyright"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Protótipo"

# green/data0 is pin 11
# white/data1 is pin 12

rpi = PinoControle()
D0 = rpi.ler(17)['gpio']
D1 = rpi.ler(27)['gpio']
bits = ''
numero_cartao = ''

def zero(self):
    global bits
    bits = bits + '0'


def um(self):
    global bits
    bits = bits + '1'
    

def leitor():
    display.mensagem("Bem-vindo!\nAPROXIME CARTAO",1,False,False)
    global bits
    global numero_cartao
    try:
        rpi.evento_falling(D0, zero)
        rpi.evento_falling(D1, um)
        while True:
            sleep(0.5)
            if len(bits) == 32:
                sleep(0.1)
                numero_cartao = int(str(bits), 2)
                print busca_id(numero_cartao).getNumero()
                print busca_id(numero_cartao).getValor()
                display.mensagem("Numero do Cartao\n ID "+str(numero_cartao),3,False,False)
                display.mensagem("Bem-vindo!\nAPROXIME CARTAO",1,False,False)
                bits = ''
            elif (len(bits) > 0) or (len(bits) > 32):
                bits = ''
                
    except KeyboardInterrupt:
        print '\nInterrompido manualmente' # pass
    except Exception:
        print '\nErro geral [Leitor RFID].'
    finally:
        print 'Leitor RFID finalizado'

def busca_id(id):
    cartao_dao = CartaoDAO()
    cartao = cartao_dao.busca(id)
    return cartao


def main():
    """Bloco principal do programa.
    """

    leitor()


if __name__ == '__main__':
    main()
    