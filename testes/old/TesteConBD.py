#!/usr/bin/python
# -*- coding: latin-1 -*-

import psycopg2
from sqlalchemy import *

con = psycopg2.connect(
    host='10.5.5.174',  
    database='db_postgres', 
    user='postgres', 
    password='postgres', 
    port='5432',
    client_encoding='latin1')
cur = con.cursor()

#sql = 'insert into tracks values (default, %s, %s)' 
#recset = [('Siberian Khatru', 'Yes'), ("Supper's Ready", 'Genesis')]

#for rec in recset:
#   cur.execute(sql, rec)
#con.commit()

cur.execute('select * from "public"."Cartoes"')
recset = cur.fetchall()

for rec in recset:
    print (rec); '\n'

con.close()
