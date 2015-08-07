/*
CREATE DATABASE raspberry
  WITH ENCODING='UTF8'
       CONNECTION LIMIT=-1;
*/

-- Table: tipos
CREATE TABLE tipos
(
  tipo_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  tipo_nome character varying(16), -- Tipos de utilizadores permitidos: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.
  CONSTRAINT pk_tipo_id PRIMARY KEY (tipo_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipos
  OWNER TO postgres;
COMMENT ON TABLE tipos
  IS 'Tabela dos tipos de utilizadores da catraca.';
COMMENT ON COLUMN tipos.tipo_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN tipos.tipo_nome IS 'Tipos de utilizadores permitidos: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.';

-- Table: cartao
CREATE TABLE cartao
(
  cart_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  cart_numero bigint, -- Numero do ID do cartao de acesso sem permissao de duplicidade.
  cart_qtd_creditos integer, -- Quantidade de creditos para uso diario do cartao.
  cart_vlr_credito numeric(8,2), -- Valor em R$ para uso diario do cartao.
  cart_tipo integer, -- 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.
  cart_dt_acesso timestamp without time zone, -- Data/hora do ultimo acesso.
  usua_id integer NOT NULL,
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id ),
  CONSTRAINT fk_usua_id FOREIGN KEY (usua_id)
      REFERENCES usuario (usua_id) MATCH SIMPLE
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
COMMENT ON COLUMN cartao.cart_qtd_creditos IS 'Quantidade de creditos para uso diario do cartao.';
COMMENT ON COLUMN cartao.cart_vlr_credito IS 'Valor em R$ para uso diario do cartao.';
COMMENT ON COLUMN cartao.cart_tipo IS '1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.';
COMMENT ON COLUMN cartao.cart_dt_acesso IS 'Data/hora do ultimo acesso.';

-- Table: usuario
CREATE TABLE usuario
(
  usua_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  usua_nome character varying(200), -- Nome completo do utilizador do cartao.
  usua_email character varying(150), -- E-mail do utilizador do cartao sem permissao de duplicidade.
  usua_login character varying(50), -- Nome de usuario do utilizador do cartao.
  usua_senha character varying(50), -- Senha de usuario do utilizador do cartao.
  usua_nivel integer, -- Nivel de acesso ao sistema do utilizador do cartao.
  id_externo bigint NOT NULL, -- Campo controle de ID unico proveniente de outros sistemas.
  usua_num_doc character varying(25), -- Numero de CPF ou CIE do utilizador do cartao sem permissao de duplicidade.
  cart_id integer NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  tipo_id integer NOT NULL,
  CONSTRAINT pk_usua_id PRIMARY KEY (usua_id ),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id)
      REFERENCES cartao (cart_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id)
      REFERENCES tipos (tipo_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT u_id_externo UNIQUE (id_externo ),
  CONSTRAINT u_usua_email UNIQUE (usua_email ),
  CONSTRAINT u_usua_num_doc UNIQUE (usua_num_doc )
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
COMMENT ON COLUMN usuario.id_externo IS 'Campo controle de ID unico proveniente de outros sistemas.';
COMMENT ON COLUMN usuario.usua_num_doc IS 'Numero de CPF ou CIE do utilizador do cartao sem permissao de duplicidade.';
COMMENT ON COLUMN usuario.cart_id IS 'Campo autoincremento destinado para chave primaria da tabela.';

-- Table: mensagem
CREATE TABLE mensagem
(
  mens_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  mens_texto_display character varying(16), -- Mensagem de texto para exibicao em display LCD de 16 caracteres.
  CONSTRAINT pk_mens_id PRIMARY KEY (mens_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE mensagem
  OWNER TO postgres;
COMMENT ON TABLE mensagem
  IS 'Tabela de mensagens para exibicao no display LCD.';
COMMENT ON COLUMN mensagem.mens_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN mensagem.mens_texto_display IS 'Mensagem de texto para exibicao em display LCD de 16 caracteres.';

-- Table: giros
CREATE TABLE giros
(
  giro_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  giro_giros_horario integer DEFAULT 0, -- Contador de giros no sentido horario(Entrada).
  giro_giros_antihorario integer DEFAULT 0, -- Contador de giros no sentido anti-horario(Saida).
  giro_data_giro time without time zone NOT NULL DEFAULT now(), -- Data/hora da ocorrencia do giro.
  CONSTRAINT pk_giro_id PRIMARY KEY (giro_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE giros
  OWNER TO postgres;
COMMENT ON TABLE giros
  IS 'Tabela de contabilizacao de giros horario e anti-horario.';
COMMENT ON COLUMN giros.giro_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN giros.giro_giros_horario IS 'Contador de giros no sentido horario(Entrada).';
COMMENT ON COLUMN giros.giro_giros_antihorario IS 'Contador de giros no sentido anti-horario(Saida).';
COMMENT ON COLUMN giros.giro_data_giro IS 'Data/hora da ocorrencia do giro.';

-- Table: catraca
CREATE TABLE catraca
(
  catr_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  catr_local character varying(16), -- Nome do local onde a catraca esta instalada.
  catr_tempo_giro integer, -- Tempo para o giro do braço da catraca em milissegundos.
  catr_sentido_trava_giro integer, -- 1 = Giro Horario(Entrada controlada com saida bloqueada),  2 = Giros Horario/Anti-horario(Entrada controlada com saida liberada), 3 = Giros Horario/Anti-horario(Entrada e saida liberadas).
  catr_hora_inicio_almoco time without time zone, -- Hora inicio do 1º periodo para liberacao da catraca.
  catr_hora_fim_almoco time without time zone, -- Hora final do 1º periodo para liberacao da catraca.
  catr_hora_inicio_janta time without time zone, -- Hora inicio do 2º periodo para liberacao da catraca.
  catr_hora_fim_janta time without time zone, -- Hora final do 2º periodo para liberacao da catraca.
  mens_id integer NOT NULL,
  giro_id integer NOT NULL,
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id ),
  CONSTRAINT fk_giro_id FOREIGN KEY (giro_id)
      REFERENCES giros (giro_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_mens_id FOREIGN KEY (mens_id)
      REFERENCES mensagem (mens_id) MATCH SIMPLE
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
COMMENT ON COLUMN catraca.catr_local IS 'Nome do local onde a catraca esta instalada.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro do braço da catraca em milissegundos.';
COMMENT ON COLUMN catraca.catr_sentido_trava_giro IS '1 = Giro Horario(Entrada controlada com saida bloqueada),  2 = Giros Horario/Anti-horario(Entrada controlada com saida liberada), 3 = Giros Horario/Anti-horario(Entrada e saida liberadas).';
COMMENT ON COLUMN catraca.catr_hora_inicio_almoco IS 'Hora inicio do 1º periodo para liberacao da catraca.';
COMMENT ON COLUMN catraca.catr_hora_fim_almoco IS 'Hora final do 1º periodo para liberacao da catraca.';
COMMENT ON COLUMN catraca.catr_hora_inicio_janta IS 'Hora inicio do 2º periodo para liberacao da catraca.';
COMMENT ON COLUMN catraca.catr_hora_fim_janta IS 'Hora final do 2º periodo para liberacao da catraca.';
