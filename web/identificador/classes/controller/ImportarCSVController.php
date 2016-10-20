<?php


class ImportarCSVController{
	
	
	public function importar(){
		$row = 1;
		$cartoes = array();
		if (($handle = fopen ( "almoco181020162.csv", "r" )) !== FALSE) {
			while ( ($data = fgetcsv ( $handle, 1000, "," )) !== FALSE ) {
				$num = count ( $data );
				$row ++;
				for($c = 0; $c < $num; $c ++) {
					$cartao = new Cartao();
					$cartao->setNumero($data[$c]);
					$cartoes[] = $cartao;
				}
			}
			fclose ( $handle );
		}
		$dao = new CatracaVirtualDAO();
// 		$dao->getConexao()->beginTransaction();
		

		
		$i = 0;
		echo '<table border=1>';
		echo '<tr><th>Cartao</th><th>Usuario</th><th>Creditos</th><th>Tipo</th></tr>';
		foreach($cartoes as $cartao){
			$vinculo = new Vinculo();
			$vinculo->setCartao($cartao);
			
			$dao->verificaVinculo($vinculo);
			if($cartao->getCreditos() == 0){
				$i++;
			}
			echo '<tr>';
			echo '<td>'.$cartao->getNumero().'</td><td>'.$vinculo->getResponsavel()->getNome().' </td><td>'.$cartao->getCreditos().' </td><td>'.$vinculo->getCartao()->getTipo()->getNome().' '.$vinculo->getCartao()->getTipo()->getValorCobrado().'</td>';
			echo '</tr>';
			
			
			$data = '2016-10-18 12:00:00';
			$valorPago = $vinculo->getCartao()->getTipo()->getValorCobrado();
			$custo = 9.5;
			$idCatraca = 2;
			$idCartao = $cartao->getId();
			$idVinculo = $vinculo->getId();
			
			
// 			$sql = "INSERT into registro(regi_data, regi_valor_pago, regi_valor_custo, catr_id, cart_id, vinc_id)
// 			VALUES('$data', $valorPago, $custo, $idCatraca, $idCartao, $idVinculo)";			
			
// 			$novoValor = floatval($vinculo->getCartao()->getCreditos()) - floatval($valorPago);
// 			$sqlUpdate = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";
			
// 			echo '<tr>';
// 			echo '<td colspan=3>';
			
// 			echo $sql;
// 			echo '</td>';
// 			if($dao->getConexao()->exec($sql)){
// 				echo '<td>Sucesso</td>';
					
// 			}else{
// 				echo '<td>Fracasso</td>';
// 				$dao->getConexao()->rollBack();
// 				return;
					
// 			}
			
// 			echo '</tr>';

// 			echo '<tr>';
// 			echo '<td colspan=3>';
// 			echo $sqlUpdate;
// 			echo '</td>';
// 			if($dao->getConexao()->exec($sqlUpdate)){
// 				echo '<td>Sucesso</td>';				
// 			}else{
// 				echo '<td>Fracasso</td>';
// 				$dao->getConexao()->rollBack();
// 				return;
// 			}

// 			echo '</tr>';
				
				
		}
// 		$dao->getConexao()->commit();
		echo '</table>';
		
		echo 'Sucesso!';
		
		
		
	}
	
	
}