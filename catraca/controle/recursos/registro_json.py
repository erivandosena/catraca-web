#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import datetime
from catraca.logs import Logs
from catraca.util import Util
from catraca.modelo.dados.servidor_restful import ServidorRestful
from catraca.modelo.dao.registro_dao import RegistroDAO
from catraca.modelo.entidades.registro import Registro
from catraca.modelo.dao.turno_dao import TurnoDAO
from catraca.controle.recursos.turno_json import TurnoJson


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


class RegistroJson(ServidorRestful):
    
    log = Logs()
    util = Util()
    turno_dao = TurnoDAO()
    registro_dao = RegistroDAO()

    hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    
    def __init__(self):
        super(RegistroJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def registro_get(self, mantem_tabela=False, limpa_tabela=False):
        servidor = self.obter_servidor()
        turno = self.obtem_turno_valido()
        if turno:
            self.hora_inicio = datetime.datetime.strptime(str(turno.inicio),'%H:%M:%S').time()
            self.hora_fim = datetime.datetime.strptime(str(turno.fim),'%H:%M:%S').time()
        try:
            if servidor:
                url = str(servidor) + "registro/jregistro/" + str(self.hora_inicio) + "/" +str(self.hora_fim)
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                #print "Status HTTP: " + str(r.status_code)
                
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["registros"]
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
            self.log.logger.error('Erro obtendo json registro', exc_info=True)
        finally:
            pass
        
    def registro_utilizacao_get(self, hora_ini, hora_fim, cartao_id):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "registro/jregistro/" +str(hora_ini) + "/" +str(hora_fim)+ "/" +str(cartao_id)
                header = {'Content-type': 'application/json'}
                r = requests.get(url, auth=(self.usuario, self.senha), headers=header)
                print "Status HTTP: " + str(r.status_code)
                
                print r.text
                
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["quantidade"]
                    if LISTA_JSON != []:
                        for item in LISTA_JSON:
                            obj = self.dict_obj_utilizacao(item)
                            if obj:
                                return int(obj)
                            else:
                                return 0
                else:
                    return None
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro obtendo json registro', exc_info=True)
        finally:
            pass
        
    def mantem_tabela_local(self, obj, limpa_tabela=False):
        if limpa_tabela:
            self.atualiza_exclui(None, limpa_tabela)
        if obj:
            resultado = self.registro_dao.busca(obj.id)
            if resultado:
                self.atualiza_exclui(obj, False)
            else:
                self.insere(obj)
        else:
            return None
        
    def atualiza_exclui(self, obj, boleano):
        self.registro_dao.atualiza_exclui(obj, boleano)
        print self.registro_dao.aviso
        
    def insere(self, obj):
        self.registro_dao.insere(obj)
        print self.registro_dao.aviso
        
    def dict_obj(self, formato_json):
        registro = Registro()
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "regi_id":
                registro.id = self.dict_obj(formato_json[item])
            if item == "regi_data":
                registro.data = self.dict_obj(formato_json[item])
            if item == "regi_valor_pago":
                registro.pago = self.dict_obj(formato_json[item])
            if item == "regi_valor_custo":
                registro.custo = self.dict_obj(formato_json[item])
            if item == "cart_id":
                registro.cartao = self.dict_obj(formato_json[item])
            if item == "catr_id":
                registro.catraca = self.dict_obj(formato_json[item])
            if item == "vinc_id":
                registro.vinculo = self.dict_obj(formato_json[item])
        return registro
    
    def dict_obj_utilizacao(self, formato_json):
        utilizado = None
        if isinstance(formato_json, list):
            formato_json = [self.dict_obj_utilizacao(x) for x in formato_json]
        if not isinstance(formato_json, dict):
            return formato_json
        for item in formato_json:
            if item == "total":
                utilizado = self.dict_obj_utilizacao(formato_json[item])
        return utilizado
    
    def lista_json(self, lista):
        if lista:
            for item in lista:
                registro = {
                    "regi_data":str(item[1]),
                    "regi_valor_pago":float(item[2]),
                    "regi_valor_custo":float(item[3]),
                    "cart_id":item[4],
                    "catr_id":item[5],
                    "vinc_id":item[6]
                }
                self.registro_post(registro)
                #self.registro_dao.mantem(self.registro_dao.busca(item[0]),True)

    def objeto_json(self, obj):
        if obj:
            registro = {
                "regi_data":str(obj.data),
                "regi_valor_pago":float(obj.pago),
                "regi_valor_custo":float(obj.custo),
                "cart_id":obj.cartao,
                "catr_id":obj.catraca,
                "vinc_id":obj.vinculo
            }
            self.registro_post(registro)
            
    def registro_post(self, formato_json):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(servidor) + "registro/insere"
                print url
                header = {'Content-type': 'application/json'}
                r = requests.post(url, auth=(self.usuario, self.senha), headers=header, data=json.dumps(formato_json))
                #print r.headers['content-type']
                #print r.headers
                print r.text
                print r.status_code
                #print 'requests.post: '+ str(formato_json)
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro enviando json registro.', exc_info=True)
        finally:
            pass

    def obtem_turno_valido(self):
        #remoto
        turno_ativo = TurnoJson().turno_funcionamento_get()
        if turno_ativo is None:
            #local
            turno_ativo = self.turno_dao.obtem_turno(self.turno_dao.obtem_catraca(), self.util.obtem_hora())
        if turno_ativo:
            return turno_ativo
        else:
            return None

        