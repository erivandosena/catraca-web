#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import threading
from catraca.logs import Logs
from catraca.dispositivos.aviso import Aviso


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class ThreadCatraca (threading.Thread):
    
    lock = threading.Lock()
    
    def __init__(self, *args):
        threading.Thread.__init__(self)
        
#     def run(self):
#         print "Iniciando Thread " + self.name
#         
#         self.executa_acoes(self.name)
#         
#         # Get lock to synchronize threads
#         #self.threadLock.acquire()
#         #self.print_time(self.name, self.counter, 1)
#         # Free lock to release next thread
#         #self.threadLock.release()
# 
#     def print_time(self, threadName, delay, counter):
#         while counter:
#             print 'passou no print_time'
#             
#             time.sleep(delay)
#             
#             
#             
#             print "%s: %s" % (threadName, time.ctime(time.time()))
#             
#             #self.executa_acoes(threadName)
#             
#             
#             counter -= 1
# #             if threadName == 'Mensagem':
# #                 #self.finaliza_mensagem()
# #                 print 'finaliza thead mensagem'
# #                 self.terminate()
#             
#     def ler_cartao(self):
#         try:
#             LeitorCartao().ler()
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception:
#             self.log.logger.error('Erro iniciando leitura do cartao.', exc_info=True)
#         finally:
#             pass
#         
#     def exibe_mensagens(self, valor):
#         try:
#             while valor:
#                 aviso = Aviso()
#                 aviso.exibir_datahora()
#                 aviso.exibir_local()
#                 aviso.exibir_desenvolvedor()
#                 
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception:
#             self.log.logger.error('Erro exibindo mensagem no display', exc_info=True)
#         finally:
#             pass
#     
#     def inicia_mensagem(self):
#         self.exibe_mensagens(True)
#         
#     def finaliza_mensagem(self):
#         self.exibe_mensagens(False)
#         
#     def executa_acoes(self, threadName):
#         if threadName == 'Acesso':
#             self.ler_cartao()
#             if LeitorCartao().ler():
#                 self.threadLock.stop()
#             else:
#                 self.threadLock.start()
#             
#         if threadName == 'Mensagem':
#             #if LeitorCartao().ler():
#             self.inicia_mensagem()
# #             else:
# #                 self.finaliza_mensagem()
#             
            