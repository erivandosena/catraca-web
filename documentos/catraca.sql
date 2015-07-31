/*
CREATE DATABASE raspberry
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_GB.UTF-8'
       LC_CTYPE = 'en_GB.UTF-8'
       CONNECTION LIMIT = -1;
*/

CREATE DATABASE raspberry
  WITH ENCODING='UTF8'
       CONNECTION LIMIT=-1;

CREATE TABLE cartao
(
  cart_id serial NOT NULL,
  cart_numero bigint, -- Numero do ID do cartao de acesso.
  cart_qtd_creditos integer,
  cart_vlr_credito numeric(8,2), -- Valor unitario em R$.
  cart_tipo integer, -- 1=Estudante, 2=Tecnico, 3=Professor, 4=Visitante, 5=Isento, 6=Operador, 7=Administrador.
  cart_dt_acesso timestamp without time zone, -- Data/hora do ultimo acesso.
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id )
);

ALTER TABLE cartao OWNER TO postgres;
COMMENT ON COLUMN cartao.cart_numero IS 'Numero do ID do cartao de acesso.';
COMMENT ON COLUMN cartao.cart_vlr_credito IS 'Valor unitario em R$.';
COMMENT ON COLUMN cartao.cart_tipo IS '1=Estudante, 2=Tecnico, 3=Professor, 4=Visitante, 5=Isento, 6=Operador, 7=Administrador.';
COMMENT ON COLUMN cartao.cart_dt_acesso IS 'Data/hora do ultimo acesso.';

CREATE TABLE catraca
(
  catr_id serial NOT NULL,
  catr_ip character varying(17), -- Numero IP da catraca.
  catr_local character varying(17), -- Nome da localizacao da catraca.
  catr_tempo_giro integer, -- Tempo para o giro em milissegundos.
  catr_mensagem character varying(40), -- Mensagem para exibicao no display LCD.
  catr_sentido_giro integer, -- Sentido do giro: 1 = Horario, 2 = Antihorario.
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id )
);

ALTER TABLE catraca OWNER TO postgres;
COMMENT ON COLUMN catraca.catr_ip IS 'Numero IP da catraca.';
COMMENT ON COLUMN catraca.catr_local IS 'Nome da localizacao da catraca.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro em milissegundos.';
COMMENT ON COLUMN catraca.catr_mensagem IS 'Mensagem para exibicao no display LCD.';
COMMENT ON COLUMN catraca.catr_sentido_giro IS 'Sentido do giro: 1 = Horario, 2 = Antihorario.';

