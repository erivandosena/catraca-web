<?php

date_default_timezone_set ( 'America/Araguaina' );

ini_set ( 'display_errors', 1 );
ini_set ( 'display_startup_erros', 1 );
error_reporting ( E_ALL );
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

if($sessao->getNivelAcesso() != Sessao::NIVEL_SUPER)
	exit(0);


 $dao = new DAO(null, DAO::TIPO_PG_LOCAL);
$result = $dao->getConexao()->query("SELECT 
		cartao.cart_id, cartao.cart_numero, cartao.cart_creditos, tipo.tipo_valor, vinculo.vinc_refeicoes, tipo.tipo_id 
		FROM cartao INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id 
		INNER JOIN vinculo
		ON vinculo.cart_id = cartao.cart_id
		WHERE ('2015-11-26 11:19:00' BETWEEN vinculo.vinc_inicio AND vinculo.vinc_fim) AND (cartao.cart_numero = 3995148318)");
foreach($result as $linha){

	print_r($linha);
}
// NOME_TABELA_NOME_CAMPO _SEQ.
// echo 'LAST:'.$dao->getConexao()->lastInsertId('atividade_tipo_atti_id_seq');
?>



