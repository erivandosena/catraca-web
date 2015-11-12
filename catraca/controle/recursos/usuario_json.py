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
    
    def __init__(self, ):
        super(UsuarioJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def usuario_get(self):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "usuario/jusuario"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "status HTTP: " + str(r.status_code)
                dados  = json.loads(r.text)
                
                if dados["usuarios"] is not []:
                    for item in dados["usuarios"]:
                        obj = self.dict_obj(item)
                        if obj.id:
                            lista = self.usuario_dao.busca(obj.id)
                            if lista is None:
                                print "nao existe - insert " + str(obj.nome)
                                self.usuario_dao.insere(obj)
                                print self.usuario_dao.aviso
                            else:
                                print "existe - update " + str(obj.nome)
                                self.usuario_dao.atualiza_exclui(obj, False)
                                print self.usuario_dao.aviso
                if dados["usuarios"] == []:
                    self.usuario_dao.atualiza_exclui(None,True)
                    print self.usuario_dao.aviso
                    
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json usuario.', exc_info=True)
        finally:
            pass
        
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
                usuario.nome = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_email":
                usuario.email = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_login":
                usuario.login = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "usua_senha":
                usuario.senha = self.dict_obj(formato_json[item])
            if item == "usua_nivel":
                usuario.nivel = self.dict_obj(formato_json[item])
                
        return usuario
    