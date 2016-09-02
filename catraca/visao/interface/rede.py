#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
import netifaces
import traceback
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.recursos.catraca_json import CatracaJson
#from catraca.controle.restful.sincronia import Sincronia
# from catraca.controle.restful.relogio import Relogio

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
    interface_atual = None
    erro = ""
    #sincronia = Sincronia()
    #relogio = Relogio()

    def __init__(self, intervalo=10):
        super(Rede, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo
        self.name = 'Thread Rede.'
        
    def run(self):
        print "%s Rodando... " % self.name
        
#         if not self.relogio.isAlive():
#             self.relogio.start()
        
        while not self._stopevent.isSet():
            if self.obtem_interface() != []:
                if not Rede.status:
                    Rede.status = True
            else:
                 Rede.status = False
            print "REDE.status = " +str(Rede.status)
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
            
#     def join(self, timeout=None):
#         self._stopevent.set()
#         threading.Thread.join(self, timeout)
            
    def obtem_interface(self):
        interface = ""
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
                            Rede.interface_ativa.insert(0, catraca_remota)
                            Rede.interface_ativa.insert(1, iface)
                            self.erro = ""
                            return Rede.interface_ativa
                #print str(iface) + " != " + str(interface)
                self.erro = ""
                return []
            else:
                self.erro = ""
                return []
        except Timeout as e:
            #print "Tempo de solicitacao expirada!", e
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        except HTTPError as e:
            #print "Resposta HTTP invalida!", e
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        except TooManyRedirects as e:
            #print "Numero de redirecionamentos excedido!", e
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        except RequestException as e:
            #print "Erro no request!", e
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        except ConnectionError as e:
            #print "Falha na conexao com o host!", e
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        except Exception as e:
            print "Stack Trace:", traceback.format_exc()
            self.log.logger.error("[REDE] Stack Trace: "+str(traceback.format_exc()), exc_info=True)
            self.erro = e
            return []
        finally:
            if self.interface_atual != interface:
                self.aviso.exibir_status_interface_rede(interface)
            self.interface_atual = interface
            if self.erro != "":
                self.aviso.exibir_falha_servidor()
                