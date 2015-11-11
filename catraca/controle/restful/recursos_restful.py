#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
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

    def __init__(self, ):
        super(RecursosRestful, self).__init__()

    def obtem_recursos(self):
        CatracaJson().catraca_get()
        TipoJson().tipo_get()
        TurnoJson().turno_get()
        UnidadeJson().unidade_get()
        CustoRefeicaoJson().custo_refeicao_get()
        UsuarioJson().usuario_get()
        GiroJson().giro_get()
        MensagemJson().mensagem_get()
        CartaoJson().cartao_get()
        VinculoJson().vinculo_get()
        IsencaoJson().isencao_get()
        UnidadeTurnoJson().unidade_turno_get()
        CatracaUnidadeJson().catraca_unidade_get()
        RegistroJson().registro_get()
        
