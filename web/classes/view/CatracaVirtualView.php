<?php


/**
 * 
 * @author Jefferson Uchôa Ponte
 *
 */
class CatracaVirtualView{
	
	/**
	 * Formulário para seleção de uma catraca virtual para abrir. 
	 * Entre com um vetor de catracas.  
	 * @param unknown $listaDeCatracas
	 */
	public function formSelecionarRu($listaDeCatracas){

		echo '<div class="navegacao">
				<div class = "simpleTabs">
			       
						<div class="doze colunas borda">';
		
		echo '<form action="" method="post">
				<label for="catraca_id">Selecione o Restaurante:</label><br>
			        <select name="catraca_id" id="catraca_id">';
		
		foreach ($listaDeCatracas as $catraca){
			echo '<option value="'.$catraca->getId().'">'.$catraca->getNome().'</option>';
		}
		 
		echo '
				</select><br>
					<input name="catraca_virtual" type="submit" class="botao" VALUE="Selecionar" />
				</form>	';
		
		
		echo '</div>
				</div>
				
				</div>';
		
	}
	
	public function exibirQuantidadesDeCadaTipo($listaDeTipos, $quantidades, Catraca $catraca){
		echo '
				
							<table class="tabela borda-vertical zebrada no-centro centralizado">
							    <thead>
							        <tr>
												<th>Unidade</th>';
		foreach($listaDeTipos as $tipo){
			echo '<th>'.$tipo->getNome().'</th>';
		
		
		}
		echo '<th>Total</th></tr></thead><tbody>';
		echo '	<tr>
				<th>'.$catraca->getNome().'</th>';
		$somatorio = 0;
		foreach ($quantidades as $quantidade){
			$somatorio += $quantidade;
			echo '<td>'.$quantidade.'</td>';
		}
		echo '<td>'.$somatorio.'</td>';
		echo '</tr>';
		echo '</tbody></table>';
	}
	
}


?>