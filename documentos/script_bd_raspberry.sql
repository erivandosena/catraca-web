/*
CREATE DATABASE raspberry WITH ENCODING='UTF8' CONNECTION LIMIT=-1;
*/

-- TABLE tipo
CREATE TABLE tipo
(
  tipo_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  tipo_nome character varying(16), -- Tipos comuns de utilizadores: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.
  tipo_vlr_credito numeric(8,2), -- Valor unitario de credito do cartao.
  CONSTRAINT pk_tipo_id PRIMARY KEY (tipo_id)
);
ALTER TABLE tipo OWNER TO postgres;
COMMENT ON TABLE tipo IS 'Tabela de tipo de portador do cartao.';
COMMENT ON COLUMN tipo.tipo_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN tipo.tipo_nome IS 'Tipos comuns de utilizadores: 1=Estudante, 2=Professor, 3=Tecnico, 4=Visitante, 5=Operador, 6=Administrador.';
COMMENT ON COLUMN tipo.tipo_vlr_credito IS 'Valor unitario de credito do cartao.';

-- TABLE perfil
CREATE TABLE perfil
(
  perf_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  perf_nome character varying(200), -- Nome completo do utilizador do cartao.
  perf_email character varying(150), -- E-mail do utilizador do cartao sem permissao de duplicidade.
  perf_tel character varying(15), -- Numero do telefone celular do utilizador.
  perf_datanascimento character varying(10), -- Mes e ano da data de nascimento.
  tipo_id integer NOT NULL, -- Campo para chave estrengeira da tabela tipo.
  CONSTRAINT pk_perf_id PRIMARY KEY (perf_id),
  CONSTRAINT fk_tipo_id FOREIGN KEY (tipo_id) REFERENCES tipo (tipo_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT u_perf_email UNIQUE (perf_email)
);
ALTER TABLE perfil OWNER TO postgres;
COMMENT ON COLUMN perfil.perf_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN perfil.perf_nome IS 'Nome completo do utilizador do cartao.';
COMMENT ON COLUMN perfil.perf_email IS 'E-mail do utilizador do cartao sem permissao de duplicidade.';
COMMENT ON COLUMN perfil.perf_tel IS 'Numero do telefone celular do utilizador.';
COMMENT ON COLUMN perfil.perf_datanascimento IS 'Mes e ano da data de nascimento.';
COMMENT ON COLUMN perfil.tipo_id IS 'Campo para chave estrangeira da tabela tipo.';

-- TABLE cartao
CREATE TABLE cartao
(
  cart_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  cart_numero bigint, -- Numero do ID do cartao de acesso sem permissao de duplicidade.
  cart_creditos integer, -- Quantidade de creditos para uso diario do cartao.
  perf_id integer NOT NULL, -- Campo para chave estrengeira da tabela perfil
  CONSTRAINT pk_cart_id PRIMARY KEY (cart_id),
  CONSTRAINT fk_perf_id FOREIGN KEY (perf_id) REFERENCES perfil (perf_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT u_cart_numero UNIQUE (cart_numero)
);
ALTER TABLE cartao OWNER TO postgres; 
COMMENT ON TABLE cartao IS 'Tabela dos registros de uso do Smart Card RFID.';
COMMENT ON COLUMN cartao.cart_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN cartao.cart_numero IS 'Numero do ID do cartao de acesso sem permissao de duplicidade.';
COMMENT ON COLUMN cartao.cart_creditos IS 'Quantidade de creditos para uso diario do cartao.';
COMMENT ON COLUMN cartao.perf_id IS 'Campo para chave estrangeira da tabela perfil';

-- TABLE turno
CREATE TABLE turno
(
  turn_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  turn_hora_inicio time without time zone, -- Hora inicio do periodo para liberacao da catraca.
  turn_hora_fim time without time zone, -- Hora final do periodo para liberacao da catraca.
  turn_data timestamp without time zone, -- Data para o periodo da liberacao da catraca.
  turn_continuo integer DEFAULT 0, -- Define a forma de liberacao dos turnos: 0=Continuo, 1=por data exclusiva.
  CONSTRAINT pk_turn_id PRIMARY KEY (turn_id)
);
ALTER TABLE turno OWNER TO postgres;
COMMENT ON COLUMN turno.turn_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN turno.turn_hora_inicio IS 'Hora inicio do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_hora_fim IS 'Hora final do periodo para liberacao da catraca.';
COMMENT ON COLUMN turno.turn_data IS 'Data para o periodo da liberacao da catraca.';
COMMENT ON COLUMN turno.turn_continuo IS 'Define a forma de liberacao dos turnos: 0=Continuo, 1=por data exclusiva.';

-- Table giro
CREATE TABLE giro
(
  giro_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  giro_giros_horario integer DEFAULT 0, -- Contador de giros no sentido horario(Entrada).
  giro_giros_antihorario integer DEFAULT 0, -- Contador de giros no sentido anti-horario(Saida).
  giro_data_giro time without time zone NOT NULL DEFAULT now(), -- Data/hora da ocorrencia do giro.
  CONSTRAINT pk_giro_id PRIMARY KEY (giro_id )
);
ALTER TABLE giro OWNER TO postgres;
COMMENT ON TABLE giro IS 'Tabela de contabilizacao de giros horario e anti-horario.';
COMMENT ON COLUMN giro.giro_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN giro.giro_giros_horario IS 'Contador de giros no sentido horario(Entrada).';
COMMENT ON COLUMN giro.giro_giros_antihorario IS 'Contador de giros no sentido anti-horario(Saida).';
COMMENT ON COLUMN giro.giro_data_giro IS 'Data/hora da ocorrencia do giro.';

-- Table mensagem
CREATE TABLE mensagem
(
  mens_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  mens_inicializacao character varying(34), -- Texto de inicializacao da catraca.
  mens_saldacao character varying(34), -- Texto de saldacao na catraca.
  mens_aguardacartao character varying(34), -- Texto solicitando o uso do cartao na catraca.
  mens_erroleitor character varying(34), -- Texto de erro na leitura do cartao na catraca.
  mens_bloqueioacesso character varying(34), -- Texto de acesso bloqueado na catraca.
  mens_liberaacesso character varying(34), -- Texto de acesso liberado na catraca.
  mens_semcredito character varying(34), -- Texto de cartao sem creditos.
  mens_semcadastro character varying(34), -- Texto de cartao nao cadastrado no sistema.
  mens_cartaoinvalido character varying(34), -- Texto de cartao que nao atende a todos os criterios de uso na catraca.
  mens_turnoinvalido character varying(34), -- Texto de uso do cartao fora da faixa de horarios do turno.
  mens_datainvalida character varying(34), -- Texto de dias nao uteis para uso da catraca.
  mens_cartaoutilizado character varying(34), -- Texto para cartao ja utilizado na catraca dentro do turno.
  mens_institucional1 character varying(34), -- Texto 01 livre para avisos, informes, etc.
  mens_institucional2 character varying(34), -- Texto 02 livre avisos, informes, etc.
  mens_institucional3 character varying(34), -- Texto 03 livre avisos, informes, etc.
  mens_institucional4 character varying(34), -- Texto 04 livre avisos, informes, etc.
  CONSTRAINT pk_mens_id PRIMARY KEY (mens_id )
);
ALTER TABLE mensagem OWNER TO postgres;
COMMENT ON TABLE mensagem IS 'Tabela de mensagens para exibicao em display LCD de 2 linhas de 16 caracteres.';
COMMENT ON COLUMN mensagem.mens_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
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

-- Inclui mensagens default na tabela mensagem
INSERT INTO mensagem(mens_inicializacao, mens_saldacao, mens_aguardacartao, 
            mens_erroleitor, mens_bloqueioacesso, mens_liberaacesso, mens_semcredito, 
            mens_semcadastro, mens_cartaoinvalido, mens_turnoinvalido, mens_datainvalida, 
            mens_cartaoutilizado, mens_institucional1, mens_institucional2, 
            mens_institucional3, mens_institucional4) 
            VALUES ('Iniciando...','   BEM-VINDO!','   APROXIME\n   SEU CARTAO','APROXIME CARTAO\n  NOVAMENTE...',
            '     ACESSO\n   BLOQUEADO!','     ACESSO\n    LIBERADO!','     CARTAO\n   SEM SALDO!',
            '     CARTAO\n NAO CADASTRADO!','     CARTAO\n  INVALIDO!','FORA DO HORARIO\n DE ATENDIMENTO',
            '  DIA NAO UTIL\nPARA ATENDIMENTO','CARTAO JA USADO\nPARA 01 REFEICAO','    UNILAB - Unilab.edu.br',
            'Desenvolvido por\n  DISUP | DTI','      RU\n   Liberdade','      BOM\n    APETITE!');

-- TABLE catraca
CREATE TABLE catraca
(
  catr_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  catr_ip character varying(12), -- Numero IP da catraca.
  catr_localizacao character varying(16), -- Nome do local de instalacao da catraca.
  catr_tempo_giro integer, -- Tempo para o giro do braço da catraca em milissegundos.
  catr_operacao integer, -- 1=Giro Horario(Entrada controlada com saida bloqueada),2=Giros Horario/Anti-horario(Entrada controlada com saida liberada),3=Giros Horario/Anti-horario(Entrada e saida liberadas).
  giro_id integer NOT NULL, -- Campo para chave estrangeira da tabela giro.
  turn_id integer NOT NULL, -- Campo para chave estrangeira da tabela turno.
  mens_id integer NOT NULL, -- Campo para chave estrangeira da tabela mensagem.
  CONSTRAINT pk_catr_id PRIMARY KEY (catr_id ),
  CONSTRAINT fk_giro_id FOREIGN KEY (giro_id) REFERENCES giro (giro_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_mens_id FOREIGN KEY (mens_id) REFERENCES mensagem (mens_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_turn_id FOREIGN KEY (turn_id) REFERENCES turno (turn_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
);
ALTER TABLE catraca OWNER TO postgres;
COMMENT ON TABLE catraca IS 'Tabela de predefinicoes e configuracoes para o funcionamento da catraca.';
COMMENT ON COLUMN catraca.catr_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN catraca.catr_localizacao IS 'Nome do local de instalacao da catraca.';
COMMENT ON COLUMN catraca.catr_tempo_giro IS 'Tempo para o giro do braço da catraca em milissegundos.';
COMMENT ON COLUMN catraca.giro_id IS 'Campo para chave estrangeira da tabela giro.';
COMMENT ON COLUMN catraca.turn_id IS 'Campo para chave estrangeira da tabela turno.';
COMMENT ON COLUMN catraca.mens_id IS 'Campo para chave estrangeira da tabela mensagem.';
COMMENT ON COLUMN catraca.catr_ip IS 'Numero IP da catraca.';
COMMENT ON COLUMN catraca.catr_operacao IS '1=Giro Horario(Entrada controlada com saida bloqueada),2=Giros Horario/Anti-horario(Entrada controlada com saida liberada),3=Giros Horario/Anti-horario(Entrada e saida liberadas).';

-- TABLE registro
CREATE TABLE registro
(
  regi_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  regi_datahora timestamp without time zone, -- Data/hora da utilizacao do cartao na catraca.
  regi_giro integer NOT NULL DEFAULT 0, -- Confirmacao de efetivacao de giro na catraca.
  regi_valor numeric(8,2) NOT NULL, -- Valor referente a refeicao.
  cart_id integer NOT NULL, -- Campo para chave estrangeira da tabela cartao.
  CONSTRAINT pk_regi_id PRIMARY KEY (regi_id ),
  CONSTRAINT fk_cart_id FOREIGN KEY (cart_id) REFERENCES cartao (cart_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
);
ALTER TABLE registro OWNER TO postgres;
COMMENT ON TABLE registro IS 'Tabela de registros de uso do cartao na catraca.';
COMMENT ON COLUMN registro.regi_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN registro.regi_datahora IS 'Data/hora da utilizacao do cartao na catraca.';
COMMENT ON COLUMN registro.regi_giro IS 'Confirmacao de efetivacao de giro na catraca.';
COMMENT ON COLUMN registro.regi_valor IS 'Valor em R$ referente a refeicao.';
COMMENT ON COLUMN registro.cart_id IS 'Campo para chave estrangeira da tabela cartao.';

-- TABLE usuario
CREATE TABLE usuario
(
  usua_id serial NOT NULL, -- Campo autoincremento destinado para chave primaria da tabela.
  usua_nome character varying(200), -- Nome completo do utilizador do cartao.
  usua_email character varying(150), -- E-mail do utilizador do cartao sem permissao de duplicidade.
  usua_login character varying(50), -- Nome de usuario do utilizador do cartao.
  usua_senha character varying(50), -- Senha de usuario do utilizador do cartao.
  usua_nivel integer, -- Nivel de acesso ao sistema do utilizador do cartao.
  CONSTRAINT pk_usua_id PRIMARY KEY (usua_id),
  CONSTRAINT u_usua_email UNIQUE (usua_email)
);
ALTER TABLE usuario OWNER TO postgres;
COMMENT ON TABLE usuario IS 'Tabela de usuario do cartao para acesso na catraca.';
COMMENT ON COLUMN usuario.usua_id IS 'Campo autoincremento destinado para chave primaria da tabela.';
COMMENT ON COLUMN usuario.usua_nome IS 'Nome completo do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_email IS 'E-mail do utilizador do cartao sem permissao de duplicidade.';
COMMENT ON COLUMN usuario.usua_login IS 'Nome de usuario do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_senha IS 'Senha de usuario do utilizador do cartao.';
COMMENT ON COLUMN usuario.usua_nivel IS 'Nivel de acesso ao sistema do utilizador do cartao.';

