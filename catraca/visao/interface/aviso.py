#!/usr/bin/env python
# -*- coding: latin-1 -*-

import locale
from datetime import datetime
from catraca.logs import Logs
from catraca.util import Util
from catraca.controle.dispositivos.display import Display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class Aviso(object):
    
    log = Logs()
    util = Util()
    display = Display()
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    def __init__(self):
        super(Aviso, self).__init__()
        
    def saldacao(self):
        hora = int(datetime.now().strftime('%H'))
        periodo = 0
        if (hora >= 0 and hora < 12):
            periodo = 1
        if (hora >= 12 and hora <= 17):
            periodo = 2
        if (hora >= 18 and hora <= 23):
            periodo = 3
        opcoes = {
                   1 : 'OLA'.center(16) +'\n'+ 'BOM DIA!'.center(16),
                   2 : 'OLA'.center(16) +'\n'+ 'BOA TARDE!'.center(16),
                   3 : 'OLA'.center(16) +'\n'+ 'BOA NOITE!'.center(16),

        }
        return opcoes.get(periodo, "Ola!".center(16) +"\n"+ self.util.obtem_data_formatada().center(16))

    def exibir_inicializacao(self):
        self.display.mensagem('Iniciando...\n'+self.util.obtem_nome_sistema(), 3, False, False)
        
    def exibir_estatus_catraca(self):
        self.display.mensagem(self.util.obtem_nome_rpi().center(16) +"\n"+ 'ON-LINE!'.center(16), 3, False, False)

    def exibir_saldacao(self, saldacao):
        self.display.mensagem(saldacao, 3, False, False)

    def exibir_datahora(self, data_hora):
        self.display.mensagem(data_hora.center(16), 3, False, False)
    
    def exibir_aguarda_cartao(self):
        self.display.mensagem("BEM-VINDO!".center(16) +"\n"+ "APROXIME CARTAO", 0, True, False)
        
    def exibir_erro_leitura_cartao(self):
        self.display.mensagem("APROXIME CARTAO".center(16) +"\n"+ "NOVAMENTE...".center(16), 0, True, False)
        
    def exibir_acesso_bloqueado(self):
        self.display.mensagem("ACESSO".center(16) +"\n"+ "BLOQUEADO!".center(16), 0, False, False)
        
    def exibir_acesso_liberado(self):
        self.display.mensagem("ACESSO".center(16) +"\n"+ "LIBERADO!".center(16), 0, False, False)

    def exibir_saldo_insuficiente(self):
        self.display.mensagem("CREDITO".center(16) +"\n"+ "INSUFICIENTE!".center(16), 1, False, False)
        
    def exibir_cartao_nao_cadastrado(self):
        self.display.mensagem("CARTAO".center(16) +"\n"+ "NAO CADASTRADO!".center(16), 1, False, False)
        
    def exibir_cartao_isento(self):
        self.display.mensagem("CARTAO ISENTO".center(16) +"\n"+ "DE PAGAMENTO!".center(16), 0, False, False)
        
    def exibir_saldo_cartao(self, saldo):
        self.display.mensagem("SALDO DO CARTAO:".center(16) +"\n"+ saldo.center(16), 1, False, False)
        
    def exibir_horario_invalido(self):
        self.display.mensagem("FORA DO HORARIO".center(16) +"\n"+ "DE ATENDIMENTO".center(16), 1, False, False)  
        
    def exibir_dia_invalido(self):
        self.display.mensagem("DIA NAO UTIL".center(16) +"\n"+ "PARA ATENDIMENTO".center(16), 1, False, False)
        
    def exibir_cartao_utilizado(self):
        self.display.mensagem("CARTAO JA USADO" +"\n"+ "PARA ESTE TURNO".center(16), 2, False, False)
        
    def exibir_acesso_livre(self):
        self.display.mensagem("BEM-VINDO!".center(16) +"\n"+ "ACESSO LIVRE".center(16), 1, False, False)

    def exibir_aguarda_consulta(self):
        self.display.mensagem('CONSULTANDO...'.center(16) +'\n'+ 'AGUARDE!'.center(16), 0, False, False)
        
    def exibir_aguarda_liberacao(self):
        self.display.mensagem('AGUARDE'.center(16) +'\n'+ 'LIBERACAO!'.center(16), 0, False, False)
        
    def exibir_aguarda_sincronizacao(self):
        self.display.mensagem('SINCRONIZANDO...'.center(16) +'\n'+ 'AGUARDE!'.center(16), 0, False, False)

    def exibir_reinicia_catraca(self):
        self.display.mensagem("REINICIANDO...".center(16) +"\n"+ "CATRACA".center(16), 4, False, False)
        
    def exibir_desliga_catraca(self):
        self.display.mensagem("DESLIGANDO...".center(16) +"\n"+ "CATRACA".center(16), 4, False, False)
        
    def exibir_turno_atual(self, nome_turno):
        self.display.mensagem('TURNO INICIADO'.center(16) +'\n'+ nome_turno.center(16), 4, False, False)
        
    def exibir_catraca_nao_cadastrada(self):
        self.display.mensagem("FAVOR CADASTRAR!".center(16) +"\n"+ "CATRACA".center(16), 4, False, False)
        self.display.limpa_lcd()

    def exibir_unidade_nao_cadastrada(self):
        self.display.mensagem("FAVOR CADASTRAR!".center(16) +"\n"+ "UNIDADE".center(16), 4, False, False)
        self.display.limpa_lcd()
        
    def exibir_catraca_unidade_nao_cadastrada(self):
        self.display.mensagem("FAVOR CADASTRAR!".center(16) +"\n"+ "CATRACA UNIDADE".center(16), 4, False, False) 
        self.display.limpa_lcd()
        
    def exibir_turno_nao_cadastrado(self):
        self.display.mensagem("FAVOR CADASTRAR!".center(16) +"\n"+ "TURNO".center(16), 4, False, False)
        self.display.limpa_lcd()
        
    def exibir_unidade_turno_nao_cadastrada(self):
        self.display.mensagem("FAVOR CADASTRAR!".center(16) +"\n"+ "UNIDADE TURNO".center(16), 4, False, False)
        self.display.limpa_lcd()
        
    def exibir_obtendo_recursos(self, nome_recurso):
        self.display.mensagem("OBTENDO...".center(16) +"\n"+ nome_recurso.center(16), 1, False, False)
        
    def exibir_uso_incorreto(self):
        self.display.mensagem("USO INCORRETO".center(16) +"\n"+ "DA CATRACA".center(16), 0, False, False)
        
    def exibir_falha_servidor(self):
        self.display.mensagem('ERRO NO SERVIDOR'.center(16) +'\n'+ 'WEB SERVICE'.center(16), 6, False, False)
        