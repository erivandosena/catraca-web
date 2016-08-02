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

if ($sessao->getNivelAcesso () != Sessao::NIVEL_SUPER){
	exit ( 0 );
}
	



// $sql = "SELECT distinct turno.turn_id, turno.turn_hora_inicio, turno.turn_hora_fim, turno.turn_descricao FROM turno
// 			INNER JOIN unidade_turno ON turno.turn_id = unidade_turno.turn_id
// 			INNER JOIN catraca_unidade ON unidade_turno.unid_id = catraca_unidade.unid_id
// 			INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id WHERE catraca.catr_ip = :ip
// 			AND turno.turn_hora_inicio <= :hora_ini
// 			AND turno.turn_hora_fim >= :hora_fim;";

// try {
// 	$db = getDB();
// 	$stmt = $db->prepare($sql);
// 	$stmt->bindParam(":ip", sprintf(long2ip($ip)), PDO::PARAM_STR);
// 	$stmt->bindParam(":hora_ini", $hora, PDO::PARAM_STR);
// 	$stmt->bindParam(":hora_fim", $hora, PDO::PARAM_STR);
// 	$stmt->execute();
// 	$dados = $stmt->fetchAll(PDO::FETCH_OBJ);
// 	$db = null;
// 	echo '{"turno": ' . json_encode($dados) . '}';
// } catch(PDOException $e) {
// 	echo '{"erro":{"text":'. $e->getMessage() .'}}';
// }


$dao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
$lista = $dao->pesquisaTesteNoSigaa("JOão");

foreach($lista as $usuario){
	echo '<hr>';
	echo $usuario->getNome();
	echo "<hr><br><hr>";
	
	
}