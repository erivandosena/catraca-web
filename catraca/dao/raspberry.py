#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Raspberry(object):

    def __init__(self):
        super(Raspberry, self).__init__()
        self.__rasp_id = None
        self.__rasp_ip = None
        self.__rasp_local = None
        self.__rasp_tempo_giro = None
        self.__rasp_mensagem = None
        self.__rasp_sentido_giro = None

    #  Gette's e Setter's
    def getId(self):
        return self.__rasp_id

    def setId(self, valor):
        self.__rasp_id = valor

    def getIp(self):
        return self.__rasp_ip

    def setIp(self, valor):
        self.__rasp_ip = valor

    def getLocal(self):
        return self.__rasp_local

    def setLocal(self, valor):
        self.__rasp_local = valor

    def getTempo(self):
        return self.__rasp_tempo_giro

    def setTempo(self, valor):
        self.__rasp_tempo_giro = valor

    def getMensagem(self):
        return self.__rasp_mensagem

    def setMensagem(self, valor):
        self.__rasp_mensagem = valor

    def getSentido(self):
        return self.__rasp_sentido_giro

    def setSentido(self, valor):
        self.__rasp_sentido_giro = valor
