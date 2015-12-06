#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.controle.recursos.tipo_json import TipoJson
from catraca.controle.recursos.turno_json import TurnoJson
from catraca.controle.recursos.catraca_json import CatracaJson
from catraca.controle.recursos.unidade_json import UnidadeJson
from catraca.controle.recursos.custo_refeicao_json import CustoRefeicaoJson
from catraca.controle.recursos.usuario_json import UsuarioJson
from catraca.controle.recursos.mensagem_json import MensagemJson
from catraca.controle.recursos.cartao_json import CartaoJson
from catraca.controle.recursos.vinculo_json import VinculoJson
from catraca.controle.recursos.isencao_json import IsencaoJson
from catraca.controle.recursos.unidade_turno_json import UnidadeTurnoJson
from catraca.controle.recursos.catraca_unidade_json import CatracaUnidadeJson
from catraca.controle.recursos.registro_json import RegistroJson


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RecursosRestful(object):
    
    log = Logs()
    aviso = Aviso()
    
    catraca_json = CatracaJson()
    tipo_json = TipoJson()
    turno_json = TurnoJson()
    unidade_json = UnidadeJson()
    custo_refeicao_json = CustoRefeicaoJson()
    usuario_json = UsuarioJson()
    mensagem_json = MensagemJson()
    cartao_json = CartaoJson()
    vinculo_json = VinculoJson()
    registro_json = RegistroJson()
    isencao_json = IsencaoJson()
    unidade_turno_json = UnidadeTurnoJson()
    catraca_unidade_json = CatracaUnidadeJson()
    
    
    def __init__(self, ):
        super(RecursosRestful, self).__init__()

    def obtem_recursos(self, display=False, limpa_tabela=False):
        self.obtem_catraca(display, limpa_tabela)
        self.obtem_tipo(display, limpa_tabela)
        self.obtem_turno(display, limpa_tabela)
        self.obtem_unidade(display, limpa_tabela)
        self.obtem_custo_refeicao(display, limpa_tabela)
        self.obtem_usuario(display, limpa_tabela)
        self.obtem_mensagem(display, limpa_tabela)
        self.obtem_cartao(display, limpa_tabela)
        self.obtem_vinculo(display, limpa_tabela)
        self.obtem_registro(display, limpa_tabela)
        self.obtem_isencao(display, limpa_tabela)
        self.obtem_unidade_turno(display, limpa_tabela)
        self.obtem_catraca_unidade(display, limpa_tabela)
        
    def obtem_catraca(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CATRACA"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Catraca")
            if limpa_tabela:
                self.catraca_json.mantem_tabela_local(True)
            else:
                self.catraca_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
        
    def obtem_tipo(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TIPO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Tipo")
            if limpa_tabela:
                self.tipo_json.mantem_tabela_local(True)
            else:
                self.tipo_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_turno(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TURNO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Turno")
            if limpa_tabela:
                self.turno_json.mantem_tabela_local(True)
            else:
                self.turno_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_unidade(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UNIDADE"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade")
            if limpa_tabela:
                self.unidade_json.mantem_tabela_local(True)
            else:
                self.unidade_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_custo_refeicao(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTO REFEICAO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Custo Refeicao")
            if limpa_tabela:
                self.custo_refeicao_json.mantem_tabela_local(True)
            else:
                self.custo_refeicao_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()         

    def obtem_usuario(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USUARIO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Usuario")
            if limpa_tabela:
                self.usuario_json.mantem_tabela_local(True)
            else:
                self.usuario_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_mensagem(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MENSAGEM"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Mensagem")
            if limpa_tabela:
                self.mensagem_json.mantem_tabela_local(True)
            else:
                self.mensagem_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_cartao(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CARTAO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Cartao")
            if limpa_tabela:
                self.cartao_json.mantem_tabela_local(True)
            else:
                self.cartao_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_vinculo(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VINCULO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Vinculo")
            if limpa_tabela:
                self.vinculo_json.mantem_tabela_local(True)
            else:
                self.vinculo_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_registro(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REGISTRO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Registro")
            if limpa_tabela:
                self.registro_json.mantem_tabela_local(True)
            else:
                self.registro_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_isencao(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ISENCAO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Isencao")
            if limpa_tabela:
                self.isencao_json.mantem_tabela_local(True)
            else:
                self.isencao_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_unidade_turno(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UNIDADE TURNO"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade Turno")
            if limpa_tabela:
                self.unidade_turno_json.mantem_tabela_local(True)
            else:
                self.unidade_turno_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()

    def obtem_catraca_unidade(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CATRACA UNIDADE"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Catraca Unidade")
            if limpa_tabela:
                self.catraca_unidade_json.mantem_tabela_local(True)
            else:
                self.catraca_unidade_json.mantem_tabela_local()
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
            