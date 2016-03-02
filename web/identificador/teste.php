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



// $dao = new DAO();

// $sql = "SELECT * FROM cartao INNER JOIN vinculo  ON cartao.cart_id = vinculo.cart_id";
// $result = $dao->getConexao()->query($sql);

// foreach($result as $linha){
// 	$vinc_id = $linha['vinc_id'];
// 	$idTipo = $linha['tipo_id'];
// 	$sqlInsert = "INSERT INTO vinculo_tipo (vinc_id, tipo_id) VALUES($vinc_id, $idTipo)";
// 	if($dao->getConexao()->exec($sqlInsert))
// 		echo "Inseriu";
// 	else
// 		echo "nao inseriu";
	
	
// }


?>
