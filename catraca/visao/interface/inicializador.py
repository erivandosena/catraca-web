#!/usr/bin/env python
# -*- coding: latin-1 -*-


import threading
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.api.gerenciador import Gerenciador
from catraca.visao.interface.alerta import Alerta
from catraca.controle.dispositivos.leitorcartao import LeitorCartao
from catraca.controle.api.sincronizador import Sincronizador


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class Inicializador(threading.Thread):
    
    log = Logs()
    util = Util()
    aviso = Aviso()
    gerenciador = Gerenciador()
    sincronizador = Sincronizador()
    leitor_cartao = LeitorCartao()
    alerta = Alerta()
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'Thread Painel'
        
    def run(self):
        print "%s Rodando... " % self.name
        
        print '\nIniciando API CATRACA...\n'
        print "=" * 50
        print 'Memoria Livre: '+str(self.util.obtem_ram()).upper()
        print 'Numero de Processos: '+str(self.util.obtem_process_count())
        print 'Numero de Conexoes: '+str(self.util.obtem_connections())
        print 'Temperatura do Processador: ' +str(self.util.obtem_temperature()) +' C'
        print 'IP LAN: ' +str(self.util.obtem_ip_por_interface('eth0'))
        print 'IP WLAN: ' +str(self.util.obtem_ip_por_interface('wlan0'))
        print "=" * 50
        print ''
        self.aviso.exibir_inicializacao()
        #self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 2)
        
        self.threads()
        
        while True:
            self.verifica_threads()
            sleep(1)            
        print "%s Finalizando..." % (self.getName(),)
        
    def threads(self):
        try:
            self.gerenciador.start()
            self.sincronizador.start()
            self.leitor_cartao.start()
            self.alerta.start()
        except Exception as excecao:
            self.log.logger.error('[THREADS] ', exc_info=True)
            
    def verifica_threads(self):
        try:
            if not self.gerenciador.isAlive():
                self.gerenciador = Gerenciador()
                self.gerenciador.start()
                
            if not self.sincronizador.isAlive():
                self.sincronizador = Sincronizador()
                self.sincronizador.start()
                    
            if not self.leitor_cartao.isAlive():
                self.leitor_cartao = LeitorCartao()
                self.leitor_cartao.start()
                
            if not self.alerta.isAlive():
                self.alerta = Alerta()
                self.alerta.start()
                
        except Exception as excecao:
            self.log.logger.error('[VERIFICA THREADS] ', exc_info=True)
            