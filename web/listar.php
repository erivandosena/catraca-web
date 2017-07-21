<?php

date_default_timezone_set ( 'America/Araguaina' );
ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

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
	echo "Nivel de acesso Não permitido: ".$sessao->getNivelAcesso();
	exit(0);
}




//Criar uma tabela. 

$sql = file_get_contents("tabelas.sql");
// echo $sql;

// $dao = new DAO();
// $dao->getConexao()->exec($sql);



// AdminPG::main();
