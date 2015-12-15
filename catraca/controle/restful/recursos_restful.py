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
    
    def __init__(self, ):
        super(RecursosRestful, self).__init__()
        
    def obtem_recursos(self, display=False, mantem_tabela=False, limpa_tabela=False):
        try:
            
            self.obtem_catraca(display, mantem_tabela, limpa_tabela)
            self.obtem_mensagem(display, mantem_tabela, limpa_tabela)
            self.obtem_unidade(display, mantem_tabela, limpa_tabela)
            self.obtem_catraca_unidade(display, mantem_tabela, limpa_tabela)
            self.obtem_turno(display, mantem_tabela, limpa_tabela)
            self.obtem_unidade_turno(display, mantem_tabela, limpa_tabela)
            self.obtem_tipo(display, mantem_tabela, limpa_tabela)
            self.obtem_usuario(display, mantem_tabela, limpa_tabela)
            self.obtem_custo_refeicao(display, mantem_tabela, limpa_tabela)
            self.obtem_cartao(display, mantem_tabela, limpa_tabela)
            self.obtem_isencao(display, mantem_tabela, limpa_tabela)
            self.obtem_vinculo(display, mantem_tabela, limpa_tabela)
            self.obtem_registro(display, mantem_tabela, limpa_tabela)
            
        except IntegrityError as excecao:
            print excecao
            self.obtem_recursos()
            self.log.logger.error('Erro ao atualizar tabelas.', exc_info=True)
        
    def obtem_catraca(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<CATRACA>---------o"
        catraca = None
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca")
        catraca = self.catraca_json.catraca_get(mantem_tabela, limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        return catraca
                
    def obtem_mensagem(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<MENSAGEM>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Mensagem")
            self.mensagem_json.mensagem_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<UNIDADE>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade")
            self.unidade_json.unidade_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_catraca_unidade(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<CATRACA UNIDADE>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Catraca Unidade")
            self.catraca_unidade_json.catraca_unidade_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<TURNO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Turno")
            self.turno_json.turno_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_unidade_turno(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<UNIDADE TURNO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Unidade Turno")
            self.unidade_turno_json.unidade_turno_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_tipo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<TIPO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Tipo")
            self.tipo_json.tipo_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_usuario(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<USUARIO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Usuario")
            self.usuario_json.usuario_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_custo_refeicao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<CUSTO REFEICAO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Custo Refeicao")
            self.custo_refeicao_json.custo_refeicao_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_cartao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<CARTAO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Cartao")
            self.cartao_json.cartao_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_vinculo(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<VINCULO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Vinculo")
            self.vinculo_json.vinculo_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_isencao(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<ISENCAO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Isencao")
            self.isencao_json.isencao_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                
    def obtem_registro(self, display=False, mantem_tabela=False, limpa_tabela=False):
        print "|---------------------------------------------------------------<REGISTRO>---------o"
        try:
            if display:
                self.aviso.exibir_obtendo_recursos("Registro")
            self.registro_json.registro_get(mantem_tabela, limpa_tabela)
        finally:
            if display:
                self.aviso.exibir_aguarda_cartao()
                