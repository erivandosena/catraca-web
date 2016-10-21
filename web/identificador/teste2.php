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



$dao = new DAO();

$result = $dao->getConexao()->query("SELECT * FROM vinculo_tipo 
		WHERE tipo_id = 9
		");

foreach($result as $linha){
	echo $linha['viti_id'];
	echo '<hr>';
}//10504


$result = $dao->getConexao()->query("SELECT * FROM cartao
		INNER JOIN vinculo 
		ON vinculo.cart_id = cartao.cart_id
		INNER JOIN usuario
		ON vinculo.usua_id = usuario.usua_id
		WHERE tipo_id = 9
		");

foreach($result as $linha){
	echo $linha['usua_nome'];
	echo $linha['cart_numero'];
	echo '<hr>';
}//10504



// echo $dao->getConexao()->exec("DELETE FROM tipo WHERE tipo_id = 9 ");

// echo $dao->getConexao()->exec("UPDATE cartao 
// 		SET tipo_id = 8
// 		WHERE tipo_id = 9");

// echo $dao->getConexao()->exec("UPDATE vinculo_tipo
// 		SET tipo_id = 8
// 		WHERE tipo_id = 9");




?>