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






$sql = "SELECT * FROM auditoria
	INNER JOIN usuario ON auditoria.usua_id = usuario.usua_id
	 ORDER BY audi_id DESC LIMIT 3000";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	
	echo $linha['audi_id'].' - '.$linha['usua_nome'].' - '.$linha['audi_pagina'].' - '.date("d/m/Y H:i:s", strtotime($linha['audi_data']));
	if($linha['usua_nivel'] > 1)		
		echo ' <b> '.$linha['usua_nivel'].'</b>';
	else
		echo ' Comum';
	echo '<hr>';
	
}


