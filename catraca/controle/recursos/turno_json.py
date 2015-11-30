#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.entidades.turno import Turno


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TurnoJson(ServidorRestful):
    
    log = Logs()
    turno_dao = TurnoDAO()
    
    def __init__(self):
        super(TurnoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def turno_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "turno/jturno"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Código: " + str(r.status_code)
                dados  = json.loads(r.text)
                LISTA_JSON = dados["turnos"]
                
                if limpa_tabela:
                    self.atualiza_exclui(None, True)
                
                if LISTA_JSON is not []:
                    for item in LISTA_JSON:
                        obj = self.dict_obj(item)
                        if obj.id:
                            resultado = self.turno_dao.busca(obj.id)
                            if resultado:
                                self.atualiza_exclui(obj, False)
                            else:
                                self.insere(obj)
                else:
                    self.atualiza_exclui(None, True)
                    
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json turno', exc_info=True)
        finally:
            pass
        
    def atualiza_exclui(self, obj, boleano):
        self.turno_dao.atualiza_exclui(obj, boleano)
        print self.turno_dao.aviso
        
    def insere(self, obj):
        self.turno_dao.insere(obj)
        print self.turno_dao.aviso
        
    def dict_obj(self, formato_json):
        turno = Turno()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "turn_id":
                turno.id = self.dict_obj(formato_json[item])
            if item == "turn_hora_inicio":
                turno.inicio = self.dict_obj(formato_json[item])
            if item == "turn_hora_fim":
                turno.fim = self.dict_obj(formato_json[item])
            if item == "turn_descricao":
                turno.descricao = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
                
        return turno
    