<?php


function mostraVetor($vetor){
	

	for($i = 0; $i < count($vetor); $i++){
	
		echo $vetor[$i].', ';
	
	
	
	}	
	
}
function selection($vetor){
	for($i = 0; $i < sizeof($vetor); $i++){
		$menor = $i;
		for($k = $i; $k < sizeof($vetor); $k++){
			if($vetor[$k] < $vetor[$menor])
				$menor = $k;
		}
		$aux = $vetor[$i];
		$vetor[$i] = $vetor[$menor];
		$vetor[$menor] = $aux;
	}
	return $vetor;
}

$lista = array(5, 4, 7, 2, 3);

mostraVetor($lista);
$lista = selection($lista);
echo '<br><hr>';
mostraVetor($lista);

