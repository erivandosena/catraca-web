<?php


class CartaoController{
	private $view;
	public static function main($nivelDeAcesso){
		
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
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
		
		echo '<section id="navegacao">
				<ul class="nav nav-tabs">';
		$selecaoUsuarios = "active";
		$selecaoCartoes = "";
		$selecaoIsentos = "";
		
		if(isset($_GET['selecionado']) || isset ( $_GET ['nome'] ) || isset($_GET['vinculoselecionado'])){
			$selecaoUsuarios = "active";
			$selecaoCartoes = "";
			$selecaoIsentos = "";
		}else if(isset($_GET['cartaoselecionado']) || isset ( $_GET ['numero'])){
			$selecaoUsuarios = "";
			$selecaoCartoes = "active";
			$selecaoIsentos = "";
		}
		echo '
					<li role="presentation" class="'.$selecaoUsuarios.'"><a href="#tab1" data-toggle="tab">Usu&aacute;rios</a></li>
					<li role="presentation" class="'.$selecaoCartoes.'"><a href="#tab2" data-toggle="tab">Cart&otilde;es</a></li>
					<li role="presentation" class="'.$selecaoIsentos.'"><a href="#tab3" data-toggle="tab">Isentos</a></li>';
		
		echo '
				</ul><div class="tab-content">';
		echo '<div class="tab-pane '.$selecaoUsuarios.'" id="tab1">';
		$this->pesquisaUsuarioAdicionarVinculo();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoCartoes.'" id="tab2">';
		$this->pesquisaCartaoCancelarVinculo();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoIsentos.'" id="tab3">
				Isentos
				</div>';
		echo '</section>';
		
	}
	public function pesquisaCartaoCancelarVinculo(){
		$this->view->formBuscaCartao();
		
		if(isset($_GET['numero'])){
			$cartaoDAO = new CartaoDAO(null, DAO::TIPO_PG_LOCAL);
			$listaDeCartoes = $cartaoDAO->pesquisaPorNumero($_GET['numero']);
			
			$this->view->mostraResultadoBuscaDeCartoes($listaDeCartoes);
			$cartaoDAO->fechaConexao();
			
		}
		if(isset($_GET['cartaoselecionado'])){
			
			$numeroDoSelecionado = intval($_GET['cartaoselecionado']);
			$cartaoDAO = new CartaoDAO(null, DAO::TIPO_PG_LOCAL);
			$cartao = new Cartao();
			$cartao->setId($numeroDoSelecionado);
			$cartaoDAO->selecionaPorId($cartao);
			$this->view->mostraCartaoSelecionado($cartao);
			
 			$vinculoDao = new VinculoDAO($cartaoDAO->getConexao());
 			
 			$vinculos = $vinculoDao->retornaVinculosValidosDeCartao($cartao);
 			$this->view->mostraVinculos($vinculos);
			
			
		}
	}
	public function pesquisaUsuarioAdicionarVinculo(){
		$this->view->formBuscaUsuarios();
		if(isset($_GET['vinculoselecionado'])){
			
			$vinculoDao = new VinculoDAO(null, DAO::TIPO_PG_LOCAL);
			$vinculoDetalhe = new Vinculo();
			$vinculoDetalhe->setId($_GET['vinculoselecionado']);
			$vinculoDao->vinculoPorId($vinculoDetalhe);
			$vinculoDao->isencaoValidaDoVinculo($vinculoDetalhe);
			$this->view->mostrarVinculoDetalhe($vinculoDetalhe);
			if($vinculoDetalhe->getIsencao()->getId()){
				$this->view->mostraIsencaoDoVinculo($vinculoDetalhe);
				
			}else{
				if(isset($_GET['addisencao'])){
					if(!isset($_POST['salve_isencao']))
						$this->view->formAdicionarIsencao($vinculoDetalhe->getCartao()->getId());
					else 
					{
						$vinculoDetalhe->getCartao()->setId($_POST['id_card']);
						$vinculoDetalhe->getIsencao()->setDataDeInicio($_POST['isen_inicio']);
						$vinculoDetalhe->getIsencao()->setDataFinal($_POST['isen_fim']);
						if($vinculoDao->adicionarIsencaoNoVinculo($vinculoDetalhe))
							$this->view->mostraSucesso("Isenção Inserida Com sucesso!");
						else{
							$this->view->mostraSucesso("Erro na tentativa de Inserir Isenção!");
						}
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&vinculoselecionado=' .$_GET['vinculoselecionado']. '">';
					}
				}else{
					$tempoA = strtotime($vinculoDetalhe->getInicioValidade());
					$tempoB = strtotime($vinculoDetalhe->getFinalValidade());
					$tempoAgora = time();
					if($tempoAgora > $tempoA && $tempoAgora < $tempoB){
						echo '<a href="?pagina=cartao&vinculoselecionado='.$vinculoDetalhe->getId().'&addisencao=1">Adicionar Isenção</a>';
					}
				}
			}
			
			
			if(isset($_POST['certeza_isencao'])){
				echo '<div class="borda">';
				echo '</p>Ok, vou deletar</p>';
				if($vinculoDao->invalidarIsencaoVinculo($vinculoDetalhe))
					echo 'Isenção Eliminada com sucesso';
				$vinculoDao->fechaConexao();
				echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&vinculoselecionado=' .$_POST['vinculoselecionado']. '">';
				echo '</div>';
				return;
			
			}
			if(isset($_POST['certeza'])){
				
				
				echo '<div class="borda">';
				echo '</p>Ok, vou deletar</p>';
				if($vinculoDao->invalidarVinculo($vinculoDetalhe))
					echo 'Eliminado com sucesso';
				
				$vinculoDao->fechaConexao();
				echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&vinculoselecionado=' .$_POST['vinculoselecionado']. '">';
				echo '</div>';
				
				return;
				
			}
			if(isset($_GET['deletar'])){
				
				echo '<div class="borda">';
				$usuario = new Usuario();
				$sessao = new Sessao();
				$usuario->setLogin($sessao->getLoginUsuario());
				$usuarioDao = new UsuarioDAO($vinculoDao->getConexao());
				$usuarioDao->preenchePorLogin($usuario);
				echo '<p>'.ucwords(strtolower($usuario->getNome())).', você tem certeza que quer eliminar este vínculo?</p><br>';
				echo '<form action="" method="post" class="formulario sequencial texto-preto">
						<input type="hidden" name="vinculoselecionado" value="'.$_GET['vinculoselecionado'].'" />
						<input  type="submit"  name="certeza" value="Tenho Certeza"/></form>';
				
				echo '</div>';
			}
			if(isset($_GET['delisencao'])){
			
				echo '<div class="borda">';
				$usuario = new Usuario();
				$sessao = new Sessao();
				$usuario->setLogin($sessao->getLoginUsuario());
				$usuarioDao = new UsuarioDAO($vinculoDao->getConexao());
				$usuarioDao->preenchePorLogin($usuario);
				echo '<p>'.ucwords(strtolower($usuario->getNome())).', você tem certeza que quer eliminar esta isenção?</p><br>';
				echo '<form action="" method="post" class="formulario sequencial texto-preto">
						<input type="hidden" name="vinculoselecionado" value="'.$_GET['vinculoselecionado'].'" />
						<input  type="submit"  name="certeza_isencao" value="Tenho Certeza"/></form>';
			
				echo '</div>';
			}
			
			$vinculoDao->fechaConexao();
			return;
			
		}
		if (isset ( $_GET ['nome'] )) {
			
			$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa( $_GET ['nome']);
			$this->view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios);
			$usuarioDao->fechaConexao();
		}
		if (isset ( $_GET ['selecionado'] )) {
			$idDoSelecionado = intval($_GET['selecionado']);
			$usuarioDao = new UsuarioDAO(null, DAO::TIPO_PG_SIGAAA);
			$usuario = new Usuario();
			$usuario->setIdBaseExterna($idDoSelecionado);
			$usuarioDao->retornaPorIdBaseExterna($usuario);
			$this->view->mostraSelecionado($usuario);
			$vinculoDao = new VinculoDAO(null, DAO::TIPO_PG_LOCAL);
			$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);
			$this->view->mostraVinculos($vinculos);
				
			if (isset ( $_POST ['salvar'] )) {
			
				// Todos os cadastros inicialmente ser�o n�o avulsos.
				$vinculo = new Vinculo();
				$vinculo->setFinalValidade($_POST ['data_validade']);
				$vinculo->getCartao()->getTipo()->setId(intval($_POST ['tipo']));
				$vinculo->getCartao()->setNumero(intval($_POST ['numero_cartao']));
				$vinculo->getResponsavel()->setIdBaseExterna(intval($_POST ['id_base_externa']));
				
				if(isset($_POST['avulso'])){
					if($_POST['avulso'] == "sim"){
						$vinculo->setAvulso(true);
						$vinculo->setQuantidadeDeAlimentosPorTurno($_POST['quantidade_refeicoes']);
						$vinculo->setDescricao($_POST['descricao']);
						
					}
				}else{
					if($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())){
						echo '<div class="borda">';
						echo '<p>Esse usuário já possui vínculos Não Avulsos. Adicione um vínculo avulso ou elmimine um não avulso.</p><br>';
						//echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';
						echo '</div>';
						return;
					}
				}
				//Só vai permitir que chame o adicionaVinculo se o cartão não possuir vinculo valido.
			
				if($vinculoDao->cartaoTemVinculo($vinculo->getCartao())){
					echo '<div class="borda">';
					echo '<p>O numero do cartão digitado já possui vinculo</p><br>';
					echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';
					echo '</div>';
					
				}else{
					$vinculoDao->adicionaVinculo ($vinculo);
					$this->view->mostraSucesso("Vinculo Adicionado Com Sucesso. ");
					// No final eu redireciono para a pagina de selecao do usuario.
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
					return;
				}
				
			}
			
			if (!isset ( $_GET ['cartao'] )){
				echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
			}else{
				$tipoDao = new TipoDAO($vinculoDao->getConexao());
				$listaDeTipos = $tipoDao->retornaLista();
				$this->view->mostraFormAdicionarVinculo($listaDeTipos, $idDoSelecionado);
		
			}
			$usuarioDao->fechaConexao();
			$vinculoDao->fechaConexao();
		}
	}
	
	
	
}



?>