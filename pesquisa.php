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

if (! ($sessao->getNivelAcesso () == Sessao::NIVEL_SUPER || $sessao->getNivelAcesso () == Sessao::NIVEL_ADMIN)) {
	exit ( 0 );
}




$dao = new DAO(null, DAO::TIPO_USUARIOS_2);

$pesquisador = new Pesquisador($dao->getConexao(), $dao->getEntidadeUsuarios(), 'NOME', $dao->getSgdb());
echo "BUSCAR USUARIOS PG: <br><br>";

$pesquisador->mostraformPesquisa();
$pesquisador->pesquisar();


echo "<br><br><hr>";

echo "BUSCAR USUARIOS SSQL: <br><br>";

$dao = new DAO(null, DAO::TIPO_USUARIOS);

$pesquisador = new Pesquisador($dao->getConexao(), $dao->getEntidadeUsuarios(), 'NOME', $dao->getSgdb());
echo "BUSCAR USUARIOS: <br><br>";
$pesquisador->pesquisar();

echo "<br><br><hr>";



echo "BUSCAR USUARIOS PG_CATRACA: <br><br>";

$dao = new DAO();


$pesquisador = new Pesquisador($dao->getConexao(), 'usuario', 'usua_nome', $dao->getSgdb());
echo "BUSCAR USUARIOS: <br><br>";

$pesquisador->pesquisar();

echo "<br><br><hr>";



