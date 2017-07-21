<?php
ini_set ( 'display_errors', 1 );
ini_set ( 'display_startup_erros', 1 );
error_reporting ( E_ALL );

date_default_timezone_set ( 'America/Araguaina' );

function __autoload($classe) {
	if (file_exists ( 'classes/dao/' . $classe . '.php' ))
		include_once 'classes/dao/' . $classe . '.php';
		if (file_exists ( 'classes/model/' . $classe . '.php' ))
			include_once 'classes/model/' . $classe . '.php';
			if (file_exists ( 'classes/controller/' . $classe . '.php' ))
				include_once 'classes/controller/' . $classe . '.php';
				if (file_exists ( 'classes/util/' . $classe . '.php' ))
					include_once 'classes/util/' . $classe . '.php';
					if (file_exists ( 'classes/view/' . $classe . '.php' ))
						include_once 'classes/view/' . $classe . '.php';
}

$sessao = new Sessao ();

if (isset ( $_GET ["sair"] )) {

	$sessao->mataSessao ();
	header ( "Location:./index.php" );
}

if(!($sessao->getNivelAcesso() == Sessao::NIVEL_SUPER || $sessao->getNivelAcesso() == Sessao::NIVEL_ADMIN)){
	exit(0);
}


$dao = new DAO();


$dao->getConexao()->query("CREATE TABLE vw_usuarios_autenticacao_catraca
( 
	vw_usu_aut_id integer, 
	id_usuario bigint, 
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
);");

AdminPG::main();

