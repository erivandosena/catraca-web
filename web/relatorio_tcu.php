<?php

ini_set ( 'display_errors', 1 );
ini_set ( 'display_startup_erros', 1 );
error_reporting ( E_ALL );


function __autoload($classe) {
	if (file_exists ( 'classes/dao/' . $classe . '.php' )){
		include_once 'classes/dao/' . $classe . '.php';
		return;
	}
	if (file_exists ( 'classes/model/' . $classe . '.php' )){
		include_once 'classes/model/' . $classe . '.php';
		return;
	}
	if (file_exists ( 'classes/controller/' . $classe . '.php' )){
		include_once 'classes/controller/' . $classe . '.php';
		return;
	}
	if (file_exists ( 'classes/util/' . $classe . '.php' )){
		include_once 'classes/util/' . $classe . '.php';
		return;
	}
	if (file_exists ( 'classes/view/' . $classe . '.php' )){
		include_once 'classes/view/' . $classe . '.php';
		return;
	}
}
$sessao = new Sessao();

if(!($sessao->getNivelAcesso() == Sessao::NIVEL_SUPER || $sessao->getNivelAcesso() == Sessao::NIVEL_ADMIN)){
	exit(0);
}



$dao = new DAO();


$result = $dao->getConexao()->query("SELECT * FROM registro 
		INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
		INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id
		INNER JOIN vinculo_tipo ON vinculo_tipo.vinc_id = vinculo.vinc_id
		INNER JOIN tipo ON vinculo_tipo.tipo_id = tipo.tipo_id
		INNER JOIN catraca ON catraca.catr_id = registro.catr_id
		INNER JOIN catraca_unidade ON catraca.catr_id = catraca_unidade.catr_id
		INNER JOIN unidade ON unidade.unid_id = catraca_unidade.unid_id
		WHERE unidade.unid_id <> 1 
		ORDER BY regi_id ASC LIMIT 1000000
		
		");


$matrix = array();
foreach($result as $linha){
	
	if(!isset($matrix[date("m/Y", strtotime($linha['regi_data']))]['total'])){
		$matrix[date("m/Y", strtotime($linha['regi_data']))]['total'] = 0;
	}
	$matrix[date("m/Y", strtotime($linha['regi_data']))]['total']++;
	
	if($linha['vinc_avulso']){
		if(!isset($matrix[date("m/Y", strtotime($linha['regi_data']))]['avulso'])){
			$matrix[date("m/Y", strtotime($linha['regi_data']))]['avulso'] = 0;
		}
		$matrix[date("m/Y", strtotime($linha['regi_data']))]['avulso']++; 
	}else{
		if(!isset($matrix[date("m/Y", strtotime($linha['regi_data']))]['proprio'])){
			$matrix[date("m/Y", strtotime($linha['regi_data']))]['proprio'] = 0;
		}
		$matrix[date("m/Y", strtotime($linha['regi_data']))]['proprio']++;
	}
	
}


echo "<table border=1>";
echo "<tr><th>Mes</th><th>Avulso</th><th>Proprio</th><th>Total</th></tr>";
foreach($matrix as $chave => $valor){
	echo '<tr><td>'.$chave.'</td>';
	
	echo '<td>'.$matrix[$chave]['avulso'].'</td><td>'.$matrix[$chave]['proprio'].'</td><td>'.$matrix[$chave]['total'].'</td>';
	
	echo '</tr>';
}

echo "</table>";


