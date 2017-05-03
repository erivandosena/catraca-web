<?php
/**
 * Classe utilizada para centralizar as demais Classes(DAO, Model, View, Util).
 * Esta classe será instaciada no index.php.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */

class RelatorioControllerGuiche {
	
	/**
	 * Metodo principal utilizada para controlar o acesso a classe através do nível de acesso do usuario.
	 *
	 * @param Sessao $nivelDeAcesso Recebe uma Sessão que contém o nível de acesso do usuario,
	 * esta Sessão é iniciada na página principal, durante o login do usuario.
	 */
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
			default :
				UsuarioController::main ( $nivel );
				break;
		}
	}
	
	/**
	 * Gera um relatório contendo as informações das transações realizadas pelos operadores.
	 * Realiza uma consulta na tabela transacao e soma todos os valores retornados.
	 * 
	 * Pode ser realizado um filtro por operador e data.
	 * 
	 */
	public function relatorioGuiche() {
		$dao = new DAO ();
		$usuarioDao = new UsuarioDAO ();
		$usuario = new Usuario ();
		$relatorioGuiche = new RelatorioControllerGuiche ();
		
		echo '	<div class="borda relatorio">
					<form action="" method="get" class="formulario-organizado">
						<label for="operador">
							<object data="" type="" class="rotulo">Operador:</object>
							<select name="operador" id="operador">';
		
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$result = $dao->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {			
			echo '
						<option value="' . $linha ['usua_id'] . '">' . ucwords ( strtolower ( htmlentities ( $linha ['usua_nome'] ) ) ) . '</option>';
		}
		
		echo '			<option value="" selected>Todos os Operadores</option>	
						</select>
						</label><br>
						<label for="data_inicio">
							Data Inicio: <input type="datetime-local" name="data_inicio">
						</label><br>
						<label for="data_fim">
							Data Fim: <input type="datetime-local" name="data_fim">
						</label><br>
						<input type="hidden" value="relatorio_guiche" name="pagina">				
						<input type="submit" value="Gerar" name="gerar">				
					</form>
				</div>';
		
		if (isset ( $_GET ['gerar'] )) {
			
			$dataInicio = date ( $_GET ['data_inicio'] );
			$dataFim = date ( $_GET ['data_fim'] );
			$idDoUsuario = ($_GET ['operador']);
			
			if ($dataInicio == null) {
				$dataInicio = date ( 'Y-m-d' ).' 00:00:00';
			}
			if ($dataFim == null) {
				$dataFim = date ( 'Y-m-d' ).' 23:59:59';
			}
			
			$operador = "";
			if ($idDoUsuario != null) {
				$operador = "AND usuario.usua_id = $idDoUsuario";
			}
			
			echo '	<div class="borda relatorio">
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
			
			$inicio = date("Y-m-d H:i:s", strtotime($dataInicio));
			$fim = date("Y-m-d H:i:s", strtotime($dataFim));
			
			$valorTotal = 0;
						
			$sqlTran = "SELECT * FROM transacao as trans 
					LEFT JOIN usuario as usuario
					on trans.usua_id = usuario.usua_id 
					WHERE (tran_data BETWEEN '$inicio' AND '$fim') $operador ";
			$result = $dao->getConexao ()->query ( $sqlTran );
			foreach ( $result as $dado ) {
				echo '	<tr>
							<td>' . date ( "d/m/Y", strtotime ( $dado ['tran_data'] ) ) . '</td>
							<td>' . date ( 'H:i:s', strtotime ( $dado ['tran_data'] ) ) . '</td>						
							<td>' . $dado ['tran_descricao'] . '</td>
							<td>' . $dado ['usua_nome'] . '</td>	
							<td>R$ ' . $dado ['tran_valor'] .' - ID:'.$dado['usua_id1'].'</td>
						</tr>';
			}
			
			$result = $dao->getConexao ()->query ( $sqlTran );
			foreach ( $result as $linha ) {
				$valor = $linha ['tran_valor'];
				floatval ( $valor );
				if ($linha) {
					$valorTotal = $valorTotal + $valor;
				}
			}
			
			echo '		<tr id="soma">
							<th>Somatório</th>							
							<td> - </td>
							<td> - </td>
							<td> - </td>
							<td>R$ ' . number_format ( $valorTotal, 2 ) . '</td>
						</tr>					
					</tbody>
				</table>
			</div>';
		}
	}
}

?>