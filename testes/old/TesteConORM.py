#!/usr/bin/python
# -*- coding: latin-1 -*-

from sqlalchemy import *
from sqlalchemy.dialects.postgresql import *

# URL => driver://username:password@host:port/database
# No SQLite:
#   sqlite:// (memória)
#   sqlite:///arquivo (arquivo em disco)


# default
#engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')

# psycopg2
#engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

# pg8000
#engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')

db = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/db_postgres', client_encoding='latin1')
connection = db.connect()
connection = connection.execution_options(isolation_level="READ COMMITTED")

# Torna acessível os metadados
metadata = MetaData(db)

# Ecoa o que SQLAlchemy está fazendo
metadata.bind.echo = False

# Tabela Cartoes
prog_table = Table('Cartoes', metadata, 
Column('cartaoId', Integer, Sequence('inc_cartao'), primary_key=True),
Column('usuarioId', String(20)), 
Column('bloqueado', String(1)), 
Column('jornadaId', String(2)), 
Column('controleFeriados', String(1)), 
Column('mensagemId', Integer), 
Column('nomePortador', String(300)), 
Column('senha', String(20)), 
Column('departamentoId', Integer), 
Column('dataInicial', Integer), 
Column('validade', Integer), 
Column('foto', BYTEA), 
Column('ultimoAcesso', String(6)), 
Column('ultimaHora', Integer), 
Column('creditos', String(5)), 
Column('acessosDia', String(5)), 
Column('numAcessos', Integer), 
Column('visitante', String(1)), 
Column('visitaId', Integer), 
Column('controleReentrada', String(1)), 
Column('mestre', String(1)), 
Column('empresaId', Integer), 
Column('informacoes', String(250)), 
Column('tipoCartao', Integer), 
Column('acompanhanteCartaoId', Integer), 
Column('creditosRefeicao', String(5)), 
Column('finger1', BYTEA), 
Column('finger2', BYTEA), 
Column('categoria', Integer), 
Column('identificacao_ufc', String(255)), 
Column('ultimaHoraCorreta', Integer))


# Cria a tabela
#prog_table.create()

# Carrega a definição da tabela
prog_table = Table('Cartoes', metadata, autoload=True)

# Insere dados
#i = prog_table.insert()
#i.execute({'name': 'Yes'}, {'name': 'Genesis'},
#    {'name': 'Pink Floyd'}, {'name': 'King Crimson'})

# Seleciona
s = prog_table.select()
r = s.execute()

for row in r.fetchall():
    print row; '\n'
