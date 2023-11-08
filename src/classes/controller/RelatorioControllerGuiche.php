<?php
class RelatorioControllerGuiche {
	private $dao;
	public function __construct()
	{
		$this->dao = new DAO ();
	}
	public static function main($nivel) {
		switch ($nivel) {
			case Sessao::NIVEL_SUPER :
				$relatorio = new RelatorioControllerGuiche ();
				$relatorio->relatorioGuiche ();
				break;
			case Sessao::NIVEL_ADMIN :
				$relatorio = new RelatorioControllerGuiche ();
				$relatorio->relatorioGuiche ();
				
				break;
			case Sessao::NIVEL_USUARIO_EXTERNO:
			    $relatorio = new RelatorioControllerGuiche ();
			    $relatorio->relatorioGuiche ();
			    
			    break;
			default :
			    echo "Acesso restrito";
				return;
				break;
		}
	}
	public function showFormParameters() {
		echo '
		<script src="https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.13.5/js/standalone/selectize.min.js" integrity="sha512-JFjt3Gb92wFay5Pu6b0UCH9JIOkOGEfjIi7yykNWUwj55DBBp79VIJ9EPUzNimZ6FvX41jlTHpWFUQjog8P/sw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.13.5/css/selectize.bootstrap2.css" integrity="sha512-Q4lVRLPgL4dk2/TIxGMiaTQszMFzW6/wULNrA0r4FCeu2eVwgfPDOXbZtntaWMV52uvKFmRx09as0caMjOeYBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
		
		<div class="borda card">
					<form action="" id="form-report-guiche" method="get" class="formulario-organizado">
						<label for="operador">
							<object data="" type="" class="rotulo">Operador:</object>
							<select name="operador" id="operador" required>';
		
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$result = $this->dao->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			
			echo '
						<option value="' . $linha ['usua_id'] . '">' . ucwords ( strtolower ( htmlentities ( $linha ['usua_nome'] ) ) ) . '</option>';
		}
		
		echo '			<option value="" selected>Selecione os Operadores</option>	
						</select>
						</label><br>
						<div class="row">
							<div class="col-md-6 mb-3">
								<label for="data_inicio">Data Início</label>
								<input type="date" class="form-control" id="data_inicio" name="data_inicio" value="" required>
							</div>

							<div class="col-md-6 mb-3">
								<label for="data_fim">Data Final</label>
								<input type="date" class="form-control" id="data_fim" name="data_fim" value="" required>
							</div>
						</div>
						
						<input type="hidden" value="relatorio_guiche" name="pagina">		
				
						<input type="submit" id="submit-default" value="Gerar" name="gerar">		
						<input type="submit" id="submit-excel" name="gerar" value="Excel">
					</form>
					<script>
						$("#operador").selectize({
							maxItems: 100,
					  	});
						function prepareData(e) {

								e.preventDefault();
								var data = {};
								data["operadores"] = $("#operador").val();
								data["data_fim"] = $("#data_fim").val();
								data["data_inicio"] = $("#data_inicio").val();
								data["gerar"] = e.target.value;
								var novaUrl = "";
	
								var i = 0;
		
								Object.keys(data).forEach(function (key) {
									
									if(data[key] != ""){
										
									
										if(i != 0){
											novaUrl += "&";
										}
										novaUrl += key+"="+data[key];
										i++;
									}
								});
								novaUrl = "?pagina=relatorio_guiche&"+novaUrl;
								window.location.href = novaUrl;
						}
						$("#submit-default").on("click", prepareData);
						$("#submit-excel").on("click", prepareData);
					</script>
				</div>';
	}
	public function relatorioGuiche() {
		
		if(!isset($_GET['gerar'])) {
			$this->showFormParameters();
			return;
		}

		if(!isset($_GET ['data_inicio'])) {
			return;
		}
		if(!isset($_GET ['data_fim'])) {
			return;
		}
		if(!isset($_GET ['operadores'])) {
			return;
		}

		
		$dataInicio = date('Y-m-d', strtotime($_GET ['data_inicio'])).' 00:00:00';
		$dataFim = date('Y-m-d', strtotime($_GET ['data_fim'])).' 23:59:59';
		
		$listIds = explode(",", $_GET ['operadores']);

		
		
		$filterOperador = " usuario.usua_id = ".implode(" OR usuario.usua_id = ", $listIds);
		
		
		
		$sqlTran = "SELECT * FROM transacao
				LEFT JOIN usuario as usuario
				on transacao.usua_id = usuario.usua_id 
				WHERE (transacao.tran_data  BETWEEN '$dataInicio' AND '$dataFim') AND ($filterOperador)";
		$result = $this->dao->getConexao ()->query ( $sqlTran );
		$listData = array();
		

		foreach ( $result as $dado ) {
			$newData = new stdClass();
			$newData->data = $dado ['tran_data'];
			$newData->descricao = $dado ['tran_descricao'];
			$newData->nome = $dado ['usua_nome'];
			$newData->valor = $dado ['tran_valor'];
			$listData[] = $newData;
		}
		if($_GET['gerar'] == 'Excel'){
			$titulo = "UNILAB - Universidade da Integração Internacional da Lusofonia Afro-Brasileira\nRelatório de Guichê de ".date("d/m/Y", strtotime($dataInicio)). " até ".date("d/m/Y", strtotime($dataFim));
			$this->printExcel($listData, $titulo);
		} else {
			$this->showData($listData);
		}
	}
	public function printExcel($data, $titulo) {
		$dados = $titulo;
		$dados .= "\nData;Hora;Descrição;Operador;Valor\n";
		$valorTotal = 0;
		foreach ( $data as $element) {
			$valorTotal = $valorTotal + $element->valor;
			$dados .= date ( "d/m/Y", strtotime ( $element->data ) ) . ";" . date ( "H:i:s", strtotime ( $element->data ) ) . ";" . $element->descricao. ";" . $element->nome. ";" . number_format( $element->valor, 2, ",", ".") .";\n";
		}
		$dados .= "\nValor total;-;-;-;".$valorTotal;

		$nomeArquivo = "../tmp/relatorio".uniqid().".csv";
		if(fwrite($file=fopen($nomeArquivo,'w+'),$dados)) {
			header('Content-Description: File Transfer');
			header('Content-Disposition: attachment; filename="relatorio.csv"');
			header('Content-Type: application/octet-stream');
			header('Content-Transfer-Encoding: binary');
			header('Content-Length: ' . filesize($nomeArquivo));
			header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
			header('Pragma: public');
			header('Expires: 0');
			fclose($file);
			readfile($nomeArquivo);
			unlink($nomeArquivo);
		}

	}
	public function showData($data) {
		echo '	<div class="borda card">
			<h2>UNILAB<small class="fim">Universidade da Integração Internacional da Lusofonia Afro-Brasileira</small></h2>
			<hr class="um">	
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

		$valorTotal = 0;
		foreach ( $data as $element) {
			$valorTotal = $valorTotal + $element->valor;
			echo '	<tr>
					<td>' . date ( "d/m/Y", strtotime ( $element->data ) ) . '</td>
					<td>' . date ( 'H:i:s', strtotime ( $element->data ) ) . '</td>						
					<td>' . $element->descricao. '</td>
					<td>' . $element->nome. '</td>	
					<td>' . number_format( $element->valor, 2, ',', '.') .'</td>
				</tr>';
		}
		
		echo '	<tr id="soma">
						<th>Somatório</th>							
						<td> - </td>
						<td> - </td>
						<td> - </td>
						<td>R$ ' .  number_format($valorTotal, 2, ',', '.') . '</td>
					</tr>					
				</tbody>
			</table>
		</div>';
	}
}

?>