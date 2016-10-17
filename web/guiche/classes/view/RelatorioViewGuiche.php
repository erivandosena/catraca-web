<?php

class RelatorioViewGuiche{
	
	
	public function formPesquisar($listaOperador){
		
		echo'	<div class="doze colunas borda relatorio">
					<form action="" method="post" class="formulario-organizado">
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
							Data Inicio: <input type="date" name="data_inicio">
							- Hora Inicio: <input type="time" name="hora_inicio">
						</label><br>
						<label for="data_fim">
							Data Fim: <input type="date" name="data_fim">
							- Hora Fim: <input type="time" name="hora_fim">
						</label><br>
						<input type="submit" value="Gerar" name="gerar">
		
					</form>
				</div>';
	}
	
}

?>