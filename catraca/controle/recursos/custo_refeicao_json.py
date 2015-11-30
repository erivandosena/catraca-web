#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.custo_refeicao_dao import CustoRefeicaoDAO
from catraca.modelo.entidades.custo_refeicao import CustoRefeicao


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CustoRefeicaoJson(ServidorRestful):
    
    log = Logs()
    custo_refeicao_dao = CustoRefeicaoDAO()
    
    def __init__(self):
        super(CustoRefeicaoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def custo_refeicao_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "custo_refeicao/jcusto_refeicao"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "status HTTP: " + str(r.status_code)
                dados  = json.loads(r.text)
                LISTA_JSON = dados["custo_refeicoes"]
                
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
            self.log.logger.error('Erro obtendo json custo-refeicao', exc_info=True)
        finally:
            pass
        
    def atualiza_exclui(self, obj, boleano):
        self.custo_refeicao_dao.atualiza_exclui(obj, boleano)
        print self.custo_refeicao_dao.aviso
        
    def insere(self, obj):
        self.custo_refeicao_dao.insere(obj)
        print self.custo_refeicao_dao.aviso
        
    def dict_obj(self, formato_json):
        custo_refeicao = CustoRefeicao()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "cure_id":
                custo_refeicao.id = self.dict_obj(formato_json[item])
            if item == "cure_valor":
                custo_refeicao.valor = self.dict_obj(formato_json[item])
            if item == "cure_data":
                custo_refeicao.data = self.dict_obj(formato_json[item])

                
        return custo_refeicao
    