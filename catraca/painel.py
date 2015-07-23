#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import socket
from datetime import datetime
from threading import Thread
from dispositivos import display
from dispositivos.acesso import Acesso
from catraca.logs import Logs

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production

class Painel(object):
    
    def __init__(self):
        super(Painel, self).__init__()
    
    def main(self):
        now = datetime.now()
        print 'Processando...'
        Logs().logger.debug('Iniciando aplicacao...')
        display.mensagem("Iniciando...\n"+os.name.upper(),1,False,False)
        display.mensagem(datetime.now().strftime('%d de %B %Y \n    %H:%M:%S'),2,False,False)
        #display.mensagem(str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"\n"+str(now.hour)+":"+str(now.minute)+":"+str(now.second),2,False,False)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('unilab.edu.br', 0))
        ip = ' IP %s' % ( s.getsockname()[0] )
        display.mensagem("Catraca 1 ONLINE\n"+ip,2,False,False)
        self.thread()
    
    def thread(self):
        #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
        try:
            acesso = Acesso()
            acesso.start()
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            Logs().logger.error('Erro executando thread.', exc_info=True)
        finally:
            pass
        