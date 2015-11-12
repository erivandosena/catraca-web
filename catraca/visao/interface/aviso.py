#!/usr/bin/env python
# -*- coding: latin-1 -*-

import os
import locale
from datetime import datetime
from catraca.logs import Logs
from catraca.controle.dispositivos.display import Display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Aviso(object):
    
    log = Logs()
    display = Display()
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    def __init__(self):
        super(Aviso, self).__init__()
        
    def saldacao(self):
        hora = int(datetime.now().strftime('%H'))
        periodo = 0
        if (hora >= 6 and hora < 12):
            periodo = 1
        if (hora >= 12 and hora < 18):
           periodo = 2
        if (hora >= 18 and hora < 00):
            periodo = 3
        opcoes = {
                   1 : '      OLA\n    BOM DIA!',
                   2 : '      OLA\n   BOA TARDE!',
                   3 : '      OLA\n   BOA NOITE!',

        }
        return opcoes.get(periodo, "      Ola!").upper()
    
    def exibir_saldacao(self):
        self.display.mensagem(self.saldacao(),2,False,False)
        
    def exibir_inicializacao(self):
        self.display.mensagem('Iniciando...\n'+os.name.upper(),3,False,False)
        
    def exibir_estatus_catraca(self):
        self.display.mensagem("Catraca ON-LINE\n RU - Liberdade",3,False,False)
        
    def exibir_local(self):
        self.display.mensagem('      RU\n   Liberdade',4,False,False)

    def exibir_datahora(self, data_hora, tempo):
        #data_hora = datetime.now().strftime('%d/%B/%Y\n     %H:%M:%S')
        #self.display.limpa_lcd()
        self.display.mensagem(data_hora, tempo, False, False)

    def exibir_ip(self):
        self.display.mensagem('       IP\n   '+ip,5,False,False)
    
    def exibir_site(self):
        self.display.mensagem('    UNILAB - Unilab.edu.br',5,False,False)
        
    def exibir_desenvolvedor(self):
        self.display.mensagem('Desenvolvido por\n  DISUP | DTI',5,False,False)
        
    def exibir_aguarda_cartao(self):
        self.display.mensagem('   BEM-VINDO!\nAPROXIME CARTAO',0,True,False)
        
    def exibir_erro_leitura_cartao(self):
        self.display.mensagem("APROXIME CARTAO\n  NOVAMENTE...",1,True,False)
        
    def exibir_acesso_bloqueado(self):
        self.display.mensagem("     ACESSO\n   BLOQUEADO!",0,False,False)
        
    def exibir_acesso_liberado(self):
        self.display.mensagem("     ACESSO\n    LIBERADO!",0,False,False)

    def exibir_cartao_sem_saldo(self):
        self.display.mensagem("   SEM SALDO\n  RECARREGUE!",1,False,False)
        
    def exibir_cartao_nao_cadastrado(self):
        self.display.mensagem("     CARTAO\n NAO CADASTRADO!",1,False,False)
        
    def exibir_cartao_valido(self, saldo):
        self.display.mensagem("SALDO DO CARTAO:\n"+saldo,1,True,False)
        
    def exibir_cartao_invalido(self):
        self.display.mensagem("     CARTAO\n  INVALIDO!",1,False,False)
        
    def exibir_horario_invalido(self):
        self.display.mensagem("FORA DO HORARIO\n DE ATENDIMENTO",1,False,False)  
        
    def exibir_turno_invalido(self):
        self.display.mensagem("NAO EXISTE TURNO\nAVISE AO GUICHE!",1,False,False)
        
    def exibir_dia_invalido(self):
        self.display.mensagem("  DIA NAO UTIL\nPARA ATENDIMENTO",1,False,False)
        
    def exibir_cartao_utilizado(self):
        self.display.mensagem("CARTAO JA USADO\n NESTE HORARIO",1,False,False)
        
    def exibir_acesso_livre(self):
        self.display.mensagem("   BEM-VINDO!\n  ACESSO LIVRE",1,False,False)

    def exibir_aguarda_consulta(self):
        self.display.mensagem(' CONSULTANDO...\n    AGUARDE!',0,False,False)
        
    def exibir_aguarda_liberacao(self):
        self.display.mensagem('    AGUARDE...\n   LIBERACAO',0,True,False)
        
    def exibir_aguarda_sincronizacao(self):
        self.display.mensagem('SINCRONIZANDO...\n    AGUARDE!',0,True,False)
        
    def exibir_agradecimento(self):
        self.display.mensagem('   OBRIGADO\n   BOM APETITE!',0,False,False)
        
    def exibir_catraca_nao_cadastrada(self):
        self.display.mensagem("    CATRACA\n NAO CADASTRADA!",1,False,False)

    def exibir_reinicia_catraca(self):
        self.display.mensagem(" REINICIANDO...\n    CATRACA",4,True,False)
        
    def exibir_desliga_catraca(self):
        self.display.mensagem(" DESLIGANDO...\n    CATRACA",4,True,False)
        
        