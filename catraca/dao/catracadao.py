#!/usr/bin/env python
# -*- coding: latin-1 -*-

from catraca import Catraca
from conexao import ConexaoFactory


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(object):

    def __init__(self):
        super(CatracaDAO, self).__init__()
        self.__erro = None
        self.__con = None
        self.__factory = None

        try:
            conexao = ConexaoFactory()
            self.__con = conexao.getConexao(1) # 1 para PostgreSQL
            self.__factory = conexao.getFactory()
        except Exception, e:
            self.__erro = str(e)

    def busca(self, id):
        obj = Raspberry()
        sql = "SELECT catr_id, "\
              "catr_ip, "\
              "catr_local, "\
              "catr_tempo_giro, "\
              "catr_mensagem, "\
              "catr_sentido_giro "\
              "FROM catraca WHERE "\
              "catr_id = " + str(id)
        try:
            cursor = self.__con.cursor()
            cursor.execute(sql)
            dados = cursor.fetchone()

            obj.setId(dados[0])
            obj.setIp(dados[1])
            obj.setLocal(dados[2])
            obj.setTempo(dados[3])
            obj.setMensagem(dados[4])
            obj.setSentido(dados[5])
        except Exception, e:
            self.__erro = str(e)
        return obj

    # Insert
    def insere(self, obj):
        sql = "INSERT INTO catraca("\
              "catr_ip, "\
              "catr_local, "\
              "catr_tempo_giro, "\
              "catr_mensagem, "\
              "catr_sentido_giro) VALUES ('" +\
              str(obj.getIp()) + "', '" +\
              str(obj.getLocal()) + "', " +\
              str(obj.getTempo()) + ", '" +\
              str(obj.getMensagem()) + "', " +\
              str(obj.getSentido()) + ")"
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False

    # Update
    def altera(self, obj):
       sql = "UPDATE catraca SET " +\
             "catr_ip = '" +\
             str(obj.getIp()) + "', " +\
             "catr_local = '" +\
             str(obj.getLocal()) + "', " +\
             "catr_tempo_giro = " +\
             str(obj.getTempo()) + ", " +\
             "catr_mensagem = '" +\
             str(obj.getMensagem()) + "', " +\
             "catr_sentido_giro = " +\
             str(obj.getSentido()) +\
             " WHERE "\
             "catr_id = " + str(obj.getId())

       try:
           cursor=self.__con.cursor()
           cursor.execute(sql)
           self.__con.commit()
           return True
       except Exception, e:
           self.__erro = str(e)
           return False

    # Delete
    def exclui(self, obj):
        sql = "DELETE FROM catraca WHERE catr_id = " + str(obj.getId())
        print sql
        try:
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception, e:
            self.__erro = str(e)
            return False

    def getErro(self):
        return self.__erro
