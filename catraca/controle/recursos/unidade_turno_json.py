#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests

from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError

from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.unidade_turno_dao import UnidadeTurnoDAO
from catraca.modelo.entidades.unidade_turno import UnidadeTurno


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class UnidadeTurnoJson(ServidorRestful):
    
    log = Logs()
    unidade_turno_dao = UnidadeTurnoDAO()
    
    def __init__(self):
        super(UnidadeTurnoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def unidade_turno_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "unidade_turno/junidade_turno"
                r = servidor.get(url)
                print url
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["unidade_turnos"]
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
        except Timeout:
            self.log.logger.error("Timeout", exc_info=True)
        except HTTPError:
            self.log.logger.error("HTTPError", exc_info=True)
        except TooManyRedirects:
            self.log.logger.error("TooManyRedirects", exc_info=True)
        except RequestException:
            self.log.logger.error("RequestException", exc_info=True)
        except ConnectionError:
            self.log.logger.error("ConnectionError", exc_info=True)
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            
    def mantem_tabela_local(self, obj, mantem_tabela=False):
        if obj:
            objeto = self.unidade_turno_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        #print "[UNIDADE TURNO]Acao de atualizacao nao necessaria!"
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
        if self.unidade_turno_dao.atualiza_exclui(obj, boleano):
            print self.unidade_turno_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.unidade_turno_dao.insere(obj):
            print self.unidade_turno_dao.aviso
            return obj
        
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
    