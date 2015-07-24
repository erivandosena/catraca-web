#!/usr/bin/env python
# -*- coding: latin-1 -*-

from threading import Thread
from catraca.logs import Logs
from catraca.dispositivos.leitorcartao import LeitorCartao

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Acesso(Thread):
    
    log = Logs()
    
    def __init__(self):
        super(Acesso, self).__init__()

    def run(self):
        self.ler_cartao()
        
    def ler_cartao(self):
        try:
            LeitorCartao().ler()
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro iniciando leitura do cartao.', exc_info=True)
        finally:
            pass
            