---------------------------------
-- Autor_script : Erivando Sena
-- Copyright    : Unilab
-- Data_criacao : 16/10/2015
-- Data_revisao : 12/07/2017
-- Status       : Em Homologação
---------------------------------

CREATE TABLE usuario
(
usua_id serial NOT NULL, 
usua_nome character varying(150), 
usua_email character varying(150),
usua_login character varying(25), 
usua_senha character varying(50), 
usua_nivel integer, 
id_base_externa integer, 
CONSTRAINT pk_usua_id PRIMARY KEY (usua_id)
);
CREATE TABLE transacao
(
tran_id serial NOT NULL,
tran_valor numeric(8,2),
tran_descricao character varying(150), 
tran_data timestamp without time zone, 
usua_id integer NOT NULL, 
usua_id1 integer NOT NULL, 
CONSTRAINT pk_tran_id PRIMARY KEY (tran_id), 
CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) 
REFERENCES usuario (usua_id)
MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_usua_id1 FOREIGN KEY (usua_id1) 
REFERENCES usuario (usua_id)
MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION   
);
CREATE TABLE tipo
(
tipo_id serial NOT NULL,
tipo_nome character varying(25), 
tipo_valor numeric(8,2),
CONSTRAINT pk_tipo_id PRIMARY KEY (tipo_id) 
);
CREATE TABLE cartao
(
cart_id serial NOT NULL,
cart_numero bigint, 
cart_creditos numeric(8,2),
tipo_id integer NOT NULL,
CONSTRAINT pk_cart_id PRIMARY KEY (cart_id),
CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo (tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT uk_cart_numero UNIQUE (cart_numero)
);
CREATE TABLE vinculo
(
vinc_id serial NOT NULL,
vinc_avulso boolean, 
vinc_inicio timestamp without time zone, 
vinc_fim timestamp without time zone, 
vinc_descricao character varying(150),
vinc_refeicoes integer, 
cart_id integer NOT NULL,
usua_id integer NOT NULL, 
CONSTRAINT pk_vinc_id PRIMARY KEY (vinc_id),
CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, -- Chave estrangeira da tabela cartao.
CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario (usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela usuario.
);
CREATE TABLE isencao
(
isen_id serial NOT NULL, 
isen_inicio timestamp without time zone, 
isen_fim timestamp without time zone, 
cart_id integer NOT NULL, 
CONSTRAINT pk_isen_id PRIMARY KEY (isen_id), 
CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION -- Chave estrangeira da tabela cartao.
);
CREATE TABLE unidade
(
unid_id serial NOT NULL, 
unid_nome character varying(50), 
CONSTRAINT pk_unid_id PRIMARY KEY (unid_id) 
);

CREATE TABLE catraca
( 
catr_id serial NOT NULL, 
catr_ip character varying(12), 
catr_tempo_giro integer, 
catr_operacao integer, 
catr_nome character varying(25), 
catr_mac_lan character varying(23), 
catr_mac_wlan character varying(23), 
catr_interface_rede character varying(10), 
catr_financeiro boolean,
CONSTRAINT pk_catr_id PRIMARY KEY (catr_id) 
);

CREATE TABLE catraca_unidade
(
caun_id serial NOT NULL, 
catr_id integer NOT NULL,
unid_id integer NOT NULL,
CONSTRAINT pk_caun_id PRIMARY KEY (caun_id), 
CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 
);
CREATE TABLE custo_unidade
( 
cuun_id serial NOT NULL, 
unid_id integer, 
cure_id integer, 
CONSTRAINT pk_cuun_id PRIMARY KEY (cuun_id), 
CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_cure_id FOREIGN KEY (cure_id) REFERENCES custo_refeicao (cure_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 

);

CREATE TABLE mensagem
(
mens_id serial NOT NULL, 
mens_institucional1 character varying(80), 
mens_institucional2 character varying(80), 
mens_institucional3 character varying(80), 
mens_institucional4 character varying(80),  
catr_id integer NOT NULL, 
CONSTRAINT pk_mens_id PRIMARY KEY (mens_id), 
CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 
);

CREATE TABLE turno
(
turn_id serial NOT NULL, 
turn_hora_inicio time without time zone, 
turn_hora_fim time without time zone, 
turn_descricao character varying(25), 
CONSTRAINT pk_turn_id PRIMARY KEY (turn_id) 
);

CREATE TABLE registro
(
regi_id bigserial NOT NULL,
regi_data timestamp without time zone,
regi_valor_pago numeric(8,2), 
regi_valor_custo numeric(8,2),
cart_id integer NOT NULL, 
catr_id integer NOT NULL, 
vinc_id integer NOT NULL, 
CONSTRAINT pk_regi_id PRIMARY KEY (regi_id),
CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_catr_id FOREIGN KEY (catr_id) REFERENCES catraca (catr_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
CONSTRAINT fk_vinc_id FOREIGN KEY (vinc_id) REFERENCES vinculo(vinc_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 
)
;
CREATE TABLE unidade_turno
(
untu_id serial NOT NULL,
turn_id integer NOT NULL, 
unid_id integer NOT NULL, 
CONSTRAINT pk_untu_id PRIMARY KEY (untu_id), 
CONSTRAINT fk_turn_id FOREIGN KEY (turn_id) REFERENCES turno (turn_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_unid_id FOREIGN KEY (unid_id) REFERENCES unidade (unid_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 
);

CREATE TABLE custo_cartao
(
cuca_id serial NOT NULL, 
cuca_valor numeric(8,2), 
cuca_data timestamp without time zone,
CONSTRAINT pk_cuca_id PRIMARY KEY (cuca_id) 
);

CREATE TABLE custo_refeicao
(
cure_id serial NOT NULL, 
cure_valor numeric(8,2), 
cure_data timestamp without time zone, 
CONSTRAINT pk_cure_id PRIMARY KEY (cure_id) 
);

CREATE TABLE auditoria
( 
audi_id serial NOT NULL, 
audi_pagina character varying(200), 
audi_data timestamp without time zone, 
usua_id integer, 
audi_observacao character varying(200), 
CONSTRAINT pk_audi_id PRIMARY KEY (audi_id) 
);

CREATE TABLE app
( 
app_id bigint, 
app_token character varying(200), 
usua_id bigint, 
id_base_externa bigint, 
CONSTRAINT pk_app_id PRIMARY KEY (app_id), 
CONSTRAINT fk_usua_id FOREIGN KEY (usua_id) REFERENCES usuario(usua_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 	
);

CREATE TABLE vinculo_tipo
( 
viti_id serial NOT NULL, 
vinc_id integer, 
tipo_id integer, 
CONSTRAINT pk_viti_id PRIMARY KEY (viti_id),
CONSTRAINT fk_vinc_id FOREIGN KEY (vinc_id) REFERENCES vinculo(vinc_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION, 
CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo(tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 	 
); 

CREATE TABLE vw_usuarios_autenticacao_catraca
( 
	vw_usu_aut_id integer, 
	id_usuario integer, 
	nome character varying(300), 
	cpf_cnpj character varying(300), 
	passaporte character varying(300), 
	email character varying(300), 
	login character varying(300), 
	senha character varying(300), 
	siape integer, 
	id_status_servidor integer, 
	status_servidor character varying(30), 
	id_tipo_usuario integer, 
	tipo_usuario character varying(200), 
	id_categoria integer, 
	categoria character varying(200)
);

CREATE TABLE vw_usuarios_catraca
	( 
	vw_usu_cat_id integer, 
	id_usuario integer, 
	nome character varying(300), 
	identidade character varying(300), 
	cpf_cnpj character varying(300), 
	passaporte character varying(300), 
	email character varying(300), 
	login character varying(300), 
	senha character varying(300), 
	matricula_disc integer, 
	nivel_discente character varying(300), 
	id_status_discente integer, 
	status_discente character varying(300), 
	siape integer, 
	id_status_servidor integer, 
	status_servidor character varying(300), 
	id_tipo_usuario integer, 
	tipo_usuario character varying(300), 
	id_categoria integer, 
	status_sistema integer, 
	categoria character varying(300), 
	id_turno integer, 
	turno character varying(50), 
	id_curso integer, 
	nome_curso character varying(150)
);

CREATE TABLE validacao
(
	vali_id serial NOT NULL, 
	vali_campo character varying(300),
	vali_valor character varying(300), 
	tipo_id integer, 
	CONSTRAINT pk_vali_id PRIMARY KEY (vali_id),
	CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo(tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION 	 
);