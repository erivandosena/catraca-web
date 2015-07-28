#!/usr/bin/env python
# -*- coding: latin-1 -*-

import time
import threading
from threading import Thread
from catraca.logs import Logs
from catraca.dispositivos.aviso import Aviso
from catraca.dispositivos.threadcatraca import ThreadCatraca

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Mensagem(ThreadCatraca):
    
    log = Logs()
    
    #threadLock = threading.Lock()
    #threads = []
    
    def __init__(self, threadID, name, counter):
        #super(Mensagem, self).__init__()
        Thread.__init__(self)
        #self.threadID = threadID
        #self.name = name
        #self.counter = counter

    def run(self):
        print "%s Rodando... " % self.name
        #self.threadLock.acquire()
        #self.print_time(self.name, self.counter, 2)
        # Free lock to release next thread
        #self.threadLock.release()
        self.exibe_mensagens()
        
    def finaliza_mensagem(self):
        return self.para()
        
        
#     def print_time(self,threadName,delay,counter):
#         while counter:
#         #while True:
#             time.sleep(delay)
#             print "%s: %s" % (threadName, time.ctime(time.time()))
#             counter -= 1

    def exibe_mensagens(self):
        try:
            while True:
                aviso = Aviso()
                aviso.exibir_datahora()
                aviso.exibir_local()
                aviso.exibir_site()
                aviso.exibir_desenvolvedor()
                
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro exibindo mensagem no display', exc_info=True)
        finally:
            pass
    
    def nome(self):
        return 'Mensagens no Display.'
            