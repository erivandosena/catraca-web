-----------------------------------------------------------------------------
-- Autor_script : Erivando Sena
-- Copyright    : Unilab
-- Data_criacao : 16/10/2015
-- Data_revisao : 04/11/2015
-- Status       : Desenvolvimento
-- Desccricao	: Popula tabelas utilizadas pela catraca com dados ficticios.
-----------------------------------------------------------------------------

-- tipo
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Estudante', 1.10);
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Professor', 2.20);
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Técnico', 1.60);
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Terceirizado', 1.60);
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Professor', 2.20);
INSERT INTO tipo(tipo_nome, tipo_valor) VALUES ('Visitante', 4.00);

-- custo_refeicao
INSERT INTO custo_refeicao(cure_valor, cure_data) VALUES (8.90, '2014-01-01');
INSERT INTO custo_refeicao(cure_valor, cure_data) VALUES (9.90, '2015-01-01');

-- cartao
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3995148318, 48.40, 1);
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3994092782, 96.80, 2);
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3994233022, 70.40, 3);
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3995295262, 70.40, 4);
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3994110398, 176.40, 5);
INSERT INTO cartao(cart_numero, cart_creditos, tipo_id)VALUES (3994142734, 0.00, 6);

-- isencao
INSERT INTO isencao(isen_inicio, isen_fim, cart_id) VALUES ('2015-11-01 11:00:00', '2015-12-31 19:30:00', 5);

-- unidade
INSERT INTO unidade(unid_nome) VALUES ('RU Campus da Liberdade');
INSERT INTO unidade(unid_nome) VALUES ('RU Campus dos Palmares');

-- catraca
INSERT INTO catraca(catr_ip, catr_tempo_giro, catr_operacao, catr_nome) VALUES ('10.5.2.253', 20, 2, 'RULIBERDADE01');
INSERT INTO catraca(catr_ip, catr_tempo_giro, catr_operacao, catr_nome) VALUES ('10.5.2.252', 20, 1, 'RULIBERDADE02');
INSERT INTO catraca(catr_ip, catr_tempo_giro, catr_operacao, catr_nome) VALUES ('10.11.20.252', 20, 1, 'RUPALMARES01');
INSERT INTO catraca(catr_ip, catr_tempo_giro, catr_operacao, catr_nome) VALUES ('10.11.20.251', 20, 3, 'RUPALMARES02');

-- catraca_unidade
INSERT INTO catraca_unidade(catr_id, unid_id) VALUES (1, 1);
INSERT INTO catraca_unidade(catr_id, unid_id) VALUES (2, 1);
INSERT INTO catraca_unidade(catr_id, unid_id) VALUES (3, 2);
INSERT INTO catraca_unidade(catr_id, unid_id) VALUES (4, 2);

-- turno
INSERT INTO turno(turn_hora_inicio, turn_hora_fim, turn_descricao)VALUES ('11:00:00', '13:30:00', 'Almoço');
INSERT INTO turno(turn_hora_inicio, turn_hora_fim, turn_descricao)VALUES ('17:30:00', '19:30:00', 'Janta');
INSERT INTO turno(turn_hora_inicio, turn_hora_fim, turn_descricao)VALUES ('17:30:00', '19:00:00', 'Janta');

-- turno_unidade
INSERT INTO unidade_turno(turn_id, unid_id)VALUES (1, 1);
INSERT INTO unidade_turno(turn_id, unid_id)VALUES (2, 1);
INSERT INTO unidade_turno(turn_id, unid_id)VALUES (1, 2);
INSERT INTO unidade_turno(turn_id, unid_id)VALUES (3, 2);

-- usuario
INSERT INTO usuario(usua_nome, usua_email, usua_login, usua_senha, usua_nivel, id_base_externa) VALUES ('Erivando Sena Ramos', 'erivandoramos@unilab.edu.br', 'erivandoramos', '87435767901e0b0bb649c3b2b8351308', 1, 1976);
INSERT INTO usuario(usua_nome, usua_email, usua_login, usua_senha, usua_nivel, id_base_externa) VALUES ('Tino Tamba', 'tinot@unilab.edu.br', 'tino', 'fb17b173788d5d0952f36ef0b953ccb5', 0, 2015);

-- vinculo
INSERT INTO vinculo(vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao, vinc_refeicoes, cart_id, usua_id) VALUES (TRUE, '2015-11-01 11:00:00', '2015-12-31 19:30:00', 'Bolsista tutor de calouros', 15, 1, 2);

