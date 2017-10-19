#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from time import sleep
import Adafruit_CharLCD as LCD
from unicodedata import normalize
from catraca.logs import Logs
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.logs import Logs


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


"""
# Layout da configuracao do display 16x2
1 : GND
2 : 5V
3 : Contrast               - (0-5V)*
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

class Display(object):
    
    rpi = PinoControle()
    log = Logs()
    
    # Definicao pinos GPIO para mapeamento LCD
    lcd_rs        = rpi.ler(20)['gpio']
    lcd_en        = rpi.ler(16)['gpio']
    lcd_d4        = rpi.ler(12)['gpio']
    lcd_d5        = rpi.ler(25)['gpio']
    lcd_d6        = rpi.ler(24)['gpio']
    lcd_d7        = rpi.ler(23)['gpio']
    lcd_backlight = rpi.ler(5)['gpio']
    
    # Definir quantidade da coluna e linha para LCD 16x2
    lcd_columns = 16
    lcd_rows    = 2
    
    # Inicializar o LCD usando os pinos especificados
    lcd = LCD.Adafruit_CharLCD(
                               lcd_rs, 
                               lcd_en, 
                               lcd_d4, 
                               lcd_d5, 
                               lcd_d6, 
                               lcd_d7, 
                               lcd_columns, 
                               lcd_rows, 
                               lcd_backlight, 
                               enable_pwm=False)
    
#     def __init__(self):
#         #super(Display, self).__init__()

    def mensagem(self, texto, duracao, cursor, scroll, limpa):
        texto = self.remove_acentos(texto)
        try:
            self.lcd.home()
            # limpa
            if limpa:
                self.lcd.clear()
            # exibe cursores
            self.lcd.show_cursor(cursor)
            self.lcd.blink(cursor)

            # rolagem do(s) texto(s)
            if scroll:
                self.lcd_scroll(texto)
#                 if "\n" in texto:
#                     l1, l2, = texto.split('\n')
#                     texto = l1+ " "+l2
#                 texto = "\n".join(texto)
#                 self.lcd.move_left()
#                 self.lcd.message(texto)
            else:
                # exibe texto(s)
                self.lcd.message(texto)
                
            # tempo de exibicao
            sleep(duracao)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def lcd_scroll(self, texto):
        for i in range(self.lcd_columns-len(texto)):
            sleep(0.5)
            self.lcd.move_right()
        for i in range(self.lcd_columns-len(texto)):
            sleep(0.5)
            self.lcd.move_left()

    def lcd_retroiluminacao(self, estado):
        if estado:
            # Turn backlight on.
            self.lcd.set_backlight(estado)
        else:
            # Turn backlight off.
            self.lcd.set_backlight(estado)
            
    def limpa_lcd(self):
        self.lcd.clear()
        
    def remove_acentos(self, texto):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            return normalize('NFKD', texto.decode("utf-8","ignore")).encode('ascii','ignore')
        except UnicodeDecodeError:
            self.log.logger.error("UnicodeDecodeError", exc_info=True)
            
              
