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
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production 


class Rede(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    interface_ativa = []
    status = False

    def __init__(self, intervalo=10):
        super(Rede, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Rede.'
        
    def run(self):
        print "%s Rodando... " % self.name
        while not self._stopevent.isSet():
            if self.obtem_interface() != []:
                if not self.status:
                    Rede.status = True
            else:
                 Rede.status = False

            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
            
    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)
            
    def obtem_interface(self):
        try:
            catraca_remota = CatracaJson().catraca_get()
            if catraca_remota:
                interface = catraca_remota.interface
                interfaces = netifaces.interfaces()
                for iface in interfaces:
                    #print iface
                    if iface == interface:
                        #print str(iface) + " == " + str(interface)
                        addrs = netifaces.ifaddresses(iface)
                        addresses = [i['addr'] for i in addrs.setdefault(netifaces.AF_INET, [{'addr':None}] )]
                        if addresses[0]:
                            Rede.interface_ativa.append(addresses[0])
                            Rede.interface_ativa.append(iface)
                            Rede.interface_ativa.append(addrs[netifaces.AF_LINK][0]['addr'])
                            Rede.interface_ativa.append(catraca_remota)
                            if not self.status:
                                self.interface_atual = Rede.interface_ativa[1]
                                self.aviso.exibir_estatus_rede(interface, Rede.interface_ativa)
                            if self.interface_atual != Rede.interface_ativa[1]:
                                self.interface_atual = Rede.interface_ativa[1]
                                self.aviso.exibir_estatus_rede(interface, Rede.interface_ativa)
                            #print Rede.interface_ativa
                            return Rede.interface_ativa
                else:
                    return []
            else:
                print "Servidor AUSENTE!"
                return []
        except Exception as excecao:
            print excecao
            return []
        finally:
            pass
        