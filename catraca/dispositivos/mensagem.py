#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import threading
from threading import Thread
from catraca.logs import Logs
from catraca.dispositivos.aviso import Aviso
from catraca.dispositivos.leitorcartao import LeitorCartao


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Mensagem(threading.Thread):
    
    log = Logs()

    def __init__(self):
        super(Mensagem, self).__init__()
        threading.Thread.__init__(self)
        self.name = 'Thread Mensagem.'
        self.iterations = 0
        self.daemon = True  # OK para o principal sair, mesmo se a instância ainda está em execução
        self.paused = True  # começar uma pausa
        self.state = threading.Condition()

    def run(self):
        print "%s Rodando... " % self.name
        self.reinicia() # cancelar pausa auto 
        while True:
            with self.state:
                if self.paused:
                    self.state.wait() # bloquear até ser notificado
            # Fazer coisas
            self.exibe_mensagens(True)
            time.sleep(.1)
            self.iterations += 1
                
    def reinicia(self):
        with self.state:
            self.paused = False
            self.state.notify()  # desbloquear auto se espera

    def pausa(self):
        with self.state:
            self.paused = True  # fazer auto bloco e esperar
            
    def para(self):
        self.stopped = True

    def exibe_mensagens(self, valor):
        try:
            while valor:
                aviso = Aviso()
                aviso.exibir_datahora()
                aviso.exibir_local()
                aviso.exibir_desenvolvedor()
                #self.lock.acquire()
                #self.join()
                
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro exibindo mensagem no display', exc_info=True)
        finally:
            pass
    
    def inicia_mensagem(self):
        return self.exibe_mensagens(True)
        
    def finaliza_mensagem(self):
        return self.exibe_mensagens(False)
            