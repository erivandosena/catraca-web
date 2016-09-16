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
from catraca.util import Util
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.cartao_dao import CartaoDAO
from catraca.modelo.entidades.cartao import Cartao
from catraca.modelo.entidades.cartao_valido import CartaoValido


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CartaoJson(ServidorRestful):
    
    log = Logs()
    cartao_dao = CartaoDAO()
    util = Util()
    
    def __init__(self):
        super(CartaoJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def cartao_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "cartao/jcartao"
                print url
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["cartoes"]
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
            
    def cartao_valido_get(self, numero_cartao):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "cartao/jcartao/" + str(numero_cartao)
                r = servidor.get(url)
                print url
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["cartao_valido"]
                    print LISTA_JSON
                    if LISTA_JSON != []:
                        for item in LISTA_JSON:
                            obj = self.dict_obj_cartao_valido(item)
                            if obj:
                                return obj
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
            objeto = self.cartao_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        #print "[CARTAO]Acao de atualizacao nao necessaria!"
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
        if self.cartao_dao.atualiza_exclui(obj, boleano):
            #self.cartao_dao.commit()
            print self.cartao_dao.aviso
            if not boleano:
                return obj
            else:
                return None
            
    def insere(self, obj):
        if self.cartao_dao.insere(obj):
            #self.cartao_dao.commit()
            print self.cartao_dao.aviso
            return obj
        
    def dict_obj(self, formato_json):
        cartao = Cartao()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "cart_id":
                cartao.id = self.dict_obj(formato_json[item])
            if item == "cart_numero":
                cartao.numero = self.dict_obj(formato_json[item])
            if item == "cart_creditos":
                cartao.creditos = self.dict_obj(formato_json[item])
            if item == "tipo_id":
                cartao.tipo = self.dict_obj(formato_json[item])
        return cartao

    def dict_obj_cartao_valido(self, formato_json):
        cartao_valido = CartaoValido()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj_cartao_valido(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "cart_id":
                cartao_valido.id = self.dict_obj_cartao_valido(formato_json[item])
            if item == "cart_numero":
                cartao_valido.numero = self.dict_obj_cartao_valido(formato_json[item])
            if item == "cart_creditos":
                cartao_valido.creditos = self.dict_obj_cartao_valido(formato_json[item])
            if item == "tipo_valor":
                cartao_valido.valor = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_refeicoes":
                cartao_valido.refeicoes = self.dict_obj_cartao_valido(formato_json[item])
            if item == "tipo_id":
                cartao_valido.tipo = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_id":
                cartao_valido.vinculo = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_descricao":
                cartao_valido.descricao = self.dict_obj_cartao_valido(formato_json[item]) if \
                self.dict_obj_cartao_valido(formato_json[item]) is None else \
                self.dict_obj_cartao_valido(formato_json[item]).encode('utf-8')
            if item == "vinc_inicio":
                cartao_valido.inicio = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_fim":
                cartao_valido.fim = self.dict_obj_cartao_valido(formato_json[item])
            if item == "usua_nome":
                cartao_valido.nome = self.dict_obj_cartao_valido(formato_json[item]) \
                if self.dict_obj_cartao_valido(formato_json[item]) is None else \
                self.dict_obj_cartao_valido(formato_json[item]).encode('utf-8')
            if item == "tipo_nome":
                cartao_valido.tiponome = self.dict_obj_cartao_valido(formato_json[item]) \
                if self.dict_obj_cartao_valido(formato_json[item]) is None else \
                self.dict_obj_cartao_valido(formato_json[item]).encode('utf-8')
            if item == "id_base_externa":
                cartao_valido.idexterno = self.dict_obj_cartao_valido(formato_json[item])
            if item == "vinc_avulso":
                cartao_valido.avulso = self.dict_obj_cartao_valido(formato_json[item])
        return cartao_valido
    
    def lista_json(self, lista):
        if lista:
            for item in lista:
                cartao = {
                    "cart_numero":item[1],
                    "cart_creditos":float(item[2]),
                    "tipo_id":item[3]
                }
                return self.cartao_put(cartao, item[0])
                
    def objeto_json(self, obj):
        if obj:
            cartao = {
                "cart_numero":obj.numero,
                "cart_creditos":float(obj.creditos),
                "tipo_id":obj.tipo
            }
            return self.cartao_put(cartao, obj.id)
            
    def cartao_put(self, formato_json, id):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "cartao/atualiza/"+ str(id)
                r = servidor.put(url, data=json.dumps(formato_json))
                return r.status_code
            else:
                return 0
        except Timeout:
            self.log.logger.error("Timeout", exc_info=True)
            return 0
        except HTTPError:
            self.log.logger.error("HTTPError", exc_info=True)
            return 0
        except TooManyRedirects:
            self.log.logger.error("TooManyRedirects", exc_info=True)
            return 0
        except RequestException:
            self.log.logger.error("RequestException", exc_info=True)
            return 0
        except ConnectionError:
            self.log.logger.error("ConnectionError", exc_info=True)
            return 0
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            return 0
        