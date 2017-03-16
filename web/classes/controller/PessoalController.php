<?php
class PessoalController {
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_ADMIN:
				$controller = new PessoalController();
				$controller->consultarUsuario();
				break;
			case Sessao::NIVEL_SUPER:
				$controller = new PessoalController();
				$controller->consultarUsuario();
				break;
			default:	
				$controller = new PessoalController();
				$controller->telaPessoal();
				break;
		}
	}
	private $dao;
	private $view;
	
	public function consultarUsuario(){
		$this->view = new PessoalView();
		
		echo '<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">
						<li><a href="#">Identifica&ccedil;&atilde;o</a></li>
			        </ul>
		        <div class = "simpleTabsContent">';
		
		$this->view->formBuscaCartao();
		
		if(isset($_GET['numero_cartao'])){
			if(strlen($_GET['numero_cartao']) > 3){
		
				$cartao = new Cartao();
				$cartao->setNumero($_GET['numero_cartao']);
				$numeroCartao = $cartao->getNumero();
				$dataTimeAtual = date ( "Y-m-d G:i:s" );
				$sqlVerificaNumero = "SELECT * FROM usuario
				INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
				LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
				LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
				WHERE cartao.cart_numero = '$numeroCartao'
				";
				$result = $this->dao->getConexao()->query($sqlVerificaNumero);
				$idCartao = 0;
				$usuario = new Usuario();
				$tipo = new Tipo();
				$vinculoDao = new VinculoDAO($this->dao->getConexao());
				$vinculo = new Vinculo();
				foreach($result as $linha){
					$idDoVinculo = $linha['vinc_id'];
					$tipo->setNome($linha['tipo_nome']);
					$usuario->setNome($linha['usua_nome']);
					$usuario->setId($linha['usua_id']);
					$usuario->setIdBaseExterna($linha['id_base_externa']);
					$idCartao = $linha['cart_id'];
					
					$vinculo->setAvulso($linha['vinc_avulso']);
					$avulso = $linha['vinc_avulso'];
					if($avulso){
						$usuario->setNome("Avulso");
					}
					break;
				}
					
				if($idCartao){
		
					$vinculo->setId($idDoVinculo);
					$cartao->setId($idCartao);
					$vinculoDao->vinculoPorId($vinculo);
					$imagem = null;
		
					if(file_exists('fotos/'.$usuario->getIdBaseExterna().'.png')){
						$imagem = $usuario->getIdBaseExterna();
					}else {
						$imagem = "sem-imagem";
					}
		
						
		
					if(!$vinculo->isActive()){
						echo '<div id="pergunta">';
						$this->view->formMensagem("-erro", "vinculo não está ativo.");
						echo '	<a href="?pagina=cartao&numero_cartao='.$_GET['numero_cartao'].'&cartao_renovar=1" class="botao">Renovar</a>
							</div>';
						if(isset($_GET['cartao_renovar'])){
							if(isset($_POST['certeza'])){
								$usuarioDao = new UsuarioDAO($this->dao->getConexao());
		
								$usuarioDao->retornaPorIdBaseExterna($usuario);
		
								if($vinculoDao->usuarioJaTemVinculo($usuario))
								{
									$this->view->formMensagem("-ajuda", "Esse usuário já possui vínculo válido.");
									echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
									return;
								}
								if($vinculo->isAvulso()){
									$this->view->formMensagem("-ajuda", "Não existe renovação de vínculos avulsos!");
									echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
									return;
								}
		
								if(!$this->verificaSeAtivo($usuario)){
									$this->view->formMensagem("-erro", "Esse usuário possui um problema quanto ao status!");
									echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
									return;
								}
		
								$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'G:00:01' );
								$vinculo->setFinalValidade($daqui3Meses);
		
								if($vinculoDao->atualizaValidade($vinculo)){
									$this->view->formMensagem("-sucesso", "Vínculo Atualizado com Sucesso!");
								}else{
									$this->view->formMensagem("-erro", "Erro ao tentar renovar vínculo.");
								}
								echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
							}
		
							$this->view->formConfirmacaoRenovarVinculo();
						}
					}
				}else{
					$this->view->formMensagem("-erro", "Cartão Não possui Vínculo Válido.");
				}
			}
			$this->telaDeCreditos($usuario);
			$this->telaDeTransacoes($usuario);
		}
		
		
		echo '	</div>
		    </div>';
	
	}
	public function PessoalController(){
		$this->dao = new DAO();
	}
	public function telaPessoal(){
		
		echo '<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">
						<li><a href="#">Identifica&ccedil;&atilde;o</a></li>
			        </ul>
		        <div class = "simpleTabsContent">';

				$usuario = new Usuario();
				$sessao = new Sessao();
				$usuarioDao = new UsuarioDAO($this->dao->getConexao());
				$usuario->setId($sessao->getIdUsuario());
				$usuarioDao->preenchePorId($usuario);
				$this->telaDeCreditos($usuario);
				$this->telaDeTransacoes($usuario);

		echo '	 </div></div>';
		
		
	}
	public function telaDeTransacoes(Usuario $usuario){
		$idUsuario = $usuario->getId();
		$result = $this->dao->getConexao()->query("SELECT * FROM transacao 
				INNER JOIN usuario ON usuario.usua_id = transacao.usua_id
				WHERE usua_id1 = $idUsuario
				ORDER BY tran_data
				 DESC LIMIT 200");
		echo '<p>&Uacute;ltimas 200 transa&ccedil;&otilde;es</p>';
		echo '<table class="tabela borda-vertical zebrada texto-preto">';
		echo '<thead>';
		echo '<tr><th>Data/Hora</th><th>Valor</th><th>Descrição</th><th>Operador</th></tr>';
		echo '</thead>';
		echo '<tbody>';
		$totalCarregado = 0;
		foreach($result as $linha){
			$time = strtotime($linha['tran_data']);
				
			echo '<tr><td>'.date('d/m/Y H:i:s', $time).'</td><td>R$'.number_format ($linha['tran_valor'], 2, ',', '.' ).'</td><td>'.$linha['tran_descricao'].'<td>'.$linha['usua_nome'].'</td></td></tr>';
			$totalCarregado += $linha['tran_valor'];
		}
		echo '<tr><th>Total Recarregado: </th><th>R$'.number_format ( $totalCarregado, 2, ',', '.' ).'</th><th>-</th><th>-</th></tr>';
		echo '</tbody>';
		echo '</table>';
		
	}
	
	public function telaDeCreditos(Usuario $usuario){
		
		$vinculoDao = new VinculoDAO($this->dao->getConexao());
		
		$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);
		
		if(count($vinculos) < 1){
			echo "<p>Nenhum cartao ativo</p>";
		}
		else if(count($vinculos) == 1){
			echo '<p>Vínculo ativo:</p>';
			$this->exibirVinculos($vinculos);
			
			
		}else if(count($vinculos) > 1){
			echo '<p>Vínculos ativos</p>';
			$this->exibirVinculos($vinculos);
		}
		
		
		$vinculos = array();
		$vinculos = $vinculoDao->retornaVinculosVencidos($usuario);
		if(count($vinculos) < 1){
			echo "<p>Nenhum cartao Inativo</p>";
		}
		else if(count($vinculos) == 1 && $vinculos[0]->isActive()){
			echo '<p>Vínculo Inativo:</p>';
			
			$this->exibirVinculos($vinculos);
				
				
		}
		
	}
	public function exibirVinculos($vinculos){
		foreach($vinculos as $vinculo){
			$this->exibirVinculo($vinculo);
		}
	}
	
	public function exibirVinculo(Vinculo $vinculo){
		if($vinculo->isAvulso() && !$vinculo->isActive()){
			return;
		}
		echo '<div class="borda">';
		echo '<p>Usuário: '.$vinculo->getResponsavel()->getNome().'</p>';
		
		echo '<p>Créditos: R$ '.number_format ( $vinculo->getCartao()->getCreditos(), 2, ',', '.' ).'</p>';
		echo '<p>Número do Cartão:'.$vinculo->getCartao()->getNumero().'</p>';
		$time = strtotime($vinculo->getInicioValidade());
		echo '<p>Início da Validade: '.date('d/m/Y H:i:s', $time).'</p>';
		
		if($vinculo->isAvulso()){
			echo '<p>Cartão Avulso</p>';
			
		}else{
			echo '<p>Cartão Pessoal</p>';
				
			
		}
		
		if(isset($_GET['id_refeicoes'])){
			$idTransacao = intval($_GET['id_refeicoes']);
			if($vinculo->getId() == $idTransacao){
				$sql = "SELECT * FROM registro 
					INNER JOIN catraca ON registro.catr_id = catraca.catr_id
					INNER JOIN catraca_unidade ON catraca_unidade.catr_id = catraca.catr_id 
					INNER JOIN unidade ON catraca_unidade.unid_id = unidade.unid_id 
					WHERE vinc_id = $idTransacao 
					AND regi_data > '2016-10-17 01:01:01' 
					ORDER BY regi_data DESC LIMIT 200";
				$result = $this->dao->getConexao()->query($sql);
				echo '<div class="borda">';
				echo '<p>&Uacute;ltimas 200 Refeições com o Cartão: </p>
				<p>OBS: mostraremos as refei&ccedil;&otilde;es a partir de 17 de outubro de 2016 porque foi quando come&ccedil;ou a funcionar o m&oacute;dulo financeiro.</p>
				';
				echo '<table  class="tabela borda-vertical zebrada texto-preto">';
				$total = 0;
				foreach($result as $linha){
					$time = strtotime($linha['regi_data']);
					
					echo '<tr><td>'.date('d/m/Y H:i:s', $time).'</td><td>R$'.number_format ( $linha['regi_valor_pago'], 2, ',', '.' ).'</td><td>'.$linha['unid_nome'].'</td></tr>';
					$total += $linha['regi_valor_pago'];
					
				}
				echo '<tr><th>TOTAL Consumido: </th><th>R$'.number_format ( $total, 2, ',', '.' ).'</th><th>-</th></tr>';
				echo '</table>';
				echo '</div>';
			}
				
		}
		if(isset($_GET['numero_cartao'])){
			echo '<p><a href="?pagina=pessoal&id_refeicoes='.$vinculo->getId().'&numero_cartao='.$_GET['numero_cartao'].'">Refeicoes</a></p>';
			
		}else{
			echo '<p><a href="?pagina=pessoal&id_refeicoes='.$vinculo->getId().'">Refeicoes</a></p>';
			
		}
		
		echo '</div>';
	}

	
}

?>