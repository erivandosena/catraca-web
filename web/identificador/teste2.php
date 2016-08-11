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




$sql = "SELECT * FROM registro WHERE(registro.regi_data BETWEEN '2016-08-11 13:30:00' AND '2016-08-11 16:55:00')
		AND (registro.cart_id = 15) 
		ORDER BY registro.regi_id DESC LIMIT 1;";
try{
	$stmt = $dao->getConexao()->prepare($sql);
	$stmt->execute();
	$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		
}catch (PDOException $e){
	echo '{"erro":{"text":'. $e->getMessage() .'}}';
}
foreach($result as $linha){
	print_r($linha);
}




?>