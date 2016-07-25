#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.isencao_dao import IsencaoDAO
from catraca.modelo.entidades.isencao import Isencao


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class IsencaoJson(ServidorRestful):
    
    log = Logs()
    isencao_dao = IsencaoDAO()
    util = Util()
    
    def __init__(self):
        super(IsencaoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def isencao_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "isencao/jisencao"
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["isencoes"]
                    if LISTA_JSON != []:
                        if limpa_tabela:
                            self.mantem_tabela_local(None, True)
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                self.mantem_tabela_local(obj)  
                        return lista
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json isencao', exc_info=True)
        finally:
            pass
        
    def isencao_ativa_get(self, numero_cartao):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "isencao/jisencao/" + str(numero_cartao)+ "/"+str(self.util.obtem_datahora().strftime("%Y%m%d%H%M%S"))
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["isencao"]
                    if LISTA_JSON != []:
                        for item in LISTA_JSON:
                            obj = self.dict_obj_isencao_ativa(item)
                            if obj:
                                return obj
                            else:
                                return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json isencao', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, mantem_tabela=False):
        if obj:
            objeto = self.isencao_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        print "Acao de atualizacao nao necessaria!"
                        return None
                else:
                    return self.insere(obj)
            else:
                if objeto:
                    return self.atualiza_exclui(obj, mantem_tabela)
        else:
            if mantem_tabela:
                return self.atualiza_exclui(obj, mantem_tabela)
            else:
                print "Nemhuma acao realizada!"
                return None

            
    def atualiza_exclui(self, obj, boleano):
        if self.isencao_dao.atualiza_exclui(obj, boleano):
            print self.isencao_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.isencao_dao.insere(obj):
            print self.isencao_dao.aviso
            return obj
        
    def dict_obj(self, formato_json):
        isencao = Isencao()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "isen_id":
                isencao.id = self.dict_obj(formato_json[item])
            if item == "isen_inicio":
                isencao.inicio = self.dict_obj(formato_json[item])
            if item == "isen_fim":
                isencao.fim = self.dict_obj(formato_json[item])
            if item == "cart_id":
                isencao.cartao = self.dict_obj(formato_json[item])
        return isencao
    
    def dict_obj_isencao_ativa(self, formato_json):
        isencao = Isencao()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj_isencao_ativa(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "isen_inicio":
                isencao.inicio = self.dict_obj_isencao_ativa(formato_json[item])
            if item == "isen_fim":
                isencao.fim = self.dict_obj_isencao_ativa(formato_json[item])
            if item == "cart_id":
                isencao.cartao = self.dict_obj_isencao_ativa(formato_json[item])
        return isencao
    