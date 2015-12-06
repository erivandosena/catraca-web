#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.catraca_dao import CatracaDAO
from catraca.modelo.entidades.catraca import Catraca


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class CatracaJson(ServidorRestful):
    
    log = Logs()
    aviso = Aviso()
    catraca_dao = CatracaDAO()
    contador_acesso_servidor = 0
    
    def __init__(self):
        super(CatracaJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def catraca_get(self, limpa_tabela=False):
        IP = Util().obtem_ip()
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "catraca/jcatraca"
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Status HTTP: " + str(r.status_code)

                if r.text == '':
                    self.contador_acesso_servidor += 1
                    if self.contador_acesso_servidor < 4:
                        self.aviso.exibir_falha_servidor()
                        self.aviso.exibir_aguarda_cartao()
                    else:
                        self.contador_acesso_servidor = 0
                else:
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["catracas"]
                    
                    if LISTA_JSON != []:
                        lista = []
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                lista.append(obj)
                                self.mantem_tabela_local(obj, limpa_tabela)
                        return lista
                    else:
                        self.atualiza_exclui(None, True)
                        #return None
                    
#                     if LISTA_JSON != []:
#                         for item in LISTA_JSON:
#                             obj = self.dict_obj(item)
#                             if obj:
#                                 return obj
#                             else:
#                                 return None
                    #else:
                        self.contador_acesso_servidor += 1
                        if self.contador_acesso_servidor < 4:
                            catraca = Catraca()
                            catraca.ip = IP
                            catraca.tempo = 20
                            catraca.operacao = 1
                            catraca.nome = Util().obtem_nome_rpi().upper()
                            self.objeto_json(catraca)
                            
                            return self.catraca_get()
                        else:
                            self.aviso.exibir_falha_servidor()
                            self.aviso.exibir_aguarda_cartao()
                            self.contador_acesso_servidor = 0
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json catraca', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.catraca_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
        
    def atualiza_exclui(self, obj, boleano):
        self.catraca_dao.atualiza_exclui(obj, boleano)
        print self.catraca_dao.aviso
        
    def insere(self, obj):
        self.catraca_dao.insere(obj)
        print self.catraca_dao.aviso
        
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
                catraca.nome = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
                
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
            
    