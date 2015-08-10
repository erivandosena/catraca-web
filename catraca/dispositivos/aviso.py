#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import socket
import locale
from time import strftime
from datetime import datetime
from catraca.logs import Logs
from catraca.dispositivos.display import Display


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
        
    def saldacaao(self):
        hora = strftime('%H')
        mensagem = ''
        if hora > 6 and hora <= 12:
            mensagem = '    BOM DIA!'
        elif hora > 12  and hora <=18:
            mensagem = '   BOA TARDE!'
        else:
            mensagem = '   BOA NOITE!'
        return mensagem
        
    def exibir_saldacaao(self):
        self.display.mensagem(self.mensagem,1,False,False)
        
    def exibir_inicializacao(self):
        self.display.mensagem('Iniciando...\n'+os.name.upper(),3,False,False)
        
    def exibir_estatus_catraca(self):
        self.display.mensagem("Catraca ON-LINE\n RU - Liberdade",3,False,False)
        
    def exibir_local(self):
        self.display.mensagem('      RU\n   Liberdade',4,False,False)

    def exibir_datahora(self):
        data_hora = datetime.now().strftime('%d/%B/%Y\n    %H:%M:%S')
        self.display.mensagem(data_hora,3,False,False)

    def exibir_ip(self):
        self.display.mensagem('       IP\n   '+ip,5,False,False)
    
    def exibir_site(self):
        self.display.mensagem('    UNILAB - Unilab.edu.br',5,False,False)
        
    def exibir_desenvolvedor(self):
        self.display.mensagem('Desenvolvido por\n  DISUP | DTI',5,False,False)
        
    def exibir_aguarda_cartao(self):
        self.display.mensagem(self.saldacaao()+'\nAPROXIME CARTAO',1,True,False)
        
    def exibir_erro_leitura_cartao(self):
        # self.display.mensagem("PROBLEMA AO LER!\nREPITA OPERACAO",1,True,False)
        self.display.mensagem("APROXIME CARTAO\n  NOVAMENTE...",1,True,False)
        
    def exibir_acesso_bloqueado(self):
        self.display.mensagem("     ACESSO\n   BLOQUEADO!",1,False,False)
        
    def exibir_acesso_liberado(self):
        self.display.mensagem("     ACESSO\n    LIBERADO!",0,False,False)

    def exibir_cartao_sem_saldo(self, tipo):
        self.display.mensagem(tipo+"\n   SEM SALDO!",2,False,False)
        
    def exibir_cartao_nao_cadastrado(self):
        self.display.mensagem("     CARTAO\n NAO CADASTRADO!",2,False,False)
        
    def exibir_cartao_valido(self, tipo, saldo):
        self.display.mensagem(tipo+"\n SALDO "+saldo,2,False,False)
        
    def exibir_cartao_invalido(self):
        self.display.mensagem("     CARTAO\n  INVALIDO!",2,False,False)
        
    def exibir_horario_invalido(self):
        self.display.mensagem("FORA DO HORARIO\n DE ATENDIMENTO",2,False,False)  
        
    def exibir_dia_invalido(self):
        self.display.mensagem("  DIA NAO UTIL\nPARA ATENDIMENTO",2,False,False)
        
    def exibir_cartao_utilizado1(self):
        self.display.mensagem("CARTAO JA USADO\nPARA 1a REFEICAO",2,False,False) 
    
    def exibir_cartao_utilizado2(self):
        self.display.mensagem("CARTAO JA USADO\nPARA 2a REFEICAO",2,False,False)
        
        