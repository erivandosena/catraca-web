#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.modelo.entidades.turno import Turno


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TurnoJson(ServidorRestful):
    
    log = Logs()
    util = Util()
    turno_dao = TurnoDAO()
    
    def __init__(self):
        super(TurnoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def turno_get(self, mantem_tabela=False, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "turno/jturno"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                #print "Status HTTP: " + str(r.status_code)

                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["turnos"]
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
            self.log.logger.error('Erro obtendo json turno', exc_info=True)
        finally:
            pass
        
    def turno_funcionamento_get(self):
        IP = Util().obtem_ip_por_interface()
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "turno/jturno/" + str(self.util.converte_ip_para_long(IP)) + "/" + str(self.util.obtem_hora())
                print url
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Status HTTP: " + str(r.status_code)
                
                print r.text

                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["turno"]
                    if LISTA_JSON != []:
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                return obj
                            else:
                                return None
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json turno', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.turno_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
                    
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
    