/*
CREATE DATABASE raspberry
  WITH ENCODING='UTF8'
       CONNECTION LIMIT=-1;
*/

-- DROP TABLE cartao;

CREATE TABLE cartao
(
  cart_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  cart_numero bigint, -- Numero do ID do cartao de acesso sem permissao de duplicidade.
  cart_creditos integer, -- Quantidade de creditos para uso diario do cartao.
  perf_id integer NOT NULL, -- Campo para chave estrengeira da tabela perfil
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id ),
  CONSTRAINT fk_perf_id FOREIGN KEY (perf_id)
      REFERENCES perfil (perf_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT u_cart_numero UNIQUE (cart_numero )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE cartao
  OWNER TO postgres;
COMMENT ON TABLE cartao
  IS 'Tabela dos registros de uso do Smart Card RFID.';
COMMENT ON COLUMN cartao.cart_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN cartao.cart_numero IS 'Numero do ID do cartao de acesso sem permissao de duplicidade.';
COMMENT ON COLUMN cartao.cart_creditos IS 'Quantidade de creditos para uso diario do cartao.';
COMMENT ON COLUMN cartao.perf_id IS 'Campo para chave estrengeira da tabela perfil';

-- DROP TABLE catraca;

CREATE TABLE catraca
(
  catr_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  catr_localizacao character varying(16), -- Nome do local de instalacao da catraca.
  catr_tempo_giro integer, -- Tempo para o giro do braço da catraca em milissegundos.
  giro_id integer NOT NULL, -- Campo para chave estrengeira da tabela giro.
  turn_id integer NOT NULL, -- Campo para chave estrengeira da tabela turno.
  catr_ip character varying(12), -- Numero IP da catraca.
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id ),
  CONSTRAINT fk_turn_id FOREIGN KEY (turn_id)
      REFERENCES turno (turn_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE catraca
  OWNER TO postgres;
COMMENT ON TABLE catraca
  IS 'Tabela de predefinicoes e configuracoes para o funcionamento da catraca.';
COMMENT ON COLUMN catraca.catr_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN catraca.catr_localizacao IS 'Nome do local de instalacao da catraca.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro do braço da catraca em milissegundos.';
COMMENT ON COLUMN catraca.giro_id IS 'Campo para chave estrengeira da tabela giro.';
COMMENT ON COLUMN catraca.turn_id IS 'Campo para chave estrengeira da tabela turno.';
COMMENT ON COLUMN catraca.catr_ip IS 'Numero IP da catraca.';

-- DROP TABLE perfil;

CREATE TABLE perfil
(
  perf_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  perf_nome character varying(200), -- Nome completo do utilizador do cartao.
  perf_email character varying(150), -- E-mail do utilizador do cartao sem permissao de duplicidade.
  perf_tel character varying(15), -- Numero do telefone celular do utilizador.
  perf_datanascimento character varying(10), -- Mes e ano da data de nascimento.
  tipo_id integer NOT NULL, -- Campo para chave estrengeira da tabela tipo.
  CONSTRAINT pk_perf_id PRIMARY KEY (perf_id ),
  CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id)
      REFERENCES tipo (tipo_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT u_perf_email UNIQUE (perf_email )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE perfil
  OWNER TO postgres;
COMMENT ON COLUMN perfil.perf_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN perfil.perf_nome IS 'Nome completo do utilizador do cartao.';
COMMENT ON COLUMN perfil.perf_email IS 'E-mail do utilizador do cartao sem permissao de duplicidade.';
COMMENT ON COLUMN perfil.perf_tel IS 'Numero do telefone celular do utilizador.';
COMMENT ON COLUMN perfil.perf_datanascimento IS 'Mes e ano da data de nascimento.';
COMMENT ON COLUMN perfil.tipo_id IS 'Campo para chave estrengeira da tabela tipo.';

-- DROP TABLE registro;

CREATE TABLE registro
(
  regi_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  regi_datahora timestamp without time zone, -- Data/hora da utilizacao do cartao na catraca.
  regi_giro integer NOT NULL DEFAULT 0, -- Confirmacao de efetivacao de giro na catraca.
  cart_id integer NOT NULL, -- Campo para chave estrengeira da tabela cartao.
  CONSTRAINT pk_regi_id PRIMARY KEY (regi_id ),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id)
      REFERENCES cartao (cart_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE registro
  OWNER TO postgres;
COMMENT ON TABLE registro
  IS 'Tabela de registros de uso do cartao na catraca.';
COMMENT ON COLUMN registro.regi_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN registro.regi_datahora IS 'Data/hora da utilizacao do cartao na catraca.';
COMMENT ON COLUMN registro.regi_giro IS 'Confirmacao de efetivacao de giro na catraca.';
COMMENT ON COLUMN registro.cart_id IS 'Campo para chave estrengeira da tabela cartao.';

-- DROP TABLE tipo;

CREATE TABLE tipo
(
  tipo_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  tipo_nome character varying(16), -- Tipos comuns de utilizadores: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.
  tipo_vlr_credito numeric(8,2), -- Valor unitario de credito do cartao.
  CONSTRAINT pk_tipo_id PRIMARY KEY (tipo_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipo
  OWNER TO postgres;
COMMENT ON TABLE tipo
  IS 'Tabela de tipo de portador do cartao.';
COMMENT ON COLUMN tipo.tipo_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN tipo.tipo_nome IS 'Tipos comuns de utilizadores: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.';
COMMENT ON COLUMN tipo.tipo_vlr_credito IS 'Valor unitario de credito do cartao.';

-- DROP TABLE turno;

CREATE TABLE turno
(
  turn_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  turn_hora_inicio time without time zone, -- Hora inicio do periodo para liberacao da catraca.
  turn_hora_fim time without time zone, -- Hora final do periodo para liberacao da catraca.
  turn_data timestamp without time zone, -- Data para o periodo da liberacao da catraca.
  turn_continuo integer DEFAULT 0, -- Define a forma de liberacao dos turnos: 0=Continuo, 1=por data exclusiva.
  CONSTRAINT pk_turn_id PRIMARY KEY (turn_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE turno
  OWNER TO postgres;
COMMENT ON COLUMN turno.turn_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN turno.turn_hora_inicio IS 'Hora inicio do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_hora_fim IS 'Hora final do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_data IS 'Data para o periodo da liberacao da catraca.';
COMMENT ON COLUMN turno.turn_continuo IS 'Define a forma de liberacao dos turnos: 0=Continuo, 1=por data exclusiva.';

-- DROP TABLE usuario;

CREATE TABLE usuario
(
  usua_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  usua_nome character varying(200), -- Nome completo do utilizador do cartao.
  usua_email character varying(150), -- E-mail do utilizador do cartao sem permissao de duplicidade.
  usua_login character varying(50), -- Nome de usuario do utilizador do cartao.
  usua_senha character varying(50), -- Senha de usuario do utilizador do cartao.
  usua_nivel integer, -- Nivel de acesso ao sistema do utilizador do cartao.
  CONSTRAINT pk_usua_id PRIMARY KEY (usua_id ),
  CONSTRAINT u_usua_email UNIQUE (usua_email )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE usuario
  OWNER TO postgres;
COMMENT ON TABLE usuario
  IS 'Tabela de usuario do cartao para acesso na catraca.';
COMMENT ON COLUMN usuario.usua_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN usuario.usua_nome IS 'Nome completo do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_email IS 'E-mail do utilizador do cartao sem permissao de duplicidade.';
COMMENT ON COLUMN usuario.usua_login IS 'Nome de usuario do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_senha IS 'Senha de usuario do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_nivel IS 'Nivel de acesso ao sistema do utilizador do cartao.';
