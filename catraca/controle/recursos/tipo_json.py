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
from catraca.modelo.dao.tipo_dao import TipoDAO
from catraca.modelo.entidades.tipo import Tipo


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class TipoJson(ServidorRestful):
    
    log = Logs()
    tipo_dao = TipoDAO()
    
    def __init__(self):
        super(TipoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def tipo_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "tipo/jtipo"
                r = servidor.get(url)
                print url
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["tipos"]
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
            objeto = self.tipo_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        #print "[TIPO]Acao de atualizacao nao necessaria!"
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
        if self.tipo_dao.atualiza_exclui(obj, boleano):
            print self.tipo_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.tipo_dao.insere(obj):
            print self.tipo_dao.aviso
            return obj
        
    def dict_obj(self, formato_json):
        tipo = Tipo()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "tipo_id":
                tipo.id = self.dict_obj(formato_json[item])
            if item == "tipo_nome":
                tipo.nome = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "tipo_valor":
                tipo.valor = self.dict_obj(formato_json[item])
                
        return tipo
    