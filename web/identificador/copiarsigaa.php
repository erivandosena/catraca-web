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
if(!($sessao->getNivelAcesso() == Sessao::NIVEL_SUPER || $sessao->getNivelAcesso() == Sessao::NIVEL_ADMIN)){
	echo "Nivel de acesso Não permitido: ".$sessao->getNivelAcesso();
	exit(0);
}

$tempoA = round(microtime(true) * 1000);



$daoSIGAA = new DAO(null, DAO::TIPO_PG_SIGAAA);
$sqlSigaa = "SELECT * FROM vw_usuarios_catraca";



$result = $daoSIGAA->getConexao()->query($sqlSigaa);

$matriz = array();


foreach ($result as $linha){
	foreach($linha as $chave => $valor){
		$linha[$chave] = str_replace("'", "''", $valor);
	}
	
	$linha['nome'] = "'".$linha['nome']."'";
	$linha['identidade'] = "'".$linha['identidade']."'";
	$linha['passaporte'] = "'".$linha['passaporte']."'";
	$linha['email'] = "'".$linha['email']."'";
	$linha['login'] = "'".$linha['login']."'";
	$linha['senha'] = "'".$linha['senha']."'";
	$linha['nivel_discente'] = "'".$linha['nivel_discente']."'";
	$linha['status_discente'] = "'".$linha['status_discente']."'";
	$linha['status_servidor'] = "'".$linha['status_servidor']."'";
	$linha['tipo_usuario'] = "'".$linha['tipo_usuario']."'";
	$linha['categoria'] = "'".$linha['categoria']."'";
	foreach($linha as $chave => $valor){
		if(!$valor || $valor == "''"){
			$linha[$chave] = "null";
		}
	}
	$matriz[$linha['id_usuario']] = $linha;
}


$daoLocal = new DAO();

foreach($matriz as $idUsuario => $linha){
	$existente = false;
	//Se esse cara existir eu atualizo. 
	//Se ele não existir eu insiro. 
	$result = $daoLocal->getConexao()->query("SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $idUsuario;");
	foreach($result as $linha2){

		$sqlUpdate = "UPDATE vw_usuarios_catraca
			SET 
			nome = ".$linha['nome'].",
			identidade = ".$linha['identidade'].",
			cpf_cnpj = ".$linha['cpf_cnpj'].",
			passaporte = ".$linha['passaporte'].",
			email = ".$linha['email'].",
			login = ".$linha['login'].",
			senha = ".$linha['senha'].",
			matricula_disc = ".$linha['matricula_disc'].",
			nivel_discente = ".$linha['nivel_discente'].",
			id_status_discente = ".$linha['id_status_discente'].",
			status_discente = ".$linha['status_discente'].",
			siape = ".$linha['siape'].",
			id_status_servidor =".$linha['id_status_servidor'].",
			status_servidor = ".$linha['status_servidor'].",
			id_tipo_usuario = ".$linha['id_tipo_usuario'].",
			tipo_usuario = ".$linha['tipo_usuario'].",
			id_categoria = ".$linha['id_categoria'].",
			status_sistema = ".$linha['status_sistema'].",
			categoria = ".$linha['categoria']."
			WHERE id_usuario = ".$linha['id_usuario'].";";
		if($daoLocal->getConexao()->exec($sqlUpdate)){
			echo '<br><br>Atualizei<br><br>';
		}else{
			echo '<br><br>Errei Atualizacao<br><br>';
		}
// 		echo '<br>Esse eu era pra ta atualizando, mas o algoritmo nao ta pronto<br>';
		$existente = true;
		break;	
	}
	if($existente){
		continue;
	}
	//Aqui a gente vai inserir se o cara nao existiu. 
	$sqlInserir = "INSERT into vw_usuarios_catraca
			(
			id_usuario,
			nome,identidade,
			cpf_cnpj,
			passaporte,
			email,
			login,
			senha, 
			matricula_disc, 
			nivel_discente,
			id_status_discente, 
			status_discente, 
			siape, 
			id_status_servidor, 
			status_servidor, 
			id_tipo_usuario, 
			tipo_usuario, 
			id_categoria, 
			status_sistema, 
			categoria 
			) 
			VALUES(
			".$linha['id_usuario'].",
			".$linha['nome'].",
			".$linha['identidade'].",
			".$linha['cpf_cnpj'].",
			".$linha['passaporte'].",
			".$linha['email'].",
			".$linha['login'].",
			".$linha['senha'].", 
			".$linha['matricula_disc'].", 
			".$linha['nivel_discente'].",
			".$linha['id_status_discente'].", 
			".$linha['status_discente'].", 
			".$linha['siape'].", 
			".$linha['id_status_servidor'].", 
			".$linha['status_servidor'].", 
			".$linha['id_tipo_usuario'].", 
			".$linha['tipo_usuario'].", 
			".$linha['id_categoria'].", 
			".$linha['status_sistema'].", 
			".$linha['categoria']."
			);";
	echo 'Tenho que executar esta SQL:<br>';
	echo $sqlInserir;
	if($daoLocal->getConexao()->exec($sqlInserir)){
		echo '<br><br>Consegui<br><br>';
	}else{
		echo '<br><br>Erreiiiiiiii<br><br>';
	}

}

$tempoB = round(microtime(true) * 1000);



//--------------------------SISTEMAS COMUM---------------------------------------------------------//

$daoSistemasComum = new DAO(null, DAO::TIPO_PG_SISTEMAS_COMUM);
$sqlComum = "SELECT * FROM vw_usuarios_autenticacao_catraca";
$result = $daoSistemasComum->getConexao()->query($sqlComum);

$matriz = array();


foreach ($result as $linha){
	foreach($linha as $chave => $valor){
		$linha[$chave] = str_replace("'", "''", $valor);
	}

	$linha['nome'] = "'".$linha['nome']."'";
	$linha['passaporte'] = "'".$linha['passaporte']."'";
	$linha['email'] = "'".$linha['email']."'";
	$linha['login'] = "'".$linha['login']."'";
	$linha['senha'] = "'".$linha['senha']."'";
	$linha['status_servidor'] = "'".$linha['status_servidor']."'";
	$linha['tipo_usuario'] = "'".$linha['tipo_usuario']."'";
	$linha['categoria'] = "'".$linha['categoria']."'";
	foreach($linha as $chave => $valor){
		if(!$valor || $valor == "''"){
			$linha[$chave] = "null";
		}
	}
	$matriz[$linha['id_usuario']] = $linha;
}




foreach($matriz as $idUsuario => $linha){
	$existente = false;
	//Se esse cara existir eu atualizo.
	//Se ele não existir eu insiro.
	$result = $daoLocal->getConexao()->query("SELECT * FROM vw_usuarios_autenticacao_catraca WHERE id_usuario = $idUsuario;");
	foreach($result as $linha2){

		$sqlUpdate = "UPDATE vw_usuarios_autenticacao_catraca
			SET
			nome = ".$linha['nome'].",
			cpf_cnpj = ".$linha['cpf_cnpj'].",
			passaporte = ".$linha['passaporte'].",
			email = ".$linha['email'].",	
			login = ".$linha['login'].",
			senha = ".$linha['senha'].",
			siape = ".$linha['siape'].",
			id_status_servidor =".$linha['id_status_servidor'].",
			status_servidor = ".$linha['status_servidor'].",
			id_tipo_usuario = ".$linha['id_tipo_usuario'].",
			tipo_usuario = ".$linha['tipo_usuario'].",
			id_categoria = ".$linha['id_categoria'].",
			categoria = ".$linha['categoria']."	
			WHERE id_usuario = ".$linha['id_usuario'].";";
		if($daoLocal->getConexao()->exec($sqlUpdate)){
			echo '<br><br>Atualizei<br><br>';
		}else{
			echo '<br><br>Errei Atualizacao<br><br>';
		}
		// 		echo '<br>Esse eu era pra ta atualizando, mas o algoritmo nao ta pronto<br>';
		$existente = true;
		break;
	}
	if($existente){
		continue;
	}
	//Aqui a gente vai inserir se o cara nao existiu.
	$sqlInserir = "INSERT into vw_usuarios_autenticacao_catraca
			(
			id_usuario,
			nome,
			cpf_cnpj,
			passaporte,
			email,
			login,
			senha,
			siape,
			id_status_servidor,
			status_servidor,
			id_tipo_usuario,
			id_categoria,
			categoria
			)
			VALUES(
			".$linha['id_usuario'].",
			".$linha['nome'].",
			".$linha['cpf_cnpj'].",
			".$linha['passaporte'].",
			".$linha['email'].",
			".$linha['login'].",
			".$linha['senha'].",
			".$linha['siape'].",
			".$linha['id_status_servidor'].",
			".$linha['status_servidor'].",					
			".$linha['id_tipo_usuario'].",
			".$linha['id_categoria'].",
			".$linha['categoria']."		
					

			);";
	echo 'Tenho que executar esta SQL:<br>';
	echo $sqlInserir;
	if($daoLocal->getConexao()->exec($sqlInserir)){
		echo '<br><br>Consegui<br><br>';
	}else{
		echo '<br><br>Erreiiiiiiii<br><br>';
	}

}

$tempoC = round(microtime(true) * 1000);

echo "Tempo BANCO 1<br>";
echo $tempoB-$tempoA;
echo "Tempo BANCO 2<br>";
echo $tempoC-$tempoA;
echo "<br>Tempo total: ".(($tempoC-$tempoA)+$tempoB-$tempoA);


?>


