<?php

/**
 * Esta classe é responsável por gerenciar telas, modelos e classes de acesso ao banco para 
 * a exibir aplicação Cartao, que consulta cartões ou faz cadastro. 
 * 
 * @author Jefferson Uchoa Ponte <jefponte@unilab.edu.br>
 * @version 1.0.0
 * 
 *
 */

class CartaoController{

	/**
	 * Retorna true para os níveis de acesso que podem acessar esta aplicação. 
	 * Niveis de acesso definidos na classe Sessao. 
	 * @param int $nivelDeAcesso
	 */
	public static function verificaPermissao($nivelDeAcesso){
		if($nivelDeAcesso == Sessao::NIVEL_SUPER){
			return true;
		}
		else if($nivelDeAcesso == Sessao::NIVEL_ADMIN){
			return true;
		}else if($nivelDeAcesso == Sessao::NIVEL_GUICHE){
			return true;
		}else if($nivelDeAcesso == Sessao::NIVEL_POLIVALENTE){
			return true;
		}else if($nivelDeAcesso == Sessao::NIVEL_CADASTRO){
			return true;
		}else if($nivelDeAcesso == Sessao::NIVEL_CATRACA_VIRTUAL){
			return true;
		}
		return false;
	}
	/**
	 * Inicia a aplicação, fazendo antes a verificação de nível de aceso. 
	 * 
	 * @param int $nivelDeAcesso
	 * @param bool $cadastroDeFotos
	 */
	public static function main($nivelDeAcesso, $cadastroDeFotos = false){
		if(self::verificaPermissao($nivelDeAcesso)){
			$controller = new CartaoController($cadastroDeFotos);
			$controller->telaCartao();
		}else{
			UsuarioController::main ( $nivelDeAcesso );
		}
	}	
	
	/**
	 * Classe de Visão utilizada na aplicação Cartão
	 * @var CartaoView
	 */
	private $view;
	
	/**
	 * Variável de configiguração, se for true o cadastro de fotos será 
	 * disponibilizado na tela de cadatro de cartão. 
	 * @var bool
	 */
	private $cadastroDeFotos;
	
	/**
	 * @param bool $cadastroDeFotos
	 */
	public function __construct($cadastroDeFotos = false){
		$this->view = new CartaoView();
		$this->cadastroDeFotos = $cadastroDeFotos;
	}
	
	public function telaCartao(){
		
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
				$dao = new DAO();
				$result = $dao->getConexao()->query($sqlVerificaNumero);
				$idCartao = 0;
				$usuario = new Usuario();
				$tipo = new Tipo();
				$vinculoDao = new VinculoDAO($dao->getConexao());
				$vinculo = new Vinculo();
				foreach($result as $linha){
					$idDoVinculo = $linha['vinc_id'];
					$tipo->setNome($linha['tipo_nome']);
					$usuario->setNome($linha['usua_nome']);
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
					$this->view->formIdentificacao($cartao, $usuario, $tipo, $imagem);
				}else{
					$this->view->formMensagem("-erro", "Cartão Não possui Vínculo Válido.");
				}
			}
		}		
	}
	
	public function telaCadastro(){
		$this->view->formBuscaUsuarios();
		
		if (isset ( $_GET ['nome'] )) {
			$mensagem = "";
			$usuarioDao = new UsuarioDAO();
			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa( $_GET ['nome']);
			$this->view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios, $mensagem);
			$usuarioDao->fechaConexao();
			return;
		}
		
		if(!isset ( $_GET ['selecionado'] )){
			return;	
		}
		$idDoSelecionado = $_GET['selecionado'];
		$usuarioDao = new UsuarioDAO();
		$usuario = new Usuario();
		$usuario->setIdBaseExterna($idDoSelecionado);
		$listaUsuariosBaseExterna = $usuarioDao->retornaListaPorIdBaseExterna($usuario);
		
		$this->view->mostraSelecionado($listaUsuariosBaseExterna, $this->cadastroDeFotos);
		$vinculoDao = new VinculoDAO($usuarioDao->getConexao());
		if(isset($_GET['vinculo_cancelar'])){
			$vinculo = new Vinculo();
			$vinculo->setId($_GET['vinculo_cancelar']);
			if(!isset($_POST['certeza'])){
				$this->view->formConfirmacaoEliminarVinculo($vinculo);
				return;
			}
			if($vinculoDao->invalidarVinculo($vinculo)){
				$this->view->formMensagem("-sucesso", "Vínculo Invalidado.");
			}else{
				$this->view->formMensagem("-erro", "Erro ao tentar invalidar vínculo.");
			}
			echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
			return;
		}
		$validacaoDao  = new ValidacaoDAO($vinculoDao->getConexao());
		if(isset($_GET['vinculo_renovar'])){
			$vinculo = new Vinculo();
			$vinculo->setId($_GET['vinculo_renovar']);
			$vinculoDao->vinculoPorId($vinculo);
		
			$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'G:00:01' );
			$vinculo->setFinalValidade($daqui3Meses);
			if(!isset($_POST['certeza'])){
				$this->view->formConfirmacaoRenovarVinculo();
				return;
			}
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
			$vinculoRenovavel = true;
			$tipo = $vinculo->getCartao()->getTipo();
			
			$vinculoRenovavel = $validacaoDao->tipoValido($vinculo->getResponsavel(), $tipo);
			if(!$vinculoRenovavel){
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
					
		
		$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);			

		$listaDeTipos = array();
		$listaDeTipos = $validacaoDao->retornaTiposValidosUsuario($usuario);
		$usuarioAtivo = false;
		if(sizeof($listaDeTipos) > 0){
			$usuarioAtivo = true;
		}
		
		if(!$vinculoDao->usuarioJaTemVinculo($usuario) && $usuarioAtivo){
				if (!isset ( $_GET ['cartao'] )){
					echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
				}else{
					
					if(isset($_GET['salvar'])){
						foreach($listaDeTipos as $tipo){
							if($tipo->getId() == $_GET['id_tipo'])
								$esseTipo = $tipo;	
						}
						$vinculo = new Vinculo();
						$daqui3Meses = date ( 'Y-m-d', strtotime ( "+182 days" ) ) . 'T' . date ( 'G:00:01' );
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
							$daoAutenticacao = new UsuarioDAO();
							
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
					}else{
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

}



?>
