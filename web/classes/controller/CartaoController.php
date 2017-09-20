<?php
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */

class CartaoController{
	private $view;
	public static function main($nivelDeAcesso){
		
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_ADMIN:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_GUICHE:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_POLIVALENTE:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_CADASTRO:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_CATRACA_VIRTUAL:
				$controller = new CartaoController();
				$controller->telaCartao();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}	
	
	public function telaCartao(){
		$this->view = new CartaoView();
		echo '<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">					
						<li><a href="#">Identifica&ccedil;&atilde;o</a></li>
						<li><a href="#">Cadastro</a></li>						
			        </ul>
		        <div class = "simpleTabsContent">';
		
		$this->telaIdentificacao();
		echo '	</div>
				<div class = "simpleTabsContent">';
		$this->telaCadastro();
		echo '	</div>		
						
		    </div>';		
	}
	
	public function telaIdentificacao(){
		$this->view->formBuscaCartao();
		if(!isset($_GET['numero_cartao'])){
			return;
		}
		if(strlen($_GET['numero_cartao']) < 3){
			return;	
		}
		
		$dao = new VinculoDAO();
		$cartao = new Cartao();
		$cartao->setNumero($_GET['numero_cartao']);
		$vinculo = $dao->vinculoDoCartao($cartao);
		if(!$vinculo->getCartao()->getId()){
			$this->view->formMensagem("-erro", "Cartão Não possui Vínculo Válido.");
			return;
		}
		$dao->vinculoPorId($vinculo);
		$imagem = "";
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
					$usuarioDao = new UsuarioDAO();
	
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
					
					$tipoDao = new TipoDAO($dao->getConexao());
					if(!$tipoDao->tipoValido($vinculo->getResponsavel(), $vinculo->getCartao()->getTipo())){
						$this->view->formMensagem("-erro", "Esse usuário possui um problema quanto ao status!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
							
					}
					
					
					$daqui3Meses = date ( 'Y-m-d', strtotime ( "+90 days" ) ) . 'T' . date ( 'G:00:01' );
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
		$this->view->formIdentificacao($cartao, $usuario, $tipo, $imagem);
	
	}
	
	public function telaCadastro(){
		$this->view->formBuscaUsuarios();
		if (isset ( $_GET ['selecionado'] )) {
			$idDoSelecionado = $_GET['selecionado'];
			$usuarioDao = new UsuarioDAO();
			$tipoDao = new TipoDAO($usuarioDao->getConexao());
			$usuario = new Usuario();
			$usuario->setIdBaseExterna($idDoSelecionado);
			$usuarioDao->retornaPorIdBaseExterna($usuario);			
			$this->view->mostraSelecionado($usuario);
			$vinculoDao = new VinculoDAO();			
			if(isset($_GET['vinculo_cancelar'])){
				$vinculo = new Vinculo();
				$vinculo->setId($_GET['vinculo_cancelar']);
				
				if(isset($_POST['certeza'])){
					if($vinculoDao->invalidarVinculo($vinculo)){
						$this->view->formMensagem("-sucesso", "Vínculo Invalidado.");						
					}else{
						$this->view->formMensagem("-erro", "Erro ao tentar invalidar vínculo.");						
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}				
				$this->view->formConfirmacaoEliminarVinculo($vinculo);
				return;
			}
			if(isset($_GET['vinculo_renovar'])){
				$vinculo = new Vinculo();
				$vinculo->setId($_GET['vinculo_renovar']);
				$vinculoDao->vinculoPorId($vinculo);
				$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'G:00:01' );
				$vinculo->setFinalValidade($daqui3Meses);				
				if(isset($_POST['certeza'])){
					if($vinculoDao->usuarioJaTemVinculo($usuario)){
						$this->view->formMensagem("-erro", "Esse usuário já possui vínculo válido.");						
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}
					
					if($vinculo->isAvulso()){
						$this->view->formMensagem("-erro", "Não existe renovação de vínculos avulsos!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}
					
					if(!$tipoDao->tipoValido($vinculo->getResponsavel(), $vinculo->getCartao()->getTipo())){
						$this->view->formMensagem("-erro", 'Esse usuário possui um problema quanto ao status! ('.$usuario->getStatusDiscente().")");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;						
					}				
					
					if($vinculoDao->atualizaValidade($vinculo)){
						$this->view->formMensagem("-sucesso", "Vínculo Atualizado com Sucesso!");						
					}else{
						$this->view->formMensagem("-erro", "Erro ao tentar renovar vínculo.");
					}
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}			
			
				$this->view->formConfirmacaoRenovarVinculo();
				return;
			}			
			$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);
			
			$listaDeTipos = array();
			$listaDeTipos = $tipoDao->retornaTiposValidosUsuario($usuario);
			$podeComer = false;
			if(sizeof($listaDeTipos) > 0){
				$podeComer = true;
			}
			if(!$vinculoDao->usuarioJaTemVinculo($usuario) && $podeComer){
				if (!isset ( $_GET ['cartao'] )){
					echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
				}else{
					
					
					if(isset($_GET['salvar'])){
						foreach($listaDeTipos as $tipo){
							if($tipo->getId() == $_GET['id_tipo'])
								$esseTipo = $tipo;	
						}
						$vinculo = new Vinculo();
						$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'G:00:01' );
						$vinculo->setFinalValidade($daqui3Meses);
						$vinculo->getCartao()->getTipo()->setId($esseTipo->getId());
						$vinculo->getCartao()->setNumero($_GET['numero_cartao2']);
						$vinculo->getResponsavel()->setIdBaseExterna(intval($usuario->getIdBaseExterna()));
						$vinculo->setInicioValidade(date ( "Y-m-d G:i:s" ));
						if($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())){							
							$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Inative o cartão atual para adicionar um novo.");
							return;	
						}
						if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
							$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '&cartao=add">';
							return;
						}
						if(isset($_POST['enviar_vinculo'])){
							if($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())){
								$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Invalide o cartão atual para adicionar um novo.");								
								return;						
							}
							if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
								$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");								
								return;
							}
							$daoAutenticacao = $vinculoDao;
							$vinculoDao->verificarUsuario($vinculo->getResponsavel(), $daoAutenticacao->getConexao());
							if($vinculoDao->adicionaVinculo ($vinculo)){
								$this->view->formMensagem("-sucesso", "Vinculo Adicionado Com Sucesso.");							
							}else{
								$this->view->formMensagem("-erro", "Erro na tentativa de Adicionar Vínculo.");							
							}
							echo '<meta http-equiv="refresh" content="10; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
							return;
						}
						$this->view->formConfirmacaoEnvioVinculo($usuario, $_GET['numero_cartao2'], $esseTipo);
					}
					else{
						$this->view->mostraFormAdicionarVinculo($listaDeTipos, $idDoSelecionado);
					}				
				}
			}
			
			foreach($vinculos as $vinculoComIsencao)
				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
			$podeRenovar = true;
			if(sizeof($vinculos)){
				$podeRenovar = false;
			}
			$vinculosVencidos = $vinculoDao->retornaVinculosVencidos($usuario);
			$vinculosALiberar = $vinculoDao->retornaVinculosFuturos($usuario);			
			
			if(sizeof($vinculos)){
				echo '<h2 class="titulo">Vinculos ativos</h2>';
				$this->view->mostraVinculos($vinculos);
			}
			
			if(sizeof($vinculosVencidos)){
				echo '<h2 class="titulo">Vinculos Vencidos</h2>';
				$this->view->mostraVinculos($vinculosVencidos, $podeRenovar);
			}
			
			if(sizeof($vinculosALiberar)){
				echo '<h2 class="titulo">Vinculos A Liberar</h2>';
				$this->view->mostraVinculos($vinculosALiberar, false);					
			}			
		}		

		if (isset ( $_GET ['nome'] )) {
			$mensagem = "";
			$usuarioDao = new UsuarioDAO();
			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa( $_GET ['nome']);
			$this->view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios, $mensagem);
			$usuarioDao->fechaConexao();
		}
	}
	
}



?>
