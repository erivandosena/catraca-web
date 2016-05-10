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
        self.obtem_catraca(display, mantem_tabela, limpa_tabela)            # 3ºGRAU DE PRIORIDADE DE SINCRONIA
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
        
    def obtem_catraca(self, display=False, mantem_tabela=False, limpa_tabela=False):
        #catraca = None
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca")
        catraca = self.catraca_json.catraca_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if catraca:
            print "Recurso CATRACA obtido!\n"
        else:
            print "Recurso CATRACA nulo!\n"
        return catraca
                
    def obtem_mensagem(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Mensagem")
        mensagem = self.mensagem_json.mensagem_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if mensagem:
            print "Recurso MENSAGEM obtido!\n"
        else:
            print "Recurso MENSAGEM nulo!\n"
        return mensagem
                
    def obtem_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade")
        unidade = self.unidade_json.unidade_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if unidade:
            print "Recurso UNIDADE obtido!\n"
        else:
            print "Recurso UNIDADE nulo!\n"
        return unidade
                
    def obtem_catraca_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca Unidade")
        catraca_unidade = self.catraca_unidade_json.catraca_unidade_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if catraca_unidade:
            print "Recurso CATRACA-UNIDADE obtido!\n"
        else:
            print "Recurso CATRACA-UNIDADE nulo!\n"
        return catraca_unidade
                
    def obtem_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Turno")
        turno = self.turno_json.turno_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if turno:
            print "Recurso TURNO obtido!\n"
        else:
            print "Recurso TURNO nulo!\n"
        return turno
                
    def obtem_unidade_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade Turno")
        unidade_turno = self.unidade_turno_json.unidade_turno_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if unidade_turno:
            print "Recurso UNIDADE-TURNO obtido!\n"
        else:
            print "Recurso UNIDADE-TURNO nulo!\n"
        return unidade_turno
                
    def obtem_tipo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Tipo")
        tipo = self.tipo_json.tipo_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if tipo:
            print "Recurso TIPO obtido!\n"
        else:
            print "Recurso TIPO nulo!\n"
        return tipo
                
    def obtem_usuario(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Usuario")
        usuario = self.usuario_json.usuario_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if usuario:
            print "Recurso USUARIO obtido!\n"
        else:
            print "Recurso USUARIO nulo!\n"
        return usuario
                
    def obtem_custo_refeicao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Custo Refeicao")
        custo_refeicao = self.custo_refeicao_json.custo_refeicao_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if custo_refeicao:
            print "Recurso CUSTO-REFEICAO obtido!\n"
        else:
            print "Recurso CUSTO-REFEICAO nulo!\n"
        return custo_refeicao
                
    def obtem_cartao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Cartao")
        cartao = self.cartao_json.cartao_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if cartao:
            print "Recurso CARTAO obtido!\n"
        else:
            print "Recurso CARTAO nulo!\n"
        return cartao
                
    def obtem_vinculo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Vinculo")
        vinculo = self.vinculo_json.vinculo_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if vinculo:
            print "Recurso VINCULO obtido!\n"
        else:
            print "Recurso VINCULO nulo!\n"
        return vinculo
                
    def obtem_isencao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Isencao")
        isencao = self.isencao_json.isencao_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if isencao:
            print "Recurso ISENCAO obtido!\n"
        else:
            print "Recurso ISENCAO nulo!\n"
        return isencao
                
    def obtem_registro(self, display=False, mantem_tabela=False, limpa_tabela=False):
        if display:
            self.aviso.exibir_obtendo_recursos("Registro")
        registro = self.registro_json.registro_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if registro:
            print "Recurso REGISTRO obtido!\n"
        else:
            print "Recurso REGISTRO nulo!\n"
        return registro
        