#!/usr/bin/env python
# -*- coding: latin-1 -*-

from raspberry import Raspberry
from conexao import ConexaoFactory


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class RaspberryDAO(object):

    def __init__(self):
        super(RaspberryDAO, self).__init__()
        self.__erro = None
        self.__con = None
        self.__factory = None

        try:
            # Em .getConexao(?) use: 1 p/(PostgreSQL) 2 p/(MySQL) 3 p/(SQLite)
            conexao = ConexaoFactory()
            self.__con = conexao.getConexao(1)
            self.__factory = conexao.getFactory()
        except Exception, e:
            self.__erro = str(e)

    # Select por id ou IP
    def busca(self, id):
        obj = Raspberry()
        sql = "SELECT rasp_id, "\
              "rasp_ip, "\
              "rasp_local, "\
              "rasp_tempo_giro, "\
              "rasp_mensagem, "\
              "rasp_sentido_giro "\
              "FROM raspberry WHERE "\
              "rasp_id = " + str(id)
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
        sql = "INSERT INTO raspberry("\
              "rasp_ip, "\
              "rasp_local, "\
              "rasp_tempo_giro, "\
              "rasp_mensagem, "\
              "rasp_sentido_giro) VALUES ('" +\
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
       sql = "UPDATE raspberry SET " +\
             "rasp_ip = '" +\
             str(obj.getIp()) + "', " +\
             "rasp_local = '" +\
             str(obj.getLocal()) + "', " +\
             "rasp_tempo_giro = " +\
             str(obj.getTempo()) + ", " +\
             "rasp_mensagem = '" +\
             str(obj.getMensagem()) + "', " +\
             "rasp_sentido_giro = " +\
             str(obj.getSentido()) +\
             " WHERE "\
             "rasp_id = " + str(obj.getId())

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
        sql = "DELETE FROM raspberry WHERE rasp_id = " + str(obj.getId())
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
