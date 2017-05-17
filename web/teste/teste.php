<?php

ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

date_default_timezone_set ( 'America/Araguaina' );


function __autoload($classe) {
	if (file_exists ( '../classes/dao/' . $classe . '.php' ))
		include_once '../classes/dao/' . $classe . '.php';
		if (file_exists ( '../classes/model/' . $classe . '.php' ))
			include_once '../classes/model/' . $classe . '.php';
			if (file_exists ( '../classes/controller/' . $classe . '.php' ))
				include_once '../classes/controller/' . $classe . '.php';
				if (file_exists ( '../classes/util/' . $classe . '.php' ))
					include_once '../classes/util/' . $classe . '.php';
					if (file_exists ( '../classes/view/' . $classe . '.php' ))
						include_once '../classes/view/' . $classe . '.php';
}

$sessao = new Sessao ();

if (isset ( $_GET ["sair"] )) {

	$sessao->mataSessao ();
	header ( "Location:./index.php" );
}



try{


	$dao = new DAO();
	
	
	$dataReferencia = date ( "Y-m-d G:i:s" );
	$sqlS = "SELECT * FROM usuario
			INNER JOIN vinculo ON
			vinculo.usua_id = usuario.usua_id
			INNER JOIN cartao ON
			cartao.cart_id = vinculo.cart_id
			INNER JOIN isencao ON
			isencao.cart_id = cartao.cart_id
			WHERE ('$dataReferencia' BETWEEN isen_inicio AND isen_fim)
			LIMIT 500
			
			";
	
	echo $sqlS;

	$result = $dao->getConexao()->query($sqlS);
	echo '<table border="1">';
	foreach($result as $linha){
		echo '<tr>';
		echo '<td>'.$linha['usua_nome'].' </td><td>  '.$linha['isen_inicio'].' </td> <td>'.$linha['isen_fim'].'</td><td>'.$linha['cart_numero'].'</td>';
		echo '</tr>';
	}
	
	
}catch (PDOException $e){
	echo $e->getMessage();
}
