#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.controle.recursos.catraca_json import CatracaJson
from catraca.controle.recursos.mensagem_json import MensagemJson
from catraca.controle.recursos.unidade_json import UnidadeJson
from catraca.controle.recursos.catraca_unidade_json import CatracaUnidadeJson
from catraca.controle.recursos.turno_json import TurnoJson
from catraca.controle.recursos.unidade_turno_json import UnidadeTurnoJson
from catraca.controle.recursos.tipo_json import TipoJson
from catraca.controle.recursos.usuario_json import UsuarioJson
from catraca.controle.recursos.custo_refeicao_json import CustoRefeicaoJson
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.isencao_json import IsencaoJson
from catraca.controle.recursos.vinculo_json import VinculoJson
from catraca.controle.recursos.registro_json import RegistroJson
from catraca.visao.interface.rede import Rede


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RecursosRestful(object):
    
    log = Logs()
    aviso = Aviso()
    
    catraca_json = CatracaJson()
    mensagem_json = MensagemJson()
    unidade_json = UnidadeJson()
    catraca_unidade_json = CatracaUnidadeJson()
    turno_json = TurnoJson()
    unidade_turno_json = UnidadeTurnoJson()
    tipo_json = TipoJson()
    usuario_json = UsuarioJson()
    custo_refeicao_json = CustoRefeicaoJson()
    cartao_json = CartaoJson()
    isencao_json = IsencaoJson()
    vinculo_json = VinculoJson()
    registro_json = RegistroJson()
    
    obtendo_recurso =  False
    
    def __init__(self, ):
        super(RecursosRestful, self).__init__()
        
    def obtem_recursos(self, display=False, mantem_tabela=False, limpa_tabela=False):
        RecursosRestful.obtendo_recurso = True
        print "\nObtendo recursos do servidor RESTful..."
        #self.obtem_catraca(display, mantem_tabela, limpa_tabela)            # 3ºGRAU DE PRIORIDADE DE SINCRONIA
        self.obtem_tipo(display, mantem_tabela, limpa_tabela)
        self.obtem_cartao(display, mantem_tabela, limpa_tabela)             # 2ºGRAU DE PRIORIDADE DE SINCRONIA
        self.obtem_usuario(display, mantem_tabela, limpa_tabela)
        self.obtem_vinculo(display, mantem_tabela, limpa_tabela)
        self.obtem_registro(display, mantem_tabela, limpa_tabela)           # 1ºGRAU DE PRIORIDADE DE SINCRONIA
        self.obtem_turno(display, mantem_tabela, limpa_tabela)              # 4ºGRAU DE PRIORIDADE DE SINCRONIA
        self.obtem_isencao(display, mantem_tabela, limpa_tabela)            # 5ºGRAU DE PRIORIDADE DE SINCRONIA
        self.obtem_unidade(display, mantem_tabela, limpa_tabela)
        self.obtem_unidade_turno(display, mantem_tabela, limpa_tabela)
        self.obtem_catraca_unidade(display, mantem_tabela, limpa_tabela)
        self.obtem_custo_refeicao(display, mantem_tabela, limpa_tabela)
        self.obtem_mensagem(display, mantem_tabela, limpa_tabela)
        RecursosRestful.obtendo_recurso = False
        return RecursosRestful.obtendo_recurso
        
    def obtem_catraca(self, display=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Catraca")
            print "\n-------------------------------"
            catraca = self.catraca_json.catraca_get(limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if catraca:
                print "Recurso CATRACA obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso CATRACA nulo!"
                print "\n-------------------------------"
            return catraca
                
    def obtem_mensagem(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Mensagem")
            print "\n-------------------------------"
            mensagem = self.mensagem_json.mensagem_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if mensagem:
                print "Recurso MENSAGEM obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso MENSAGEM nulo!"
                print "\n-------------------------------"
            return mensagem
                
    def obtem_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade")
            print "\n-------------------------------"
            unidade = self.unidade_json.unidade_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if unidade:
                print "Recurso UNIDADE obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso UNIDADE nulo!"
                print "\n-------------------------------"
            return unidade
                
    def obtem_catraca_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Catraca Unidade")
            print "\n-------------------------------"
            catraca_unidade = self.catraca_unidade_json.catraca_unidade_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if catraca_unidade:
                print "Recurso CATRACA-UNIDADE obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso CATRACA-UNIDADE nulo!"
                print "\n-------------------------------"
            return catraca_unidade
                
    def obtem_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Turno")
            print "\n-------------------------------"
            turno = self.turno_json.turno_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if turno:
                print "Recurso TURNO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso TURNO nulo!"
                print "\n-------------------------------"
            return turno
                
    def obtem_unidade_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade Turno")
            print "\n-------------------------------"
            unidade_turno = self.unidade_turno_json.unidade_turno_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if unidade_turno:
                print "Recurso UNIDADE-TURNO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso UNIDADE-TURNO nulo!"
                print "\n-------------------------------"
            return unidade_turno
                
    def obtem_tipo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Tipo")
            print "\n-------------------------------"
            tipo = self.tipo_json.tipo_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if tipo:
                print "Recurso TIPO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso TIPO nulo!"
                print "\n-------------------------------"
            return tipo
                
    def obtem_usuario(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Usuario")
            print "\n-------------------------------"
            usuario = self.usuario_json.usuario_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if usuario:
                print "Recurso USUARIO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso USUARIO nulo!"
                print "\n-------------------------------"
            return usuario
                
    def obtem_custo_refeicao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Custo Refeicao")
            print "\n-------------------------------"
            custo_refeicao = self.custo_refeicao_json.custo_refeicao_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if custo_refeicao:
                print "Recurso CUSTO-REFEICAO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso CUSTO-REFEICAO nulo!"
                print "\n-------------------------------"
            return custo_refeicao
                
    def obtem_cartao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Cartao")
            print "\n-------------------------------"
            cartao = self.cartao_json.cartao_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if cartao:
                print "Recurso CARTAO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso CARTAO nulo!"
                print "\n-------------------------------"
            return cartao
                
    def obtem_vinculo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Vinculo")
            print "\n-------------------------------"
            vinculo = self.vinculo_json.vinculo_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if vinculo:
                print "Recurso VINCULO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso VINCULO nulo!"
                print "\n-------------------------------"
            return vinculo
                
    def obtem_isencao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Isencao")
            print "\n-------------------------------"
            isencao = self.isencao_json.isencao_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if isencao:
                print "Recurso ISENCAO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso ISENCAO nulo!"
                print "\n-------------------------------"
            return isencao
                
    def obtem_registro(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if Rede.status:
            if display:
                self.aviso.exibir_obtendo_recursos("Registro")
            print "\n-------------------------------"
            registro = self.registro_json.registro_get(mantem_tabela, limpa_tabela)
            if display:
                self.aviso.exibir_aguarda_cartao()
            if registro:
                print "Recurso REGISTRO obtido!"
                print "\n-------------------------------"
            else:
                print "\n-------------------------------"
                print "Recurso REGISTRO nulo!"
                print "\n-------------------------------"
            return registro
        