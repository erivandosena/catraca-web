#!/usr/bin/env python
# -*- coding: latin-1 -*-


import pingo 
from time import sleep
from catraca import configuracao 
from catraca.dispositivos import display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


# verde  /data0 - pin 11 gpio 17
# branco /data1 - pin 12 gpio 18
placa = configuracao.pinos_rpi()
DO_GPIO = 17 
D1_GPIO = 18
D0 = placa.pins[11]
D1 = placa.pins[12]
D0.mode = configuracao.pino_entrada()
D1.mode = configuracao.pino_entrada()
bits = ''
numero_cartao = ''

def zero(self):
    global bits
    bits = bits + '0'

def um(self):
    global bits
    bits = bits + '1'

def leitor():
    display.display("Bem-vindo!","APROXIME CARTAO",2,0)
    global bits
    global numero_cartao
    try:
        configuracao.detecta_evento(DO_GPIO, zero)
        configuracao.detecta_evento(D1_GPIO, um)
        while True:
            if len(bits) == 32:
                numero_cartao = int(str(bits), 2)
                bits = ''
                ler_cartao(numero_cartao)
                
    except KeyboardInterrupt:
        print '\nInterrupido manualmente' # pass
    #except Exception:
    #    print '\nErro geral [Leitor RFID].'
    finally:
        print 'Leitor RFID finalizado'

def ler_cartao(id_cartao):
    ID = id_cartao #int(leitor())
    if (len(str(ID)) == 0):
        display.display("Por favor...","APROXIME CARTAO",2,2)
    else:
        if (ID == 3995148318): # or (ID == 3995121086):
            print 'Cartão Válido. ID:'+ str(ID)
            display.display("ID: "+str(ID),"Administrador",2,3)
            display.display("SALDO ATUAL","R$ 1,60",2,3)
            display.display("ACESSO","LIBERADO!",2,3)
            display.display("Bem-vindo!","APROXIME CARTAO",2,0)
            return True
        else:
            print 'Cartão inválido.'
            display.display("ID: "+str(ID),"Cadastro Ausente",2,3)
            display.display("ACESSO","BLOQUEADO!",2,3)
            display.display("Bem-vindo!","APROXIME CARTAO",2,0)
            return False

def libera_acesso():
    #display.display("Bem-vindo!","APROXIME CARTAO",2,0)
    if (ler_cartao(numero_cartao)) and (len(str(numero_cartao)) == 10):
        return True
    else:
        return False

