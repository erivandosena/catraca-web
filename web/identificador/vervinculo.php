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


$dao = new DAO();
$result = $dao->getConexao()->query("SELECT * FROM vinculo INNER JOIN 
		cartao ON 
		vinculo.cart_id = cartao.cart_id 
		INNER JOIN usuario ON vinculo.usua_id = usuario.usua_id
		WHERE cart_numero = '399500147F'");




foreach($result as $linha){
	
	print_r($linha);
	echo '<br><hr>';
	
	
}

$sql= "SELECT * FROM usuario WHERE usua_id = 3951";
echo '<br><br><hr>';
foreach($dao->getConexao()->query($sql) as $eh){
	echo '<hr>';
	print_r($eh);

}

// echo $dao->getConexao()->exec("UPDATE cartao set cart_numero = '399500147F' WHERE cart_numero = '3995001470'");
