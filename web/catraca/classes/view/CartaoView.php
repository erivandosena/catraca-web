<?php
class CartaoView {
	
	public function formBuscaCartao(){
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
		
										<label for="opcoes-1">
											<object class="rotulo texto-preto">Buscar por: </object>
											<select name="opcoes-1" id="opcoes-1" class="texto-preto">
												<option value="1">Numero</option>
		
											</select>
											<input class="texto-preto" type="text" name="numero" id="campo-texto-2" /><br>
											<input type="submit" />
										</label>
		
									</form>
									</div>';
	}
	public function mostraResultadoBuscaDeCartoes($cartoes) {
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Busca de Cartões:</h2>';
		echo '</div>';
		echo '<div class="borda">
				<table class="tabela borda-vertical zebrada texto-preto">
				<thead>
					<tr>
			            <th>Numero</th>
			            <th>Créditos</th>
			            <th>Tipo de Usuário</th>
			            <th>Selecionar</th>
			        </tr>
			    </thead>
			<tbody>';
		foreach ( $cartoes as $cartao) {
			$this->mostraLinhaDaBuscaCartao ( $cartao);
		}
		echo '</tbody></table></div>';
	}
	public function mostraLinhaDaBuscaCartao(Cartao $cartao) {
		echo '<tr>';
		echo '<td>' .  $cartao->getNumero() . '</a></td>';
		echo '<td>' .$cartao->getCreditos(). '</td>';
		echo '<td>' . $cartao->getTipo()->getNome() . '</td>';
		echo '<td class="centralizado"><a href="?pagina=cartao&cartaoselecionado=' . $cartao->getId() . '"><span class="icone-checkmark texto-verde2 botao" title="Selecionar"></span></a></td>';
		echo '</tr>';
	}
	public function mostraCartaoSelecionado(Cartao $cartao){
		echo '<div class="borda">
				Nome: ' . $cartao->getNumero() . '
				<br>Creditos: ' . $cartao->getCreditos() . '
				<br>Nome do Tipo: ' . $cartao->getTipo()->getNome(). '
				</div>';
	}
	public function formBuscaUsuarios() {
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
		
										<label for="opcoes-1">
											<object class="rotulo texto-preto">Buscar por: </object>
											<select name="opcoes-1" id="opcoes-1" class="texto-preto">
												<option value="1">Nome</option>
		
											</select>
											<input class="texto-preto" type="text" name="nome" id="campo-texto-2" /><br>
											<input type="submit" />
										</label>
		
									</form>
									</div>';
	}
	public function formBuscaVinculo() {
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
	
										<label for="parametro">Buscar por:</label>
											<select name="parametro" id="parametro" class="texto-preto">
												<option value="1">Nome do Usuário</option>
											</select>';
		if(isset($_GET['filtro_data']))
			echo '<input type="hidden" name="filtro_data" value="'.$_GET['filtro_data'].'"/>';
		echo '		
											<input class="texto-preto" type="text" name="busca_vinculos" id="busca_vinculos" /><br>
											<input type="submit" />
										
	
									</form>
									</div>';
	}
	public function formBuscaVinculoIsencao() {
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
	
										<label for="parametro">Buscar por:</label>
											<select name="parametro" id="parametro" class="texto-preto">
												<option value="1">Nome do Usuário</option>
											</select>';
		if(isset($_GET['filtro_data_isen']))
			echo '<input type="hidden" name="filtro_data_isen" value="'.$_GET['filtro_data_isen'].'"/>';
		echo '
											<input class="texto-preto" type="text" name="busca_vinculos_isen" id="busca_vinculos_isen" /><br>
											<input type="submit" />
	
	
									</form>
									</div>';
	}
	public function filtroData(){
		
		$dataHoje = date ('Y-m-d') . 'T' . date ( 'H:00:01' );
		
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
										<label for="filtro_data">Filtro de Data:</label>
											<input class="texto-preto" value="'.$dataHoje.'" type="datetime-local" name="filtro_data" id="filtro_data" /><br>';
		if(isset($_GET['busca_vinculos']))
			echo '<input type="hidden" name="busca_vinculos" value="'.$_GET['busca_vinculos'].'"/>';
		echo '
											<input type="submit" />
									</form>
									</div>';
	}
	public function filtroDataIsencao(){
	
		$dataHoje = date ('Y-m-d') . 'T' . date ( 'H:00:01' );
	
		echo '					<div class="borda">
									<form method="get" action="" class="formulario em-linha" >
										<label for="filtro_data_isen">Filtro de Data:</label>
											<input class="texto-preto" value="'.$dataHoje.'" type="datetime-local" name="filtro_data_isen" id="filtro_data_isen" /><br>';
		if(isset($_GET['busca_vinculos_isen']))
			echo '<input type="hidden" name="busca_vinculos_isen" value="'.$_GET['busca_vinculos_isen'].'"/>';
		echo '
											<input type="submit" />
									</form>
									</div>';
	}
	/**
	 *
	 * @param array $usuarios        	
	 */
	public function mostraResultadoBuscaDeUsuarios($usuarios) {
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Resultado da busca:</h2>';
		echo '</div><div class="borda">
				<table class="tabela borda-vertical zebrada texto-preto">
				<thead>
					<tr>
											            <th>Nome</th>
											            <th>CPF</th>
											            <th>Passaporte</th>
											            <th>Status Discente</th>
														<th>Status Servidor</th>
														<th>Tipo de Usuario</th>
											            <th>Selecionar</th>
											        </tr>
											    </thead>
												<tbody>';
		foreach ( $usuarios as $usuario ) {
			$this->mostraLinhaDaBusca ( $usuario );
		}
		echo '</tbody></table></div>';
	}
	
	
	
	public function mostraLinhaDaBusca(Usuario $usuario) {
		echo '<tr>';
		echo '<td>' . $usuario->getNome () . '</a></td>';
		echo '<td>' . $usuario->getCpf () . '</td>';
		echo '<td>' . $usuario->getPassaporte () . '</td>';
		echo '<td>' . $usuario->getStatusDiscente () . '</td>';
		echo '<td>' . $usuario->getStatusServidor () . '</td>';
		echo '<td>' . $usuario->getTipodeUsuario () . '</td>';
		echo '<td class="centralizado"><a href="?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna () . '"><span class="icone-checkmark texto-verde2 botao" title="Selecionar"></span></a></td>';
		echo '</tr>';
	}
	

	public function mostraSelecionado(Usuario $usuario) {
		echo '<div class="borda">
				Nome: ' . $usuario->getNome () . '
				<br>Login: ' . $usuario->getLogin () . '
				<br>Identidade: ' . $usuario->getIdentidade () . '
				<br> CPF: ' . $usuario->getCpf () . '
				<br> Passaporte: ' . $usuario->getPassaporte() . '
				<br>Tipo de Usuario: ' . $usuario->getTipodeUsuario() . '
				<br>Status Servidor: ' . $usuario->getStatusServidor(). '
				<br>Categoria: ' . $usuario->getCategoria(). '
				<br>SIAPE: ' . $usuario->getSiape(). '
				
				<br>Status Discente: ' . $usuario->getStatusDiscente(). '
				<br>Nivel Discente: ' . $usuario->getNivelDiscente(). '
				<br>Matricula Discente: ' . $usuario->getMatricula() . '</div>';
	}
	
	
	
	public function mostraVinculos($lista){
		if(!count($lista))
		{
			echo '<div class="borda"><p>Nenhum ítem na lista</p></div>';
			return;
		}
		echo '<div class="borda">
						<table class="tabela borda-vertical zebrada texto-preto">';
		echo '<tr>
								<th>Avulso</th>
								<th>Responsável</th>
								<th>Tipo</th>
								<th>Cartão</th>
								<th>Validade</th>
								<th>Isento</th>
								<th>Detalhes</th>
							</tr>';
		foreach ( $lista as $vinculo) {
			$this->mostraLinhaVinculo($vinculo);
			
		}
		echo '</table></div>';
		
	}
	public function mostraLinhaVinculo(Vinculo $vinculo){
		echo '<tr>';
		if($vinculo->isAvulso())
			echo 	'<td>Sim</td>';
		else 
			echo 	'<td>Não</td>';
		
		echo '
				<td><a href="?pagina=cartao&selecionado='.$vinculo->getResponsavel()->getIdBaseExterna().'">' . $vinculo->getResponsavel()->getNome(). '</a></td>
				<td>' .$vinculo->getCartao()->getTipo()->getNome() . '</td>
				<td><a href="?pagina=cartao&cartaoselecionado='.$vinculo->getCartao()->getId().'">' . $vinculo->getCartao()->getNumero() . '</a></td>
				<td>' . date("d/m/Y G:i:s", strtotime($vinculo->getFinalValidade())) . '</td>';
		if($vinculo->getIsencao()->getId())
			echo '<td>Sim</td>';
		else
			echo '<td>Não</td>';
		echo '
				<td><a href="?pagina=cartao&vinculoselecionado='.$vinculo->getId().'">Detalhes</a></td>
			</tr>';
	}
	public function mostraFormAdicionarVinculo($listaDeTipos, $idSelecionado){
		$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'H:00:01' );
		$dataHoje = date ('Y-m-d') . 'T' . date ( 'H:00:01' );
			
		echo '<div class="borda">
				<script type="text/javascript">
				function modificaForm(campoCheck){
					if(campoCheck.checked){
						document.getElementById("vinc_refeicoes").disabled = 0;
						document.getElementById("descricao").disabled = 0;
						//document.getElementById("cadastrar").style.visibility = "visible";
					}
					else{
						document.getElementById("vinc_refeicoes").disabled = 1;
						document.getElementById("descricao").disabled = 1;
						//document.getElementById("vinc_refeicoes").style.visibility = "hidden";
					}
				}
				
				</script>
				<form method="post" action="" class="formulario sequencial texto-preto" >
						    <label for="numero_cartao">Número do Cartão</label>
						        <input type="text" name="numero_cartao" id="numero_cartao" />
							<label for="inicio_vinculo">Início:</label>
						         <input id="inicio_vinculo" type="datetime-local" name="inicio_vinculo" value="' . $dataHoje . '" />
						    <label for="validade">Validade:</label>
						         <input id="validade" type="datetime-local" name="data_validade" value="' . $daqui3Meses . '" />
						     <label for="tipo">Tipo</label>
						       <select id="tipo" name="tipo">';
		foreach ( $listaDeTipos as $tipo) {
			echo '<option value="' . $tipo->getId() . '">' . $tipo->getNome() . '</option>';
		}
		echo '

			        </select><br>
	
			        <label for="avulso">Avulso:</label>
			            <input id="avulso" onchange="modificaForm(this)" type="checkbox" name="avulso" value="sim"/>
			        
				<label for="vinc_refeicoes"> Quantidade de refeições:</label>
			        <input disabled type="number" min="1" max="200" value="1" name="quantidade_refeicoes" id="vinc_refeicoes" />
				
				<label for="descricao"> Descrição:</label>
			        <textarea disabled type="text" placeholder="O Motivo desse vínculo avulso" name="descricao" id="descricao" ></textarea>
				<input type="hidden" name="id_base_externa"  value="' . $idSelecionado . '"/>
			   <br> <br>	<input  type="submit"  name="salvar" value="Salvar"/>
			</form>
			</div>';
	}
	public function mostraSucesso($mensagem){
		echo '<div class="borda"><p>'.$mensagem.'</p></div>';
	
	}
	public function mostrarVinculoDetalhe(Vinculo $vinculo){
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Vinculo Selecionado:</h2>';
		echo '</div>';
		echo '<div class="borda">';
		if($vinculo->isAvulso())
			echo '<p>Avulso</p>';
		echo '<p>Responsável: '.ucwords(strtolower($vinculo->getResponsavel()->getNome())).'</p>';
		echo '<p>Cartão: '.$vinculo->getCartao()->getNumero().'</p>';
		echo '<p>Créditos no Cartão: R$' . number_format($vinculo->getCartao()->getCreditos(), 2, ',', '.').'</p>';
		echo '<p>Tipo de Vínculo: '.$vinculo->getCartao()->getTipo()->getNome().'</p>';
		echo '<p>Refeições Por Turno: '.$vinculo->getQuantidadeDeAlimentosPorTurno().'</p>';
		
		if($vinculo->isActive()){
			echo '<p>Vinculo ativo</p>';
			echo '<p>Início do Vínculo: '.date('d/m/Y H:i:s', strtotime($vinculo->getInicioValidade())).'</p>';
			echo '<p>Fim do Vínculo: '.date('d/m/Y H:i:s', strtotime($vinculo->getFinalValidade())).'</p>';
			
			echo '<a class="botao b-erro" href="?pagina=cartao&vinculoselecionado='.$vinculo->getId().'&deletar=1">Eliminar Vinculo</a>';
		}
		else{
			echo '<p>Vinculo inativo</p>';
			echo '<p>Início do Vínculo: '.date('d/m/Y H:i:s', strtotime($vinculo->getInicioValidade())).'</p>';
			echo '<p>Fim do Vínculo: '.date('d/m/Y H:i:s', strtotime($vinculo->getFinalValidade())).'</p>';
			
			
			
		}
		
		
		
		echo '</div>';
		
	}
	
	
	public function mostraIsencaoDoVinculo(Vinculo $vinculo){
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Vinculo Selecionado:</h2>';
		echo '</div>';
		echo '<div class="borda">';
		if($vinculo->getIsencao()->getId())
		{
			$tempoA = strtotime($vinculo->getIsencao()->getDataDeInicio());
			$tempoB = strtotime($vinculo->getIsencao()->getDataFinal());
			$tempoAgora = time();
			if($tempoAgora > $tempoA && $tempoAgora < $tempoB){
				echo '<p>Isenção ativa</p>';
				echo '<p>Início da Isenção: '.date('d/m/Y H:i:s', strtotime($vinculo->getIsencao()->getDataDeInicio())).'</p>';
				echo '<p>Fim da Isenção: '.date('d/m/Y H:i:s', strtotime($vinculo->getIsencao()->getDataFinal())).'</p>';
				echo '<a href="?pagina=cartao&vinculoselecionado='.$vinculo->getId().'&delisencao=1">Eliminar Isenção</a>';
				
			}
			else if($tempoAgora < $tempoB){
				echo '<p>Isenção no Futuro</p>';
				echo '<p>Início da Isenção: '.date('d/m/Y H:i:s', strtotime($vinculo->getIsencao()->getDataDeInicio())).'</p>';
				echo '<p>Fim da Isenção: '.date('d/m/Y H:i:s', strtotime($vinculo->getIsencao()->getDataFinal())).'</p>';
				echo '<p><a href="?pagina=cartao&vinculoselecionado='.$vinculo->getId().'&delisencao=1">Eliminar Isenção</a></p>';
			}else
			{
				echo '<p>Isenção inativa</p>';
			}
				
			
				
		}
		echo '</div>';
	}
	
	public function formAdicionarIsencao($idSelecionado){
		
		$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'H:00:01' );
		$hoje = date ('Y-m-d') . 'T' . date ( 'H:00:01' );
		
		
		
		echo '<div class="borda">
				<form method="post" action="" class="formulario sequencial texto-preto" >
					
						    <label for="isen_inicio">Início:</label>
						         <input id="isen_inicio" type="datetime-local" name="isen_inicio" value="' . $hoje . '" />
				    	    <label for="isen_fim">Fim:</label>
						         <input id="isen_fim" type="datetime-local" name="isen_fim" value="' . $daqui3Meses . '" />
							<input type="hidden" name="id_card"  value="' . $idSelecionado . '"/>
			   <br> <br>	<input  type="submit"  name="salve_isencao" value="Salvar"/>
			</form>
			</div>';
		
	}
	
	public function formAdicionarCreditos($idSelecionado){
	
		$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'H:00:01' );
		$hoje = date ('Y-m-d') . 'T' . date ( 'H:00:01' );
	
	
	
		echo '<div class="borda">
				<form method="post" action="" class="formulario sequencial texto-preto" >
			
						   
				    	    <label for="valor_creditos">Valor A Adicionar:</label>
						         <input id="valor_creditos" type="number"  max="100"  name="valor_creditos" step="0.01" value="1.6" />
							<input type="hidden" name="id_card"  value="' . $idSelecionado . '"/>
			   <br> <br>	<input  type="submit"  name="salve_creditos" value="Salvar"/>
			</form>
			</div>';
	
	}
	
}

?>