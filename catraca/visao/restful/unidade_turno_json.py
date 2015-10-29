#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.unidade_turno_dao import UnidadeTurnoDAO
from catraca.modelo.entidades.unidade_turno import UnidadeTurno


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class UnidadeTurnoJson(ServidorRestful):
    
    log = Logs()
    unidade_turno_dao = UnidadeTurnoDAO()
    
    def __init__(self, ):
        super(UnidadeTurnoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def unidade_turno_get(self):
        url = self.obter_servidor() + "unidade_turno/junidade_turno"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.unidade_turno, self.senha), headers=header)
        print "status HTTP: " + str(r.status_code)
        dados  = json.loads(r.text)
        
        for item in dados["unidade_turnos"]:
            obj = self.dict_obj(item)
            if obj.id:
                lista = self.unidade_turno_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.nome)
                    self.unidade_turno_dao.insere(obj)
                    print self.unidade_turno_dao.aviso
                else:
                    print "existe - update " + str(obj.nome)
                    self.unidade_turno_dao.atualiza_exclui(obj, False)
                    print self.unidade_turno_dao.aviso
        
    def dict_obj(self, formato_json):
        unidade_turno = UnidadeTurno()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "untu_id":
                unidade_turno.id = self.dict_obj(formato_json[item])
            if item == "turn_id":
                unidade_turno.turno = self.dict_obj(formato_json[item])
            if item == "unid_id":
                unidade_turno.unidade = self.dict_obj(formato_json[item])
                
        return unidade_turno
    