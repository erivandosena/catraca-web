-- Database: catraca

-- DROP DATABASE catraca;

CREATE DATABASE catraca
  WITH OWNER = postgres
       ENCODING = 'LATIN1'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR'
       LC_CTYPE = 'pt_BR'
       CONNECTION LIMIT = -1;

-- Table: cartao

-- DROP TABLE cartao;

CREATE TABLE cartao
(
  cart_id integer NOT NULL DEFAULT nextval('cartoes_cart_id_seq'::regclass),
  cart_numero bigint, -- Numero do ID do cartao de acesso.
  cart_qtd_creditos integer,
  cart_vlr_credito numeric(8,2), -- Valor unitario em R$.
  cart_tipo integer, -- 1=Estudante, 2=Docente, 3=Tecnico, 4=Terceirizado, 5=Visitante, 6=Administrador.
  cart_dt_acesso timestamp without time zone, -- Data/hora do ultimo acesso.
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE cartao
  OWNER TO postgres;
COMMENT ON COLUMN cartao.cart_numero IS 'Numero do ID do cartao de acesso.';
COMMENT ON COLUMN cartao.cart_vlr_credito IS 'Valor unitario em R$.';
COMMENT ON COLUMN cartao.cart_tipo IS '1=Estudante, 2=Docente, 3=Tecnico, 4=Terceirizado, 5=Visitante, 6=Administrador.';
COMMENT ON COLUMN cartao.cart_dt_acesso IS 'Data/hora do ultimo acesso.';

-- Table: raspberry

-- DROP TABLE raspberry;

CREATE TABLE raspberry
(
  rasp_id serial NOT NULL,
  rasp_ip character varying(17), -- Numero IP da catraca.
  rasp_local character varying(17), -- Nome da localizacao da catraca.
  rasp_tempo_giro integer, -- Tempo para o giro em milissegundos.
  rasp_mensagem character varying(36), -- Mensagem para exibicao no display LCD.
  rasp_sentido_giro integer, -- Sentido do giro: 1 = Horario, 2 = Antihorario.
  CONSTRAINT pk_rasp_id PRIMARY KEY (rasp_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE raspberry
  OWNER TO postgres;
COMMENT ON COLUMN raspberry.rasp_ip IS 'Numero IP da catraca.';
COMMENT ON COLUMN raspberry.rasp_local IS 'Nome da localizacao da catraca.';
COMMENT ON COLUMN raspberry.rasp_tempo_giro IS 'Tempo para o giro em milissegundos.';
COMMENT ON COLUMN raspberry.rasp_mensagem IS 'Mensagem para exibicao no display LCD.';
COMMENT ON COLUMN raspberry.rasp_sentido_giro IS 'Sentido do giro: 1 = Horario, 2 = Antihorario.';


