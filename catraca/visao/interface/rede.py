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
    status = False
    interface = []
    catraca_remota = None
    interface_atual = ""

    def __init__(self, intervalo=10):
        super(Rede, self).__init__()
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Rede.'
        
    def run(self):
        print "%s Rodando... " % self.name
        while True:
            rede = self.obtem_interface()
            if rede != []:
                Rede.interface = rede
                print Rede.interface 
                if not self.status:
                    Rede.status = True
            sleep(self.intervalo)
            
    def obtem_interface(self):
        rede = []
        interface = ""
        try:
            #Rede.catraca_remota = CatracaJson().obtem_catraca_rest()
            Rede.catraca_remota = CatracaJson().catraca_get()
            if Rede.catraca_remota:
                interface = self.catraca_remota.interface
                interfaces = netifaces.interfaces()
                for iface in interfaces:
                    if iface == interface:
                        addrs = netifaces.ifaddresses(iface)
                        addresses = [i['addr'] for i in addrs.setdefault(netifaces.AF_INET, [{'addr':None}] )]
                        if addresses[0]:
                            rede.append(addresses[0])
                            rede.append(iface)
                            rede.append(addrs[netifaces.AF_LINK][0]['addr'])
                            rede.append(Rede.catraca_remota)
                            if not self.status:
                                self.interface_atual = rede[1]
                                self.aviso.exibir_estatus_rede(interface, rede)
                                Rede.status = True
                            if self.interface_atual != rede[1]:
                                self.interface_atual = rede[1]
                                self.aviso.exibir_estatus_rede(interface, rede)
                            return rede
                else:
                    Rede.status = False
                    return []
            else:
                print "Servidor AUSENTE!"
                Rede.status = False
                return []
        except Exception as excecao:
            print excecao
            Rede.status = False
            return []
        finally:
            pass
        