#!/usr/bin/env python
# -*- coding: latin-1 -*-


from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


"""
# Layout da configuracao do display 16x2
1 : GND
2 : 5V
3 : Contrast 		   - (0-5V)*
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
15: LCD Backlight 	   - +5V**
16: LCD Backlight 	   - GND
"""

rpi = PinoControle()
baixo = rpi.baixo()
alto = rpi.alto()

# Definicao pinos GPIO para mapeamento LCD
LCD_RS = rpi.ler(7)['gpio']
LCD_E  = rpi.ler(8)['gpio']
LCD_D4 = rpi.ler(25)['gpio']
LCD_D5 = rpi.ler(24)['gpio']
LCD_D6 = rpi.ler(23)['gpio']
LCD_D7 = rpi.ler(22)['gpio']

# Definicao de constantes
LCD_WIDTH = 16 # Maximo de caracteres por linha
LCD_CHR = True # True p/ caractere
LCD_CMD = False # False p/ comando
# Endereco RAM do LCD para a 1a linha
LCD_LINE_1 = 0x80 
# Endereco RAM do LCD para a 2a linha 
LCD_LINE_2 = 0xC0  
# Constantes de temporizacao
E_PULSE = 0.00005
E_DELAY = 0.00005

def display(linha_1, linha_2, posicao, duracao):
    try:
        # Inicializa o display
        lcd_init()
   
        # Envia texto
        lcd_byte(LCD_LINE_1, LCD_CMD)
        lcd_string(linha_1, posicao)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string(linha_2, posicao)
        #Atraso(delay) em segundos
        sleep(duracao)
    except KeyboardInterrupt:
        print '\nInterrompido manualmente.' # pass
    except Exception:
        print '\nErro geral [Display].'
    finally:
        print 'Display finalizado'


def lcd_init():
    # Inicializa display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)


def lcd_string(message,style):
    if style == 1:
        message = message.ljust(LCD_WIDTH," ")  
    elif style == 2:
        message = message.center(LCD_WIDTH," ")
    elif style == 3:
        message = message.rjust(LCD_WIDTH," ")
    
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)


def lcd_byte(bits, mode):
    # bits = data (byte para pinos de dados)
    rpi.atualiza(LCD_RS, alto if mode else baixo) #RS
    sleep(0.001)

    rpi.atualiza(LCD_D4, baixo)
    rpi.atualiza(LCD_D5, baixo)
    rpi.atualiza(LCD_D6, baixo)
    rpi.atualiza(LCD_D7, baixo)

    if bits & 0x10 == 0x10:
        rpi.atualiza(LCD_D4, alto)
    if bits & 0x20 == 0x20:
        rpi.atualiza(LCD_D5, alto)
    if bits & 0x40 == 0x40:
        rpi.atualiza(LCD_D6, alto)
    if bits & 0x80 == 0x80:
        rpi.atualiza(LCD_D7, alto)

    sleep(E_DELAY)
    rpi.atualiza(LCD_E, alto)
    sleep(E_PULSE)
    rpi.atualiza(LCD_E, baixo)
    sleep(E_DELAY)

    rpi.atualiza(LCD_D4, baixo)
    rpi.atualiza(LCD_D5, baixo)
    rpi.atualiza(LCD_D6, baixo)
    rpi.atualiza(LCD_D7, baixo)
    if bits & 0x01 == 0x01:
        rpi.atualiza(LCD_D4, alto)
    if bits & 0x02 == 0x02:
        rpi.atualiza(LCD_D5, alto)
    if bits & 0x04 == 0x04:
        rpi.atualiza(LCD_D6, alto)
    if bits & 0x08 == 0x08:
        rpi.atualiza(LCD_D7, alto)

    sleep(E_DELAY)
    rpi.atualiza(LCD_E, alto)
    sleep(E_PULSE)
    rpi.atualiza(LCD_E, baixo)
    sleep(E_DELAY)
