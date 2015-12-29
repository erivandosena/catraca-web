#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import threading
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dao.mensagem_dao import MensagemDAO
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.controle.restful.relogio import Relogio
#from catraca.controle.dispositivos.leitorcartao import LeitorCartao


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Mensagem(threading.Thread):
    
    log = Logs()
    aviso = Aviso()
    util = Util()
    catraca_dao = CatracaDAO()
    mensagem_dao = MensagemDAO()
    
    def __init__(self):
        super(Mensagem, self).__init__()
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self._sleepperiod = 1
        self.name = 'Thread Mensagem.'

    def run(self):
        print "%s Rodando... " % self.name
        self.aviso.exibir_estatus_catraca(self.util.obtem_ip())
        self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 2)
        #self.aviso.exibir_datahora(self.util.obtem_datahora_display())
        self.aviso.exibir_aguarda_cartao()

        count = 0
        while not self._stopevent.isSet():
            count += 1
            #print "|-----------------------------------------------<Mensagem DISPLAY "+str(LeitorCartao.uso_do_cartao)+">---------o"
            print "LOOP %d" % (count)
            if not Relogio.periodo:
                self.exibe_mensagem()
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % self.getName()
  
    def join(self, timeout=None):
        self._stopevent.set()
        super(Mensagem, self).join(timeout)
        threading.Thread.join(self, timeout)

    def exibe_mensagem(self):
        catraca = self.catraca_dao.obtem_catraca()
        if catraca:
            mensagens = self.mensagem_dao.obtem_mensagens(catraca)
            try:
                self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 3)
                if mensagens:
                    for msg in mensagens:
                        for i in range (len(msg)-2):
                            self.aviso.exibir_mensagem_institucional_scroll(str(msg[i+1]), 0.4, False)
                self.aviso.exibir_mensagem_institucional_fixa("Temperatura CPU", self.util.obtem_cpu_temp() +" C", 5)
                #self.aviso.exibir_mensagem_institucional_fixa("Desempenho CPU", self.util.obtem_cpu_speed() +" RPM", 5)
            except Exception as excecao:
                print excecao
                self.log.logger.error('Erro exibindo mensagem no display', exc_info=True)
            finally:
                pass
