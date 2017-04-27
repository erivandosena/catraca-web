<?php
/**
 * Nesta Classe estão contidos os Códigos HTML, responsáveis pela geração das Telas.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package View
 */
/**
 * Nesta Classe estão contidos os Códigos HTML
 * responsáveis por gerar os elementos e as telas da página Catraca Virtual.
 */
class CatracaVirtualView {
	
	/**
	 * Gera um formulário para buscar pelo Usuario através do seu cartão.
	 */
	public function formBuscaCartao() {
		echo '	<script>
					$(document).bind(\'autofocus_ready\', function() {
				    	if (!("autofocus" in document.createElement("input"))) {
				      		$("#numero_cartao").focus();
				    	}
				  	});
				</script>
					<form method="get" action="" class="formulario em-linha" >
						<input type="hidden" name="pagina" value="gerador" />
						<label for="numero_cartao">
							<object class="rotulo texto-preto">Buscar por Número: </object><br><br>		
							<input class="texto-preto" type="number" name="numero_cartao" id="numero_cartao" autofocus /><br>
							 <script>$(document).trigger(\'autofocus_ready\');</script>
							<input type="submit" />
						</label>
					</form>';
	}
	
	/**
	 * Gera o formulário paara a seleção do RU a ser utilizado.
	 * 
	 * @param array $listaDeCatracas        	
	 */
	public function formSelecionarRu($listaDeCatracas) {
		echo '	<div class="navegacao">
					<div class = "simpleTabs">
				        <ul class = "simpleTabsNavigation">
							<li><a href="#">Cadastro</a></li>
				        </ul>
			        	<div class = "simpleTabsContent">
							<div class="doze colunas borda">		
								<form action="" method="post">
									<label for="catraca_id">Selecione o Restaurante:</label><br>
				       				<select name="catraca_id" id="catraca_id">';
		
		foreach ( $listaDeCatracas as $catraca ) {
			echo '<option value="' . $catraca->getId () . '">' . $catraca->getNome () . '</option>';
		}
		echo ' 		      			</select><br>
									<input name="catraca_virtual" type="submit" class="botao" VALUE="Selecionar" />
								</form>			
							</div>
						</div>
					</div>
				</div>';
	}
	
	/**
	 * Gera uma tabela contendo as informações referentes ao RU anteriomente selecionado.
	 * A tabela distingue tipos e quantidades de refeições do RU.
	 * 
	 * @param array $listaDeTipos        	
	 * @param array $quantidades        	
	 * @param Catraca $catraca        	
	 */
	public function exibirQuantidadesDeCadaTipo($listaDeTipos, $quantidades, Catraca $catraca) {
		echo '	<table class="tabela borda-vertical zebrada no-centro centralizado">
					<thead>
						<tr>
							<th>Unidade</th>';
		
		foreach ( $listaDeTipos as $tipo ) {
			echo '			<th>' . $tipo->getNome () . '</th>';
		}
		
		echo '				<th>Total</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<th>' . $catraca->getNome () . '</th>';
		$somatorio = 0;
		foreach ( $quantidades as $quantidade ) {
			$somatorio += $quantidade;
			echo '			<td>' . $quantidade . '</td>';
		}
		echo '				<td>' . $somatorio . '</td>		
						</tr>';
		echo '		</tbody>
				</table>';
	}
}

?>