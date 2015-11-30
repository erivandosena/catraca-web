#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.unidade_dao import UnidadeDAO
from catraca.modelo.entidades.unidade import Unidade


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class UnidadeJson(ServidorRestful):
    
    log = Logs()
    unidade_dao = UnidadeDAO()
    
    def __init__(self):
        super(UnidadeJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def unidade_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "unidade/junidade"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "status HTTP: " + str(r.status_code)
                dados  = json.loads(r.text)
                LISTA_JSON = dados["unidades"]
                
                if limpa_tabela:
                    self.atualiza_exclui(None, True)
                
                if LISTA_JSON is not []:
                    for item in LISTA_JSON:
                        obj = self.dict_obj(item)
                        if obj.id:
                            self.atualiza_exclui(obj, False)
                        else:
                            self.insere(obj)
                else:
                    self.atualiza_exclui(None, True)
                    
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json unidade', exc_info=True)
        finally:
            pass
        
    def atualiza_exclui(self, obj, boleano):
        self.unidade_dao.atualiza_exclui(obj, boleano)
        print self.unidade_dao.aviso
        
    def insere(self, obj):
        self.unidade_dao.insere(obj)
        print self.unidade_dao.aviso
        
    def dict_obj(self, formato_json):
        unidade = Unidade()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "unid_id":
                unidade.id = self.dict_obj(formato_json[item])
            if item == "unid_nome":
                unidade.nome = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
                
        return unidade
    