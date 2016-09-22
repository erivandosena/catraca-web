----------------------------------------------------------------------------
-- Autor_script : Erivando Sena											  --
-- Copyright    : Unilab											      --
-- Data_criacao : 16/10/2015											  --
-- Data_revisao : 14/09/2016											  --
-- Status       : Desenvolvimento										  --
----------------------------------------------------------------------------

----------------------------------------------------------------------------
--                             BANCO DE DADOS                             --
----------------------------------------------------------------------------

-- Database: desenvolvimento

CREATE DATABASE desenvolvimento WITH OWNER = catraca ENCODING = 'UTF8';
COMMENT ON DATABASE desenvolvimento IS 'Bando de dados de desenvolvimento.';

-- Conectar a base raspberrypi
\connect raspberrypi;

-- Criacao das tabelas
----------------------------------------------------------------------------
--                                 TABELAS                                --
----------------------------------------------------------------------------

-- Table: tipo
CREATE TABLE tipo
(
  tipo_id integer NOT NULL, -- Campo para chave primaria da tabela.
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

-- Table: turno
CREATE TABLE turno
(
  turn_id integer NOT NULL, -- Campo para chave primaria da tabela.
  turn_hora_inicio time without time zone, -- Hora inicio do periodo para liberacao da catraca.
  turn_hora_fim time without time zone, -- Hora final do periodo para liberacao da catraca.
  turn_descricao character varying(16), -- Descricao da refeicao disponibilizada durante o turno. Ex.: Cafe, Almoco, Janta.
  CONSTRAINT pk_turn_id PRIMARY KEY (turn_id) -- Chave primaria da tabela turno.
);
ALTER TABLE turno OWNER TO postgres;
COMMENT ON TABLE turno IS 'Tabela que armazena os horarios de inicio e fim de funcionamento dos turnos.';
COMMENT ON COLUMN turno.turn_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN turno.turn_hora_inicio IS 'Hora inicio do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_hora_fim IS 'Hora final do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_descricao IS 'Descricao da refeicao disponibilizada durante o turno. Ex.: Cafe, Almoco, Janta.';
COMMENT ON CONSTRAINT pk_turn_id ON turno IS 'Chave primaria da tabela turno.';

-- Table: unidade
CREATE TABLE unidade
(
  unid_id integer NOT NULL, -- Campo autoincremento para chave primaria da tabela.
  unid_nome character varying(50), -- Nome do local de funcionamento da catraca.
  CONSTRAINT pk_unid_id PRIMARY KEY (unid_id) -- Chave primaria da tabela unidade.
);
ALTER TABLE unidade OWNER TO postgres;
COMMENT ON TABLE unidade IS 'Tabela que armazena o local fisico de funcionamento das catracas.';
COMMENT ON COLUMN unidade.unid_id IS 'Campo autoincremento para chave primaria da tabela.';
COMMENT ON COLUMN unidade.unid_nome IS 'Nome do local de funcionamento da catraca.';
COMMENT ON CONSTRAINT pk_unid_id ON unidade IS 'Chave primaria da tabela unidade.';

-- Table: custo_refeicao
CREATE TABLE custo_refeicao
(
  cure_id integer NOT NULL, -- Campo para chave primaria da tabela.
  cure_valor numeric(8,2), -- Valor em R$ do custo da refeicao.
  cure_data timestamp without time zone, -- Data e hora de cadastro do custo.
  CONSTRAINT pk_cure_id PRIMARY KEY (cure_id) -- Chave primaria da tabela custo_refeicao.
);
ALTER TABLE custo_refeicao OWNER TO postgres;
COMMENT ON TABLE custo_refeicao IS 'Tabela que armazena os registros de custo da refeicao.';
COMMENT ON COLUMN custo_refeicao.cure_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN custo_refeicao.cure_valor IS 'Valor em R$ do custo da refeicao.';
COMMENT ON COLUMN custo_refeicao.cure_data IS 'Data e hora de cadastro do custo.';
COMMENT ON CONSTRAINT pk_cure_id ON custo_refeicao IS 'Chave primaria da tabela custo_refeicao.';

-- Table: custo_unidade
CREATE TABLE custo_unidade
(
  cuun_id integer NOT NULL, -- Campo para chave primaria da tabela.
  unid_id integer NOT NULL, -- Chave estrangeira da tabela unidade.
  cure_id integer NOT NULL, -- Chave estrangeira da tabela custo_refeicao.
  CONSTRAINT pk_cuun_id PRIMARY KEY (cuun_id ), -- Chave primaria da tabela custo_unidade.
  CONSTRAINT fk_cure_id FOREIGN KEY (cure_id) REFERENCES custo_refeicao (cure_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela custo_refeicao.
  CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela unidade.
);
ALTER TABLE custo_unidade OWNER TO postgres;
COMMENT ON TABLE custo_unidade IS 'Tabela que armazena os custo de refeicoes por unidade.';
COMMENT ON COLUMN custo_unidade.cuun_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN custo_unidade.unid_id IS 'Chave estrangeira da tabela unidade.';
COMMENT ON COLUMN custo_unidade.cure_id IS 'Chave estrangeira da tabela custo_refeicao.';
COMMENT ON CONSTRAINT pk_cuun_id ON custo_unidade IS 'Chave primaria da tabela custo_unidade.';
COMMENT ON CONSTRAINT fk_cure_id ON custo_unidade IS 'Chave estrangeira da tabela custo_refeicao.';
COMMENT ON CONSTRAINT fk_unid_id ON custo_unidade IS 'Chave estrangeira da tabela unidade.';

-- Table: usuario
CREATE TABLE usuario
(
  usua_id integer NOT NULL, -- Campo para chave primaria da tabela.
  usua_nome character varying(150), -- Nome completo do usuario no SIG.
  usua_email character varying(150), -- Endereco de e-mail do usuario no SIG.
  usua_login character varying(25), -- Nome de usuario no SIG.
  usua_senha character varying(50), -- Senha cadastrada no SIG.
  usua_nivel integer, -- Status atual do usuario no SIG.
  id_base_externa integer, -- Campo da chave primaria (uid) no sistema SIG.
  CONSTRAINT pk_usua_id PRIMARY KEY (usua_id) -- Chave primaria da tabela usuario.
);
ALTER TABLE usuario OWNER TO postgres;
COMMENT ON TABLE usuario IS 'Tabela que armazena as informacoes externas de usuarios do sistema provenientes do SIG.';
COMMENT ON COLUMN usuario.usua_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN usuario.usua_nome IS 'Nome completo do usuario no SIG.';
COMMENT ON COLUMN usuario.usua_email IS 'Endereco de e-mail do usuario no SIG.';
COMMENT ON COLUMN usuario.usua_login IS 'Nome de usuario no SIG.';
COMMENT ON COLUMN usuario.usua_senha IS 'Senha cadastrada no SIG.';
COMMENT ON COLUMN usuario.usua_nivel IS 'Status atual do usuario no SIG.';
COMMENT ON COLUMN usuario.id_base_externa IS 'Campo da chave primaria (uid) no sistema SIG.';
COMMENT ON CONSTRAINT pk_usua_id ON usuario IS 'Chave primaria da tabela usuario.';

-- Table: catraca
CREATE TABLE catraca
(
  catr_id integer NOT NULL, -- Campo para chave primaria da tabela.
  catr_ip character varying(12), -- Numero IP da catraca.
  catr_tempo_giro integer, -- Tempo para o giro na catraca em segundos.
  catr_operacao integer, -- 1=Giro Horario(Entrada controlada com saida bloqueada),2=Giro Anti-horario(Entrada controlada com saida liberada),3=Giro Horario/Anti-horario(Entrada e saida liberadas).
  catr_nome character varying(25), -- Nome da catraca formado pelo nome do host, nome da unidade e numero da catraca.
  catr_mac_lan character varying(23), -- Registro do endereco fisico do hardware fixo LAN.
  catr_mac_wlan character varying(23), -- Registro do endereco fisico do hardware fixo ou plugue de rede WLAN.
  catr_interface_rede character varying(10), -- Informa se a interface de rede utilizada sera eth0 ou wlan0
  catr_financeiro boolean NOT NULL DEFAULT false, -- Habilita ou desabilita a debitacao de creditos do cartao com relacao ao financeiro.
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id ) -- Chave primaria da tabela catraca.
);
ALTER TABLE catraca OWNER TO postgres;
COMMENT ON TABLE catraca IS 'Tabela que armazena as predefinicoes e configuracoes para o funcionamento da catraca..';
COMMENT ON COLUMN catraca.catr_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN catraca.catr_ip IS 'Numero IP da catraca.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro na catraca em segundos.';
COMMENT ON COLUMN catraca.catr_operacao IS '1=Giro Horario(Entrada controlada com saida bloqueada),2=Giro Anti-horario(Entrada controlada com saida liberada),3=Giro Horario/Anti-horario(Entrada e saida liberadas).';
COMMENT ON COLUMN catraca.catr_nome IS 'Nome da catraca formado pelo nome do host, nome da unidade e numero da catraca. ';
COMMENT ON COLUMN catraca.catr_mac_lan IS 'Registro do endereco fisico do hardware fixo LAN.';
COMMENT ON COLUMN catraca.catr_mac_wlan IS 'Registro do endereco fisico do hardware fixo ou plugue de rede WLAN.';
COMMENT ON COLUMN catraca.catr_interface_rede IS 'Informa se a interface de rede utilizada sera eth0 ou wlan0';
COMMENT ON COLUMN catraca.catr_financeiro IS 'Habilita ou desabilita a debitacao de creditos do cartao com relacao ao financeiro.';
COMMENT ON CONSTRAINT pk_catr_id ON catraca IS 'Chave primaria da tabela catraca.';

-- Table: mensagem
CREATE TABLE mensagem
(
  mens_id integer NOT NULL, -- Campo para chave primaria da tabela.
  mens_institucional1 character varying(80), -- Texto 01 livre para avisos, informes, etc.
  mens_institucional2 character varying(80), -- Texto 02 livre para avisos, informes, etc.
  mens_institucional3 character varying(80), -- Texto 03 livre para avisos, informes, etc.
  mens_institucional4 character varying(80), -- Texto 04 livre para avisos, informes, etc.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  CONSTRAINT pk_mens_id PRIMARY KEY (mens_id), -- Chave primaria da tabela mensagem.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela catraca.
);
ALTER TABLE mensagem OWNER TO postgres;
COMMENT ON TABLE mensagem IS 'Tabela que armazena as mensagens para exibicao em display LCD de 2 linhas de 16 caracteres.';
COMMENT ON COLUMN mensagem.mens_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN mensagem.mens_institucional1 IS 'Texto 01 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional2 IS 'Texto 02 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional3 IS 'Texto 03 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.mens_institucional4 IS 'Texto 04 livre para avisos, informes, etc.';
COMMENT ON COLUMN mensagem.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT pk_mens_id ON mensagem IS 'Chave primaria da tabela mensagem.';
COMMENT ON CONSTRAINT fk_catr_id ON mensagem IS 'Chave estrangeira da tabela catraca.';

-- Table: cartao
CREATE TABLE cartao
(
  cart_id integer NOT NULL, -- Campo para chave primaria da tabela.
  cart_numero character varying(10), -- Numero ID do cartao Smart Card sem permissao de duplicidade.
  cart_creditos numeric(8,2), -- Total de creditos em R$ para uso do cartao.
  tipo_id integer NOT NULL, -- Campo para chave estrangeira da tabela tipo.
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id ), -- Chave primaria da tabela cartao.
  CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo (tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela tipo.
  CONSTRAINT uk_cart_numero UNIQUE (cart_numero ) -- Restricao de duplicidades para o campo cart_numero.
);
ALTER TABLE cartao OWNER TO postgres;
COMMENT ON TABLE cartao IS 'Tabela que armazena os registros de uso do cartao RFID.';
COMMENT ON COLUMN cartao.cart_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN cartao.cart_numero IS 'Numero ID do cartao Smart Card sem permissao de duplicidade.';
COMMENT ON COLUMN cartao.cart_creditos IS 'Total de creditos em R$ para uso do cartao.';
COMMENT ON COLUMN cartao.tipo_id IS 'Campo para chave estrangeira da tabela tipo.';
COMMENT ON CONSTRAINT pk_cart_id ON cartao IS 'Chave primaria da tabela cartao.';
COMMENT ON CONSTRAINT fk_tipo_id ON cartao IS 'Chave estrangeira da tabela tipo.';
COMMENT ON CONSTRAINT uk_cart_numero ON cartao IS 'Restricao de duplicidades para o campo cart_numero.';

-- Table: vinculo
CREATE TABLE vinculo
(
  vinc_id integer NOT NULL, -- Campo para chave primaria da tabela.
  vinc_avulso boolean NOT NULL DEFAULT false, -- Status que informa se o vinculo esta ativo.
  vinc_inicio timestamp without time zone, -- Data e hora de inicio da validade do vinculo.
  vinc_fim timestamp without time zone, -- Data e hora de fim da validade do vinculo.
  vinc_descricao character varying(250) NOT NULL, -- Descricao sobre a finalidade do vinculo.
  vinc_refeicoes integer NOT NULL, -- Quantidade de uso do cartao por refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  usua_id integer NOT NULL, -- Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de vinculo).
  CONSTRAINT pk_vinc_id PRIMARY KEY (vinc_id),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela cartao.
  CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario (usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela usuario.
);
ALTER TABLE vinculo OWNER TO postgres;
COMMENT ON TABLE vinculo IS 'Tabela que armazena as informacoes de vinculo entre o usuario e o tipo de cartao.';
COMMENT ON COLUMN vinculo.vinc_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN vinculo.vinc_avulso IS 'Status que informa se o vinculo esta ativo.';
COMMENT ON COLUMN vinculo.vinc_inicio IS 'Data e hora de inicio da validade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_fim IS 'Data e hora de fim da validade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_descricao IS 'Descricao sobre a finalidade do vinculo.';
COMMENT ON COLUMN vinculo.vinc_refeicoes IS 'Quantidade de uso do cartao por refeicao.';
COMMENT ON COLUMN vinculo.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON COLUMN vinculo.usua_id IS 'Campo para chave estrangeira da tabela usuario.(Usuario responsavel por realizar a operacao de vinculo).';
COMMENT ON CONSTRAINT fk_cart_id ON vinculo IS 'Chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT fk_usua_id ON vinculo IS 'Chave estrangeira da tabela usuario.';
COMMENT ON CONSTRAINT pk_vinc_id ON vinculo IS 'Chave primaria da tabela vinculo.';

-- Table: isencao
CREATE TABLE isencao
(
  isen_id integer NOT NULL, -- Campo para chave primaria da tabela.
  isen_inicio timestamp without time zone, -- Data e hora do inico da validade para isencao de pagamento.
  isen_fim timestamp without time zone, -- Data e hora do fim da validade para isencao de pagamento.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  CONSTRAINT pk_isen_id PRIMARY KEY (isen_id), -- Chave primaria da tabela isencao.
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela cartao.
);
ALTER TABLE isencao OWNER TO postgres;
COMMENT ON TABLE isencao IS 'Tabela que armazena as validades para isencao das refeicoes.';
COMMENT ON COLUMN isencao.isen_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN isencao.isen_inicio IS 'Data e hora do inico da validade para isencao de pagamento.';
COMMENT ON COLUMN isencao.isen_fim IS 'Data e hora do fim da validade para isencao de pagamento.';
COMMENT ON COLUMN isencao.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT pk_isen_id ON isencao IS 'Chave primaria da tabela isencao.';
COMMENT ON CONSTRAINT fk_cart_id ON isencao IS 'Chave estrangeira da tabela cartao. ';

-- Table: unidade_turno
CREATE TABLE unidade_turno
(
  untu_id integer NOT NULL, -- Campo para chave primaria da tabela.
  turn_id integer NOT NULL, -- Campo para chave estrangeira da tabela turno.
  unid_id integer NOT NULL, -- Campo para chave estrangeira da tabela unidade.
  CONSTRAINT pk_untu_id PRIMARY KEY (untu_id), -- Chave primaria da tabela unidade_turno.
  CONSTRAINT fk_turn_id FOREIGN KEY (turn_id) REFERENCES turno (turn_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela turno.
  CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela unidade.
);
ALTER TABLE unidade_turno OWNER TO postgres;
COMMENT ON TABLE unidade_turno IS 'Tabela que armazena o local fisico de funcionamento das catracas para o turno.';
COMMENT ON COLUMN unidade_turno.untu_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN unidade_turno.turn_id IS 'Campo para chave estrangeira da tabela turno.';
COMMENT ON COLUMN unidade_turno.unid_id IS 'Campo para chave estrangeira da tabela unidade.';
COMMENT ON CONSTRAINT pk_untu_id ON unidade_turno IS 'Chave primaria da tabela unidade_turno.';
COMMENT ON CONSTRAINT fk_turn_id ON unidade_turno IS 'Chave estrangeira da tabela turno.';
COMMENT ON CONSTRAINT fk_unid_id ON unidade_turno IS 'Chave estrangeira da tabela unidade.';

-- Table: catraca_unidade
CREATE TABLE catraca_unidade
(
  caun_id integer NOT NULL, -- Campo para chave primaria da tabela.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  unid_id integer NOT NULL, -- Campo para chave estrangeira da tabela unidade.
  CONSTRAINT pk_caun_id PRIMARY KEY (caun_id), -- Chave primaria da tabela catraca_unidade.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela catraca.
  CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela unidade.
);
ALTER TABLE catraca_unidade OWNER TO postgres;
COMMENT ON TABLE catraca_unidade IS 'Tabela que armazena as informacoes da unidade e da catraca.';
COMMENT ON COLUMN catraca_unidade.caun_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN catraca_unidade.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON COLUMN catraca_unidade.unid_id IS 'Campo para chave estrangeira da tabela unidade.';
COMMENT ON CONSTRAINT pk_caun_id ON catraca_unidade IS 'Chave primaria da tabela catraca_unidade.';
COMMENT ON CONSTRAINT fk_catr_id ON catraca_unidade IS 'Chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT fk_unid_id ON catraca_unidade IS 'Chave estrangeira da tabela unidade.';

-- Table: registro
CREATE TABLE registro
(
  regi_id bigint NOT NULL, -- Campo para chave primaria da tabela.
  regi_data timestamp without time zone, -- Data e hora que efetivou o giro na catraca.
  regi_valor_pago numeric(8,2), -- Valor em R$ da refeicao.
  regi_valor_custo numeric(8,2), -- Valor em R$ do custo da refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  vinc_id integer NOT NULL, -- Campo para chave estrangeira da tabela vinculo.
  CONSTRAINT pk_regi_id PRIMARY KEY (regi_id ), -- Chave primaria da tabela registro.
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela cartao.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela catraca.
  CONSTRAINT fk_vinc_id FOREIGN KEY (vinc_id) REFERENCES vinculo (vinc_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela vinculo.
);
ALTER TABLE registro OWNER TO postgres;
COMMENT ON TABLE registro IS 'Tabela que armazena os registros de uso do cartao na catraca.';
COMMENT ON COLUMN registro.regi_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN registro.regi_data IS 'Data e hora que efetivou o giro na catraca.';
COMMENT ON COLUMN registro.regi_valor_pago IS 'Valor em R$ da refeicao.';
COMMENT ON COLUMN registro.regi_valor_custo IS 'Valor em R$ do custo da refeicao.';
COMMENT ON COLUMN registro.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON COLUMN registro.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON COLUMN registro.vinc_id IS 'Campo para chave estrangeira da tabela vinculo.';
COMMENT ON CONSTRAINT pk_regi_id ON registro IS 'Chave primaria da tabela registro.';
COMMENT ON CONSTRAINT fk_cart_id ON registro IS 'Chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT fk_catr_id ON registro IS 'Chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT fk_vinc_id ON registro IS 'Chave estrangeira da tabela vinculo.';

-- Table: registro_offline
CREATE TABLE registro_offline
(
  reof_id bigserial NOT NULL, -- Campo para chave primaria da tabela.
  reof_data timestamp without time zone, -- Data e hora que efetivou o giro na catraca.
  reof_valor_pago numeric(8,2), -- Valor em R$ da refeicao.
  reof_valor_custo numeric(8,2), -- Valor em R$ do custo da refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  catr_id integer NOT NULL, -- Campo para chave estrangeira da tabela catraca.
  vinc_id integer NOT NULL, -- Campo para chave estrangeira da tabela vinculo.
  CONSTRAINT pk_reof_id PRIMARY KEY (reof_id ), -- Chave primaria da tabela registro_offline.
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela cartao.
  CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE, -- Chave estrangeira da tabela catraca.
  CONSTRAINT fk_vinc_id FOREIGN KEY (vinc_id) REFERENCES vinculo (vinc_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE CASCADE -- Chave estrangeira da tabela vinculo.
);
ALTER TABLE registro_offline OWNER TO postgres;
COMMENT ON TABLE registro_offline IS 'Tabela que armazena os registros off-lines de uso do cartao na catraca.';
COMMENT ON COLUMN registro_offline.reof_id IS 'Campo para chave primaria da tabela.';
COMMENT ON COLUMN registro_offline.reof_data IS 'Data e hora que efetivou o giro na catraca.';
COMMENT ON COLUMN registro_offline.reof_valor_pago IS 'Valor em R$ da refeicao.';
COMMENT ON COLUMN registro_offline.reof_valor_custo IS 'Valor em R$ do custo da refeicao.';
COMMENT ON COLUMN registro_offline.cart_id IS 'Campo para chave estrangeira da tabela cartao.';
COMMENT ON COLUMN registro_offline.catr_id IS 'Campo para chave estrangeira da tabela catraca.';
COMMENT ON COLUMN registro_offline.vinc_id IS 'Campo para chave estrangeira da tabela vinculo.';
COMMENT ON CONSTRAINT pk_reof_id ON registro_offline IS 'Chave primaria da tabela registro_offline.';
COMMENT ON CONSTRAINT fk_cart_id ON registro_offline IS 'Chave estrangeira da tabela cartao.';
COMMENT ON CONSTRAINT fk_catr_id ON registro_offline IS 'Chave estrangeira da tabela catraca.';
COMMENT ON CONSTRAINT fk_vinc_id ON registro_offline IS 'Chave estrangeira da tabela vinculo.';
