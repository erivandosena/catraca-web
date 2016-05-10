#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
#from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.usuario_dao import UsuarioDAO
from catraca.controle.restful.relogio import Relogio
from time import sleep


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class SincroniaUsuario(threading.Thread):
    
    log = Logs()
    aviso = Aviso()
    util = Util()
    usuario_dao = UsuarioDAO()
    
    def __init__(self):
        super(SincroniaUsuario, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = 1
        self.name = 'Thread Sincronia Usuario.'
        
    def run(self):
        print "%s Rodando... " % self.name
        count = 0
        while not self._stopevent.isSet():
            count += 1
            self.pesquisa()
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % self.getName()
        
    def join(self, timeout=None):
        self._stopevent.set()
        super(SincroniaUsuario, self).join(timeout)
        
    def pesquisa(self, obj):
        usuario = self.usuario_dao.busca(obj.vinculo)
        try:
            if usuario is None:
                self.usuario_dao.insere(usuario)
                print self.usuario_dao.aviso
                return True
            else:
                return False
        except Exception as excecao:
            print excecao
            return False
            
            
            