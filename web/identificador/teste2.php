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

/*

$sql = "SELECT * FROM cartao WHERE cart_numero = '0401320170'";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){

	print_r($linha);
}
echo '<hr>';
$sql = "SELECT * FROM vinculo INNER JOIN cartao
ON cartao.cart_id = vinculo.cart_id
INNER JOIN 
vinculo_tipo ON vinculo_tipo.vinc_id = vinculo.vinc_id
WHERE cart_numero = '0401320170'";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){

	print_r($linha);
}
echo '<hr>';


$sql = "UPDATE vinculo set usua_id = 1
WHERE vinc_id = 173";
*/

$strCatr = "AND catr_id = 3";
$data1 = "2016-07-25 08:00:00";
$data2 = "2016-07-25 22:00:00";

$i = 0;
$sql = "SELECT * FROM registro INNER JOIN 
vinculo ON vinculo.vinc_id = registro.vinc_id
INNER JOIN 
usuario on vinculo.usua_id = usuario.usua_id";

//WHERE (registro.regi_data BETWEEN '$data1'	AND '$data2')  $strCatr	";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	$i++;
	//echo $linha['usua_nome'].$linha['regi_data'].'-'.$i.'<br>';
}

echo $i.' refeicoes<br>';


$i = 0;
$sql = "SELECT * FROM registro INNER JOIN
vinculo ON vinculo.vinc_id = registro.vinc_id
INNER JOIN
usuario on vinculo.usua_id = usuario.usua_id
WHERE (vinculo.vinc_avulso = TRUE)";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	$i++;
	//echo $linha['usua_nome'].$linha['regi_data'].'-'.$i.'<br>';
}

echo $i.' Clicks Avulsos <br>';


// $i = 0;
// $sql = "SELECT * FROM vinculo INNER JOIN 
// cartao ON cartao.cart_id = vinculo.cart_id
// INNER JOIN usuario ON vinculo.usua_id = usuario.usua_id
//  WHERE vinculo.vinc_avulso <> 'TRUE' ORDER BY vinc_inicio";
// $result = $dao->getConexao()->query($sql);
// foreach($result as $linha){
// 	$i++;
// 	//echo ' - '.$linha['cart_numero'].' - '.$linha['vinc_inicio'].' - '.$i.'<br>';
	
// }

// echo $i.' cadastros';
// echo '<br>';

// $sql = "SELECT * FROM auditoria
// 	INNER JOIN usuario ON auditoria.usua_id = usuario.usua_id
// 	 ORDER BY audi_id DESC LIMIT 100";
// $result = $dao->getConexao()->query($sql);
// foreach($result as $linha){
// 	echo $linha['audi_id'].' - '.$linha['usua_nome'].' - '.$linha['audi_pagina'].' - '.$linha['audi_data'].'<br>';
	
// }


echo '<br><br>';


$sql = "SELECT * FROM registro 
	INNER JOIN vinculo
	ON vinculo.vinc_id = registro.vinc_id
	INNER JOIN usuario
	ON usuario.usua_id = vinculo.vinc_id
	WHERE (registro.regi_data BETWEEN '$data1' AND '$data2') $strCatr
	ORDER BY regi_id DESC";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	
	if(!$linha['vinc_avulso'])
		echo $linha['regi_id'].' - '.$linha['regi_valor_custo'].' '.$linha['regi_data'].' Cliente: '.$linha['usua_nome'].'<br>';
	else{
		echo $linha['regi_id'].' - '.$linha['regi_valor_custo'].' '.$linha['regi_data'].' Cliente: AVULSO<br>';
	}
}





?>