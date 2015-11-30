#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.giro_dao import GiroDAO
from catraca.modelo.entidades.giro import Giro


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class GiroJson(ServidorRestful):
    
    log = Logs()
    giro_dao = GiroDAO()
    
    def __init__(self):
        super(GiroJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def giro_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "giro/jgiro"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "status HTTP:" + str(r.status_code)
                dados  = json.loads(r.text)
                LISTA_JSON = dados["giros"]
                
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
            self.log.logger.error('Erro obtendo json giro', exc_info=True)
        finally:
            pass
        
    def atualiza_exclui(self, obj, boleano):
        self.giro_dao.atualiza_exclui(obj, boleano)
        print self.giro_dao.aviso
        
    def insere(self, obj):
        self.giro_dao.insere(obj)
        print self.giro_dao.aviso
        
    def dict_obj(self, formato_json):
        giro = Giro()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "giro_id":
                giro.id = self.dict_obj(formato_json[item])
            if item == "giro_giros_horario":
                giro.horario = self.dict_obj(formato_json[item])
            if item == "giro_giros_antihorario":
                giro.antihorario = self.dict_obj(formato_json[item])
            if item == "giro_data_giros":
                giro.data = self.dict_obj(formato_json[item])
            if item == "catr_id":
                giro.catraca = self.dict_obj(formato_json[item])
                
        return giro
    