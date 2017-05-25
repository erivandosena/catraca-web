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

if($sessao->getNivelAcesso() != Sessao::NIVEL_ADMIN){
	exit(0);
	
}

$dao = new DAO();


echo "<br><br>";

// $sqlUpdate = "UPDATE registro
// 		set regi_data = '2017-05-20 12:00:00'
// 		WHERE regi_id > 154207

// 		";

// echo $dao->getConexao()->exec($sqlUpdate);

// echo '<br><br>';


// $result = $dao->getConexao()->query("SELECT * FROM registro 
// 		WHERE regi_id > 154207
// 		ORDER BY regi_id DESC LIMIT 102 ");
// foreach($result as $linha){
// 	print_r($linha);
// 	echo '<br>';
	
	
// }


