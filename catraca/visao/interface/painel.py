#!/usr/bin/env python
# -*- coding: latin-1 -*-


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
from time import sleep
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.visao.interface.acesso import Acesso
from catraca.visao.interface.alerta import Alerta
from catraca.controle.restful.controle_restful import ControleRestful
from catraca.controle.restful.cliente_restful import ClienteRestful
<<<<<<< HEAD
=======
import os
from time import sleep
from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.visao.interface.acesso import Acesso
from catraca.visao.interface.alerta import Alerta
from catraca.visao.restful.cliente_restful import ClienteRestful
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Painel(object):
    
    log = Logs()
    aviso = Aviso() 
<<<<<<< HEAD
<<<<<<< HEAD
    util = Util()
=======
>>>>>>> remotes/origin/web_backend
=======
    util = Util()
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
    
    def __init__(self):
        super(Painel, self).__init__()
    
    def main(self):
        print 'Iniciando...'
        self.log.logger.info('Iniciando aplicacao...')
        self.aviso.exibir_inicializacao()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        self.aviso.exibir_datahora(self.util.obtem_datahora_display(), 4)
        self.aviso.exibir_saldacao()
        self.aviso.exibir_estatus_catraca()
        self.threads()
    
    def threads(self):
        #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
        try:
            Alerta().start()
            ControleRestful().start()
            ClienteRestful().start()
            #Acesso().start()
#         except (SystemExit, KeyboardInterrupt):
#             raise
#         except Exception:
#             self.log.logger.error('Erro executando thread.', exc_info=True)
        finally:
            pass
        
<<<<<<< HEAD
=======
        self.aviso.exibir_datahora()
        self.aviso.exibir_saldacao()
        self.aviso.exibir_estatus_catraca()
        self.thread()
    
    def thread(self):
        #os.system("echo 'Sistema da Catraca iniciado!' | mail -s 'Raspberry Pi B' erivandoramos@bol.com.br")
        try:
            acesso = Acesso()
            acesso.start()
            #sleep(5)
            alerta = Alerta()
            #sleep(5)
            cr = ClienteRestful()
 
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            self.log.logger.error('Erro executando thread.', exc_info=True)
        finally:
            pass
>>>>>>> remotes/origin/web_backend
=======
>>>>>>> 148eaee1089907e52c4801e9755f71d977892af4
        