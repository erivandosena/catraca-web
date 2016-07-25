#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.usuario_dao import UsuarioDAO
from catraca.modelo.entidades.usuario import Usuario


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


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
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["usuarios"]
                    if LISTA_JSON != []:
                        if limpa_tabela:
                            self.mantem_tabela_local(None, True)
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                self.mantem_tabela_local(obj)  
                        return lista
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json usuario', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, mantem_tabela=False):
        if obj:
            objeto = self.usuario_dao.busca(obj.id)
            if not mantem_tabela:
                if objeto:
                    if not objeto.__eq__(obj):
                        return self.atualiza_exclui(obj, mantem_tabela)
                    else:
                        print "Acao de atualizacao nao necessaria!"
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
                
        return usuario
    