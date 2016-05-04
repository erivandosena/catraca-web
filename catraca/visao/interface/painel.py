#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.visao.interface.alerta import Alerta
from catraca.controle.dispositivos.leitorcartao import LeitorCartao
from catraca.controle.restful.relogio import Relogio
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
        print '\nIniciando API...\n'
        
#         print "IP " + str(self.util.obtem_ip()) 
#         
#         print 'Free RAM: '+str(self.util.obtem_ram())
#         print 'Nr. of processes: '+str(self.util.obtem_process_count())
#         print 'Up time: '+str(self.util.obtem_up_time())
#         print 'Nr. of connections: '+str(self.util.obtem_connections())
#         print 'Temperature in C: ' +str(self.util.obtem_temperature())
#         print 'IP-address: '+str(self.util.obtem_ipaddress())
#         print 'CPU speed: '+str(self.util.obtem_cpu_speed())
        
        
        self.log.logger.info('Iniciando Api...')
        self.aviso.exibir_inicializacao()
        self.aviso.exibir_estatus_catraca(self.util.obtem_ip_por_interface())
        #self.aviso.exibir_mensagem_institucional_fixa(self.aviso.saldacao(), self.util.obtem_datahora_display(), 2)
        
#         self.aviso.exibir_estatus_catraca(self.util.obtem_ip())
        self.threads()
            
    def threads(self):
        #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
        try:
            #Mensagem().start()
            Relogio().start()
            Alerta().start()
            Sincronia().start()
            LeitorCartao().start()
            
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro executando Painel.', exc_info=True)
        finally:
            pass
        