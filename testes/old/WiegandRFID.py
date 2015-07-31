# -*- coding: cp1252 -*-
#!/usr/bin/env python

#green/data0 is pin 22
#white/data1 is pin 7

import time
import RPi.GPIO as GPIO

D0 = 11
D1 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(D0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(D1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bits = ''
timeout = 5

def zero(channel):
 global bits
 bits = bits + '0'
 timeout = 5


def one(channel):
 global bits
 bits = bits + '1'
 timeout = 5

GPIO.add_event_detect(D0, GPIO.FALLING, callback=zero)
GPIO.add_event_detect(D1, GPIO.FALLING, callback=one)

print "Apresente o Cartão"

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
  print "Apresente o Cartão"
