#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.vinculo_dao import VinculoDAO
from catraca.modelo.entidades.vinculo import Vinculo


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class VinculoJson(ServidorRestful):
    
    log = Logs()
    vinculo_dao = VinculoDAO()
    
    def __init__(self):
        super(VinculoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def vinculo_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "vinculo/jvinculo"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Status HTTP: " + str(r.status_code)

                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["vinculos"]
                    if LISTA_JSON != []:
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                self.mantem_tabela_local(obj, limpa_tabela)
                        return lista
                    else:
                        self.atualiza_exclui(None, True)
                        return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json vinculo', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.vinculo_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
        
    def atualiza_exclui(self, obj, boleano):
        self.vinculo_dao.atualiza_exclui(obj, boleano)
        print self.vinculo_dao.aviso
        
    def insere(self, obj):
        self.vinculo_dao.insere(obj)
        print self.vinculo_dao.aviso
        
    def dict_obj(self, formato_json):
        vinculo = Vinculo()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "vinc_id":
                vinculo.id = self.dict_obj(formato_json[item])
            if item == "vinc_avulso":
                vinculo.avulso = self.dict_obj(formato_json[item])
            if item == "vinc_inicio":
                vinculo.inicio = self.dict_obj(formato_json[item])
            if item == "vinc_fim":
                vinculo.fim = self.dict_obj(formato_json[item])
            if item == "vinc_descricao":
                    vinculo.fim = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "vinc_refeicoes":
                vinculo.refeicoes = self.dict_obj(formato_json[item])
            if item == "cart_id":
                vinculo.cartao = self.dict_obj(formato_json[item])
            if item == "usua_id":
                vinculo.usuario = self.dict_obj(formato_json[item])
                
        return vinculo
    