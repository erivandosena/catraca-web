#!/usr/bin/env python
# -*- coding: utf-8 -*-


from argparse import Namespace
import simplejson as json
from simplejson import JSONDecodeError
import requests

from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
from requests.exceptions import RequestException
from requests.exceptions import ConnectionError

from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.usuario_dao import UsuarioDAO
from catraca.modelo.entidades.usuario import Usuario
from catraca.modelo.entidades.usuario_externo import UsuarioExterno


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class UsuarioJson(ServidorRestful):
    
    log = Logs()
    usuario_dao = UsuarioDAO()
    
    def __init__(self):
        super(UsuarioJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def usuario_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "usuario/jusuario"
                r = servidor.get(url)
                print url
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["usuarios"]
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
            
    def status_usuario_externo_get(self, id_externo):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "usuario/jusuario/" + str(id_externo)
                r = servidor.get(url)
                print url
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["status_usuario"]
                    if LISTA_JSON != []:
                        dic_namespace = json.dumps(LISTA_JSON[0], use_decimal=False, ensure_ascii=True, sort_keys=False, encoding='utf-8')
                        obj = json.loads(dic_namespace, object_hook=lambda i: Namespace(**i))
#                         for item in LISTA_JSON:
#                             obj = self.dict_obj_usuario_externo(item)
#                             if obj:
#                                 return obj
                        return obj
                    else:
                        return None
        except JSONDecodeError:
            self.log.logger.error("JSONDecodeError", exc_info=True)
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
            objeto = self.usuario_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
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
        if self.usuario_dao.atualiza_exclui(obj, boleano):
            print self.usuario_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.usuario_dao.insere(obj):
            print self.usuario_dao.aviso
            return obj
        
    def dict_obj(self, formato_json):
        usuario = Usuario()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "usua_id":
                usuario.id = self.dict_obj(formato_json[item])
            if item == "usua_nome":
                usuario.nome = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is \
                None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_email":
                usuario.email = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is \
                None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_login":
                usuario.login = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is \
                None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_senha":
                usuario.senha = self.dict_obj(formato_json[item])
            if item == "usua_nivel":
                usuario.nivel = self.dict_obj(formato_json[item])
            if item == "id_base_externa":
                usuario.idexterno = self.dict_obj(formato_json[item])
                
        return usuario
    