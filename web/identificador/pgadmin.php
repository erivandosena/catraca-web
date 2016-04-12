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

$sql = "SELECT schemaname AS esquema, tablename AS tabela, tableowner AS dono
 FROM pg_catalog.pg_tables
 WHERE schemaname NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
 ORDER BY schemaname, tablename";
$result = $dao->getConexao()->query($sql);

foreach($result as $linha){
	
	
	$nomeDaTabela =  $linha['tabela'];
	echo '<h1>'.$nomeDaTabela.'</h1>';
	$sqlColunas = "select
	c.relname,
	a.attname as column,
	pg_catalog.format_type(a.atttypid, a.atttypmod) as datatype
		
	from pg_catalog.pg_attribute a
	inner join pg_stat_user_tables c on a.attrelid = c.relid
	WHERE
	c.relname = '$nomeDaTabela' AND
	a.attnum > 0 
	AND NOT a.attisdropped
	";
	$resultDasColunas = $dao->getConexao()->query($sqlColunas);
	foreach ($resultDasColunas as $linhaDasColunas){
		echo $linhaDasColunas['column'].' | '.$linhaDasColunas['datatype'].'<br>';
	}
	$n = 10;
	
	echo '<br>'.$n.' primeiros dados<br>';
	$sqlPrimeirosDados = "SELECT * FROM $nomeDaTabela LIMIT $n";
	$resultPrimeirosDados = $dao->getConexao()->query($sqlPrimeirosDados);
	$i = 0;
	echo '<table border=1>';
	foreach ($resultPrimeirosDados as $linhaPrimeirosDados){
		
		if(!$i){
			echo '<tr>';
			foreach ($linhaPrimeirosDados as $chave => $valor){
				if(!is_int($chave))
					echo '<th>'.$chave.'</th>';
			}
			echo '</tr>';
			$i++;
			
		}
		echo '<tr>';
		foreach ($linhaPrimeirosDados as $chave => $valor){
			if(!is_int($chave))
				echo '<td>'.$valor.'</td>';
		}
		echo '</tr>';
		
	}
	echo '</table>';
	
	echo '<hr>';
	
	
	
}

echo '<br><br>';



// $result = $dao->getConexao()->query($sql);

// foreach($result as $linha){

// 	print_r($linha);
// 	echo '<hr>';
// 	//Vamos mostrar as linhas de uma tabela.
// }




//Testes



?>