<?php

class RelatorioControllerGuiche{
	
	public static function main($nivel){
		switch ($nivel) {
			case Sessao::NIVEL_SUPER :
				$relatorio = new RelatorioControllerGuiche();
				$relatorio->relatorioGuiche();
				break;
			case Sessao::NIVEL_ADMIN :
				$relatorio = new RelatorioControllerGuiche();
				$relatorio->relatorioGuiche();
								
				break;
			default :
				UsuarioController::main ( $nivel );
				break;
		}		
	}
	
	public function relatorioGuiche(){
		
		$dao = new DAO();
		$view = new RelatorioViewGuiche();
		$usuarioDao = new UsuarioDAO();
		$usuario = new Usuario();
		$relatorioGuiche = new RelatorioControllerGuiche();
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$listaOperador =  $dao->getConexao()->query($sql);
		$view->formPesquisar($listaOperador);
			
		
		if (isset($_POST['gerar'])){		
		
		$dataInicio = date ($_POST['data_inicio']);
		$dataFim = date ($_POST['data_fim']);
		$idDoUsuario = ($_POST['operador']);		
		$horaIni = $_POST['hora_inicio'];
		$horaFim = $_POST['hora_fim'];
				
		if($dataInicio == null){
			$dataInicio = date('Y-m-d');
		}
		if($dataFim == null){
			$dataFim = date('Y-m-d');
		}
		if ($horaIni == null){
			$horaIni = ('00:00:00');	
		}		
		if ($horaFim == null){
			$horaFim = ('23:59:59');
		}
		
		$operador = "";			
		if($idDoUsuario != null){
			$operador = "AND usuario.usua_id = $idDoUsuario";
		}
			
		echo '	<div class="doze colunas borda relatorio">
				
					<div class="doze colunas">						
				
						<div class="duas colunas">
							<a href="http://www.unilab.edu.br">
								<img class="imagem-responsiva centralizada" src="img/logo-unilab.png" alt="">
							</a>
						</div>
						<div class="oito colunas">
							<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>				
						</div>
						<div class="duas colunas">
							<a href="http://www.unilab.edu.br">
								<img class="imagem-responsiva centralizada" src="img/pp.jpg" alt="">
							</a>
						</div>		
						<hr class="um"><br>
					</div>		
				
					<table class="tabela-relatorio">
						<thead>
							<tr>
								<th>Data</th>
								<th>Hora</th>								
								<th>Descrição</th>
								<th>Operador</th>
								<th>Valor</th>
							</tr>
						</thead>
						<tbody>';		
			
		$inicio = $dataInicio.' '.$horaIni;
		$fim = $dataFim.' '.$horaFim;
			
		$valorTotal = 0;
		$sqlTran = "SELECT * FROM transacao as trans 
					LEFT JOIN usuario as usuario
					on trans.usua_id = usuario.usua_id 
					WHERE (tran_data BETWEEN '$inicio' AND '$fim') $operador ";
		$result =  $dao->getConexao()->query($sqlTran);			
		foreach ($result as $dado){			
			echo '	<tr>
						<td>'.date("d/m/Y",strtotime($dado['tran_data'])).'</td>
						<td>'.date('H:i:s',strtotime($dado['tran_data'])).'</td>						
						<td>'.$dado['tran_descricao'].'</td>
						<td>'.$dado['usua_nome'].'</td>	
						<td>R$ '.$dado['tran_valor'].'</td>
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
			
				echo '	<tr id="soma">
							<th>Somatório</th>							
							<td> - </td>
							<td> - </td>
							<td> - </td>
							<td>R$ '.number_format($valorTotal, 2).'</td>
						</tr>					
					</tbody>
				</table>
				<div class="doze colunas relatorio-rodape">
					<span>CATRACA | Copyright © 2015 - DTI</span>
					<span>Relatório Emitido em: '.$date = date('d-m-Y H:i:s').'</span>';
		
 		echo '<a class="botao icone-printer" href="?pagina=relatorio_guiche&gerarpdf=1"> Imprimir</a>	
 				</div>
			</div>';
		
 					
		
		}
		
		
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