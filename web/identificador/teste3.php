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
$sessao = new Sessao ();

if (isset ( $_GET ["sair"] )) {
	
	$sessao->mataSessao ();
	header ( "Location:./index.php" );
}

	
$unidadeDao = new UnidadeDAO();

$lista  = $unidadeDao->retornaCatracasPorUnidade();
foreach($lista as $catraca){
	
	echo $catraca;
	echo '<br><hr>';
	
}

// echo $unidadeDao->getConexao()->exec("UPDATE catraca set catr_financeiro = 'TRUE';");

// $sql = "SELECT * FROM usuario 
// 		INNER JOIN vinculo ON vinculo.usua_id = usuario.usua_id 
// 		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id 
// 		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id 
// 		WHERE cartao.cart_numero = '3995578542' ";

// try {
// 	$db = $dao->getConexao();
// 	$stmt = $db->prepare($sql);
	
// 	$stmt->execute();
// 	$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
// 	foreach($result as $linha){
// 		print_r($linha);
// 		echo "<br><hr>";
		
// 	}	
// 	$db = null;
// 	echo '{"turno": ' . json_encode($dados) . '}';
// } catch(PDOException $e) {
// 	echo '{"erro":{"text":'. $e->getMessage() .'}}';
// }
