<?php

ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

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

/*
 * Combo dinamico do relatório.
 */

if (isset($_GET['unidade'])){
	$dao = new DAO();
	$idUnidade = $_GET['unidade'];
	$sql = "SELECT * FROM catraca
	INNER JOIN catraca_unidade ON catraca_unidade.catr_id = catraca.catr_id
	INNER JOIN unidade ON unidade.unid_id = catraca_unidade.unid_id
	WHERE unidade.unid_id = $idUnidade";
	$result = $dao->getConexao()->query($sql);
	$option = '<option value="">Selecione uma Catraca</option>';
	foreach ($result as $linha){
		$option .= '<option value="'.$linha['catr_id'].'">'.$linha['catr_nome'].'</option>';
	}	
	print $option;
	return ;
}

// if (isset($_GET['catraca_id'])){
// 	$dao = new DAO();
// 	$idCatraca = $_GET['catraca_id'];
// 	$sql = "SELECT * FROM turno
// 			INNER JOIN unidade_turno ON unidade_turno.turn_id = turno.turn_id
// 			INNER JOIN unidade ON unidade.unid_id = unidade_turno.unid_id
// 			INNER JOIN catraca_unidade ON catraca_unidade.unid_id = unidade.unid_id
// 			WHERE catraca_unidade.catr_id = $idCatraca";
// 	$result = $dao->getConexao()->query($sql);
// 	$option = '<option value="">Selecione um Turno</option>';
// 	foreach ($result as $linha){
// 		$option .= '<option value="'.$linha['turn_id'].'">'.$linha['turn_descricao'].'</option>';
// 	}
// 	print $option;
// 	return ;
// }

/*
 * Combo dinamico da tela de mensagens.
 */
// if (isset($_GET['catraca'])){	
// 	$idCatraca = $_GET['catraca'];
// 	$idUnidade = $_GET['unidade'];
// 	$i = 0;
// 	$dao = new DAO();
// 	$view = new DefinicoesView();
	
// 	$sql = "SELECT * FROM catraca
// 	INNER JOIN catraca_unidade ON catraca_unidade.catr_id = catraca.catr_id
// 	INNER JOIN unidade ON unidade.unid_id = catraca_unidade.unid_id
// 	WHERE unidade.unid_id = $idUnidade AND catraca.catr_id = $idCatraca";
	
// 	$result = $dao->getConexao()->query($sql);
// 	foreach ($result as $linha){
// 		$nomeCatraca = $linha['catr_nome'];
// 		$nomeUnidade = $linha['unid_nome'];
// 	}
	
// 	$sql = "SELECT * FROM mensagem
// 			INNER JOIN catraca_unidade ON catraca_unidade.catr_id = mensagem.catr_id
// 			INNER JOIN unidade ON unidade.unid_id = catraca_unidade.unid_id
// 			INNER JOIN catraca ON catraca_unidade.catr_id = catraca.catr_id
// 			WHERE mensagem.catr_id = $idCatraca";
// 	$result = $dao->getConexao()->query($sql);
// 	foreach ($result as $linha){
// 		$msg1 = $linha['mens_institucional1'];
// 		$msg2 = $linha['mens_institucional2'];
// 		$msg3 = $linha['mens_institucional3'];
// 		$msg4 = $linha['mens_institucional4'];
// 		$nomeCatraca = $linha['catr_nome'];
// 		$nomeUnidade = $linha['unid_nome'];		
// 	}	
// 	$args = array($nomeUnidade, $nomeCatraca, $msg1, $msg2, $msg3, $msg4);
// 	$view->formEditarMensagensCatraca($args);
// 	return ;
// }

?>