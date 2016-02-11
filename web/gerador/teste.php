<?php
date_default_timezone_set ( 'America/Araguaina' );

ini_set ( 'display_errors', 1 );
ini_set ( 'display_startup_erros', 1 );
error_reporting ( E_ALL );
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


// $dao = new DAO(NULL, DAO::TIPO_PG_LOCAL);

// if($dao->getConexao()->exec("INSERT INTO catraca(catr_ip, catr_tempo_giro, catr_operacao, catr_nome)VALUES('Tablet', 25, 2, 'Manual Via Tablet')"))
// 	echo "Adicionei o tai";

// $result = $dao->getConexao()->query("Select * FROM tipo");
// foreach($result as $linha){
	
// 	print_r($linha);
	
// }

?>