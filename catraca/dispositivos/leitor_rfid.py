#!/usr/bin/env python
# -*- coding: latin-1 -*-


#import pingo 
from time import sleep
from catraca.pinos import PinoControle
from catraca import configuracao 
from catraca.dispositivos import display, solenoide


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


# verde  /data0 - pin 11 gpio 17
# branco /data1 - pin 12 gpio 18
#placa = configuracao.pinos_rpi()
rpi = PinoControle()
#DO_GPIO = 17 
#D1_GPIO = 18
D0 = rpi.ler(17)['gpio']
D1 = rpi.ler(18)['gpio']
#D0.mode = configuracao.pino_entrada()
#D1.mode = configuracao.pino_entrada()
baixo = configuracao.pino_baixo()
bits = ''
numero_cartao = ''

ACESSO = False

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
        configuracao.detecta_evento(D0, zero)
        configuracao.detecta_evento(D1, um)
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
    global ACESSO
    ID = id_cartao #int(leitor())
    if (len(str(ID)) == 0):
        display.display("Por favor...","APROXIME CARTAO",2,2)
    else:
        if (ID == 3995148318): # or (ID == 3995121086):
            print 'Cartao Valido! ID:'+ str(ID)
            display.display("ID: "+str(ID),"Administrador",2,3)
            ACESSO = True
            display.display("SALDO ATUAL","R$ 1,60",2,3)
            display.display("ACESSO","LIBERADO!",2,3)
            sleep(0.05)
            ACESSO = False
            display.display("Bem-vindo!","APROXIME CARTAO",2,0)
            #return True
        else:
            print 'Cartao invalido!'
            ACESSO = False
            display.display("ID: "+str(ID),"Cadastro Ausente",2,3)
            display.display("ACESSO","BLOQUEADO!",2,3)
            display.display("Bem-vindo!","APROXIME CARTAO",2,0)
            #return False

def verifica_acesso():
    global ACESSO
    return ACESSO

