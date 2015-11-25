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
	
	public function mostraLista() {
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
	/**
	 *
	 * @param array $usuarios        	
	 */
	public function mostraResultadoBuscaDeUsuarios($usuarios) {
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Resultado da busca:</h2>';
		echo '</div>
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
		echo '</tbody></table>';
	}
	
	/**
	 *
	 * @param array $usuarios
	 */
	public function mostraResultadoBuscaDeCartoes($cartoes) {
		echo '<div class="doze linhas">';
		echo '<br><h2 class="texto-preto">Resultado da busca:</h2>';
		echo '</div>
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
		foreach ( $cartoes as $cartao) {
			$this->mostraLinhaDaBuscaCartao ( $cartao);
		}
		echo '</tbody></table>';
	}
	public function mostraLinhaDaBuscaCartao(Cartao $cartao) {
		echo '<tr>';
		echo '<td>' . $cartao->getId() . '</a></td>';
		echo '<td>' . $cartao->getNumero(). '</td>';
		echo '<td>' . $cartao->getCreditos() . '</td>';
		echo '<td>' . $cartao->getTipo()->getNome() . '</td>';
		echo '<td></td>';
		echo '<td></td>';
		echo '<td class="centralizado"><a href="?pagina=cartao&cartaoselecionado=' . $cartao->getId() . '"><span class="icone-checkmark texto-verde2 botao" title="Selecionar"></span></a></td>';
		echo '</tr>';
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
	public function mostraCartaoSelecionado(Cartao $cartao){
		echo '<div class="borda">
				Nome: ' . $cartao->getNumero() . '
				<br>Creditos: ' . $cartao->getCreditos() . '
				<br>Nome do Tipo: ' . $cartao->getTipo()->getNome(). '
				</div>';
	}
	
	
	public function mostraVinculos($lista){
		echo '<div class="borda">
						<table class="tabela borda-vertical zebrada texto-preto">';
		echo '<tr>
								<th>ID usuario</th>
								<th>Nome</th>
								<th>Tipo</th>
								<th>Cartao</th>
								<th>Inicio</th>
								<th>Fim</th>
		
							</tr>';
		foreach ( $lista as $vinculo) {
			$this->mostraLinhaVinculo($vinculo);
			
		}
		echo '</table></div>';
		
	}
	public function mostraLinhaVinculo(Vinculo $vinculo){
		echo '<tr>
				<td>' . $vinculo->getResponsavel()->getIdBaseExterna() . '</td>
				<td>' . $vinculo->getResponsavel()->getNome(). '</td>
				<td>' .$vinculo->getCartao()->getTipo()->getNome() . '</td>
				<td>' . $vinculo->getCartao()->getNumero() . '</td>
				<td>' . $vinculo->getInicioValidade() . '</td>
				<td>' . $vinculo->getFinalValidade() . '</td>
			</tr>';
	}
	public function mostraFormAdicionarVinculo($listaDeTipos, $idSelecionado){
		$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'H:00:01' );
			
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
	
}

?>