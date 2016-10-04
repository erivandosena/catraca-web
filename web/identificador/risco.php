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



$sql =  "SELECT * FROM vinculo
INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id
INNER JOIN cartao ON cartao.cart_id = vinculo.cart_id
INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id

WHERE cart_numero = '0866174378'
";
$result = $dao->getConexao ()->query ($sql);
foreach($result as $linha){
	echo $linha['cart_numero'].' '. $linha['vinc_id'].' ';
	print_r($linha);	

}






//echo $dao->getConexao()->exec("UPDATE vinculo set vinc_fim = '2016-10-14 08:00:00' WHERE vinc_id = 4087");



//echo $dao->getConexao()->exec("UPDATE vinculo set vinc_refeicoes = 80 WHERE vinc_id = 4106");
