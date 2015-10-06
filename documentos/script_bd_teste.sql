-------------------------------
-- Autor_script: Erivando Sena
-- Data_revisao: 16/10/2015
-- Status: Teste
-------------------------------

-- Database: bd_teste
--CREATE DATABASE bd_teste WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8' CONNECTION LIMIT = -1;
--COMMENT ON DATABASE bd_teste IS 'Bando de dados de teste.';

-- Table: usuario
CREATE TABLE usuario
(
  usua_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  usua_nome character varying(150), -- Nome completo do usuario no SIG.
  usua_email character varying(150), -- Endereco de e-mail do usuario no SIG.
  usua_login character varying(25), -- Nome de usuario no SIG.
  usua_senha character varying(50), -- Senha cadastrada no SIG.
  usua_nivel integer, -- Status atual do usuario no SIG.
  id_base_externa integer, -- Campo da chave primaria (uid) no sistema SIG.
  CONSTRAINT pk_usua PRIMARY KEY (usua_id) -- Chave primaria da tabela usuario.
);
ALTER TABLE usuario OWNER TO postgres;
COMMENT ON TABLE usuario IS 'Tabela que armazena as informacoes externas de usuarios do sistema provenientes do SIG.';
COMMENT ON COLUMN usuario.usua_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN usuario.usua_nome IS 'Nome completo do usuario no SIG.';
COMMENT ON COLUMN usuario.usua_email IS 'Endereco de e-mail do usuario no SIG.';
COMMENT ON COLUMN usuario.usua_login IS 'Nome de usuario no SIG.';
COMMENT ON COLUMN usuario.usua_senha IS 'Senha cadastrada no SIG.';
COMMENT ON COLUMN usuario.usua_nivel IS 'Status atual do usuario no SIG.';
COMMENT ON COLUMN usuario.id_base_externa IS 'Campo da chave primaria (uid) no sistema SIG.';
COMMENT ON CONSTRAINT pk_usua ON usuario IS 'Chave primaria da tabela usuario.';

-- Table: transacao
CREATE TABLE transacao
(
  tran_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  tran_valor numeric(8,2), -- Valor total em R$ contabil do turno.
  tran_descricao character varying(150), -- Descricao referente a transacao contabilizada do turno.
  tran_data timestamp without time zone, -- Data e hora da execucao.
  usua_id integer NOT NULL, -- Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de transacao).
  CONSTRAINT pk_tran_id PRIMARY KEY (tran_id), -- Chave primaria da tabela transacao.
  CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario (usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela usuario.
);
ALTER TABLE transacao OWNER TO postgres;
COMMENT ON TABLE transacao IS 'Tabela que armazena a contabilidade do guiche durante o turno.';
COMMENT ON COLUMN transacao.tran_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN transacao.tran_valor IS 'Valor total em R$ contabil do turno.';
COMMENT ON COLUMN transacao.tran_descricao IS 'Descricao referente a transacao contabilizada do turno.';
COMMENT ON COLUMN transacao.tran_data IS 'Data e hora da execucao.';
COMMENT ON COLUMN transacao.usua_id IS 'Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de transacao).';
COMMENT ON CONSTRAINT pk_tran_id ON transacao IS 'Chave primaria da tabela transacao.';
COMMENT ON CONSTRAINT fk_usua_id ON transacao IS 'Chave estrangeira da tabela usuario.';

-- Table: tipo
CREATE TABLE tipo
(
  tipo_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  tipo_nome character varying(25), -- Nome do tipo de utilizador: Estudante, Professor, Visitante, Servidor, Terceirizado, Isento, Operador, Administrador, Suporte.
  tipo_valor numeric(8,2), -- Valor em R$ da refeição de acordo com o tipo de utilizador.
  CONSTRAINT pk_tipo_id PRIMARY KEY (tipo_id) -- Chave primaria da tabela tipo.
);
ALTER TABLE tipo OWNER TO postgres;
COMMENT ON TABLE tipo IS 'Tabela que armazena os tipos de usuarios da catraca, ex. estudante, professor, visitante ...';
COMMENT ON COLUMN tipo.tipo_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN tipo.tipo_nome IS 'Nome do tipo de utilizador: Estudante, Professor, Visitante, Servidor, Terceirizado, Isento, Operador, Administrador, Suporte.';
COMMENT ON COLUMN tipo.tipo_valor IS 'Valor em R$ da refeição de acordo com o tipo de utilizador.';
COMMENT ON CONSTRAINT pk_tipo_id ON tipo IS 'Chave primaria da tabela tipo.';

-- Table: cartao
CREATE TABLE cartao
(
  cart_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  cart_numero bigint, -- Numero ID do cartao Smart Card sem permissao de duplicidade.
  cart_creditos numeric(8,2), -- Total de creditos em R$ para uso do cartao.
  tipo_id integer NOT NULL, -- Campo para chave estrangeira da tabela tipo.
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id), -- Chave primaria da tabela cartao.
  CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo (tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabelatipo.
  CONSTRAINT uk_cart_numero UNIQUE (cart_numero) -- Restricao de duplicidades para o campo cart_numero.
);
ALTER TABLE cartao OWNER TO postgres;
COMMENT ON TABLE cartao IS 'Tabela que armazena os registros de uso do cartao RFID.';
COMMENT ON COLUMN cartao.cart_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN cartao.cart_numero IS 'Numero ID do cartao Smart Card sem permissao de duplicidade.';
COMMENT ON COLUMN cartao.cart_creditos IS 'Total de creditos em R$ para uso do cartao.';
COMMENT ON COLUMN cartao.tipo_id IS 'Campo para chave estrangeira da tabela tipo.';
COMMENT ON CONSTRAINT pk_cart_id ON cartao IS 'Chave primaria da tabela cartao.';
COMMENT ON CONSTRAINT fk_tipo_id ON cartao IS 'Chave estrangeira da tabelatipo.';
COMMENT ON CONSTRAINT uk_cart_numero ON cartao IS 'Restricao de duplicidades para o campo cart_numero.';

-- Table: vinculo
CREATE TABLE vinculo
(
  vinc_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  vinc_avulso boolean, -- Status que informa se o vinculo esta ativo.
  vinc_inicio timestamp without time zone, -- Data e hora de inicio da validade do vinculo.
  vinc_fim timestamp without time zone, -- Data e hora de fim da validade do vinculo.
  vinc_descricao character varying(150), -- Descricao sobre a finalidade do vinculo.
  vinc_refeicoes integer, -- Quantidade de uso do cartao por refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  usua_id integer NOT NULL, -- Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de vinculo).
  CONSTRAINT pk_vinc_id PRIMARY KEY (vinc_id),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabela cartao.
  CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario (usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela usuario.
);
ALTER TABLE vinculo OWNER TO postgres;
COMMENT ON TABLE vinculo IS 'Tabela que armazena as informacoes de vinculo entre o usuario e o tipo de cartao.';
COMMENT ON COLUMN vinculo.vinc_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN vinculo.vinc_avulso IS 'Status que informa se o vinculo esta ativo.';
COMMENT ON COLUMN vinculo.vinc_inicio IS 'Data e hora de inicio da validade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_fim IS 'Data e hora de fim da validade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_descricao IS 'Descricao sobre a finalidade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_refeicoes IS 'Quantidade de uso do cartao por refeicao.';
COMMENT ON COLUMN vinculo.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON COLUMN vinculo.usua_id IS 'Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de vinculo).';
COMMENT ON CONSTRAINT fk_cart_id ON vinculo IS 'Chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT fk_usua_id ON vinculo IS 'Chave estrangeira da tabela usuario.';

-- Table: isencao
CREATE TABLE isencao
(
  isen_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  isen_inicio timestamp without time zone, -- Data e hora do inico da validade para isencao de pagamento.
  isen_fim timestamp without time zone, -- Data e hora do fim da validade para isencao de pagamento.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  CONSTRAINT pk_isen_id PRIMARY KEY (isen_id), -- Chave primaria da tabela isencao.
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela cartao.
);
ALTER TABLE isencao OWNER TO postgres;
COMMENT ON TABLE isencao IS 'Tabela que armazena as validades para isencao das refeicoes.';
COMMENT ON COLUMN isencao.isen_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN isencao.isen_inicio IS 'Data e hora do inico da validade para isencao de pagamento.';
COMMENT ON COLUMN isencao.isen_fim IS 'Data e hora do fim da validade para isencao de pagamento.';
COMMENT ON COLUMN isencao.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT pk_isen_id ON isencao IS 'Chave primaria da tabela isencao.';
COMMENT ON CONSTRAINT fk_cart_id ON isencao IS 'Chave estrangeira da tabela cartao. ';

-- Table: unidade
CREATE TABLE unidade
(
  unid_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  unid_nome character varying(50), -- Nome do local de funcionamento da catraca.
  CONSTRAINT pk_unid_id PRIMARY KEY (unid_id) -- Chave primaria da tabela unidade.
);
ALTER TABLE unidade OWNER TO postgres;
COMMENT ON TABLE unidade IS 'Tabela que armazena o local fisico de funcionamento das catracas.';
COMMENT ON COLUMN unidade.unid_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN unidade.unid_nome IS 'Nome do local de funcionamento da catraca.';
COMMENT ON CONSTRAINT pk_unid_id ON unidade IS 'Chave primaria da tabela unidade.';

-- Table: catraca
CREATE TABLE catraca
(
  catr_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  catr_ip character varying(12), -- Numero IP da catraca.
  catr_tempo_giro integer, -- Tempo para o giro na catraca em segundos.
  catr_operacao integer, -- 1=Giro Horario(Entrada controlada com saida bloqueada),...
  unid_id integer, -- Campo para chave estrengeira da tabela unidade.
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id), -- Chave primaria da tabela catraca.
  CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela unidade.
);
ALTER TABLE catraca OWNER TO postgres;
COMMENT ON TABLE catraca IS 'Tabela que armazena as predefinicoes e configuracoes para o funcionamento da catraca.';
COMMENT ON COLUMN catraca.catr_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN catraca.catr_ip IS 'Numero IP da catraca.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro na catraca em segundos.';
COMMENT ON COLUMN catraca.catr_operacao IS '1=Giro Horario(Entrada controlada com saida bloqueada),2=Giros Horario/Anti-horario(Entrada controlada com saida liberada),3=Giros Horario/Anti-horario(Entrada e saida liberadas).';
COMMENT ON COLUMN catraca.unid_id IS 'Campo para chave estrengeira da tabela unidade.';
COMMENT ON CONSTRAINT pk_catr_id ON catraca IS 'Chave primaria da tabela catraca.';
COMMENT ON CONSTRAINT fk_unid_id ON catraca IS 'Chave estrangeira da tabela unidade.';

-- Table: giro
CREATE TABLE giro
(
  giro_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  giro_giros_horario integer DEFAULT 0, -- Contador de giros no sentido horario.
  giro_giros_antihorario integer DEFAULT 0, -- Contador de giros no sentido anti-horario.
  giro_data_giros timestamp without time zone NOT NULL DEFAULT now(), -- Registro de data e hora da ocorrencia dos giros.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  CONSTRAINT pk_giro_id PRIMARY KEY (giro_id), -- Chave primaria da tabela giro.
  CONSTRAINT pk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela catraca.
);
ALTER TABLE giro OWNER TO postgres;
COMMENT ON TABLE giro IS 'Tabela que armazena a contabilizacao de giros da catraca.';
COMMENT ON COLUMN giro.giro_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN giro.giro_giros_horario IS 'Contador de giros no sentido horario.';
COMMENT ON COLUMN giro.giro_giros_antihorario IS 'Contador de giros no sentido anti-horario.';
COMMENT ON COLUMN giro.giro_data_giros IS 'Registro de data e hora da ocorrencia dos giros.';
COMMENT ON COLUMN giro.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT pk_giro_id ON giro IS 'Chave primaria da tabela giro.';
COMMENT ON CONSTRAINT pk_catr_id ON giro IS 'Chave estrangeira da tabela catraca.';

-- Table: mensagem
CREATE TABLE mensagem
(
  mens_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  mens_inicializacao character varying(35), -- Texto de inicializacao da catraca.
  mens_saldacao character varying(35), -- Texto de saldacao na catraca.
  mens_aguardacartao character varying(35), -- Texto solicitando o uso do cartao na catraca.
  mens_erroleitor character varying(35), -- Texto de erro na leitura do cartao na catraca.
  mens_bloqueioacesso character varying(35), -- Texto de acesso bloqueado na catraca.
  mens_liberaacesso character varying(35), -- Texto de acesso liberado na catraca.
  mens_semcredito character varying(35), -- Texto de cartao sem creditos.
  mens_semcadastro character varying(35), -- Texto de cartao nao cadastrado no sistema.
  mens_cartaoinvalido character varying(35), -- Texto de cartao que nao atende a todos os criterios de uso na catraca.
  mens_turnoinvalido character varying(35), -- Texto de uso do cartao fora da faixa de horarios do turno.
  mens_datainvalida character varying(35), -- Texto de dias nao uteis para uso da catraca.
  mens_cartaoutilizado character varying(35), -- Texto para cartao ja utilizado na catraca dentro do turno.
  mens_institucional1 character varying(35), -- Texto 01 livre para avisos, informes, etc.
  mens_institucional2 character varying(35), -- Texto 02 livre para avisos, informes, etc.
  mens_institucional3 character varying(35), -- Texto 03 livre para avisos, informes, etc.
  mens_institucional4 character varying(35), -- Texto 04 livre para avisos, informes, etc.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  CONSTRAINT pk_mens_id PRIMARY KEY (mens_id), -- Chave primaria da tabela mensagem.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela catraca.
);
ALTER TABLE mensagem OWNER TO postgres;
COMMENT ON TABLE mensagem IS 'Tabela que armazena as mensagens para exibicao em display LCD de 2 linhas de 16 caracteres.';
COMMENT ON COLUMN mensagem.mens_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN mensagem.mens_inicializacao IS 'Texto de inicializacao da catraca.';
COMMENT ON COLUMN mensagem.mens_saldacao IS 'Texto de saldacao na catraca.';
COMMENT ON COLUMN mensagem.mens_aguardacartao IS 'Texto solicitando o uso do cartao na catraca.';
COMMENT ON COLUMN mensagem.mens_erroleitor IS 'Texto de erro na leitura do cartao na catraca.';
COMMENT ON COLUMN mensagem.mens_bloqueioacesso IS 'Texto de acesso bloqueado na catraca.';
COMMENT ON COLUMN mensagem.mens_liberaacesso IS 'Texto de acesso liberado na catraca.';
COMMENT ON COLUMN mensagem.mens_semcredito IS 'Texto de cartao sem creditos.';
COMMENT ON COLUMN mensagem.mens_semcadastro IS 'Texto de cartao nao cadastrado no sistema.';
COMMENT ON COLUMN mensagem.mens_cartaoinvalido IS 'Texto de cartao que nao atende a todos os criterios de uso na catraca.';
COMMENT ON COLUMN mensagem.mens_turnoinvalido IS 'Texto de uso do cartao fora da faixa de horarios do turno.';
COMMENT ON COLUMN mensagem.mens_datainvalida IS 'Texto de dias nao uteis para uso da catraca.';
COMMENT ON COLUMN mensagem.mens_cartaoutilizado IS 'Texto para cartao ja utilizado na catraca dentro do turno.';
COMMENT ON COLUMN mensagem.mens_institucional1 IS 'Texto 01 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional2 IS 'Texto 02 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional3 IS 'Texto 03 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional4 IS 'Texto 04 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT pk_mens_id ON mensagem IS 'Chave primaria da tabela mensagem.';
COMMENT ON CONSTRAINT fk_catr_id ON mensagem IS 'Chave estrangeira da tabela catraca.';

-- Table: guiche
CREATE TABLE guiche
(
  guic_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  guic_abertura timestamp without time zone, -- Data e hora do inicio de funcionamento do guiche.
  guic_encerramento timestamp without time zone, -- Data e hora do fim de funcionamento do guiche.
  guic_ativo boolean, -- Status de atividade atual do guiche.
  unid_id integer NOT NULL, -- Campo para chave estrangeira da tabela unidade.
  usua_id integer NOT NULL, -- Campo para chave estrangeira da tabela usuario.
  CONSTRAINT pk_guic_id PRIMARY KEY (guic_id), -- Chave primaria da tabela guiche.
  CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabela unidade.
  CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario (usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela usuario.
);
ALTER TABLE guiche OWNER TO postgres;
COMMENT ON TABLE guiche IS 'Tabela que armazena as infiomacoes do guiche que ira realizar as operacoes financeiras.';
COMMENT ON COLUMN guiche.guic_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN guiche.guic_abertura IS 'Data e hora do inicio de funcionamento do guiche.';
COMMENT ON COLUMN guiche.guic_encerramento IS 'Data e hora do fim de funcionamento do guiche.';
COMMENT ON COLUMN guiche.guic_ativo IS 'Status de atividade atual do guiche.';
COMMENT ON COLUMN guiche.unid_id IS 'Campo para chave estrangeira da tabela unidade.';
COMMENT ON COLUMN guiche.usua_id IS 'Campo para chave estrangeira da tabela usuario.';
COMMENT ON CONSTRAINT pk_guic_id ON guiche IS 'Chave primaria da tabela guiche.';
COMMENT ON CONSTRAINT fk_unid_id ON guiche IS 'Chave estrangeira da tabela unidade.';
COMMENT ON CONSTRAINT fk_usua_id ON guiche IS 'Chave estrangeira da tabela usuario.';


-- Table: fluxo
CREATE TABLE fluxo
(
  flux_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  flux_data timestamp without time zone, -- Registro de data e hora do cadastro.
  flux_valor numeric(8,2), -- Valor em R$ da receita ou despesa.
  flux_descricao character varying(200), -- Descricao para o historio do fluxo de caixa.
  guic_id integer NOT NULL, -- Campo para chave estrengeira da tabela guiche.
  CONSTRAINT pk_flux_id PRIMARY KEY (flux_id), -- Chave primaria da tabela fluxo.
  CONSTRAINT fk_guic_id FOREIGN KEY (guic_id) REFERENCES guiche (guic_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela guiche.
);
ALTER TABLE fluxo OWNER TO postgres;
COMMENT ON TABLE fluxo IS 'Tabela que armazena os registros dos fluxos de caixa.';
COMMENT ON COLUMN fluxo.flux_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN fluxo.flux_data IS 'Registro de data e hora do cadastro.';
COMMENT ON COLUMN fluxo.flux_valor IS 'Valor em R$ da receita ou despesa.';
COMMENT ON COLUMN fluxo.flux_descricao IS 'Descricao para o historio do fluxo de caixa.';
COMMENT ON COLUMN fluxo.guic_id IS 'Campo para chave estrengeira da tabela guiche.';
COMMENT ON CONSTRAINT pk_flux_id ON fluxo IS 'Chave primaria da tabela fluxo.';
COMMENT ON CONSTRAINT fk_guic_id ON fluxo IS 'Chave estrangeira da tabela guiche.';

-- Table: turno
CREATE TABLE turno
(
  turn_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  turn_hora_inicio time without time zone, -- Hora inicio do periodo para liberacao da catraca.
  turn_hora_fim time without time zone, -- Hora final do periodo para liberacao da catraca.
  CONSTRAINT pk_turn_id PRIMARY KEY (turn_id) -- Chave primaria da tabela turno.
);
ALTER TABLE turno OWNER TO postgres;
COMMENT ON TABLE turno IS 'Tabela que armazena os horarios de inicio e fim de funcionamento dos turnos.';
COMMENT ON COLUMN turno.turn_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN turno.turn_hora_inicio IS 'Hora inicio do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_hora_fim IS 'Hora final do periodo para liberacao da catraca.';
COMMENT ON CONSTRAINT pk_turn_id ON turno IS 'Chave primaria da tabela turno.';

-- Table: registro
CREATE TABLE registro
(
  regi_id bigserial NOT NULL,
  regi_data timestamp without time zone, -- Data e hora que efetivou o giro na catraca.
  regi_valor_pago numeric(8,2), -- Valor em R$ da refeicao.
  regi_valor_custo numeric(8,2), -- Valor em R$ do custo da refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  turn_id integer NOT NULL, -- Campo para chave estrangeira da tabela turno.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  CONSTRAINT pk_regi PRIMARY KEY (regi_id),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabela cartao.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabela catraca.
  CONSTRAINT fk_turn_id FOREIGN KEY (turn_id) REFERENCES turno (turn_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela turno.
);
ALTER TABLE registro OWNER TO postgres;
COMMENT ON TABLE registro IS 'Tabela que armazena os registros de uso do cartao na catraca.';
COMMENT ON COLUMN registro.regi_data IS 'Data e hora que efetivou o giro na catraca.';
COMMENT ON COLUMN registro.regi_valor_pago IS 'Valor em R$ da refeicao.';
COMMENT ON COLUMN registro.regi_valor_custo IS 'Valor em R$ do custo da refeicao.';
COMMENT ON COLUMN registro.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON COLUMN registro.turn_id IS 'Campo para chave estrangeira da tabela turno.';
COMMENT ON COLUMN registro.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT fk_cart_id ON registro IS 'Chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT fk_catr_id ON registro IS 'Chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT fk_turn_id ON registro IS 'Chave estrangeira da tabela turno.';

-- Table: unidade_turno
CREATE TABLE turno
(
  turn_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  turn_hora_inicio time without time zone, -- Hora inicio do periodo para liberacao da catraca.
  turn_hora_fim time without time zone, -- Hora final do periodo para liberacao da catraca.
  turn_descricao character varying(25), -- Descricao da refeicao disponibilizada durante o turno. Ex.: Cafe, Almoco, Janta.
  CONSTRAINT pk_turn_id PRIMARY KEY (turn_id) -- Chave primaria da tabela turno.
);
ALTER TABLE turno OWNER TO postgres;
COMMENT ON TABLE turno IS 'Tabela que armazena os horarios de inicio e fim de funcionamento dos turnos.';
COMMENT ON COLUMN turno.turn_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN turno.turn_hora_inicio IS 'Hora inicio do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_hora_fim IS 'Hora final do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_descricao IS 'Descricao da refeicao disponibilizada durante o turno. Ex.: Cafe, Almoco, Janta.';
COMMENT ON CONSTRAINT pk_turn_id ON turno IS 'Chave primaria da tabela turno.';

-- Table: custo_cartao
CREATE TABLE custo_cartao
(
  cuca_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  cuca_valor numeric(8,2), -- Valor em R$ do custo do cartao.
  cuca_data timestamp without time zone, -- Data de cadastro do custo.
  CONSTRAINT pk_cuca_id PRIMARY KEY (cuca_id) -- Chave primaria da tabela custo_cartao.
);
ALTER TABLE custo_cartao OWNER TO postgres;
COMMENT ON TABLE custo_cartao IS 'Tabela que armazena os registros de custo do cartao.';
COMMENT ON COLUMN custo_cartao.cuca_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN custo_cartao.cuca_valor IS 'Valor em R$ do custo do cartao.';
COMMENT ON COLUMN custo_cartao.cuca_data IS 'Data de cadastro do custo.';
COMMENT ON CONSTRAINT pk_cuca_id ON custo_cartao IS 'Chave primaria da tabela custo_cartao.';

-- Table: custo_refeicao
CREATE TABLE custo_refeicao
(
  cure_id serial NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  cure_valor numeric(8,2), -- Valor em R$ do custo da refeicao.
  cure_data timestamp without time zone, -- Data e hora de cadastro do custo.
  CONSTRAINT pk_cure_id PRIMARY KEY (cure_id) -- Chave primaria da tabela custo_refeicao.
);
ALTER TABLE custo_refeicao OWNER TO postgres;
COMMENT ON TABLE custo_refeicao IS 'Tabela que armazena os registros de custo da refeicao.';
COMMENT ON COLUMN custo_refeicao.cure_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN custo_refeicao.cure_valor IS 'Valor em R$ do custo da refeicao.';
COMMENT ON COLUMN custo_refeicao.cure_data IS 'Data e hora de cadastro do custo.';
COMMENT ON CONSTRAINT pk_cure_id ON custo_refeicao IS 'Chave primaria da tabela custo_refeicao.';
