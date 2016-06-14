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

$tipoDao = new TipoDAO($dao->getConexao());
foreach ($tipoDao->retornaLista() as $tipo){
	
	$idTipo = $tipo->getId();
	$sql = "SELECT * FROM cartao
	INNER JOIN vinculo ON cartao.cart_id = vinculo.cart_id
	WHERE tipo_id = $idTipo
	AND vinculo.vinc_avulso = 'TRUE'
	LIMIT 1";
	
	$result = $dao->getConexao()->query($sql);
	
	foreach($result as $linha){
		echo $linha['cart_id'].' - '.$linha['cart_numero'].' - '.$tipo->getNome().'<br>';
	}	
	
	
}

echo '<br><br><br>';

/*
 * Como faço para corrigir os erros? 
 * Tenho pegar registros que se repetiram no turno. 
 * 
 * 
 */

$sql = "
		";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	
	print_r($linha);
	echo '<hr>';
	
	
}
