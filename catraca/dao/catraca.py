#!/usr/bin/env python
# -*- coding: latin-1 -*-


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Catraca(object):

    def __init__(self):
        super(Catraca, self).__init__()
        self.__catr_id = None
        self.__catr_ip = None
        self.__catr_local = None
        self.__catr_tempo_giro = None
        self.__catr_mensagem = None
        self.__catr_sentido_giro = None

    def getId(self):
        return self.__catr_id

    def setId(self, valor):
        self.__catr_id = valor

    def getIp(self):
        return self.__catr_ip

    def setIp(self, valor):
        self.__catr_ip = valor

    def getLocal(self):
        return self.__catr_local

    def setLocal(self, valor):
        self.__catr_local = valor

    def getTempo(self):
        return self.__catr_tempo_giro

    def setTempo(self, valor):
        self.__catr_tempo_giro = valor

    def getMensagem(self):
        return self.__catr_mensagem

    def setMensagem(self, valor):
        self.__catr_mensagem = valor

    def getSentido(self):
        return self.__catr_sentido_giro

    def setSentido(self, valor):
        self.__catr_sentido_giro = valor
