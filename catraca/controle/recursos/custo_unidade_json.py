#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.custo_unidade_dao import CustoUnidadeDAO
from catraca.modelo.entidades.custo_unidade import CustoUnidade


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CustoUnidadeJson(ServidorRestful):
    
    log = Logs()
    custo_unidade_dao = CustoUnidadeDAO()
    
    def __init__(self):
        super(CustoUnidadeJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def custo_unidade_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "custo_unidade/jcusto_unidade"
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["custo_unidade"]
                    if LISTA_JSON != []:
                        if limpa_tabela:
                            return self.mantem_tabela_local(None, True)
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                self.mantem_tabela_local(obj)  
                        return lista
                else:
                    return None
#         except Exception as excecao:
#             print excecao
#             self.log.logger.error('Erro obtendo json custo-unidade', exc_info=True)
#             return None
        finally:
            pass
        
#     def custo_unidade_atual_get(self):
#         servidor = self.obter_servidor()
#         try:
#             if servidor:
#                 url = str(self.URL) + "custo_unidade/jcusto_unidade"
#                 r = servidor.get(url)
#                 if r.text != '':
#                     dados  = json.loads(r.text)
#                     LISTA_JSON = dados["custo_unidade"]
#                     if LISTA_JSON != []:
#                         for item in LISTA_JSON:
#                             obj = self.dict_obj(item)
#                             return obj.valor if obj else 0
#                 else:
#                     return None
#         except Exception as excecao:
#             print excecao
#             self.log.logger.error('Erro obtendo json custo-unidade', exc_info=True)
#             return None
#         finally:
#             pass
        
    def mantem_tabela_local(self, obj, mantem_tabela=False):
        if obj:
            objeto = self.custo_unidade_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        #print "[CUSTO UNIDADE]Acao de atualizacao nao necessaria!"
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
        if self.custo_unidade_dao.atualiza_exclui(obj, boleano):
            print self.custo_unidade_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.custo_unidade_dao.insere(obj):
            print self.custo_unidade_dao.aviso
            return obj
        
    def dict_obj(self, formato_json):
        custo_unidade = CustoUnidade()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "cuun_id":
                custo_unidade.id = self.dict_obj(formato_json[item])
            if item == "unid_id":
                custo_unidade.unidade = self.dict_obj(formato_json[item])
            if item == "cure_id":
                custo_unidade.custo = self.dict_obj(formato_json[item])
        return custo_unidade
    