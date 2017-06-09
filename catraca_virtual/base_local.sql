CREATE TABLE `sqlite_sequence` (
	`name`	TEXT,
	`seq`	TEXT
);

CREATE TABLE `tipo` (
	`tipo_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tipo_nome`	TEXT,
	`tipo_valor`	NUMERIC
);

CREATE TABLE `cartao` (
	`cart_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`cart_numero`	INTEGER,
	`cart_creditos`	NUMERIC,
	`tipo_id`	INTEGER
);

CREATE TABLE 
`usuario` 
(
	`usua_id` INTEGER PRIMARY KEY AUTOINCREMENT, 
	`usua_nome` TEXT, 
	`usua_email` TEXT, 
	`usua_login` TEXT, 
	`usua_senha` TEXT, 
	`usua_nivel` TEXT, 
	`id_base_externa` INTEGER 
);

CREATE TABLE `vinculo` (
	`vinc_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`vinc_avulso`	INTEGER,
	`vinc_inicio`	TEXT,
	`vinc_fim`	TEXT,
	`vinc_descricao`	TEXT,
	`vinc_refeicoes`	INTEGER,
	`cart_id`	INTEGER,
	`usua_id`	INTEGER
);

CREATE TABLE `vinculo_tipo` (
	`viti_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`vinc_id`	INTEGER,
	`tipo_id`	INTEGER
);

CREATE TABLE `catraca` (
	`catr_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`catr_nome`	TEXT,
	`catr_financeiro`	INTEGER
);

CREATE TABLE `unidade` (
	`unid_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`unid_nome`	TEXT
);
CREATE TABLE `catraca_unidade` (
	`caun_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`catr_id`	INTEGER,
	`unid_id`	INTEGER
);


CREATE TABLE `turno` (
	`turn_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`turn_hora_inicio`	TEXT,
	`turn_hora_fim`	TEXT,
	`turn_descricao`	TEXT
);

CREATE TABLE `unidade_turno` (
	`untu_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`turn_id`	INTEGER,
	`unid_id`	INTEGER
);


CREATE TABLE `custo_refeicao` (
	`cure_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`cure_valor`	NUMERIC,
	`cure_data`	TEXT
);

CREATE TABLE `custo_unidade` (
	`cuun_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`unid_id`	INTEGER,
	`cure_id`	INTEGER
);

CREATE TABLE `registro` (
	`regi_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`regi_data`	TEXT,
	`regi_valor_pago`	NUMERIC,
	`regi_valor_custo`	NUMERIC,
	`catr_id`	INTEGER,
	`catr_id`	INTEGER,
	`vinc_id`	INTEGER
);