#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from time import sleep
from catraca.controle.restful.relogio import Relogio


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Sincronia(Relogio):
    
    contador_status_recursos = 0

    def __init__(self, intervalo=1):
        super(Sincronia, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Sincronia'
        
    def run(self):
        print "%s. Rodando... " % self.name
        while True:
            print "|-------------<SINCRONIA "+str(Relogio.periodo)+">---------o"
            self.executa_controle_recursos()
            sleep(self.intervalo)

    def executa_controle_recursos(self):
        self.contador_status_recursos += 1
        print "|-------------<RECURSOS "+str(Relogio.hora)+">---------o"
        if (Relogio.periodo == True) and (self.contador_status_recursos >= 10):
            self.contador_status_recursos = 0
            self.recursos_restful.obtem_recursos(False, True, False)
        elif (Relogio.periodo == False) and (str(Relogio.hora) == "00:00:01"):
            self.util.beep_buzzer(855, .5, 1)
            self.aviso.exibir_aguarda_sincronizacao()
            self.recursos_restful.catraca_json.mantem_tabela_local(None, True)
            self.recursos_restful.unidade_json.mantem_tabela_local(None, True)
            self.recursos_restful.turno_json.mantem_tabela_local(None, True)
            self.recursos_restful.tipo_json.mantem_tabela_local(None, True)
            self.recursos_restful.usuario_json.mantem_tabela_local(None, True)
            self.recursos_restful.custo_refeicao_json.mantem_tabela_local(None, True)
            sleep(2)
            self.recursos_restful.obtem_recursos(True, True, False)
            