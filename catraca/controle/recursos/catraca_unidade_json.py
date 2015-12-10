#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.catraca_unidade_dao import CatracaUnidadeDAO
from catraca.modelo.entidades.catraca_unidade import CatracaUnidade


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CatracaUnidadeJson(ServidorRestful):
    
    log = Logs()
    catraca_unidade_dao = CatracaUnidadeDAO()
    
    def __init__(self):
        super(CatracaUnidadeJson, self).__init__()
        ServidorRestful.__init__(self)

    def catraca_unidade_get(self, mantem_tabela=False, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "catraca_unidade/jcatraca_unidade"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                #print "Status HTTP: " + str(r.status_code)

                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["catraca_unidades"]
                    if LISTA_JSON != []:
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                if mantem_tabela:
                                    self.mantem_tabela_local(obj, limpa_tabela)
                        return lista
                    else:
                        self.atualiza_exclui(None, True)
                        return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json catraca-unidade', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.catraca_unidade_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
        
    def atualiza_exclui(self, obj, boleano):
        self.catraca_unidade_dao.atualiza_exclui(obj, boleano)
        print self.catraca_unidade_dao.aviso
        
    def insere(self, obj):
        self.catraca_unidade_dao.insere(obj)
        print self.catraca_unidade_dao.aviso
        
    def dict_obj(self, formato_json):
        catraca_unidade = CatracaUnidade()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "caun_id":
                catraca_unidade.id = self.dict_obj(formato_json[item])
            if item == "catr_id":
                catraca_unidade.catraca = self.dict_obj(formato_json[item])
            if item == "unid_id":
                catraca_unidade.unidade = self.dict_obj(formato_json[item])
                
        return catraca_unidade
    