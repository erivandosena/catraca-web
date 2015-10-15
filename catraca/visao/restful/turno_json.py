#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.visao.restful.servidor_restful import ServidorRestful
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.entidades.turno import Turno


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TurnoJson(ServidorRestful):
    
    log = Logs()
    turno_dao = TurnoDAO()
    
    def __init__(self, ):
        super(TurnoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def turno_get(self):
        url = self.obter_servidor() + "turno/jturno"
        header = {'Content-type': 'application/json'}
        r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
        print "Código: " + str(r.status_code)
        dados  = json.loads(r.text)
        
        for item in dados["turnos"]:
            obj = self.dict_obj(item)
            if obj.id:
                lista = self.turno_dao.busca(obj.id)
                if lista is None:
                    print "nao existe - insert " + str(obj.descricao)
                    self.turno_dao.insere(obj)
                    print self.turno_dao.aviso
                else:
                    print "existe - update " + str(obj.descricao)
                    self.turno_dao.atualiza_exclui(obj, False)
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
                turno.descricao = self.dict_obj(formato_json[item]).encode('utf-8')
                
        return turno
    