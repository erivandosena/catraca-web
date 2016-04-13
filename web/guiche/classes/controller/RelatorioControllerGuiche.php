<?php

class RelatorioControllerGuiche{
	
	public static function main($nivel){
		
		$relatorio = new RelatorioControllerGuiche();
		$relatorio->relatorioGuiche();
		
	}
	
	public function relatorioGuiche(){
		
		$dao = new DAO();
		$usuarioDao = new UsuarioDAO();
		$usuario = new Usuario();
		$relatorioGuiche = new RelatorioControllerGuiche();
		
		echo'	<div class="borda relatorio">
					<form action="" method="post" class="formulario-organizado">
						<label for="operador">
							<object data="" type="" class="rotulo">Operador:</object>
							<select name="operador" id="operador">';
		
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$result =  $dao->getConexao()->query($sql);		
		foreach ($result as $linha){
		echo'
						<option value="'.$linha['usua_id'].'">'.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</option>';
				}
			
		echo'			<option value="">Todos os Operadores</option>	
						</select>
						</label><br>
						<label for="data_inicio">
							Data Inicio: <input type="date" name="data_inicio">
						</label><br>
						<label for="data_fim">
							Data Inicio: <input type="date" name="data_fim">
						</label><br>
							<input type="submit" value="gerar" name="gerar">
					</form>
				</div>';		
		
			if (isset($_POST['gerar'])){
			
			$dataInicio = date ($_POST['data_inicio']);
			$dataFim = date ($_POST['data_fim']);
			$idDoUsuario = ($_POST['operador']);
			
			if($dataInicio == null){
				$dataInicio = date('Y-m-d');
			}
			if($dataFim == null){
				$dataFim = date('Y-m-d');
			}
			
			$operador = "";
			
			if($idDoUsuario != null){
				$operador = "AND usuario.usua_id = $idDoUsuario";
			}
			
			echo'	<div class="borda relatorio">
					<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>
					<hr class="um">	
					<table class="tabela-relatorio">
							<thead>
								<tr>
									<th>Data</th>
									<th>Valor</th>
									<th>Descrição</th>
									<th>Operador</th>
								</tr>
							</thead>
							<tbody>';			
			
// 			$dataInicio = new DateTime($dataInicio);
// 			$dataFim = new DateTime($dataFim);
			
// 			while ( $dataInicio <= $dataFim ) {
// 				$listaDeDatas [] = $dataInicio->format ( 'Y-m-d' );
// 				$dataInicio = $dataInicio->modify ( '+1day' );
// 			}
			
// 			foreach ($listaDeDatas as $data){			
			
			$inicio = $dataInicio . ' 00:00:00';
			$fim = $dataFim . ' 23:59:59';
				
			$valorTotal = 0;
			$sqlTran = "SELECT * FROM transacao as trans 
				LEFT JOIN usuario as usuario
				on trans.usua_id = usuario.usua_id 
				WHERE (tran_data BETWEEN '$inicio' AND '$fim') $operador ";
//			$sqlTran = "SELECT * FROM transacao WHERE tran_data BETWEEN '2016-04-07' AND '2016-04-07'";
			$result =  $dao->getConexao()->query($sqlTran);			
			foreach ($result as $dado){			
				echo'	<tr>
							<td>'.date("d/m/y",strtotime($dado['tran_data'])).'</td>
							<td>R$ '.$dado['tran_valor'].'</td>
							<td>'.$dado['tran_descricao'].'</td>
							<td>'.$dado['usua_nome'].'</td>	
						</tr>';				
			}
			
			$result =  $dao->getConexao()->query($sqlTran);
			foreach ($result as $linha){
				$valor = $linha['tran_valor'];
				floatval ($valor);
				if($linha){
					$valorTotal = $valorTotal + $valor;
				}
			}
			
					echo'	<tr id="soma">
								<th>Somatório</th>
								<td>R$ '.number_format($valorTotal, 2).'</td>
								<td> - </td>
								<td> - </td>
							</tr>					
						</tbody>
					</table>
				</div>';
			}
			
//		}
		
	}
	
	public function retornaUsuario(){
		
		$dao = new DAO();		
		$usuario = new Usuario();
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$result =  $dao->getConexao()->query($sql);
		
		foreach ($result as $linha){
			$usuario->setId($linha['usua_id']);
			$usuario->setNome($linha['usua_nome']);
			return $usuario;
		}
		
	}
	
}

?>