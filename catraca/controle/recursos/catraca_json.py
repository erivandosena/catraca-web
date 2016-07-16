#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import requests
import traceback
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
    util = Util()
    
    def __init__(self):
        super(CatracaJson, self).__init__()
        ServidorRestful.__init__(self)
        
    def __cmp__(self, valor):
        return cmp(self.name, valor.name)
        
    def catraca_get(self, limpa_tabela=False):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "catraca/jcatraca"
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["catracas"]
                    if LISTA_JSON != []:
                        catraca_local = None
                        if limpa_tabela:
                            self.mantem_tabela_local(None, 0)
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                catraca = self.catraca_dao.busca(obj.id)
                                if catraca is None:
                                    print 'catraca remoto ausente no local'
                                    self.mantem_tabela_local(obj, 1)
                                    return self.catraca_get()
                                if obj.interface == 'eth0' or obj.interface == 'wlan0':
                                    if (self.util.obtem_nome_rpi().upper() == obj.nome.upper()):
                                        print "catraca fisica local"
                                        
                                        catraca_local = catraca
                                        ip_local = self.util.obtem_ip_por_interface(obj.interface.lower())
                                        mac_local = self.util.obtem_MAC_por_interface(obj.interface.lower())
                                         
                                        if obj.ip != ip_local:
                                             catraca_local.ip = ip_local
                                               
                                        if obj.interface.lower() == "eth0":
                                            if mac_local != obj.maclan:
                                                catraca_local.maclan = mac_local
                                                  
                                        if obj.interface.lower() == "wlan0":
                                            if mac_local != obj.macwlan:
                                                catraca_local.macwlan = mac_local
                                                
                                        if not catraca_local.__eq__(obj):
                                            self.mantem_tabela_local(obj, 2)

                                        if obj.nome.lower() != self.util.obtem_nome_rpi().lower():
                                            print "REINICIAR SISTEMA...."
                                            self.util.altera_hostname( self.util.obtem_string_normalizada( obj.nome.lower() ) )
                                            self.util.reinicia_raspberrypi()
                                            return self.aviso.exibir_reinicia_catraca()
                                    else:
                                        print "catraca fisica remota"
                                        if not catraca.__eq__(obj):
                                            self.mantem_tabela_local(obj, 2)
                                            print "catraca fisica remota atualizada localmente"
                                else:
                                    print "catraca virtual remota"
                                    if not catraca.__eq__(obj):
                                        self.mantem_tabela_local(obj, 2)
                                        print "catraca virtual remota atualizada localmente"
                        if catraca_local is None:
                            print "catraca local ausente no remoto"
                            self.cadastra_catraca_remoto()
                            return self.catraca_get()
                        else:  
                            return catraca_local
        except Exception:
            print traceback.format_exc()
            return None
        finally:
            pass
        
    def obtem_catraca_rest(self):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "catraca/jcatraca"
                r = servidor.get(url)
                if r.text != '':
                    dados  = json.loads(r.text)
                    LISTA_JSON = dados["catracas"]
                    if LISTA_JSON != []:
                        catraca_local = None
                        obj = None
                        for item in LISTA_JSON:
                            obj = self.dict_obj(item)
                            if obj:
                                if obj.nome.upper() == self.util.obtem_nome_rpi().upper():
                                    return obj
        except Exception as excecao:
            print excecao
            return None
        
    def mantem_tabela_local(self, obj, acao):
        # 0=exclui    1=insere    2=atualiza
        if acao == 0:
            return self.atualiza_exclui(obj, True)
        if acao == 1:
            return self.insere(obj)
        if acao == 2:
            return self.atualiza_exclui(obj, False)
        
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
            if item == "catr_mac_lan":
                catraca.maclan = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "catr_mac_wlan":
                catraca.macwlan = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
            if item == "catr_interface_rede":
                catraca.interface = self.dict_obj(formato_json[item]) if self.dict_obj(formato_json[item]) is None else self.dict_obj(formato_json[item]).encode('utf-8')
                
        return catraca
    
    def lista_json(self, lista):
        if lista:
            for item in lista:
                catraca = {
                    "catr_ip":str(item[1]),
                    "catr_tempo_giro":item[2],
                    "catr_operacao":item[3],
                    "catr_nome":str(item[4]),
                    "catr_mac_lan":str(item[5]),
                    "catr_mac_wlan":str(item[6]),
                    "catr_interface_rede":str(item[7])
                }
                self.catraca_post(catraca)

    def objeto_json(self, obj, operacao="POST"):
        if obj:
            catraca = {
                "catr_ip":str(obj.ip),
                "catr_tempo_giro":obj.tempo,
                "catr_operacao":obj.operacao,
                "catr_nome":str(obj.nome),
                "catr_mac_lan":str(obj.maclan),
                "catr_mac_wlan":str(obj.macwlan),
                "catr_interface_rede":str(obj.interface)
            }
            if operacao == "POST":
                self.catraca_post(catraca)
            if operacao == "PUT":
                self.catraca_put(catraca, obj.id)
            
    def catraca_post(self, formato_json):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "catraca/insere"
                r = servidor.post(url, data=json.dumps(formato_json))
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro enviando json catraca.', exc_info=True)
        finally:
            pass
        
    def catraca_put(self, formato_json, id):
        servidor = self.obter_servidor()
        try:
            if servidor:
                url = str(self.URL) + "catraca/atualiza/"+ str(id)
                r = servidor.put(url, data=json.dumps(formato_json))
                return True
            else:
                return False
        except Exception as excecao:
            print excecao
            self.log.logger.error('Erro enviando json catraca.', exc_info=True)
        finally:
            pass
    
    def cadastra_catraca_remoto(self):
        interface_padrao = "eth0"
        catraca = Catraca()
        catraca.ip = self.util.obtem_ip_por_interface(interface_padrao)
        catraca.tempo = 20
        catraca.operacao = 1
        catraca.nome = self.util.obtem_nome_rpi().upper()
        catraca.maclan = self.util.obtem_MAC_por_interface('eth0')
        catraca.macwlan = self.util.obtem_MAC_por_interface('wlan0')
        catraca.interface = interface_padrao
        self.objeto_json(catraca)
        
        