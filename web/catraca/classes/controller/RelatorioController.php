<?php
class RelatorioController {
	private $view;
	private $dao;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$controller = new RelatorioController ();
				$controller->relatorio ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function relatorio() {
		$this->dao = new UnidadeDAO ();
		$listaDeUnidades = $this->dao->retornaLista ();
		
		echo '<div class="borda">
									<form action="" class="formulario sequencial">									
											<div id="data">
												<label for="opcoes-1">
													<object class="rotulo texto-preto">Unidade Acadêmica: </object>
													<select name="unidade" id="unidade" class="texto-preto">';
		foreach ( $listaDeUnidades as $unidade ) {
			echo '<option value="' . $unidade->getId () . '">' . $unidade->getNome () . '</option>';
		}
		echo '								            										            
												    </select>
												</label><br>
												<label for="data_inicial" class="texto-preto">
												    Data Inicial: <input id="data_inicial" type="date" name="data_inicial"/>
												</label><br>
												<label for="data_final" class="texto-preto">
												    Data Final: <input id="data_final" type="date" name="data_final"/>
												</label><br>
												<label for="tipo_de_relatorio">
													Tipo De Relatório
												</label>
												<select id="tipo_de_relatorio" name="tipo_de_relatorio">
													<option value="1">Pratos Consumidos</option>
													<option value="2">Valores Arrecadados</option>
													<option value="3">Relação Pratos e Valores</option>
												</select>
												<input type="hidden" name="pagina" value="relatorio" />
												<input  type="submit"  name="gerar" value="Gerar"/>
											</div>									    							
									</form>																			
									</div>';
		
		if (isset ( $_GET ['gerar'] )) {
			switch ($_GET ['tipo_de_relatorio']) {
				case "1" :
					$this->gerarPratosConsumidos ( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final'] );
					break;
				case "2" :
					$this->geraValoresArrecadados ( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final'] );
					break;
				case "3" :
					$this->geraRelacaoPratosValores ( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final'] );
					break;
				default :
					$this->gerarPratosConsumidos ( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final'] );
					break;
			}
		}
	}
	public function gerarPratosConsumidos($idUnidade, $dateStart, $dataEnd) {
		$idUnidade = intval ( $idUnidade );
		$dao = new TipoDAO ( null, DAO::TIPO_PG_LOCAL );
		$tipos = $dao->retornaLista ();
		
		$dateStart = new DateTime ( $dateStart );
		$dateEnd = new DateTime ( $dataEnd );
		
		// Prints days according to the interval
		$dateRange = array ();
		while ( $dateStart <= $dateEnd ) {
			$listaDeDatas [] = $dateStart->format ( 'Y-m-d' );
			$dateStart = $dateStart->modify ( '+1day' );
		}
		
		$listaDeDados = array ();
		foreach ( $listaDeDatas as $data ) {
			$total = 0;
			foreach ( $tipos as $tipo ) {
				
				$dataInicial = $data . ' 00:00:00';
				$dataFinal = $data . ' 23:59:59';
				$tipoId = $tipo->getId ();
				
				$sql = "SELECT sum(1) valor FROM registro
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
				WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
				foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
					$valor = $linha ['valor'];
				}
				
				if ($valor)
					$listaDeDados [$data] [$tipo->getId ()] = $valor;
				else
					$listaDeDados [$data] [$tipo->getId ()] = '-';
				
				$total += intval ( $valor );
			}
			$listaDeDados [$data] ['total'] = $total;
		}
		
		$this->mostraListaDeDados ( $listaDeDados, 'Liberdade - Todos os Turnos', $tipos, $listaDeDatas );
		
		$listaDeDados = array ();
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		$listaDeTurnos = $turnoDao->retornaLista ();
		foreach ( $listaDeTurnos as $turno ) {
			foreach ( $listaDeDatas as $data ) {
				$total = 0;
				foreach ( $tipos as $tipo ) {
					
					$dataInicial = $data . ' ' . $turno->getHoraInicial ();
					$dataFinal = $data . ' ' . $turno->getHoraFinal ();
					$tipoId = $tipo->getId ();
					
					$sql = "SELECT sum(1) valor FROM registro
					INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
					INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
					WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
					foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
						$valor = $linha ['valor'];
					}
					
					if ($valor)
						$listaDeDados [$data] [$tipo->getId ()] = $valor;
					else
						$listaDeDados [$data] [$tipo->getId ()] = '-';
					
					$total += intval ( $valor );
				}
				$listaDeDados [$data] ['total'] = $total;
			}
			$this->mostraListaDeDados ( $listaDeDados, 'Liberdade - turno: ' . $turno->getDescricao () . ' - entre: ' . $turno->getHoraInicial () . ' e ' . $turno->getHoraFinal (), $tipos, $listaDeDatas );
		}
	}
	public function geraValoresArrecadados($idUnidade, $dateStart, $dataEnd) {
		$idUnidade = intval ( $idUnidade );
		$dao = new TipoDAO ( null, DAO::TIPO_PG_LOCAL );
		$tipos = $dao->retornaLista ();
		
		$dateStart = new DateTime ( $dateStart );
		$dateEnd = new DateTime ( $dataEnd );
		
		// Prints days according to the interval
		$dateRange = array ();
		while ( $dateStart <= $dateEnd ) {
			$listaDeDatas [] = $dateStart->format ( 'Y-m-d' );
			$dateStart = $dateStart->modify ( '+1day' );
		}
		
		$listaDeDados = array ();
		foreach ( $listaDeDatas as $data ) {
			$total = 0;
			foreach ( $tipos as $tipo ) {
				
				$dataInicial = $data . ' 00:00:00';
				$dataFinal = $data . ' 23:59:59';
				$tipoId = $tipo->getId ();
				
				$sql = "SELECT sum(regi_valor_pago) valor FROM registro
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
				WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
				foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
					$valor = $linha ['valor'];
				}
				
				if ($valor)
					$listaDeDados [$data] [$tipo->getId ()] = $valor;
				else
					$listaDeDados [$data] [$tipo->getId ()] = '-';
				
				$total += floatval ( $valor );
			}
			$listaDeDados [$data] ['total'] = $total;
		}
		
		$this->mostraListaDeDados ( $listaDeDados, 'Liberdade - Todos os Turnos', $tipos, $listaDeDatas );
		
		$listaDeDados = array ();
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		$listaDeTurnos = $turnoDao->retornaLista ();
		foreach ( $listaDeTurnos as $turno ) {
			foreach ( $listaDeDatas as $data ) {
				$total = 0;
				foreach ( $tipos as $tipo ) {
					
					$dataInicial = $data . ' ' . $turno->getHoraInicial ();
					$dataFinal = $data . ' ' . $turno->getHoraFinal ();
					$tipoId = $tipo->getId ();
					
					$sql = "SELECT sum(regi_valor_pago) valor FROM registro
					INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
					INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
					WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
					foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
						$valor = $linha ['valor'];
					}
					
					if ($valor)
						$listaDeDados [$data] [$tipo->getId ()] = $valor;
					else
						$listaDeDados [$data] [$tipo->getId ()] = '-';
					
					$total += intval ( $valor );
				}
				$listaDeDados [$data] ['total'] = $total;
			}
			$this->mostraListaDeDados ( $listaDeDados, 'Liberdade - turno: ' . $turno->getDescricao () . ' - entre: ' . $turno->getHoraInicial () . ' e ' . $turno->getHoraFinal (), $tipos, $listaDeDatas );
		}
	}
	public function geraRelacaoPratosValores($idUnidade, $data1, $data2) {
		$idUnidade = intval ( $idUnidade );
		$dao = new TipoDAO ( null, DAO::TIPO_PG_LOCAL );
		$tipos = $dao->retornaLista ();
		
		$dateStart = new DateTime ( $data1);
		$dateEnd = new DateTime ( $data2);
		
		// Prints days according to the interval
		$dateRange = array ();
		while ( $dateStart <= $dateEnd ) {
			$listaDeDatas [] = $dateStart->format ( 'Y-m-d' );
			$dateStart = $dateStart->modify ( '+1day' );
		}
		
		$listaDeDados = array ();
		$totalValor = 0;
		$totalPratos  = 0;
		foreach ( $tipos as $tipo ) {
			$listaDeDados [$tipo->getId ()] ['pratos'] = 0;
			$listaDeDados [$tipo->getId ()] ['valor'] = 0;
			
			foreach($listaDeDatas as $data){
				$dataInicial = $data . ' 00:00:00';
				$dataFinal = $data . ' 23:59:59';
				$tipoId = $tipo->getId ();
				$sql = "SELECT sum(1) pratos,sum(regi_valor_pago) valor  FROM registro
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
				WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
				foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
					$pratos = $linha ['pratos'];
					$valor = $linha ['valor'];
					
				}
				$listaDeDados [$tipo->getId ()] ['pratos'] += $pratos;
				$listaDeDados [$tipo->getId ()] ['valor'] += $valor;
				
				$totalValor += $valor;
				$totalPratos  += $pratos;
			}
			$totalValor += floatval ( $valor );
			$totalPratos += intval ( $pratos );
		}
		$listaDeDados ['total'] ['pratos'] = $totalPratos;
		$listaDeDados ['total'] ['valor'] = $totalValor;
		
		echo '<div class=" doze colunas borda">';
		
		echo '<table class="tabela quadro no-centro fundo-branco">';
		echo '<tr><th colspan="3">Restaurante Universitário de Liberdade -  Todos os turnos</th></tr>';
		echo '<tr><th>Data:</th><td colspan="2">Entre '.date('d/m/Y',strtotime($data1)).' e '.date('d/m/Y', strtotime($data2)).'</td></trt>';
		echo '<tr><td>-</td><th>Pratos</th><th>Valores</th></tr>';
		foreach ( $tipos as $tipo ) {
			echo '<tr><th>' . $tipo->getNome () . '</th><td>' . $listaDeDados [$tipo->getId ()] ['pratos'] . '</td><td>R$ ' . number_format($listaDeDados [$tipo->getId ()] ['valor'], 2, ',', '.')  . '</td></tr>';
		}
		echo '<tr><th>Somatório</th><td>' . $listaDeDados ['total'] ['pratos'] . '</td><td>R$ ' .number_format($listaDeDados ['total'] ['valor'], 2, ',', '.'). '</td></tr>';
		echo '</table>';
		echo '</div>';
		
		
		
		
	
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		$listaDeTurnos = $turnoDao->retornaLista ();
		
		foreach($listaDeTurnos as $turno){
			$listaDeDados = array ();
			$totalValor = 0;
			$totalPratos  = 0;
			foreach ( $tipos as $tipo ) {
				$listaDeDados [$tipo->getId ()] ['pratos'] = 0;
				$listaDeDados [$tipo->getId ()] ['valor'] = 0;
					
				foreach($listaDeDatas as $data){
					$dataInicial = $data . ' '.$turno->getHoraInicial();
					$dataFinal = $data . ' '.$turno->getHoraFinal();
					$tipoId = $tipo->getId ();
					$sql = "SELECT sum(1) pratos,sum(regi_valor_pago) valor  FROM registro
					INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
					INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
					WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
					foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
						$pratos = $linha ['pratos'];
						$valor = $linha ['valor'];
							
					}
					$listaDeDados [$tipo->getId ()] ['pratos'] += $pratos;
					$listaDeDados [$tipo->getId ()] ['valor'] += $valor;
			
					$totalValor += $valor;
					$totalPratos  += $pratos;
				}
				$totalValor += floatval ( $valor );
				$totalPratos += intval ( $pratos );
			}
			$listaDeDados ['total'] ['pratos'] = $totalPratos;
			$listaDeDados ['total'] ['valor'] = $totalValor;
			
			echo '<div class=" doze colunas borda">';
			
			echo '<table class="tabela quadro no-centro fundo-branco">';
			echo '<tr><th colspan="3">Restaurante Universitário de Liberdade -  '.$turno->getDescricao().'</th></tr>';
			echo '<tr><th>Data:</th><td colspan="2">Entre '.date('d/m/Y',strtotime($data1)).' e '.date('d/m/Y', strtotime($data2)).'</td></trt>';
			echo '<tr><td>-</td><th>Pratos</th><th>Valores</th></tr>';
			foreach ( $tipos as $tipo ) {
				echo '<tr><th>' . $tipo->getNome () . '</th><td>' . $listaDeDados [$tipo->getId ()] ['pratos'] . '</td><td>R$ ' . number_format( $listaDeDados [$tipo->getId ()] ['valor'], 2, ',', '.') . '</td></tr>';
			}
			echo '<tr><th>Somatório</th><td>' . $listaDeDados ['total'] ['pratos'] . '</td><td>R$ ' . number_format($listaDeDados ['total'] ['valor'], 2, ',', '.') . '</td></tr>';
			echo '</table>';
			echo '</div>';
			
			
		}
		
		
		
		
	}
	
	public function mostraListaDeDados($listaDeDados, $titulo, $tipos, $listaDeDatas) {
		$subTotal = array();
		foreach($tipos as $tipo){
			$subTotal[$tipo->getId()] = 0;
			
		}
		$subTotal['total'] = 0;
		
		echo '
		
		<div class=" doze colunas borda">';
		
		echo '<table class="tabela quadro no-centro fundo-branco">';
		echo '<tr class="centralizado"><td colspan="' . (count ( $tipos ) + 2) . '">' . $titulo . '</td></tr>';
		echo '<tr>';
		echo '<td>Data</td>';
		foreach ( $tipos as $tipo ) {
			echo '<td>' . $tipo->getNome () . '</td>';
		}
		echo '<td>Total</td>';
		echo '</tr>';
		foreach ( $listaDeDatas as $data ) {
			echo '<tr>';
			echo '<td>' . date ( 'd/m/Y', strtotime ( $data ) ) . '</td>';
			foreach ( $tipos as $tipo ) {
				
				echo '<td>' . $listaDeDados [$data] [$tipo->getId ()] . '</td>';
				$subTotal[$tipo->getId()] += $listaDeDados [$data] [$tipo->getId ()];
			}
			echo '<td>' . $listaDeDados [$data] ['total'] . '</td>';
			echo '</tr>';
			$subTotal['total'] += $listaDeDados [$data] ['total'];
		}
		echo '<tr><th>Somatório</th>';
		foreach($tipos as $tipo){
			echo '<td>'.$subTotal[$tipo->getId()].'</td>';
			
		}
		echo '<td>'.$subTotal['total'].'</td>';
		echo '</tr>';
		echo '</table>';
		
		echo '</div>';
	}
}

?>