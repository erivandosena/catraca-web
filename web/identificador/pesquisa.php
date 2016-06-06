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

if($sessao->getNivelAcesso() != Sessao::NIVEL_SUPER)
	exit(0);




echo '<form action="" method="get">
	<input type="text" name="nome" placeholder="nome"/>
	<input type="submit" value="pesquisar">
</form>';
if(isset($_GET['nome'])){

	

	$pesquisa = preg_replace ('/[^a-zA-Z0-9\s]/', '', $_GET['nome'] );
	$pesquisa = strtoupper ( $pesquisa );
	echo '<br>Pesquisa: '.$pesquisa.'<br><br>';

	$daoSistemasComum = new DAO(null, DAO::TIPO_PG_SISTEMAS_COMUM);
	echo 'SISTEMAS COMUM - vw_usuarios_autenticacao_catraca<br>';
	$result2 = $daoSistemasComum->getConexao()->query("SELECT * FROM vw_usuarios_autenticacao_catraca WHERE nome like '%$pesquisa%'");
	$i = 0;
	echo '<table border = 1>';
	foreach($result2 as $linha)
	{
		if($i == 0){

			echo '<tr>';
			foreach($linha as $chave => $valor){
				if(!is_int($chave))
					echo '<th>'.$chave.'</th>';
			}
			echo '</tr>';
			$i++;

		}
		
		echo '<tr>';
		foreach ($linha as $chave => $valor){
			if(!is_int($chave))
				echo '<td>'.$valor.'</td>';
		}
		echo '</tr>';	

		
		//print_r($linha);
		echo '</tr>';
	}
	echo '</table>';
	echo '<hr>';
	$daoSIGAA = new DAO(null, DAO::TIPO_PG_SIGAAA);
	echo 'SIGAA - vw_usuarios_catraca<br>';
	$result2 = $daoSIGAA->getConexao()->query("SELECT * FROM vw_usuarios_catraca WHERE nome like '%$pesquisa%'");
	$i = 0;
	echo '<table border = 1>';
	foreach($result2 as $linha)
	{
		if($i == 0){

			echo '<tr>';
			foreach($linha as $chave => $valor){
				if(!is_int($chave))
					echo '<th>'.$chave.'</th>';
			}
			echo '</tr>';
			$i++;

		}
		
		echo '<tr>';
		foreach ($linha as $chave => $valor){
			if(!is_int($chave))
				echo '<td>'.$valor.'</td>';
		}
		echo '</tr>';	

		
		//print_r($linha);
		echo '</tr>';
	}
	echo '</table>';





	$dao = new DAO();
	echo 'Base Local<br>';
	$result2 = $dao->getConexao()->query("SELECT * FROM usuario WHERE usua_nome like '%$pesquisa%'");
	$i = 0;
	echo '<table border = 1>';
	foreach($result2 as $linha)
	{
		if($i == 0){

			echo '<tr>';
			foreach($linha as $chave => $valor){
				if(!is_int($chave))
					echo '<th>'.$chave.'</th>';
			}
			echo '</tr>';
			$i++;

		}
		
		echo '<tr>';
		foreach ($linha as $chave => $valor){
			if(!is_int($chave))
				echo '<td>'.$valor.'</td>';
		}
		echo '</tr>';	

		
		//print_r($linha);
		echo '</tr>';
	}
	echo '</table>';


}




// $sql = "DELETE FROM vinculo_tipo";
// $sql = "DELETE FROM vinculo WHERE vinc_avulso <> 'TRUE'";
//$sql = "INSERT INTO vinculo_tipo (vinc_id, tipo_id) VALUES(8, 13)";
// $sql = "DELETE FROM catraca WHERE catr_id > 5";

// $sql = "UPDATE turno set turn_hora_fim = '13:30:00'
// 		WHERE turn_id = 1";

// $i = $result = $dao->getConexao()->exec($sql);
// echo $i;


?>
