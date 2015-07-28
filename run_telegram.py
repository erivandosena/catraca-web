#!/usr/bin/env python
# -*- coding: latin1 -*-

import os
import tgl
import sys
import time
import shlex
import locale
import picamera
import subprocess
import datetime as dt
import RPi.GPIO as GPIO
from functools import partial
from datetime import datetime
from datetime import timedelta


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Universidade da Integracao Internacional da Lusofonia Afro-Brasileira" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

our_id = 0
binlog_done = False;
enable_bot = False
#strup_msg = False 

HISTORY_QUERY_SIZE = 100
print(os.path.abspath(__file__))
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def on_binlog_replay_end():
    binlog_done = True;

def on_get_difference_end():
    pass

def on_our_id(id):
    our_id = id
    return "ID: " + str(our_id)

def msg_cb(success, msg):
    pass
    #pp.pprint(success)
    #pp.pprint(msg)

def history_cb(msg_list, peer, success, msgs):
    print(len(msgs))
    msg_list.extend(msgs)
    print(len(msg_list))
    if len(msgs) == HISTORY_QUERY_SIZE:
        tgl.get_history(peer, len(msg_list), HISTORY_QUERY_SIZE, partial(history_cb, msg_list, peer));

def cb(success):
    print(success)
    print("\ncb function")

def on_msg_receive(msg):
    if msg.out and not binlog_done:
        return;

    global enable_bot
    peer = msg.src
    mystr = msg.text.lower()
    w = mystr.split()
    if (msg.src.id == 72196132): #ID ADMIN
        if (mystr =='dison'):
            enable_bot = True
            peer.send_msg ('Programa Desabilitado!')
            return;
            
        elif (mystr =='disoff'):
            enable_bot = False
            peer.send_msg ('Programa Habilitado!')
            return;
            
        elif (mystr == 'reiniciar'):
            peer.send_msg ('O sistema será reiniciado.')
            cmd = 'sudo reboot'
            subprocess.call(cmd.split())
            return;
            
        elif (mystr == 'desligar'):
            peer.send_msg ('O sistema será desligado.')
            cmd = 'sudo shutdown -h now'
            subprocess.call(cmd.split())        
            return;
        
        elif (w[0] == 'led') and (not(w[1] == None)):
            if (w[1]=='off'):
                peer.send_msg ('Led apagado')
                GPIO.output(27,0)
                return;
            elif (w[1]=='on'):
                peer.send_msg ('Led acesso')
                GPIO.output(27,1)
                return;
            else:
                peer.send_msg ('Comando desconhecido.')    
                return;    
            
    if (not(enable_bot)):
            if (mystr=='sobre'):
                linha1 = 'Projeto CATRACA'
                linha2 = '\n\n© 2015 Unilab\nUniversidade da Integração Internacional da Lusofonia Afro-Brasileira'
                linha3 = '\n\nDISUP-Divisão de Suporte\nDTI-Diretoria de Tecnologia da Informação'
                linha4 = '\n\nScrumMaster: @ErivandoSena\nTécnico em Laboratório de Informática\nerivandoramos@unilab.edu.br'
                linha5 = '\n\nEquipe(Team): Fabiane Lima, Háquila Andréa, Erivando Sena, Jefferson Ponte, Michel Pereia, Francisco Kleber'
                peer.send_msg(linha1+linha2+linha3+linha4+linha5)
                return;
                
            elif (mystr == '!photo'):
                path=os.getenv("HOME")
                with picamera.PiCamera() as picam:
                    #picam.led = False
                    #picam.rotation=90
                    picam.framerate = 24
                    picam.start_preview()
                    picam.annotate_background = picamera.Color('black')
                    picam.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    picam.capture(path+'/pic.jpg',resize=(640,480))
                    time.sleep(2)
                    picam.stop_preview()
                    picam.close()
                print(path)    
                peer.send_photo ('/root/pic.jpg')
                peer.send_msg ('Isso pode demorar algum tempo, por favor, aguarde...')
                return;
                
            elif (mystr == 'id'):
                iid = 'Seu ID Telegram: '+str(msg.src.id)
                peer.send_msg(iid)
                return;
                
            elif (mystr == 'hora'):
                ttime=datetime.now().strftime('%H:%M:%S')
                peer.send_msg (ttime)
                return;    
            
            elif (mystr == 'data'):
                                ttime=datetime.now().strftime('%d/%m/%Y')
                                peer.send_msg (ttime)
                                return;
                
            elif (mystr=='uptime'):
                with open('/proc/uptime', 'r') as f:
                    usec = float(f.readline().split()[0])
                    usec_str = str(timedelta(seconds = usec))
                peer.send_msg(usec_str)
                return;
            
            elif (mystr == 'ajuda') or (mystr == '?'):
                peer.send_msg ('Lista de comandos:\n\nid\nsobre\ndata\nhora')
                return;
                
            else:
                peer.send_msg ('Envie ajuda ou ? para obter uma lista dos comandos válidos.')
                peer.send_msg (msg.src)
                return;
            
def print_path(success, filename):
    print(filename)    

def on_secret_chat_update(peer, types):
    return "on_secret_chat_update"

def on_user_update(peer, what_changed):
    pass

def on_chat_update(peer, what_changed):
    pass    

# callbacks
tgl.set_on_binlog_replay_end(on_binlog_replay_end)
tgl.set_on_get_difference_end(on_get_difference_end)
tgl.set_on_our_id(on_our_id)    
tgl.set_on_secret_chat_update(on_secret_chat_update)
tgl.set_on_user_update(on_user_update)
tgl.set_on_chat_update(on_chat_update)    
tgl.set_on_msg_receive(on_msg_receive)
