#!/usr/bin/env python
# -*- coding: latin-1 -*-

#import pingo
from time import sleep
from catraca.pinos import PinoControle
from catraca import configuracao
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

#placa = configuracao.pinos_rpi()
rpi = PinoControle()

saida = configuracao.pino_saida()

baixo = configuracao.pino_baixo()
alto = configuracao.pino_alto()

# Definição pinos GPIO para mapeamento LCD
LCD_RS = rpi.ler(7)['gpio'] #placa.pins[26] # GPIO 7
LCD_E  = rpi.ler(8)['gpio'] #placa.pins[24] # GPIO 8
LCD_D4 = rpi.ler(25)['gpio'] #placa.pins[22] # GPIO 25
LCD_D5 = rpi.ler(24)['gpio'] #placa.pins[18] # GPIO 24
LCD_D6 = rpi.ler(23)['gpio'] #placa.pins[16] # GPIO 23
LCD_D7 = rpi.ler(22)['gpio'] #placa.pins[15] # GPIO 22

# Definição de constantes
LCD_WIDTH = 16 # Máximo de caracteres por linha
LCD_CHR = True # True p/ caractere
LCD_CMD = False # False p/ comando
# Endereço RAM do LCD para a 1ª linha
LCD_LINE_1 = 0x80 
# Endereço RAM do LCD para a 2ª linha 
LCD_LINE_2 = 0xC0  
# Constantes de temporização
E_PULSE = 0.00005
E_DELAY = 0.00005

def display(linha_1, linha_2, posicao, duracao):
    try:
        #LCD_E.mode  = saida # E
        #LCD_RS.mode = saida # RS
        #LCD_D4.mode = saida # DB4
        #LCD_D5.mode = saida # DB5
        #LCD_D6.mode = saida # DB6
        #LCD_D7.mode = saida # DB7

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
        print '\nInterrupido manualmente.' # pass
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
    #LCD_RS.state = alto if mode else baixo # RS
    rpi.atualiza(LCD_RS, alto if mode else baixo) #RS
    sleep(0.001)

    #LCD_D4.state = baixo
    #LCD_D5.state = baixo
    #LCD_D6.state = baixo
    #LCD_D7.state = baixo

    rpi.atualiza(LCD_D4, baixo)
    rpi.atualiza(LCD_D5, baixo)
    rpi.atualiza(LCD_D6, baixo)
    rpi.atualiza(LCD_D7, baixo)

    if bits & 0x10 == 0x10:
        #LCD_D4.state = alto
        rpi.atualiza(LCD_D4, alto)
    if bits & 0x20 == 0x20:
        #LCD_D5.state = alto
        rpi.atualiza(LCD_D5, alto)
    if bits & 0x40 == 0x40:
        #LCD_D6.state = alto
        rpi.atualiza(LCD_D6, alto)
    if bits & 0x80 == 0x80:
        #LCD_D7.state = alto
        rpi.atualiza(LCD_D7, alto)

    sleep(E_DELAY)
    #LCD_E.state = alto
    rpi.atualiza(LCD_E, alto)
    sleep(E_PULSE)
    #LCD_E.state = baixo
    rpi.atualiza(LCD_E, baixo)
    sleep(E_DELAY)

    rpi.atualiza(LCD_D4, baixo)
    rpi.atualiza(LCD_D5, baixo)
    rpi.atualiza(LCD_D6, baixo)
    rpi.atualiza(LCD_D7, baixo)
    if bits & 0x01 == 0x01:
        #LCD_D4.state = alto
        rpi.atualiza(LCD_D4, alto)
    if bits & 0x02 == 0x02:
        #LCD_D5.state = alto
        rpi.atualiza(LCD_D5, alto)
    if bits & 0x04 == 0x04:
        #LCD_D6.state = alto
        rpi.atualiza(LCD_D6, alto)
    if bits & 0x08 == 0x08:
        #LCD_D7.state = alto
        rpi.atualiza(LCD_D7, alto)

    sleep(E_DELAY)
    #LCD_E.state = alto
    rpi.atualiza(LCD_E, alto)
    sleep(E_PULSE)
    #LCD_E.state = baixo
    rpi.atualiza(LCD_E, baixo)
    sleep(E_DELAY)

