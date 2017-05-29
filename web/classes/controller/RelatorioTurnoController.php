<?php
class RelatorioTurnoController{
	private $view;
	private $dao;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$controller = new RelatorioTurnoController ();
				$controller->relatorio ();
				break;
			case Sessao::NIVEL_ADMIN :
				$controller = new RelatorioTurnoController ();
				$controller->relatorio ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function RelatorioTurnoController(){
		$this->view = new RelatorioTurnoView();
		$this->dao = new UnidadeDAO ();
		
	}
	public function relatorio() {
		
		$listaDeUnidades = $this->dao->retornaLista ();
		//Esse codigo nao faz parte do sistema. 
		foreach ($listaDeUnidades as $chave => $linha){
			if($linha->getId() == 1){
				unset($listaDeUnidades[$chave]);
			}
		}
		//Fim do codigo que nao faz parte do sistema. 
		
		$this->view->mostrarFormulario($listaDeUnidades);
				
		
		if (isset ( $_GET ['gerar'] )) {
			$dados = $this->gerarDados( $_GET ['unidade'], $_GET ['data_inicial'], $_GET ['data_final']);
			//$this->view->mostraMatriz($dados);
		}
	}
	
	
	public function gerarDados($idUnidade = NULL, $data1 = null, $data2 = null){
		$dados = array();
		if($idUnidade == NULL){
			$idUnidade = 1;
		}
		if ($data1 == null){
			$data1 = date ( 'Y-m-d' );
		}
		if ($data2 == null){
			$data2 = date ( 'Y-m-d' );
		}
		
		
		$listaDeDatas = $this->intervaloDeDatas($data1, $data2);
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		$listaDeTurnos = $turnoDao->retornaLista ();
		
		
		
		$strFiltroUnidade = "";
		$strUnidade =  'Todos os restaurantes ';
		if($idUnidade != NULL){
				
			$idUnidade = intval($idUnidade);
			$strFiltroUnidade  = " AND catraca_unidade.unid_id = $idUnidade";
			
			$unidade = new Unidade();
			$unidade->setId($idUnidade);
			$this->dao->preenchePorId($unidade);
			$strUnidade =  $unidade->getNome();
		}
		
		$result = $this->dao->getConexao()->query("SELECT * FROM registro 
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN usuario ON vinculo.usua_id = usuario.usua_id
				WHERE regi_data = '2017-05-19 12:50:43'");
		foreach($result as $linha){
			$id = $linha['id_base_externa'];
			$sql2 = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $id LIMIT 1";
			$res = $this->dao->getConexao()->query($sql2);
			foreach($res as $linha2){
				print_r($linha2);
				echo '<br><hr>';
			}
		}
		
		foreach($listaDeTurnos as $turno){
			foreach($listaDeDatas as $data){
				
			
			}	
		}		
		
		
		
		return $dados;
		
	}
	/**
	 * @param string $data1
	 * @param string $data2
	 * 
	 * @return array $listaDeDatas
	 */
	public function intervaloDeDatas($data1, $data2){
		$dateStart = new DateTime ( $data1 );
		$dateEnd = new DateTime ( $data2 );
		$dateRange = array ();
		$listaDeDatas = array();
		while ( $dateStart <= $dateEnd ) {
			$listaDeDatas [] = $dateStart->format ( 'Y-m-d' );
			$dateStart = $dateStart->modify ( '+1day' );
		}
		return $listaDeDatas;
	
	}

	
	/*
	

	public function geraRelacaoPratosValores($idUnidade = NULL, $data1 = null, $data2 = null) {
		

		$strFiltroUnidade = "";
		$strUnidade = "Todos os restaurantes";
		if($idUnidade != NULL){
			$idUnidade = intval($idUnidade);
			$strFiltroUnidade  = " AND catraca_unidade.unid_id = $idUnidade";
			$unidadeDao = new UnidadeDAO($this->dao->getConexao());
			$unidade = new Unidade();
			$unidade->setId($idUnidade);
			$unidadeDao->preenchePorId($unidade);
			$strUnidade =  $unidade->getNome();
			
		}
		$idUnidade = intval ( $idUnidade );
		$dao = new TipoDAO ();
		$tipos = $dao->retornaLista ();
		

		$ultimoCusto = $this->pegaUltimoCusto();
		
		
		$listaDeDados = array ();
		$totalValor = 0;
		$totalPratos = 0;
		foreach ( $tipos as $tipo ) {
			$listaDeDados [$tipo->getId ()] ['pratos'] = 0;
			$listaDeDados [$tipo->getId ()] ['valor'] = 0;
			$listaDeDados [$tipo->getId ()] ['custo'] = 0;
		}
		foreach ( $tipos as $tipo ) {
			
			foreach ( $listaDeDatas as $data ) {
				$dataInicial = $data . ' 00:00:00';
				$dataFinal = $data . ' 23:59:59';
				$tipoId = $tipo->getId ();
				$sql = "SELECT  sum(1) pratos,sum(regi_valor_pago) valor FROM registro
					INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
					INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
					INNER JOIN catraca ON catraca.catr_id = registro.catr_id
					INNER JOIN catraca_unidade ON catraca.catr_id = catraca_unidade.catr_id
					WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId
				$strFiltroUnidade;";
				foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
					//print_r($linha);
					$ultimoCusto = $this->pegaUltimoCusto($idUnidade);
					$pratos = floatval($linha ['pratos']);
					$valor = floatval($linha ['valor']);

					$listaDeDados [$tipo->getId ()] ['pratos'] += $pratos;
					$listaDeDados [$tipo->getId ()] ['valor'] += floatval($valor);
					$listaDeDados [$tipo->getId ()] ['custo'] += $ultimoCusto * $pratos;
					

					$totalValor += floatval ( $valor );
					
					$totalPratos += intval ( $pratos );
					$listaDeDados ['total'] ['pratos'] = floatval($totalPratos);
					$listaDeDados ['total'] ['valor'] = floatval($totalValor);
					$listaDeDados ['total'] ['custo'] = floatval($totalPratos * $ultimoCusto);
				}
				
				
			}
			
			
// 			$this->mostraMatriz($listaDeDados);
			
		}

		
		echo '<div class=" doze colunas borda relatorio">';		
		echo '<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>
				<hr class="um">
				<h3>'.$strUnidade.'</h3>
				<span>De '. date ( 'd/m/Y', strtotime ( $data1 ) ) . ' a ' . date ( 'd/m/Y', strtotime ( $data2 ) ) .'</span>
				<span>Todos os Turnos</span>
				<hr class="dois">
				
					<table class="tabela-relatorio">
						<thead>
							<tr>
								<th>Tipo Usuário</th>
								<th>Pratos</th>
								<th>%Pratos</th>
								<th>Valores Arrecadados</th>
								<th>Valores Custo</th>
								<th>Despesa(Custo - Arrecadação)</th>
								<th>%Despesa</th>
							</tr>
						<thead>
						<tbody>
							';
		foreach ( $tipos as $tipo ) {
			
			$percentual = 0;
			if($listaDeDados ['total']['custo'] - $listaDeDados ['total']['valor'])
				$percentual = ($listaDeDados [$tipo->getId ()] ['custo'] - $listaDeDados [$tipo->getId ()] ['valor'])/($listaDeDados ['total'] ['custo'] - $listaDeDados ['total']['valor'])*100;
			$percentualPratos = 0;
			if($listaDeDados ['total']['pratos'])
				$percentualPratos = ($listaDeDados [$tipo->getId ()] ['pratos'])/($listaDeDados ['total'] ['pratos'])*100;
			
			echo'	<tr >	
						<th id="limpar">' . $tipo->getNome () . '</th>
						<td>' . $listaDeDados [$tipo->getId ()] ['pratos'] . '</td>
						<td>'.number_format ( $percentualPratos, 2, ',', '.' ).'</td>
						<td>R$ ' . number_format ( $listaDeDados [$tipo->getId ()] ['valor'], 2, ',', '.' ) . '</td>
						<td>R$ ' . number_format ( $listaDeDados [$tipo->getId ()] ['custo'], 2, ',', '.' ) . '</td>
						<td>R$ ' . number_format ( ($listaDeDados [$tipo->getId ()] ['custo'] - $listaDeDados [$tipo->getId ()] ['valor']), 2, ',', '.' ) . '</td>
						
						<td> ' . number_format ( ($percentual), 2, ',', '.' ) . '</td>
														
					</tr>';
		}		
		
		echo'		<tr id="soma">
						<th id="limpar">Somatório</th><td>' . $listaDeDados ['total'] ['pratos'] . '</td><td>-</td>
						<td>R$ ' . number_format ( $listaDeDados ['total'] ['valor'], 2, ',', '.' ) . '</td>
						<td>R$ ' . number_format ( $listaDeDados ['total'] ['custo'], 2, ',', '.' ) . '</td>
						<td>R$ ' . number_format ( ($listaDeDados ['total'] ['custo'] - $listaDeDados ['total']['valor']), 2, ',', '.' ) . '</td>
						<td>-</td>
					</tr>';
		
		echo'			</tbody>
					</table>';
					
		
		echo'<div class="doze colunas relatorio-rodape">
			<span>CATRACA | Copyright © 2015 - DTI</span>
			<span>Relatório Emitido em:'.$date = date('d-m-Y H:i:s').'</span>';
// 		echo '<a class="botao icone-printer"> Imprimir</a>';
		echo '	</div>	
				</div>';		
		
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		$listaDeTurnos = $turnoDao->retornaLista ();
		foreach ( $listaDeTurnos as $turno ) {
			$inicial = $turno->getHoraInicial ();
			$final = $turno->getHoraFinal ();
			
			$listaDeDados = array ();
			$totalValor = 0;
			$totalPratos = 0;
			foreach ( $tipos as $tipo ) {
				$listaDeDados [$tipo->getId ()] ['pratos'] = 0;
				$listaDeDados [$tipo->getId ()] ['valor'] = 0;
				$listaDeDados [$tipo->getId ()] ['custo'] = 0;
				
				foreach ( $listaDeDatas as $data ) {
					$dataInicial = $data . ' '.$turno->getHoraInicial();
					$dataFinal = $data . ' '.$turno->getHoraFinal();
					$tipoId = $tipo->getId ();
					$sql = "SELECT sum(1) pratos,sum(regi_valor_pago) valor  FROM registro
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
				INNER JOIN catraca ON catraca.catr_id = registro.catr_id
				INNER JOIN catraca_unidade ON catraca.catr_id = catraca_unidade.catr_id
				WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId
				$strFiltroUnidade;";
					foreach ( $dao->getConexao ()->query ( $sql ) as $linha ) {
						$ultimoCusto = $this->pegaUltimoCusto($idUnidade);
						$pratos = $linha ['pratos'];
						$valor = $linha ['valor'];
						$listaDeDados [$tipo->getId ()] ['pratos'] += $pratos;
						$listaDeDados [$tipo->getId ()] ['valor'] += $valor;
						$listaDeDados [$tipo->getId ()] ['custo'] += $ultimoCusto * $pratos;

						$totalValor += floatval ( $valor );
						$totalPratos += intval ( $pratos );
						$listaDeDados ['total'] ['pratos'] = $totalPratos;
						$listaDeDados ['total'] ['valor'] = $totalValor;
						$listaDeDados ['total'] ['custo'] = $totalPratos * $ultimoCusto;
					}
					
				}
			}
			
		echo '<div class="doze colunas borda relatorio">
				<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>
				<hr class="um">
				<h3>'.$strUnidade.'</h3>
				<span>Data: '. date ( 'd/m/Y', strtotime ( $data1 ) ) . ' e ' . date ( 'd/m/Y', strtotime ( $data2 ) ) .'</span>
				<span>Unidade Acadêmica:</span>
				<span>Turno: '.$turno->getDescricao().'</span>
				<hr class="dois">
						<table class="tabela-relatorio">
							<thead>								
									<tr>
									<th>Tipo Usuário</th>
									<th>Pratos</th>
									<th>%Pratos</th>
									<th>Valores Arrecadados</th>
									<th>Valores Custo</th>
									<th>Despesa(Custo - Arrecadação)</th>
									<th>%Despesa</th>
								
								</tr>';
		foreach ( $tipos as $tipo ) {
			$percentual = 0;
			if($listaDeDados ['total']['custo'] - $listaDeDados ['total']['valor'])
				$percentual = ($listaDeDados [$tipo->getId ()] ['custo'] - $listaDeDados [$tipo->getId ()] ['valor'])/($listaDeDados ['total'] ['custo'] - $listaDeDados ['total']['valor'])*100;
			$percentualPratos = 0;
			if($listaDeDados ['total']['pratos'])
				$percentualPratos = ($listaDeDados [$tipo->getId ()] ['pratos'])/($listaDeDados ['total'] ['pratos'])*100;
			
			
			echo '<tr >
					<th id="limpar">' . $tipo->getNome () . '</th>
					<td>' . $listaDeDados [$tipo->getId ()] ['pratos'] . '</td>
					<td>'.number_format ( $percentualPratos, 2, ',', '.' ).'</td>
					<td>R$ ' . number_format ( $listaDeDados [$tipo->getId ()] ['valor'], 2, ',', '.' ) . '</td>
					<td>R$ ' . number_format ( $listaDeDados [$tipo->getId ()] ['custo'], 2, ',', '.' ) . '</td>
					<td>R$ ' . number_format ( ($listaDeDados [$tipo->getId ()] ['custo'] - $listaDeDados [$tipo->getId ()] ['valor']), 2, ',', '.' ) . '</td>
					<td> ' . number_format ( ($percentual), 2, ',', '.' ) . '</td>
				</tr>';
		}
		echo '<tr id="soma">
			<th id="limpar">Somatário</th><td>' . $listaDeDados ['total'] ['pratos'] . '</td>';
		echo '<td>-</td>';
		echo '<td>R$ ' . number_format ( $listaDeDados ['total'] ['valor'], 2, ',', '.' ) . '</td>';
		echo '<td>R$ ' . number_format ( $listaDeDados ['total'] ['custo'], 2, ',', '.' ) . '</td>';
		echo '<td>R$ ' . number_format ( ($listaDeDados ['total'] ['custo'] - $listaDeDados ['total'] ['valor']), 2, ',', '.' ) . '</td><td>-</td>';
		echo '</tr>';
		echo '</table>';
		echo '</div>';
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
	

	*/
}

?>