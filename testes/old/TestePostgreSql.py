#!/usr/bin/python
#testando a conexao postgres 
 
import psycopg2
import pprint
 
print "Content-type: text\html"
print
conn = psycopg2.connect("\
	dbname='postgres'\
	user='postgres'\
	host='localhost'\
	password='postgres'\
");
c = conn.cursor()
c.execute("SELECT * FROM teste")
records = c.fetchall()
pprint.pprint(records)
