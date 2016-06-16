<?php

class OperacaoController{
	
	public static function main($nivel){
		
		$controller = new OperacaoController();
		$controller->telaOperacao();
		
	}
	
	public function selecionaUnidade(){
		
	}
	
	public function telaOperacao(){
		
		$unidade = new Unidade();
		$unidadeDao = new UnidadeDAO();
		$unidades = $unidadeDao->retornaLista();	
		
		echo'	<div class="borda relatorio">
					<form action="" class="formulario em-linha" method="post">
						<label for="">
							<object class="rotulo">Selecione a Unidade: </object>
							<select name="unidade" id="">';
		foreach ($unidades as $unidade)
		echo'						<option value="'.$unidade->getId().'">'.$unidade->getNome().'</option>';
		echo'				</select>
						</label>							
						<input type="submit" name="buscar" value="Buscar">
					</form>						
				</div>';
				
		if(isset($_POST['buscar'])){
			
			$catraca = new Catraca();
			$unidade->setId($_POST['unidade']);
			$idUnidade = $unidade->getId();
			$catracas = $unidadeDao->retornaCatracasPorUnidade($unidade);
		
		echo'	<div class="borda relatorio">
					<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Lista de Catracas - RU</h2>
					<table class="tabela borda-vertical zebrada">
						<thead>
							<tr>
								<th>Código</th>
								<th>IP</th>
								<th>Nome da Catraca</th>
								<th>Operacao</th>
								<th> - </th>
							</tr>			
						</thead>
						<tbody>';
		$i = 1;
		foreach ($catracas as $catraca){
			
			echo'			<tr>
								<td>'.$i++.'</td>
								<td>'.$catraca->getIp().'</td>
								<td>'.$catraca->getNome().'</td>
								<td>'.$catraca->getOperacao().'</td>
							</tr>';
		}		
		echo'			</tbody>
					</table>
				</div>';
		}
	}
	
}

?>