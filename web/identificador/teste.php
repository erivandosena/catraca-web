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


$i = 0;
$sql = "SELECT * FROM registro INNER JOIN 
vinculo ON vinculo.vinc_id = registro.vinc_id
INNER JOIN 
usuario on vinculo.usua_id = usuario.usua_id";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	$i++;
	//echo $linha['usua_nome'].$linha['regi_data'].'-'.$i.'<br>';
}

echo $i.' refeicoes<br>';

$i = 0;
$sql = "SELECT * FROM vinculo INNER JOIN 
cartao ON cartao.cart_id = vinculo.cart_id
INNER JOIN usuario ON vinculo.usua_id = usuario.usua_id
 WHERE vinculo.vinc_avulso <> 'TRUE' ORDER BY vinc_inicio";
$result = $dao->getConexao()->query($sql);
foreach($result as $linha){
	$i++;
	echo ' - '.$linha['cart_numero'].' - '.$linha['vinc_inicio'].' - '.$i.'<br>';

}

echo $i.' cadastros';


$sql = "UPDATE usuario set 
	usua_nivel = 3 
	WHERE usua_login = 'marcosv'";
echo $dao->getConexao()->exec($sql);





?>
