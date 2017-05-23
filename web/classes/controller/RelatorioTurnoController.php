<?php
class RelatorioTurnoController {
	private $view;
	private $dao;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$controller = new RelatorioController ();
				$controller->relatorio ();
				break;
			case Sessao::NIVEL_ADMIN :
				$controller = new RelatorioController ();
				$controller->relatorio ();
				break;
			case Sessao::NIVEL_RELATORIO:
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
		
		echo '<div class="doze colunas borda relatorio">
									<form action="" class="formulario sequencial">									
											<div id="data">
												<label for="opcoes-1">
													<object class="rotulo texto-preto">Unidade Acadêmica: </object>
													<select name="unidade" id="unidade" class="texto-preto">';
		foreach ( $listaDeUnidades as $unidade ) {
			echo '<option value="' . $unidade->getId () . '">' . $unidade->getNome () . '</option>';
		}
		//echo '<option value="">Todos as Unidades</option>';
		echo '								            										            
												    </select>
												</label><br>
												<label for="data_inicial" class="texto-preto">
												    Data Inicial: <input id="data_inicial" type="date" name="data_inicial"/>
												</label><br>
												<label for="data_final" class="texto-preto">
												    Data Final: <input id="data_final" type="date" name="data_final"/>
												</label><br>
		
												<input type="hidden" name="pagina" value="relatorio" />
												<input  type="submit"  name="gerar" value="Gerar"/>
											</div>									    							
									</form>																			
									</div>';
		
		if (isset ( $_GET ['gerar'] )) {
			$this->gerarPratosConsumidos ( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final'] );
		
		}else{
			$this->geraRelacaoPratosValores ();
				
		}
	}
	public function gerarPratosConsumidos($idUnidade = NULL, $dateStart = null, $dataEnd = null) {

		if ($dateStart == null)
			$dateStart = date ( 'Y-m-d' );
		if ($dataEnd == null)
			$dataEnd = date ( 'Y-m-d' );
		
		
		$strFiltroUnidade = "";
		$strUnidade =  'Todos os restaurantes ';
		if($idUnidade != NULL){
			
			$idUnidade = intval($idUnidade);
			$strFiltroUnidade  = " AND catraca_unidade.unid_id = $idUnidade";
			$unidadeDao = new UnidadeDAO($this->dao->getConexao());
			$unidade = new Unidade();
			$unidade->setId($idUnidade);
			$unidadeDao->preenchePorId($unidade);
			$strUnidade =  $unidade->getNome();
		}
		
		$dao = new TipoDAO ();
		$tipos = $dao->retornaLista ();
		
		$dateStart = new DateTime ( $dateStart );
		$dateEnd = new DateTime ( $dataEnd );
		
		$dateRange = array ();
		while ( $dateStart <= $dateEnd ) {
			$listaDeDatas [] = $dateStart->format ( 'Y-m-d' );
			$dateStart = $dateStart->modify ( '+1day' );
		}
		
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
					INNER JOIN catraca ON registro.catr_id = catraca.catr_id
					INNER JOIN catraca_unidade ON catraca.catr_id = catraca_unidade.catr_id
					WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId
					$strFiltroUnidade;";
					foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
						$valor = $linha ['valor'];
					}
					
					if ($valor)
						$listaDeDados [$data] [$tipo->getId ()] = $valor;
					else
						$listaDeDados [$data] [$tipo->getId ()] = 0;
					
					$total += intval ( $valor );
				}
				$listaDeDados [$data] ['total'] = $total;
			}
			
			$this->mostraListaDeDadosPratos($listaDeDados, $strUnidade.' - turno: ' . $turno->getDescricao () . ' - entre: ' . $turno->getHoraInicial () . ' e ' . $turno->getHoraFinal (), $tipos, $listaDeDatas );
		}
	}

	
	public function mostraListaDeDados($listaDeDados, $titulo, $tipos, $listaDeDatas) {
		$subTotal = array ();
		foreach ( $tipos as $tipo ) {
			$subTotal [$tipo->getId ()] = 0;
		}
		$subTotal ['total'] = 0;
	
		
		echo '<div class=" doze colunas borda relatorio">
				<h2>UNILAB<small class="fim">Universidade da Integraçao Internacional da Lusofonia Afro-Brasileira</small></h2>	
				<hr class="um">
				<h3>'.$titulo.'</h3>
				<hr class="dois">';
		
		echo '<table class="tabela-relatorio">
				<thead>
					<tr>
						<th>Data</th>';
		foreach ( $tipos as $tipo ) {
			echo '<th>' . $tipo->getNome () . '</th>';
		}		
		echo'			<th>Total</th>
				</thead>';
		
		echo '<tbody>';
		
		foreach ( $listaDeDatas as $data ) {
			echo '<tr>';
			echo '<td>' . date ( 'd/m/Y', strtotime ( $data ) ) . '</td>';
			foreach ( $tipos as $tipo ) {
				
				echo '<td>'.number_format (floatval($listaDeDados [$data] [$tipo->getId ()]) , 2, ',', '.' )    . '</td>';
				$subTotal [$tipo->getId ()] += $listaDeDados [$data] [$tipo->getId ()];
			}
			echo '<td>'.number_format ($listaDeDados [$data] ['total'] , 2, ',', '.' )   . '</td>';
			echo '</tr>';
			$subTotal ['total'] += $listaDeDados [$data] ['total'];
		}
		echo '<tr id="soma">
				<th>Somatório</th>';
		foreach ( $tipos as $tipo ) {
			echo '<td>'.number_format ( $subTotal [$tipo->getId ()] , 2, ',', '.' )  . '</td>';
		}
		echo '<td>' . number_format ( $subTotal ['total']  , 2, ',', '.' )  . '</td>';
		echo '</tr>';
		echo '</table>
				<div class="doze colunas relatorio-rodape">
					<span>CATRACA | Copyright © 2015 - DTI</span>
					<span>Relatório Emitido em: '.$date = date('d/m/Y').'</span>';
// 		echo '<a class="botao icone-printer"> Imprimir</a>';
				
		echo '		</div>		
			</div>';
	}
	
	
	public function mostraListaDeDadosPratos($listaDeDados, $titulo, $tipos, $listaDeDatas) {
		$subTotal = array ();
		foreach ( $tipos as $tipo ) {
			$subTotal [$tipo->getId ()] = 0;
		}
		$subTotal ['total'] = 0;
	
		echo '<div class=" doze colunas borda relatorio">
				<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>	
				<hr class="um">
				<h3>'.$titulo.'</h3>							
				<hr class="dois">';
		
		echo '<table class="tabela-relatorio">
				<thead>
					<tr>
						<th>Data</th>';
		foreach ( $tipos as $tipo ) {
			echo '<th>' . $tipo->getNome () . '</th>';
		}		
		echo'			<th>Total</th>
				</thead>';
		
		echo '<tbody>';
		
		foreach ( $listaDeDatas as $data ) {
			echo '<tr>';
			echo '<td>' . date ( 'd/m/Y', strtotime ( $data ) ) . '</td>';
			foreach ( $tipos as $tipo ) {
				
				echo '<td>'.$listaDeDados [$data] [$tipo->getId ()] . '</td>';
				$subTotal [$tipo->getId ()] += $listaDeDados [$data] [$tipo->getId ()];
			}
			echo '<td>'.$listaDeDados [$data] ['total'] . '</td>';
			echo '</tr>';
			$subTotal ['total'] += $listaDeDados [$data] ['total'];
		}
		echo '<tr id="soma">
				<th id="limpar">Somatório</th>';
		foreach ( $tipos as $tipo ) {
			echo '<td>'.$subTotal [$tipo->getId ()] . '</td>';
		}
		echo '<td>' . $subTotal ['total'] . '</td>';
		echo '</tr>';
		
		
		
		echo '</table>
				<div class="doze colunas relatorio-rodape">
					<span>CATRACA | Copyright © 2015 - DTI</span>
					<span>Relatório Emitido em: '.$date = date('d-m-Y H:i:s').'</span>';
		
// 		echo '<a class="botao icone-printer"> Imprimir</a>';
		echo '</div>		
			</div>';
	}
	
	public function mostraMatriz($matriz){
		echo '<br><br><br><table border="1">';
		foreach($matriz as $chave => $valor){
			echo '<tr><th>'.$chave.'</th>';
			foreach($valor as $chave2 => $valor2){
				echo '<td>'.$chave2.' - '.$valor2.'</td>';
			}
			echo '</tr>';
		}
		echo '</table>';
		
	}
}

?>