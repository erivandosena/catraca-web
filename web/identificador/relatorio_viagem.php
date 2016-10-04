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









$dao = new VinculoDAO();



$data1 = '2016-10-01 01:00:00';
$data2 = '2016-10-01 14:00:00';
$sql =  "SELECT * FROM registro 
	INNER JOIN vinculo ON registro.vinc_id = vinculo.vinc_id
	WHERE regi_data BETWEEN '$data1' AND '$data2'
	AND regi_valor_pago = 0";
$result = $dao->getConexao ()->query ($sql);
foreach($result as $linha){
		
	print_r($linha);

}




