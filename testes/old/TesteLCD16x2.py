#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Exibe informações através de caracteres em um display LCD.

As informações são exibidas em duas linhas de caractres no dysplay LCD
16x2 marca winstar mod. 1602L rev.A com 16 pinos.
"""

import socket
from datetime import datetime
from time import sleep, strftime
import Adafruit_CharLCD as LCD
from catraca.dao.cartao import Cartao
from catraca.dao.cartaodao import CartaoDAO
from catraca.pinos import PinoControle


__author__ = "Erivando, Sena, e Ramos"
__copyright__ = "Copyright 2015, ©"
__credits__ = ["Erivando", "Sena", "Ramos"]
__license__ = "Copyright"
__version__ = "1.0.0"
__maintainer__ = "Erivando"
__email__ = "erivandoramos@bol.com.br"
__status__ = "Protótipo"



"""
# Layout da configuracao do display 16x2
1 : GND
2 : 5V
3 : Contrast            - (0-5V)*
4 : RS (Register Select)
5 : R/W (Read Write)       - GROUND THIS PIN
6 : Enable or Strobe
7 : Data Bit 0             - NOT USED
8 : Data Bit 1             - NOT USED
9 : Data Bit 2             - NOT USED
10: Data Bit 3             - NOT USED
11: Data Bit 4
12: Data Bit 5
13: Data Bit 6
14: Data Bit 7
15: LCD Backlight        - +5V**
16: LCD Backlight        - GND
"""

rpi = PinoControle()

# Definicao pinos GPIO para mapeamento do LCD
lcd_rs        = rpi.ler(20)['gpio']
lcd_en        = rpi.ler(16)['gpio']
lcd_d4        = rpi.ler(12)['gpio']
lcd_d5        = rpi.ler(25)['gpio']
lcd_d6        = rpi.ler(24)['gpio']
lcd_d7        = rpi.ler(23)['gpio']
lcd_backlight = 4

# Definir quantidade da coluna e linha para LCD 16x2
lcd_columns = 16
lcd_rows    = 2

# Inicializar o LCD usando os pinos especificados
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                            lcd_columns, lcd_rows, lcd_backlight)


def display(texto, duracao, cursor, scroll):
    try:
        # limpa
        lcd.clear()
        # exibe cursores
        lcd.show_cursor(cursor)
        lcd.blink(cursor)
        # exibe texto(s)
        lcd.message(texto)
        # rolagem do(s) texto(s)
        if scroll:
            lcd_scroll(texto)
        # tempo de exibicao
        sleep(duracao)
    except KeyboardInterrupt:
        print '\nInterrompido manualmente.' # pass
    except Exception:
        print '\nErro geral [Display].'
    finally:
        #lcd.clear()
        print 'Display finalizado'


def lcd_scroll(texto):
    for i in range(lcd_columns-len(texto)):
        sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns-len(texto)):
        sleep(0.5)
        lcd.move_left()


def main():
    """Bloco principal do programa.
    """

    # Inicializa o display
    display("Testando...",2,True,False)
    #display("\n.",0,False,True)
    #display("Sena\nRamos",1,False,False)
    display(datetime.now().strftime('%d de %B %Y \n    %H:%M:%S'),3,False,False)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    ip = ' IP %s' % ( s.getsockname()[0] )
    
    display("Catraca 1 ONLINE\n"+ip,2,False,False)


if __name__ == '__main__':
    main()
