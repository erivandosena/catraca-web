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



// if (($handle = fopen ( "lista.csv", "r" )) !== FALSE) {
// 	$row = 0;
// 	while ( ($data = fgetcsv ( $handle, 1000, "," )) !== FALSE ) {
// 		$num = count ( $data );
// 		for($c = 0; $c < $num; $c ++) {
// 			if($data[$c] == null){
// 				echo "Pulou<br>";
// 				continue;
// 			}
// 			$row++;
// 			$cartao = new Cartao();
// 			$cartao->setNumero($data[$c]);
// 			$cartoes[] = $cartao;
// 		}
// 	}
// 	fclose ( $handle );
// }

$dao = new CartaoDAO();
foreach($dao->retornaListaTotal() as $cartao){
// 	$cartoes[] = $cartao;
	echo $cartao->getNumero();
	echo '<br>';
}


