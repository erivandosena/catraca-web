#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.visao.interface.alerta import Alerta
from catraca.controle.dispositivos.leitorcartao import LeitorCartao
from catraca.controle.restful.sincronia import Sincronia


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Painel(object):
    
    log = Logs()
    util = Util()
    aviso = Aviso() 
    
    def __init__(self):
        super(Painel, self).__init__()
    
    def main(self):
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
        self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 2)
        self.threads()
            
    def threads(self):
        try:
#             Alerta().start()
            Sincronia().start()
            LeitorCartao().start()
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro executando Painel.', exc_info=True)
            