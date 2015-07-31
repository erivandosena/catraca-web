#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import threading
from threading import Thread
from dispositivos.acesso import Acesso
from logs import Logs
from dispositivos.mensagem import Mensagem
from dispositivos.aviso import Aviso
from dispositivos.threadcatraca import ThreadCatraca
from dispositivos.mensagemcondicao import MensagemCondicao


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Painel(object):
    
    log = Logs()
    aviso = Aviso() 
    
    
    def __init__(self):
        super(Painel, self).__init__()
    
    def main(self):
        print 'Processando...'
        self.log.logger.debug('Iniciando aplicacao...')
        self.aviso.exibir_inicializacao()
        self.aviso.exibir_datahora()
        self.aviso.exibir_estatus_catraca()
        self.thread()
    
    def thread(self):
        #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
        try:
            #threads = []
            
            acesso = Acesso()
            mensagem = Mensagem()
            mcondicao = MensagemCondicao()
            
            
            #acesso = ThreadCatraca(1, "Acesso", 1)
            #mensagem = ThreadCatraca(2, "Mensagem", 2)

            acesso.start()
            mensagem.start() # Chama o método run ()
                
            #mensagem.start()
            
            #threads.append(acesso)
            #threads.append(mensagem)

            
#             for t in threads:
#                 print t
#                 t.join()
#                 print t
#                 #mensagem.join()
#                 
#                 
#             print "Saindo da Thread principal"


            while mcondicao.condition:
                mensagem.reinicia()
                # depois de alguma operação
                
               # print 'depois de alguma operação'
                
                mensagem.pausa()
                # alguma outra operação
                
               # print 'alguma outra operação'
            
            
            print('mensagem.iterations == {}'.format(mensagem.iterations))  # mostrar conversa executado
            # http://stackoverflow.com/questions/15729498/how-to-start-and-stop-thread
 
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            self.log.logger.error('Erro executando thread.', exc_info=True)
        finally:
            pass
        