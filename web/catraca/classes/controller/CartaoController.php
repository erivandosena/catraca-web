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
		$selecaoVinculos = "";
		$selecaoIsencoes = "";
		if(isset($_GET['selecionado']) || isset ( $_GET ['nome'] ) || isset($_GET['vinculoselecionado'])){
			$selecaoUsuarios = "active";
			$selecaoCartoes = "";
			$selecaoVinculos = "";
			$selecaoIsencoes = "";
		}else if(isset($_GET['cartaoselecionado']) || isset ( $_GET ['numero'])){
			$selecaoUsuarios = "";
			$selecaoCartoes = "active";
			$selecaoVinculos = "";
			$selecaoIsencoes = "";
		}else if(isset($_GET['filtro_data']) || isset ( $_GET ['busca_vinculos']) || isset($_GET['vinculos_validos'])){
			$selecaoUsuarios = "";
			$selecaoCartoes = "";
			$selecaoVinculos = "active";
			$selecaoIsencoes = "";
		}else if(isset($_GET['filtro_data_isen']) || isset ( $_GET ['busca_vinculos_isen']) || isset($_GET['vinculos_validos_isen'])){
			$selecaoUsuarios = "";
			$selecaoCartoes = "";
			$selecaoVinculos = "";
			$selecaoIsencoes = "active";
		}
		echo '
					<li role="presentation" class="'.$selecaoUsuarios.'"><a href="#tab1" data-toggle="tab">Usu&aacute;rios</a></li>
					<li role="presentation" class="'.$selecaoCartoes.'"><a href="#tab2" data-toggle="tab">Cart&otilde;es</a></li>
					<li role="presentation" class="'.$selecaoVinculos.'"><a href="#tab3" data-toggle="tab">Vínculos</a></li>
					<li role="presentation" class="'.$selecaoIsencoes.'"><a href="#tab4" data-toggle="tab">Isenções</a></li>
							
							';
		
		echo '
				</ul><div class="tab-content">';
		echo '<div class="tab-pane '.$selecaoUsuarios.'" id="tab1">';
		$this->pesquisaUsuarioAdicionarVinculo();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoCartoes.'" id="tab2">';
		$this->pesquisaCartaoCancelarVinculo();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoVinculos.'" id="tab3">';
		$this->pesquisaVinculosAtivos();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoIsencoes.'" id="tab4">';
		$this->pesquisaIsencoes();
		echo '</div>';
		echo '</section>';
		
	}
	public function pesquisaIsencoes(){
		$this->view->formBuscaVinculoIsencao();
		$this->view->filtroDataIsencao();
		$vinculoDao = new VinculoDAO(null, DAO::TIPO_PG_LOCAL);
		$data = "";
		$nome = "";
		if(isset($_GET['busca_vinculos_isen']))
			$nome = $_GET['busca_vinculos_isen'];
		if(isset($_GET['filtro_data_isen']))
			$data = $_GET['filtro_data_isen'];
		
		if(isset($_GET['filtro_data_isen']) || isset($_GET['busca_vinculos_isen']) || isset($_GET['vinculos_validos_isen'])){
			$vinculos = $vinculoDao->isencoesValidas($data, $nome);
			foreach($vinculos as $vinculoComIsencao)
				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
			$this->view->mostraVinculos($vinculos);
		}else{
			echo '<a href="?pagina=cartao&vinculos_validos_isen=1">Buscar</a>';
		}
		
		
		
	}
	
	public function pesquisaVinculosAtivos(){
		
		$this->view->formBuscaVinculo();
		$this->view->filtroData();
		$vinculoDao = new VinculoDAO(null, DAO::TIPO_PG_LOCAL);
		$data = "";
		$nome = "";
		if(isset($_GET['busca_vinculos']))
			$nome = $_GET['busca_vinculos'];
		if(isset($_GET['filtro_data']))
			$data = $_GET['filtro_data'];
		
		if(isset($_GET['filtro_data']) || isset($_GET['busca_vinculos']) || isset($_GET['vinculos_validos'])){
			$vinculos = $vinculoDao->buscaVinculos($data, $nome);
			foreach($vinculos as $vinculoComIsencao)
				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
			$this->view->mostraVinculos($vinculos);
		}else{
			echo '<a href="?pagina=cartao&vinculos_validos=1">Buscar</a>';
		}
		
		
		
		
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
 			
 			foreach($vinculos as $vinculoComIsencao)
 				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
 			echo '<h1>Vínculos Válidos</h1>';
 			$this->view->mostraVinculos($vinculos);
 			
 			if (!isset ( $_GET ['vinculos_inativos'] )){
 				echo '<a class="botao" href="?pagina=cartao&cartaoselecionado=' . $numeroDoSelecionado . '&vinculos_inativos=ver">Ver Vínculos Inativos</a>';
 			}else
 			{
 				echo '<h1>Vínculos aguardando liberação</h1>';
 				$vinculosVencidosAguardando  = $vinculoDao->retornaVinculosFuturosDeCartao($cartao);
 				$this->view->mostraVinculos($vinculosVencidosAguardando);
 				echo '<h1>Vínculos vencidos</h1>';
 				$vinculosVencidos  = $vinculoDao->retornaVinculosVencidosDeCartao($cartao);
 				$this->view->mostraVinculos($vinculosVencidos);
 				echo '<a class="botao" href="?pagina=cartao&cartaoselecionado=' . $numeroDoSelecionado. '">Ocultar Vínculos Inativos</a>';
 			}
			
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
				}else if(isset($_GET['addcreditos'])){
					
					if(!isset($_POST['salve_creditos']))
						$this->view->formAdicionarCreditos($vinculoDetalhe->getCartao()->getId());
					else
					{
						$vinculoDetalhe->getCartao()->setId($_POST['id_card']);
						$valorVendido = floatval($_POST['valor_creditos']);
						$vinculoDetalhe->getCartao()->adicionaCreditos($valorVendido);
						$sessao = new Sessao();
						if($vinculoDao->adicionarCreditos($vinculoDetalhe, $valorVendido, $sessao->getIdUsuario()))
							$this->view->mostraSucesso("Creditos atualizados!");
						else{
							$this->view->mostraSucesso("Erro na tentativa de Inserir Isenção!");
						}
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&vinculoselecionado=' .$_GET['vinculoselecionado']. '">';
					}
				}			
				else{
					$tempoA = strtotime($vinculoDetalhe->getInicioValidade());
					$tempoB = strtotime($vinculoDetalhe->getFinalValidade());
					$tempoAgora = time();
					if($tempoAgora > $tempoA && $tempoAgora < $tempoB){
						echo '<a class="botao b-primario" href="?pagina=cartao&vinculoselecionado='.$vinculoDetalhe->getId().'&addisencao=1">Adicionar Isenção</a>';
						echo '<a class="botao b-secundario" href="?pagina=cartao&vinculoselecionado='.$vinculoDetalhe->getId().'&addcreditos=1">Adicionar Créditos</a>';
						
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
			
			foreach($vinculos as $vinculoComIsencao)
				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
			
			
			

			
			if (isset ( $_POST ['salvar'] )) {
			
				// Todos os cadastros inicialmente ser�o n�o avulsos.
				$vinculo = new Vinculo();
				$vinculo->setFinalValidade($_POST ['data_validade']);
				$vinculo->getCartao()->getTipo()->setId(intval($_POST ['tipo']));
				$vinculo->getCartao()->setNumero(intval($_POST ['numero_cartao']));
				$vinculo->getResponsavel()->setIdBaseExterna(intval($_POST ['id_base_externa']));
				$vinculo->setInicioValidade($_POST['inicio_vinculo']);
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
					if($vinculoDao->adicionaVinculo ($vinculo)){
						$this->view->mostraSucesso("Vinculo Adicionado Com Sucesso. ");
					}else{
						$this->view->mostraSucesso("Erro na tentativa de Adicionar Vínculo. ");
					}
					
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
			echo '<h1>Vínculos Ativos</h1>';
			$this->view->mostraVinculos($vinculos);
			
			if (!isset ( $_GET ['vinculos_inativos'] )){
				echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&vinculos_inativos=ver">Ver Vínculos Inativos</a>';
			}else
			{
				echo '<h1>Vínculos aguardando liberação</h1>';
				$vinculosVencidosAguardando  = $vinculoDao->retornaVinculosFuturos($usuario);
				$this->view->mostraVinculos($vinculosVencidosAguardando);
				echo '<h1>Vínculos vencidos</h1>';
				$vinculosVencidos  = $vinculoDao->retornaVinculosVencidos($usuario);
				$this->view->mostraVinculos($vinculosVencidos);
				echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '">Ocultar Vínculos Inativos</a>';
			}
			
			
			$usuarioDao->fechaConexao();
			$vinculoDao->fechaConexao();
		}
	}
	
	
	
}



?>