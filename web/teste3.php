<?php


ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

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

$sql = "SELECT * FROM usuario WHERE usua_nivel <> 1";

foreach($dao->getConexao()->query($sql) as $linha){

	echo $linha['usua_id'].$linha['usua_nome'].'<br>';

}





echo "<hr>";



$sql = "SELECT auditoria.* FROM auditoria 
INNER JOIN usuario 
ON usuario.usua_id = auditoria.usua_id
WHERE usuario.usua_id = 609
 LIMIT 100";

foreach($dao->getConexao()->query($sql) as $linha){

	print_r($linha);
	echo "<br>";

}

