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

	

$dao = new CatracaVirtualDAO();
if($turnoAtual = $dao->retornaTurnoAtual()){
	echo 'Turno Ativo';
	
}
else{
	
	echo "Turno Inativo";
	exit(0);
	
}

$cartao = new Cartao();
$cartao->setNumero("3994113038");
$vinculo = new Vinculo();
$vinculo->setCartao($cartao);
echo '<br>';
if($dao->verificaVinculo($vinculo)){
	echo '<br>Cartao Tem vinculo<br>';
}
else{
	echo "<br>Cartao Nao tem vinculo<br>";
	//A gente renova se for proprio. 
	
}
echo '<hr>';
if($dao->podeContinuarComendo($vinculo, $turnoAtual)){
	echo 'POde';
}else{
	echo 'Pode nao';
}
if($dao->vinculoEhIsento($vinculo))
	echo "<hr>ISento<hr>";//Valor pago eh zero. //Valor de custo depende da unidade academica. 
else
	echo '<hr>Nao isento<hr>';


?>