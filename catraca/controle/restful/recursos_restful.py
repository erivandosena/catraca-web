#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.visao.interface.aviso import Aviso
from catraca.controle.recursos.tipo_json import TipoJson
from catraca.controle.recursos.turno_json import TurnoJson
from catraca.controle.recursos.catraca_json import CatracaJson
from catraca.controle.recursos.giro_json import GiroJson
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

    def __init__(self, ):
        super(RecursosRestful, self).__init__()

    def obtem_recursos(self, display=False, limpa_tabela=False):
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CATRACA"
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca")
        if limpa_tabela:
            CatracaJson().catraca_get(True)
        else:
            CatracaJson().catraca_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TIPO"
        if display:
            self.aviso.exibir_obtendo_recursos("Tipo")
        if limpa_tabela:
            TipoJson().tipo_get(True)
        else:
            TipoJson().tipo_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TURNO"
        if display:
            self.aviso.exibir_obtendo_recursos("Turno")
        if limpa_tabela:
            TurnoJson().turno_get(True)
        else:
            TurnoJson().turno_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UNIDADE"
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade")
        if limpa_tabela:
            UnidadeJson().unidade_get(True)
        else:
            UnidadeJson().unidade_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTO REFEICAO"
        if display:
            self.aviso.exibir_obtendo_recursos("Custo Refeicao")
        if limpa_tabela:
            CustoRefeicaoJson().custo_refeicao_get(True)
        else:
            CustoRefeicaoJson().custo_refeicao_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USUARIO"
        if display:
            self.aviso.exibir_obtendo_recursos("Usuario")
        if limpa_tabela:
            UsuarioJson().usuario_get(True)
        else:
            UsuarioJson().usuario_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GIRO"
        if display:
            self.aviso.exibir_obtendo_recursos("Giro")
        if limpa_tabela:
            GiroJson().giro_get(True)
        else:
            GiroJson().giro_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MENSAGEM"
        if display:
            self.aviso.exibir_obtendo_recursos("Mensagem")
        if limpa_tabela:
            MensagemJson().mensagem_get(True)
        else:
            MensagemJson().mensagem_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CARTAO"
        if display:
            self.aviso.exibir_obtendo_recursos("Cartao")
        if limpa_tabela:
            CartaoJson().cartao_get(True)
        else:
            CartaoJson().cartao_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VINCULO"
        if display:
            self.aviso.exibir_obtendo_recursos("Vinculo")
        if limpa_tabela:
            VinculoJson().vinculo_get(True)
        else:
            VinculoJson().vinculo_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ISENCAO"
        if display:
            self.aviso.exibir_obtendo_recursos("Isencao")
        if limpa_tabela:
            IsencaoJson().isencao_get(True)
        else:
            IsencaoJson().isencao_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UNIDADE TURNO"
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade Turno")
        if limpa_tabela:
            UnidadeTurnoJson().unidade_turno_get(True)
        else:
            UnidadeTurnoJson().unidade_turno_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CATRACA UNIDADE"
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca Unidade")
        if limpa_tabela:
            CatracaUnidadeJson().catraca_unidade_get(True)
        else:
            CatracaUnidadeJson().catraca_unidade_get()
        
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REGISTRO"
        if display:
            self.aviso.exibir_obtendo_recursos("Registro")
        if limpa_tabela:
            RegistroJson().registro_get(True)
        else:
            RegistroJson().registro_get()
        