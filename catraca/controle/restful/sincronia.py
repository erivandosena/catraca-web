#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import datetime
from time import sleep
from catraca.controle.restful.relogio import Relogio
from catraca.visao.interface.rede import Rede
from catraca.modelo.dao.registro_offline_dao import RegistroOfflineDAO


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Sincronia(Relogio):
    
    contador_status_recursos = 0
    rede = Rede()
    relogio = Relogio()

    def __init__(self, intervalo=1):
        super(Sincronia, self).__init__()
        Relogio.__init__(self)
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self.name = 'Thread Sincronia'
        
    def run(self):
        print "%s. Rodando... " % self.name
        
        self.rede.start()
        self.relogio.start()
        
        while True:
            self.executa_controle_recursos()
            sleep(self.intervalo)
               
    def executa_controle_recursos(self):
        if Relogio.catraca:
            if (Relogio.catraca.operacao == 1) or (Relogio.catraca.operacao == 2) or (Relogio.catraca.operacao == 3) or (Relogio.catraca.operacao == 4):
                self.contador_status_recursos += 1
                if Rede.status and Relogio.periodo:
                    if self.contador_status_recursos >= 20:
                        self.contador_status_recursos = 0
                        self.recursos_restful.obtem_recursos()
                elif Rede.status:
                    if RegistroOfflineDAO().busca():
                    
                        #if datetime.datetime.strptime(str(Relogio.hora),'%H:%M:%S').time() >= datetime.datetime.strptime('00:00:00','%H:%M:%S').time() and datetime.datetime.strptime(str(Relogio.hora),'%H:%M:%S').time() <= datetime.datetime.strptime('00:00:10','%H:%M:%S').time():
                        if datetime.datetime.strptime('00:00:00','%H:%M:%S').time() >= datetime.datetime.strptime(str(self.util.obtem_hora()),'%H:%M:%S').time() <= datetime.datetime.strptime('00:00:15','%H:%M:%S').time():    
                            print Relogio.hora
                            self.util.beep_buzzer(855, .5, 1)
    
                            if self.relogio.isAlive():
                                self.relogio.join()
                            if self.rede.isAlive():
                                self.rede.join()
                                
                            self.aviso.exibir_aguarda_sincronizacao()
                            
                            # realiza limpeza das tabelas locais
                            print "\nLimpando... tabela local CATRACA"
                            self.recursos_restful.catraca_json.catraca_get(True)
                            print "Concluido!\n"
                            print "\nLimpando... tabela local UNIDADE"
                            self.recursos_restful.unidade_json.unidade_get(True)
                            print "Concluido!\n"
                            print "\nLimpando... tabela local TURNO"
                            self.recursos_restful.turno_json.turno_get(True)
                            print "Concluido!\n"
                            print "\nLimpando... tabela local TIPO"
                            self.recursos_restful.tipo_json.tipo_get(True)
                            print "Concluido!\n"
                            print "\nLimpando... tabela local USUARIO"
                            self.recursos_restful.usuario_json.usuario_get(True)
                            print "Concluido!\n"
                            print "\nLimpando... tabela local CUSTO-REFEICAO"
                            self.recursos_restful.custo_refeicao_json.custo_refeicao_get(True)
                            print "Concluido!\n"
                            
    #                         print "Iniciando a sincronia com o servidor RESTful..."
    #                         print "espera 10"
    #                         sleep(10)
    #                         self.recursos_restful.obtem_recursos()
                            print "espera 10"
                            sleep(5)
                            
                            if not self.rede.isAlive():
                                self.rede = Rede()
                                self.rede.start()
                            if not self.relogio.isAlive():
                                self.relogio = Relogio()
                                self.relogio.start()
                