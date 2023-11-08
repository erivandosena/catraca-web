<?php
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */

<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
class CartaoAvulsoController{
========
class CartaoController{
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
	private $view;
	public static function main($nivelDeAcesso){
		
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new CartaoAvulsoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_ADMIN:
				$controller = new CartaoAvulsoController();
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
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
		$this->view = new CartaoAvulsoView();
		echo '<div class="conteudo"> 
				<div class = "simpleTabs">';		

		$this->telaCadastro();
		echo '	</div>		
		    </div>';
		
		
		
========
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
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
	}
	
	public function telaIdentificacao(){
		
		$this->view->formBuscaCartao();
		
		if(isset($_GET['numero_cartao'])){
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
				
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
				echo '</h1>';
				
				if(file_exists('fotos/'.$usuario->getIdBaseExterna().'.png')){
						
					echo '<img width="300" src="fotos/'.$usuario->getIdBaseExterna().'.png" />';
						
				}
				
				if(!$vinculo->isActive()){
					echo '<p>O vinculo não está ativo </p><br>
							<a href="?pagina=avulso&numero_cartao='.$_GET['numero_cartao'].'&cartao_renovar=1" class="botao">Renovar</a> ';
				
					if(isset($_GET['cartao_renovar'])){
						if(isset($_POST['certeza'])){
							$usuarioDao = new UsuarioDAO();
							
							
========
				$this->view->formIdentificacao($cartao, $usuario, $tipo, $imagem);
		
				if(!$vinculo->isActive()){
					echo '<div id="pergunta">';
					$this->view->formMensagem("-erro", "vinculo não está ativo.");
					echo '	<a href="?pagina=cartao&numero_cartao='.$_GET['numero_cartao'].'&cartao_renovar=1" class="botao">Renovar</a> 
							</div>';
					if(isset($_GET['cartao_renovar'])){
						if(isset($_POST['certeza'])){
							$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);								
								
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
							$usuarioDao->retornaPorIdBaseExterna($usuario);
								
							if($vinculoDao->usuarioJaTemVinculo($usuario))
							{
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
								$this->view->mostraSucesso("Esse usuário já possui vínculo válido.");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
							}
							if($vinculo->isAvulso()){
						
								$this->view->mostraSucesso("Não existe renovação de vínculos avulsos!");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
							}
							
							
							
							if(!$this->verificaSeAtivo($usuario)){
								$this->view->mostraSucesso("Esse usuário possui um problema quanto ao status!");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
						
							}
========
								$this->view->formMensagem("-ajuda", "Esse usuário já possui vínculo válido.");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
							}
							if($vinculo->isAvulso()){
								$this->view->formMensagem("-ajuda", "Não existe renovação de vínculos avulsos!");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
								return;
							}								
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
								
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
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
								
								$this->view->mostraSucesso("Erro ao tentar renovar vínculo.  ");
								
							}
							echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
========
								$this->view->formMensagem("-erro", "Erro ao tentar renovar vínculo.");		
							}
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
							return;
						}
						
						$this->view->formConfirmacaoRenovarVinculo();
					}
				}				
			}else{
				$this->view->formMensagem("-erro", "Cartão Não possui Vínculo Válido.");	
			}			
		}		
	}
	
	public function telaCadastro(){
		$this->view->formBuscaUsuarios();
		
		if (isset ( $_GET ['selecionado'] )) {
			
			$idDoSelecionado = $_GET['selecionado'];
			$usuarioDao = new UsuarioDAO();
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
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
						$this->view->mostraSucesso("Erro ao tentar invalidar vínculo.  ");
						
					}
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
========
						$this->view->formMensagem("-erro", "Erro ao tentar invalidar vínculo.");						
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
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
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
					if($vinculoDao->usuarioJaTemVinculo($usuario))
					{
						$this->view->mostraSucesso("Esse usuário já possui vínculo válido.");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
========
					if($vinculoDao->usuarioJaTemVinculo($usuario)){
						$this->view->formMensagem("-erro", "Esse usuário já possui vínculo válido.");						
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
						return;
					}
					
					if($vinculo->isAvulso()){
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
						
						$this->view->mostraSucesso("Não existe renovação de vínculos avulsos!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
========
						$this->view->formMensagem("-erro", "Não existe renovação de vínculos avulsos!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
						return;
					}
					
					if(!$this->verificaSeAtivo($usuario)){
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
						$this->view->mostraSucesso("Esse usuário possui um problema quanto ao status!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
						
					}
					
					
========
						$this->view->formMensagem("-erro", "Esse usuário possui um problema quanto ao status!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;						
					}					
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
					
					if($vinculoDao->atualizaValidade($vinculo)){
						$this->view->formMensagem("-sucesso", "Vínculo Atualizado com Sucesso!");						
					}else{
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
						$this->view->mostraSucesso("Erro ao tentar renovar vínculo.  ");

========
						$this->view->formMensagem("-erro", "Erro ao tentar renovar vínculo.");
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
					}
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}			
			
				$this->view->formConfirmacaoRenovarVinculo();
				return;
			}			
			
			$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);			
			
			$podeComer = $this->verificaSeAtivo($usuario);
			
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
			if($podeComer){
========
			if(!$vinculoDao->usuarioJaTemVinculo($usuario) && $podeComer){
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
				if (!isset ( $_GET ['cartao'] )){
					echo '<a class="botao" href="?pagina=avulso&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
				}else{
					$tipoDao = new TipoDAO($vinculoDao->getConexao());
					$listaDeTipos = $tipoDao->retornaLista();
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
					foreach($listaDeTipos as $chave => $tipo ){
						if(strtolower (trim($listaDeTipos[$chave]->getNome())) == 'isento'){
							unset($listaDeTipos[$chave]);
							
						}
========
					foreach ($listaDeTipos as $chave => $tipo){
						if(strtolower (trim( $tipo->getNome())) == 'aluno'){
							if(strtolower (trim($usuario->getStatusDiscente())) == 'ativo' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - formando' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - graduando'){
								continue;
							}
							unset($listaDeTipos[$chave]);
							continue;
						}
						if(strtolower (trim( $tipo->getNome())) == 'servidor tae'){
							
							if(strtolower (trim($usuario->getStatusServidor())) == 'ativo' && strpos(strtolower (trim($usuario->getCategoria())), 'administrativo')){
								continue;
							}
							if($usuario->getIDCategoria() == 3){								
								continue;
							}
							unset($listaDeTipos[$chave]);
							continue;
						}
						if(strtolower (trim( $tipo->getNome())) == 'servidor docente'){
							if(strtolower (trim($usuario->getStatusServidor())) == 'ativo' && strtolower (trim($usuario->getCategoria())) == 'docente'){
								continue;								
							}
							unset($listaDeTipos[$chave]);
							continue;
						}
						if(strtolower (trim( $tipo->getNome())) == 'terceirizado'){
							if(strtolower (trim($usuario->getTipodeUsuario())) == 'terceirizado' || strtolower (trim($usuario->getTipodeUsuario())) == 'outros'){
								continue;
							}
							unset($listaDeTipos[$chave]);
							continue;
						}
						unset($listaDeTipos[$chave]);							
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
					}
					
					if(isset($_GET['salvar'])){
						foreach($listaDeTipos as $tipo ){
								
							if($tipo->getId() == $_GET['id_tipo']){
								$esseTipo = $tipo;	
							
							}
						}
						$vinculo = new Vinculo();
						$daqui3Meses = date ( 'Y-m-d', strtotime ( "+60 days" ) ) . 'T' . date ( 'G:00:01' );
						
						$vinculo->getCartao()->getTipo()->setId($esseTipo->getId());
						$vinculo->getCartao()->setNumero($_GET['numero_cartao2']);
						$vinculo->getResponsavel()->setIdBaseExterna(intval($usuario->getIdBaseExterna()));
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
						
						
						if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
							echo '<div class="borda">';
							echo '<p>O numero do cartão digitado já possui vinculo, utilize outro cartão.</p><br>';
							echo '</div>';
							echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '&cartao=add">';
========
						$vinculo->setInicioValidade(date ( "Y-m-d G:i:s" ));
						if($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())){							
							$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Inative o cartão atual para adicionar um novo.");
							//echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';
							return;	
						}
						
						if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
							$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '&cartao=add">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
							return;
						}
						$vinculoDao->verificarUsuario($vinculo->getResponsavel(), $vinculoDao->getConexao());

						if(isset($_POST['enviar_vinculo'])){
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
							if(strlen($_POST['obs']) > 16){
								
								$this->view->mostraSucesso("Erro muitos digitos na observa&ccedil;&atilde;o. Digite no máximo 16. ");
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
								return;
							}
							$vinculo->setAvulso(true);
							$vinculo->setFinalValidade($_POST['vinc_fim']);
							$vinculo->setInicioValidade($_POST['vinc_inicio']);
							$vinculo->setDescricao($_POST['obs']);
							$vinculo->setQuantidadeDeAlimentosPorTurno($_POST['vinc_refeicoes']);
========
							
							if($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())){
								$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Invalide o cartão atual para adicionar um novo.");								
								//echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';								
								return;						
							}
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
							
							if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
								$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");								
								return;
							}
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php

========
							
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
							if($vinculoDao->adicionaVinculo ($vinculo)){
								$this->view->formMensagem("-sucesso", "Vinculo Adicionado Com Sucesso.");								
							}else{
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
								$this->view->mostraSucesso("Erro na tentativa de Adicionar Vínculo. ");
								
							}
							echo '<meta http-equiv="refresh" content="4; url=.\?pagina=avulso&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
========
								$this->view->formMensagem("-erro", "Erro na tentativa de Adicionar Vínculo.");							
							}
							echo '<meta http-equiv="refresh" content="10; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
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

		if (isset ( $_GET ['nome'] )) {
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
			$usuarioDao = new UsuarioDAO();
========
			$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa( $_GET ['nome']);
			$this->view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios);
			$usuarioDao->fechaConexao();
		}		
	}
	
	public function verificaSeAtivo(Usuario $usuario){
		if(strtolower (trim($usuario->getStatusServidor())) == 'ativo'){			
			return true;
		}
		if(strtolower (trim($usuario->getStatusDiscente())) == 'ativo' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - formando' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - graduando'){
<<<<<<<< HEAD:web/classes/controller/CartaoAvulsoController.php
			return true;	
		}
		
========
			return true;		
		}		
>>>>>>>> origin/guiche2:web/guiche/classes/controller/CartaoController.php
		if(strtolower (trim($usuario->getTipodeUsuario())) == 'terceirizado' || strtolower (trim($usuario->getTipodeUsuario())) == 'outros'){
			return true;
		}
		return false;
	}
	
}



?>