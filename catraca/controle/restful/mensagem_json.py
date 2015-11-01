#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.mensagem_dao import MensagemDAO
from catraca.modelo.entidades.mensagem import Mensagem


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class MensagemJson(ServidorRestful):
    
    log = Logs()
    mensagem_dao = MensagemDAO()
    
    def __init__(self, ):
        super(MensagemJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def mensagem_get(self):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "mensagem/jmensagem"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "status HTTP:" + str(r.status_code)
                dados  = json.loads(r.text)
                
                for item in dados["mensagens"]:
                    obj = self.dict_obj(item)
                    if obj.id:
                        lista = self.mensagem_dao.busca(obj.id)
                        if lista is None:
                            print "nao existe - insert " + str(obj.numero)
                            self.mensagem_dao.insere(obj)
                            self.mensagem_dao.commit()
                            print self.mensagem_dao.aviso
                        else:
                            print "existe - update " + str(obj.numero)
                            self.mensagem_dao.atualiza_exclui(obj, False)
                            self.mensagem_dao.commit()
                            print self.mensagem_dao.aviso
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json mensagem.', exc_info=True)
        finally:
            pass
        
    def dict_obj(self, formato_json):
        mensagem = Mensagem()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            
            if item == "mens_id":
                mensagem.id = self.dict_obj(formato_json[item])
            if item == "mens_inicializacao":
                mensagem.inicializacao = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_saldacao":
                mensagem.saldacao = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_aguardacartao":
                mensagem.aguardacartao = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_erroleitor":
                mensagem.erroleitor = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_bloqueioacesso":
                mensagem.bloqueioacesso = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_liberaacesso":
                mensagem.liberaacesso = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_semcredito":
                mensagem.semcredito = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_semcadastro":
                mensagem.semcadastro = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_turnoinvalido":
                mensagem.turnoinvalido = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_datainvalida":
                mensagem.datainvalida = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_cartaoutilizado":
                mensagem.cartaoutilizado = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_institucional1":
                mensagem.institucional1 = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_institucional2":
                mensagem.institucional2 = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_institucional3":
                mensagem.institucional3 = self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "mens_institucional4":
                mensagem.institucional4 = self.dict_obj(formato_json[item]).encode('utf-8')

        return mensagem
    