#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import threading
from catraca.logs import Logs
from catraca.controle.dispositivos.leitorcartao import LeitorCartao


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Acesso(threading.Thread):
    
    log = Logs()
 
    def __init__(self):
        super(Acesso, self).__init__()
        threading.Thread.__init__(self)
        self.name = 'Thread Leitor RFID.'

    def run(self):
        print "%s Rodando... " % self.name
        self.ler_cartao()

    def ler_cartao(self):
        try:
            leitor = LeitorCartao()
            leitor.ler()
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro iniciando leitura do cartao.', exc_info=True)
        finally:
            pass
        