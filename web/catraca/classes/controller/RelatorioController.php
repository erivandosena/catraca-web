<?php


class RelatorioController{
	private $view;
	private $dao;
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new RelatorioController();
				$controller->relatorio();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	
	public function relatorio(){
		$this->dao = new UnidadeDAO();
		$listaDeUnidades = $this->dao->retornaLista();
		
		echo '<div class="borda">
									<form action="" class="formulario sequencial">									
											<div id="data">
												<label for="opcoes-1">
													<object class="rotulo texto-preto">Unidade Acadêmica: </object>
													<select name="unidade" id="unidade" class="texto-preto">';
		foreach ($listaDeUnidades as $unidade){
			echo '<option value="'.$unidade->getId().'">'.$unidade->getNome().'</option>';
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
												<input type="hidden" name="pagina" value="relatorio" />
												<input  type="submit"  name="gerar" value="Gerar"/>
											</div>									    							
									</form>																			
									</div>';
		
		
		if(isset($_GET['gerar'])){
			$this->gerarRelatorios($_GET['unidade'], $_GET['data_inicial'], $_GET['data_final']);
						
		}
			
	}
	public function gerarRelatorios($idUnidade, $dateStart, $dataEnd){
		$idUnidade = intval($idUnidade);
		$dao = new TipoDAO(null, DAO::TIPO_PG_LOCAL);
		$tipos = $dao->retornaLista();
			
		$dateStart = new DateTime($dateStart);
		$dateEnd = new DateTime($dataEnd);

		//Prints days according to the interval
		$dateRange = array();
		while($dateStart <= $dateEnd){
			$listaDeDatas[] = $dateStart->format('Y-m-d');
			$dateStart = $dateStart->modify('+1day');
		}
		$listaDeDados = array();
		foreach($listaDeDatas as $data){
			$total = 0;
			foreach($tipos as $tipo){
					
				$dataInicial = $data.' 00:00:00';
				$dataFinal = $data.' 23:59:59';
				$tipoId = $tipo->getId();
		
				$sql = "SELECT sum(1) valor FROM registro
				INNER JOIN vinculo ON vinculo.vinc_id = registro.vinc_id
				INNER JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
				WHERE (regi_data BETWEEN '$dataInicial' AND '$dataFinal') AND vinculo_tipo.tipo_id =  $tipoId;";
				foreach($dao->getConexao()->query($sql) as $linha){
				$valor = $linha['valor'];
				}
		
						if($valor)
				$listaDeDados[$data][$tipo->getId()] = $valor;
				else
					$listaDeDados[$data][$tipo->getId()] = '-';
		
					$total += intval($valor);
					
			}
			$listaDeDados[$data]['total'] = $total;
		}
			
			
		echo '
		
		<div class=" doze colunas borda">';
			
			
			
			echo '<table class="tabela quadro no-centro fundo-branco">';
		echo '<tr class="centralizado"><td>Liberdade</td></tr>';
			echo '<tr>';
					echo '<td>Data</td>';
			foreach($tipos as $tipo){
		echo '<td>'.$tipo->getNome().'</td>';
		}
		echo '<td>Total</td>';
		echo '</tr>';
				foreach($listaDeDatas as $data){
		echo '<tr>';
				echo '<td>'.date('d/m/Y',strtotime($data)).'</td>';
						foreach($tipos as $tipo){
			
		echo '<td>'.$listaDeDados[$data][$tipo->getId()].'</td>';
			
			
		}
		echo '<td>'.$listaDeDados[$data]['total'].'</td>';
		echo '</tr>';
		}
		echo '</table>';
			
		echo '</div>';
			
		
	}
	
	
}


?>