#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.entidades.catraca import Catraca


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CatracaJson(ServidorRestful):
    
    log = Logs()
    catraca_dao = CatracaDAO()
    
    def __init__(self, ):
        super(CatracaJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def catraca_get(self):
        IP = Util().obtem_ip()
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "catraca/jcatraca"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Código: " + str(r.status_code)
                dados  = json.loads(r.text)

                if dados["catracas"] is not []:
                    print "PASSOU ===>>>>>>>>> if dados[catracas] is not []:"
                    for item in dados["catracas"]:
                        obj = self.dict_obj(item)
                        if obj.id:
                            lista = self.catraca_dao.busca(obj.id)
                            if lista is None:
                                print "nao existe - insert " + str(obj.nome)
                                self.catraca_dao.insere(obj)
                                print self.catraca_dao.aviso
                            else:
                                print "existe - update " + str(obj.nome)
                                self.catraca_dao.atualiza_exclui(obj, False)
                                print self.catraca_dao.aviso
                                
                if dados["catracas"] == []:
                    print "PASSOU ===>>>>>>>>> if dados[catracas] == []:"
                    print "limpa tabela"
                    self.catraca_dao.atualiza_exclui(None,True)
                    print self.catraca_dao.aviso
                    
                    catraca = Catraca()
                    catraca.ip = IP
                    catraca.tempo = 20
                    catraca.operacao = 1
                    catraca.nome = Util().obtem_nome_rpi().upper()
                    self.objeto_json(catraca)
                    
                    print "PASSarr em ==> self.catraca_get()"
                    self.catraca_get()
       
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json catraca.', exc_info=True)
        finally:
            pass
        
    def dict_obj(self, formato_json):
        catraca = Catraca()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "catr_id":
                catraca.id = self.dict_obj(formato_json[item])
            if item == "catr_ip":
                catraca.ip = self.dict_obj(formato_json[item])
            if item == "catr_tempo_giro":
                catraca.tempo = self.dict_obj(formato_json[item])
            if item == "catr_operacao":
                catraca.operacao = self.dict_obj(formato_json[item])
            if item == "catr_nome":
                catraca.nome = self.dict_obj(formato_json[item]).encode('utf-8')
                
        return catraca
    
    def lista_json(self, lista):
        if lista:
            for item in lista:
                catraca = {
                    "catr_ip":str(item[1]),
                    "catr_tempo_giro":item[2],
                    "catr_operacao":item[3],
                    "catr_nome":str(item[4])
                }
                self.catraca_post(catraca)
                #self.registro_dao.mantem(self.registro_dao.busca(item[0]),True)

    def objeto_json(self, obj):
        if obj:
            catraca = {
                "catr_ip":str(obj.ip),
                "catr_tempo_giro":obj.tempo,
                "catr_operacao":obj.operacao,
                "catr_nome":str(obj.nome)
            }
            self.catraca_post(catraca)
            
    def catraca_post(self, formato_json):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "catraca/insere"
                print url
                header = {'Content-type': 'application/json'}
                r = requests.post(url, auth=(self.usuario, self.senha), headers=header, data=json.dumps(formato_json))
                print r.text
                print r.status_code
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro enviando json catraca.', exc_info=True)
        finally:
            pass
            
    