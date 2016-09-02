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
from catraca.controle.recursos.custo_unidade_json import CustoUnidadeJson
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
    custo_unidade_json = CustoUnidadeJson()
    cartao_json = CartaoJson()
    isencao_json = IsencaoJson()
    vinculo_json = VinculoJson()
    registro_json = RegistroJson()
    
    obtendo_recurso =  False
    
    def __init__(self, ):
        super(RecursosRestful, self).__init__()
        
    def obtem_recursos(self, display=False, limpa_tabela=False):
        #RecursosRestful.obtendo_recurso = True
        if RecursosRestful.obtendo_recurso:
            print "\nObtendo recursos do servidor RESTful..."
            #self.obtem_catraca(display, limpa_tabela)
            self.obtem_unidade(display, limpa_tabela)
            self.obtem_catraca_unidade(display, limpa_tabela)
            self.obtem_turno(display, limpa_tabela)
            self.obtem_unidade_turno(display, limpa_tabela)
            self.obtem_custo_refeicao(display, limpa_tabela)
            self.obtem_custo_unidade(display, limpa_tabela)
            self.obtem_tipo(display, limpa_tabela)
            self.obtem_cartao(display, limpa_tabela)
            self.obtem_usuario(display, limpa_tabela)
            self.obtem_vinculo(display, limpa_tabela)
            self.obtem_isencao(display, limpa_tabela)
            self.obtem_mensagem(display, limpa_tabela)
            #RecursosRestful.obtendo_recurso = False
            #return RecursosRestful.obtendo_recurso
        
    def obtem_catraca(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca")
        catraca = self.catraca_json.catraca_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if catraca:
            print "-------------------------------"
            print "Recurso CATRACA obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso CATRACA nulo!"
            print "-------------------------------"
        return catraca
        
    def obtem_mensagem(self, display=False, limpa_tabela=False):
       # if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Mensagem")
        mensagem = self.mensagem_json.mensagem_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if mensagem:
            print "-------------------------------"
            print "Recurso MENSAGEM obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso MENSAGEM nulo!"
            print "-------------------------------"
        return mensagem
                
    def obtem_unidade(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade")
        unidade = self.unidade_json.unidade_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if unidade:
            print "-------------------------------"
            print "Recurso UNIDADE obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso UNIDADE nulo!"
            print "-------------------------------"
        return unidade
                
    def obtem_catraca_unidade(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Catraca Unidade")
        catraca_unidade = self.catraca_unidade_json.catraca_unidade_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if catraca_unidade:
            print "-------------------------------"
            print "Recurso CATRACA-UNIDADE obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso CATRACA-UNIDADE nulo!"
            print "-------------------------------"
        return catraca_unidade
                
    def obtem_turno(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Turno")
        turno = self.turno_json.turno_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if turno:
            print "-------------------------------"
            print "Recurso TURNO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso TURNO nulo!"
            print "-------------------------------"
        return turno
                
    def obtem_unidade_turno(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Unidade Turno")
        unidade_turno = self.unidade_turno_json.unidade_turno_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if unidade_turno:
            print "-------------------------------"
            print "Recurso UNIDADE-TURNO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso UNIDADE-TURNO nulo!"
            print "-------------------------------"
        return unidade_turno
                
    def obtem_tipo(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Tipo")
        tipo = self.tipo_json.tipo_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if tipo:
            print "-------------------------------"
            print "Recurso TIPO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso TIPO nulo!"
            print "-------------------------------"
        return tipo
                
    def obtem_usuario(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Usuario")
        usuario = self.usuario_json.usuario_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if usuario:
            print "-------------------------------"
            print "Recurso USUARIO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso USUARIO nulo!"
            print "-------------------------------"
        return usuario
                
    def obtem_custo_refeicao(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Custo Refeicao")
        custo_refeicao = self.custo_refeicao_json.custo_refeicao_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if custo_refeicao:
            print "-------------------------------"
            print "Recurso CUSTO-REFEICAO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso CUSTO-REFEICAO nulo!"
            print "-------------------------------"
        return custo_refeicao
        
    def obtem_custo_unidade(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Custo Unidade")
        custo_unidade = self.custo_unidade_json.custo_unidade_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if custo_unidade:
            print "-------------------------------"
            print "Recurso CUSTO-UNIDADE obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso CUSTO-UNIDADE nulo!"
            print "-------------------------------"
        return custo_unidade
                
    def obtem_cartao(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Cartao")
        cartao = self.cartao_json.cartao_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if cartao:
            print "-------------------------------"
            print "Recurso CARTAO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso CARTAO nulo!"
            print "-------------------------------"
        return cartao
                
    def obtem_vinculo(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Vinculo")
        vinculo = self.vinculo_json.vinculo_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if vinculo:
            print "-------------------------------"
            print "Recurso VINCULO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso VINCULO nulo!"
            print "-------------------------------"
        return vinculo
                
    def obtem_isencao(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Isencao")
        isencao = self.isencao_json.isencao_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if isencao:
            print "-------------------------------"
            print "Recurso ISENCAO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso ISENCAO nulo!"
            print "-------------------------------"
        return isencao
                
    def obtem_registro(self, display=False, limpa_tabela=False):
        #if Rede.status:
        if display:
            self.aviso.exibir_obtendo_recursos("Registro")
        registro = self.registro_json.registro_get(limpa_tabela)
        if display:
            self.aviso.exibir_aguarda_cartao()
        if registro:
            print "-------------------------------"
            print "Recurso REGISTRO obtido!"
            print "-------------------------------"
        else:
            print "-------------------------------"
            print "Recurso REGISTRO nulo!"
            print "-------------------------------"
        return registro
        