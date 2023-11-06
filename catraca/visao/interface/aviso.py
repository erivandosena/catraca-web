#!/usr/bin/env python
# -*- coding: latin-1 -*-


import locale
from datetime import datetime
from catraca.logs import Logs
from catraca.util import Util
from catraca.controle.dispositivos.display import Display


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


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
                   1 : 'BOM DIA!',
                   2 : 'BOA TARDE!',
                   3 : 'BOA NOITE!',

        }
        return opcoes.get(periodo, "Ola!")

    def exibir_inicializacao(self):
        self.display.mensagem('Iniciando...\n'+self.util.obtem_nome_sistema().center(16), 5, False, False, True)
        
    def exibir_saldacao(self, saldacao, mensagem=None):
        if mensagem:
            self.display.mensagem(saldacao.center(16) + "\n"+ mensagem.center(16), 5, False, False, True)
        else:
            #self.display.mensagem(str(saldacao + " "+ str(self.util.obtem_horario())).center(16), 2, False, False, True)
            self.display.mensagem((str(self.util.obtem_data_hora_atual()[0]) + " " +  str(self.util.obtem_data_hora_atual()[1]))[0:16].center(16), 2, False, False, True)
            
    def exibir_data_hora_atual(self, mensagem=None):
        if mensagem:
            self.display.mensagem((str(self.util.obtem_data_hora_atual()[0]) + " " +  str(self.util.obtem_data_hora_atual()[1]))[0:16].center(16) + "\n"+ mensagem.center(16), 2, False, False, True)
        else:
            self.display.mensagem(str(self.util.obtem_data_hora_atual()[0]).center(16) + "\n" +  str(self.util.obtem_data_hora_atual()[1]).center(16), 3, False, False, True)
            
    def exibir_mensagem_institucional_fixa(self, texto1, texto2, tempo=0, cursor=False, scroll=False, limpa=True):
        if scroll:
            self.display.mensagem(texto1+ "\n"+ texto2, tempo, cursor, scroll, limpa)
        else:
            self.display.mensagem(texto1.center(16) +"\n"+ texto2.center(16), tempo, cursor, scroll, limpa)
            
    def exibir_mensagem_institucional_scroll(self, msg_fixa, texto, verifica_status, tempo):
        tempo_padrao = tempo
        for i in range (len(texto) - 16 + 1):
            if not verifica_status():
                print "EXECUTOU verifica_status!!!!!!"
                break
            texto_scroll = "{}{}".format(texto[i:i+16], texto[i:i+16])
            if i == 0:
                tempo = 3
            else:
                tempo = tempo_padrao
            if i == len(texto)-16:
                tempo = 3
            self.display.mensagem(msg_fixa.center(16)+"\n"+texto_scroll, tempo, False, False, True)
            if i == len(texto)-16:
                break
            
    def exibir_aguarda_cartao(self):
        self.display.mensagem("APROXIME".center(16) +"\n"+ " (( O CARTAO ))", 1, True, False, True)
        
    def exibir_erro_leitura_cartao(self):
        self.display.mensagem("APROXIME CARTAO".center(16) +"\n"+ "NOVAMENTE...".center(16), 1, True, False, True)
        
    def exibir_acesso_bloqueado(self):
        self.display.mensagem("ACESSO".center(16) +"\n"+ "BLOQUEADO!".center(16), 1, False, False, True)
        
    def exibir_acesso_liberado(self):
        self.display.mensagem("ACESSO".center(16) +"\n"+ "LIBERADO!".center(16), 0, False, False, True)

    def exibir_saldo_insuficiente(self):
        self.display.mensagem("CREDITO".center(16) +"\n"+ "INSUFICIENTE!".center(16), 1, False, False, True)
        
    def exibir_cartao_nao_cadastrado(self):
        self.display.mensagem("CARTAO".center(16) +"\n"+ "NAO CADASTRADO!".center(16), 2, False, False, True)
        
    def exibir_vinculo_invalido(self):
        self.display.mensagem("CARTAO COM".center(16) +"\n"+ "VINCULO EXPIRADO".center(16), 2, False, False, True)
        
    def exibir_renova_vinculo_vencido(self):
        self.display.mensagem("AGUARDE...".center(16) +"\n"+ "RENOVACAO AUT.".center(16), 2, False, False, True)
        
    def exibir_vinculo_renovado(self):
        self.display.mensagem("VINCULO".center(16) +"\n"+ "RENOVADO!".center(16), 3, False, False, True)
        
    def exibir_vinculo_nao_renovado(self):
        self.display.mensagem("NAO RENOVADO!".center(16) +"\n"+ "INFORME A ADMIN.".center(16), 2, False, False, True)
        
    def exibir_cartao_isento(self, dada_hora_fim):
        self.display.mensagem("ISENTO ATE".center(16) +"\n"+ dada_hora_fim.center(16), 2, False, False, True)
        
    def exibir_saldo_cartao(self, usuario, saldo):
        self.display.mensagem(usuario.center(16) + "\n"+ str("SALDO " + saldo).center(16), 1, False, False, True)
        
    def exibir_horario_invalido(self):
        self.display.mensagem("FORA DO HORARIO".center(16) +"\n"+ "DE ATENDIMENTO".center(16), 1, False, False, True)  

    def exibir_cartao_utilizado(self, turno):
        self.display.mensagem("JA USADO PARA".center(16) +"\n"+ turno.center(16), 2, False, False, True)
        
    def exibir_acesso_livre(self):
        self.display.mensagem("BEM-VINDO!".center(16) +"\n"+ "ACESSO LIVRE".center(16), 0, False, False, True)
        
    def exibir_bloqueio_total(self):
        self.display.mensagem("BLOQUEIO TOTAL".center(16) +"\n"+ "DEFINIR OPERACAO".center(16), 2, False, False, True)

    def exibir_aguarda_consulta(self):
        self.display.mensagem('CONSULTANDO...'.center(16) +'\n'+ 'AGUARDE!'.center(16), 0, False, False, True)
        
    def exibir_aguarda_liberacao(self):
        self.display.mensagem('AGUARDE'.center(16) +'\n'+ 'LIBERACAO!'.center(16), 0, False, False, True)
        
    def exibir_aguarda_sincronizacao(self):
        self.display.mensagem('SINCRONIZANDO...'.center(16) +'\n'+ 'AGUARDE!'.center(16), 1, False, False, True)

    def exibir_reinicia_catraca(self):
        self.display.mensagem("REINICIANDO...".center(16) +"\n"+ "CATRACA".center(16), 5, False, False, True)
        
    def exibir_desliga_catraca(self):
        self.display.mensagem("DESLIGANDO...".center(16) +"\n"+ "CATRACA".center(16), 5, False, False, True)
        
    def exibir_turno_atual(self, nome_turno):
        self.display.mensagem('TURNO INICIADO'.center(16) +'\n'+ nome_turno.center(16), 2, False, False, True)
        
    def exibir_catraca_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "A CATRACA.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()

    def exibir_unidade_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "A UNIDADE.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_catraca_unidade_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "CATRACA NA UNID.".center(16), 3, False, False, True) 
        #self.display.limpa_lcd()
        
    def exibir_turno_nao_cadastrado(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "O TURNO.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_unidade_turno_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "O TURNO NA UNID.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_custo_refeicao_nao_cadastrado(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "O CUSTO REFEICAO".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_custo_unidade_nao_cadastrado(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "CUSTO NA UNID.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()

    def exibir_tipo_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "TIPO DE USAURIO.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_usuario_nao_cadastrado(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "USUARIO.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()
        
    def exibir_cartao_nao_cadastrada(self):
        self.display.mensagem("FAVOR, CADASTRAR".center(16) +"\n"+ "CARTAO.".center(16), 3, False, False, True)
        #self.display.limpa_lcd()

    def exibir_obtendo_recursos(self, nome_recurso):
        self.display.mensagem("OBTENDO...".center(16) +"\n"+ nome_recurso.center(16), 1, False, False, True)
        
    def exibir_uso_incorreto(self):
        self.display.mensagem("USO INCORRETO".center(16) +"\n"+ "DA CATRACA".center(16), 0, False, False, True)
        
    def exibir_falha_servidor(self):
        self.display.mensagem("ERRO NO SERVIDOR".center(16) +'\n'+ "WEBSERVICE".center(16), 3, False, False, True)
        
    def exibir_status_interface_rede(self, interface):
        self.display.mensagem(str("LAN" if interface == "eth0" else "WLAN").center(16) +"\n"+ 'HABILITADA!'.center(16), 3, False, False, True)
        
    def limpa_display(self):
        self.display.limpa_lcd()
        
        