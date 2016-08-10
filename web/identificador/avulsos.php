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


$lista = array();
$nomeUsuario = null;
$dataReferencia = null;
if($dataReferencia == null)
	$dataReferencia = date ( "Y-m-d G:i:s" );
$outroFiltro = "";
if($nomeUsuario != null){
	$nomeUsuario = preg_replace ('/[^a-zA-Z0-9\s]/', '', $nomeUsuario);
	$nomeUsuario = strtoupper ( $nomeUsuario );
	$outroFiltro = "AND usua_nome LIKE '%$nomeUsuario%'";
}

$sql =  "SELECT * FROM usuario INNER JOIN vinculo
ON vinculo.usua_id = usuario.usua_id
LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id

WHERE '$dataReferencia' BETWEEN vinc_inicio AND vinc_fim  $outroFiltro";
$result = $dao->getConexao ()->query ($sql);
foreach($result as $linha){
		
	$vinculo = new Vinculo();
	$vinculo->setId($linha['vinc_id']);
	$vinculo->getCartao()->setTipo(new Tipo());
	$vinculo->getResponsavel()->setId($linha['usua_id']);
	$vinculo->getResponsavel()->setNome($linha['usua_nome']);
	$vinculo->getResponsavel()->setIdBaseExterna($linha['id_base_externa']);
	$vinculo->getCartao()->setId($linha['cart_id']);
	$vinculo->getCartao()->getTipo()->setNome($linha ['tipo_nome']);
	$vinculo->getCartao()->setNumero($linha ['cart_numero']);
	$vinculo->setInicioValidade($linha ['vinc_inicio']);
	$vinculo->setFinalValidade($linha['vinc_fim']);
	$vinculo->setAvulso($linha['vinc_avulso']);
	$lista[] = $vinculo;
	

}



// echo '<table border="1">';
// echo '<tr><th>Avulso</th><tr>';
$i = 0;
foreach($lista as $vinculo){
	
// 	echo '<tr>';
// 	echo '<td>'.$vinculo->isAvulso().'<td>';
// 	echo '<td>'.$vinculo->getResponsavel()->getNome().'</td>';
// 	echo '</tr>';
	$i++;
	
}

// echo '</table>';

echo $i;