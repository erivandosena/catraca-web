#!/usr/bin/env python
# -*- coding: latin-1 -*-


import psycopg2


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Conexao(object):

    global cur

    def __init__(self):
        try:
            con = psycopg2.connect("\
                    dbname='catraca'\
                    user='postgres'\
                    host='localhost'\
                    password='postgres'\
            ")
            self.cur = con.cursor
        except Exception, e:
            print "Erro ao conectar o BD."
            print e

    def __del__(self):
        print "Conexão finalizada."
        del self
