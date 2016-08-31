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
        
    def turno_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "turno/jturno"
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["turnos"]
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
#             self.log.logger.error('Erro obtendo json turno', exc_info=True)
#             return None
        finally:
            pass
        
    def turno_funcionamento_get(self):
        IP = Util().obtem_ip_por_interface()
        servidor = self.obter_servidor()
        try:
            if servidor and IP:
                url = str(self.URL) + "turno/jturno/" + str(self.util.converte_ip_para_long(IP)) + "/" + str(self.util.obtem_hora())
                r = servidor.get(url)
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
            return None
        finally:
            pass
        
    def mantem_tabela_local(self, obj, mantem_tabela=False):
        if obj:
            objeto = self.turno_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        #print "[TURNO]Acao de atualizacao nao necessaria!"
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
        if self.turno_dao.atualiza_exclui(obj, boleano):
            print self.turno_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.turno_dao.insere(obj):
            print self.turno_dao.aviso
            return obj
        
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
    