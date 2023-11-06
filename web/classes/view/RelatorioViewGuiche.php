<?php

class RelatorioViewGuiche{
	
	
	public function formPesquisar($listaOperador){
		
		$data_ini = date ('Y-m-d') . 'T' . date ( '00:00' );
		$data_fim = date ('Y-m-d') . 'T' . date ( '23:59' );
		
		echo'	<div class="doze colunas borda relatorio">
					<form action="" method="" class="formulario-organizado">
						<input type="hidden" name="pagina" value="relatorio_guiche">
						<label for="operador">
							<object data="" type="" class="rotulo">Operador:</object>
							<select name="operador" id="operador">
							<option value="">Selecione um operador</option>';
		foreach ($listaOperador as $linha){
			echo'
						<option value="'.$linha['usua_id'].'">'.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</option>';
		}
		echo'			<option value="">Todos os Operadores</option>
						</select>
						</label><br>
						<label for="data_inicio">
							Data Inicio: <input type="datetime-local" name="data_inicio" value="'.$data_ini.'">							
						</label><br>
						<label for="data_fim">
							Data Fim: <input type="datetime-local" name="data_fim" value="'.$data_fim.'">							
						</label><br>
						<label>
							<object data="" type="" class="rotulo">Tipo Operação:</object>
							<select name="operacoes" id="operacoes">
								<option values="">Todas as Operações</option>
								<option values="1">Venda</option>
								<option values="2">Estorno</option>
							</select>
						</label>
						<input type="submit" value="Gerar" name="gerar">
		
					</form>
				</div>';
	}
	
}

?>