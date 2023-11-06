#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Procura a cidade pelo nome neste site: http://openweathermap.org/help/city_list.txt
# Ex.: 3390732    Redencao    -4.225830    -38.730560    BR
# http://api.openweathermap.org/data/2.5/forecast/city?id={CIDADE_ID}&APPID={APIKEY}


import json
import urllib
import datetime
import threading
import calendar
from catraca.util import Util
from catraca.logs import Logs

__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"

class PrevisaoTempo(threading.Thread):
    
    WEATHER_DATA_URL = 'http://api.openweathermap.org/data/2.5/weather?id=3390732,4225830,38730560&lang=pt&APPID=bfb3aa83ead78a09aea4d487ba1b48b9'
    log = Logs()
    
    def __init__(self, intervalo=10):
        threading.Thread.__init__(self)
        self.intervalo = intervalo
        self._stopevent = threading.Event()
        self._sleepperiod = intervalo

        self.__temperatura = None
        self.__pressao = None
        self.__humidade = None
        self.__vento = None
        self.__nebulosidade = None
        
        self.__horainicio = None
        self.__horafinal = None

        self.name = 'Thread Previsao Tempo'
        
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        self.__temperatura = valor
        
    @property
    def pressao(self):
        return self.__pressao
    
    @pressao.setter
    def pressao(self, valor):
        self.__pressao = valor
        
    @property
    def humidade(self):
        return self.__humidade
    
    @humidade.setter
    def humidade(self, valor):
        self.__humidade = valor
        
    @property
    def vento(self):
        return self.__vento
    
    @vento.setter
    def vento(self, valor):
        self.__vento = valor
        
    @property
    def nebulosidade(self):
        return self.__nebulosidade
    
    @nebulosidade.setter
    def nebulosidade(self, valor):
        self.__nebulosidade = valor
        
    @property
    def horainicio(self):
        return self.__horainicio
    
    @horainicio.setter
    def horainicio(self, valor):
        self.__horainicio = valor
        
    @property
    def horafinal(self):
        return self.__horafinal
    
    @horafinal.setter
    def horafinal(self, valor):
        self.horafinal = valor
        
    def run(self):
        print "%s Rodando... " % self.name
        while not self._stopevent.isSet():
            
#             agora = calendar.timegm(Util().obtem_datahora.timetuple())
#             if PrevisaoTempo.horainicio < agora < PrevisaoTempo.horafinal:
            self.obtem_dados()
            
            self._stopevent.wait(self._sleepperiod)
        print "%s Finalizando..." % (self.getName(),)
        
    def obtem_meteorologia(self):
        """obter dados de tempo da openweathermap.org"""
        response = urllib.urlopen(self.WEATHER_DATA_URL)
        try:
            data = json.loads(response.read())
            if data:
                temp = data['main']['temp']
                pressure = data['main']['pressure']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                weather_description = data['weather'][0]['description']
                sunrise = data['sys']['sunrise']
                sunset = data['sys']['sunset']
                
                dados = [temp, pressure, humidity, wind_speed, weather_description, sunrise, sunset]
                if dados:
                    dados = [
                             '%.1f' % (dados[0] - 273), 
                             dados[1], dados[2], '%.1f' % (dados[3] * 1.852), 
                             dados[4], 
#                              datetime.datetime.fromtimestamp(dados[5]).time(), 
#                              datetime.datetime.fromtimestamp(dados[6]).time()
                             dados[5], 
                             dados[6]
                            ]
                    return dados
                else:
                    return []
            else:
                return []
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            return []
        
    def obtem_dados(self):
        try:
            informacoes = self.obtem_meteorologia()
            if informacoes:
                PrevisaoTempo.temperatura = str(informacoes[0]) +" C"
                PrevisaoTempo.pressao = str(informacoes[1]) + " hPa"
                PrevisaoTempo.humidade = str(informacoes[2]) +" %"
                PrevisaoTempo.vento = str(informacoes[3]) +" Km/h"
                PrevisaoTempo.nebulosidade = informacoes[4][0:16]
                PrevisaoTempo.horainicio = informacoes[5]
                PrevisaoTempo.horafinal = informacoes[6]
#             print "Temperatura", self.temperatura
#             print "Pressão Atmosférica", self.pressao
#             print "Humidade do ar", self.humidade
#             print "Rajada de Vento", self.vento
#             print "Nebulosidade", self.nebulosidade
                
        except Exception:
            self.log.logger.error("Exception", exc_info=True)
            