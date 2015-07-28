#!/usr/bin/env python
# -*- coding: latin-1 -*-

from catraca.dispositivos.display import Display
from catraca.logs import Logs
from datetime import datetime
import locale
import os
import socket


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Aviso(object):
    
    log = Logs()
    display = Display()
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('unilab.edu.br', 0))
    ip = '%s' % ( s.getsockname()[0] )
    
    def __init__(self):
        super(Aviso, self).__init__()
        
    def exibir_inicializacao(self):
        self.display.mensagem('Iniciando...\n'+os.name.upper(),3,False,False)
        
    def exibir_estatus_catraca(self):
        self.display.mensagem("Catraca ON-LINE\n IP "+self.ip,3,False,False)
        
    def exibir_local(self):
        self.display.mensagem('       RU\n   Liberdade',4,False,False)

    def exibir_datahora(self):
        data_hora = datetime.now().strftime('%d de %B %Y \n    %H:%M:%S')
        self.display.mensagem(data_hora,3,False,False)

    def exibir_ip(self):
        self.display.mensagem('       IP\n   '+ip,4,False,False)
    
    def exibir_site(self):
        self.display.mensagem('    ACESSE\n Unilab.edu.br',4,False,False)
        
    def exibir_aguarda_cartao(self):
        self.display.mensagem("  Bem-vindo!\nAPROXIME CARTAO",0,True,False)
        
    def exibir_erro_leitura_cartao(self):
        self.display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",1,True,False)
        
    def exibir_acesso_bloqueado(self):
        self.display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
        
    def exibir_acesso_liberado(self):
        self.display.mensagem("     ACESSO\n    LIBERADO!",0,False,False)

    def exibir_cartao_saldo_negativo(self, tipo):
        self.display.mensagem(tipo+"\n   SEM SALDO!",2,False,False)
        
    def exibir_cartao_invalido(self, tipo):
        self.display.mensagem(tipo+"\n NAO CADASTRADO!",2,False,False)
        
    def exibir_cartao_valido(self, tipo, saldo):
        self.display.mensagem(tipo+"\n SALDO "+saldo,2,False,False)
        
    def exibir_desenvolvedor(self):
        self.display.mensagem('     DISUP\n      DTI',3,False,False)
        
        
    

        
    
        
    
        
        
        
        
        
        