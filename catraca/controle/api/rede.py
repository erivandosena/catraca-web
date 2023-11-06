#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
import netifaces
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.recursos.catraca_json import CatracaJson


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Rede(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    interface_ativa = []
    status = False
    interface_atual = None
    contador = 19

    def __init__(self, intervalo=10):
        #super(Rede, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Rede.'
        
    def run(self):
        print "%s Rodando... " % self.name
        while not self._stopevent.isSet():
            if self.obtem_interface() != []:
                if not Rede.status:
                    Rede.status = True
            else:
                 Rede.status = False
                 Rede.interface_ativa = []
                 
            if not Rede.status:
                self.contador += 1
                print self.contador
                if self.contador == 20:
                    self.aviso.exibir_falha_servidor()
                    self.contador = 0
                 
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
        
    def obtem_interface(self):
        interface = ""
        interface_atual = []
        try:
            catraca_remota = CatracaJson().catraca_get()
            if catraca_remota:
                interface = catraca_remota.interface
                for iface in netifaces.interfaces():
                    if iface == interface:
                        #print str(iface) + " == " + str(interface)
                        addrs = netifaces.ifaddresses(iface)
                        addresses = [i['addr'] for i in addrs.setdefault(netifaces.AF_INET, [{'addr':None}] )]
                        if addresses[0]:
                            interface_atual.insert(0, catraca_remota)
                            interface_atual.insert(1, iface)
                Rede.interface_ativa = interface_atual
                return Rede.interface_ativa
            else:
                return []
        except Exception as e:
            self.log.logger.error("Exception", exc_info=True)
        finally:
            if self.interface_atual != interface:
                self.aviso.exibir_status_interface_rede(interface)
                self.aviso.exibir_aguarda_cartao()
            self.interface_atual = interface
            