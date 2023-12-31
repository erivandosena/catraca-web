<?php

/**
 *
 * @author Jefferson Uchoa Ponte
 *
 */

class CartaoController
{
	private $view;
	private $dao;
	public static function main($nivelDeAcesso)
	{

		switch ($nivelDeAcesso) {
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
				UsuarioController::main($nivelDeAcesso);
				break;
		}
	}

	public function telaCartao()
	{
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


	public function telaIdentificacao()
	{

		$this->view->formBuscaCartao();

		if (isset($_GET['numero_cartao'])) {
			if (strlen($_GET['numero_cartao']) < 3) {
				return;
			}

			$cartao = new Cartao();
			$cartao->setNumero($_GET['numero_cartao']);
			$numeroCartao = $cartao->getNumero();
			$sqlVerificaNumero = "SELECT * FROM usuario
				INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
				LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
				LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
				WHERE cartao.cart_numero = '$numeroCartao'
				";
			$this->dao = new DAO();
			$result = $this->dao->getConexao()->query($sqlVerificaNumero);
			$idCartao = 0;
			$usuario = new Usuario();
			$tipo = new Tipo();
			$vinculoDao = new VinculoDAO($this->dao->getConexao());
			$vinculo = new Vinculo();
			foreach ($result as $linha) {
				$idDoVinculo = $linha['vinc_id'];
				$tipo->setNome($linha['tipo_nome']);
				$usuario->setNome($linha['usua_nome']);
				$usuario->setIdBaseExterna($linha['id_base_externa']);
				$idCartao = $linha['cart_id'];
				$vinculo->setAvulso($linha['vinc_avulso']);
				$avulso = $linha['vinc_avulso'];
				if ($avulso) {
					$usuario->setNome("Avulso");
				}
				break;
			}

			if (!$idCartao) {
				$this->view->formMensagem("-erro", "Cartão Não possui Vínculo Válido.");
				return;
			}

			$vinculo->setId($idDoVinculo);
			$cartao->setId($idCartao);
			$vinculoDao->vinculoPorId($vinculo);




			if (!$vinculo->isActive()) {
				echo '<div id="pergunta">';

				echo '		<div class="alerta-erro">
									<div class="icone icone-notification ix16"></div>
									<div class="titulo-alerta">Aten&ccedil&atildeo</div>
									<div class="subtitulo-alerta">Vínculo não está ativo.</div>
								</div>';
				echo '	<a href="?pagina=cartao&numero_cartao=' . $_GET['numero_cartao'] . '&cartao_renovar=1" class="botao">Renovar Cartão?</a>
							<a href="?pagina=cartao&numero_cartao=' . $_GET['numero_cartao'] . '&cartao_reciclar=1" class="botao">Reciclar Cartão?</a>
							</div>';
				if (isset($_GET['cartao_reciclar'])) {
					$this->recicleCard();
					return;
				}
				if (isset($_GET['cartao_renovar'])) {
					if (!isset($_POST['certeza'])) {
						echo '<div class="alerta-ajuda">
						<div class="icone icone-notification ix16"></div>
						<div class="titulo-alerta">Aten&ccedil&atildeo</div>
						<div class="subtitulo-alerta">Tem certeza que deseja renovar esse vínculo?</div>
						</div>
						<form id="form-confirma-cartao" action="" method="post">
							<input type="submit" class="botao" value="certeza" name="certeza" />
						</form>';
						return;
					}
					$usuarioDao = new UsuarioDAO();

					$usuarioDao->retornaPorIdBaseExterna($usuario);

					if ($vinculoDao->usuarioJaTemVinculo($usuario)) {
						echo '<div class="alerta-ajuda">
							<div class="icone icone-notification ix16"></div>
							<div class="titulo-alerta">Aten&ccedil&atildeo</div>
							<div class="subtitulo-alerta">Esse usuário já possui vínculo válido.</div>
							</div>';
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}
					if ($vinculo->isAvulso()) {
						echo '<div class="alerta-ajuda">
							<div class="icone icone-notification ix16"></div>
							<div class="titulo-alerta">Aten&ccedil&atildeo</div>
							<div class="subtitulo-alerta">Não existe renovação de vínculos avulsos!</div>
						</div>';
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}

					$validacaoDao = new ValidacaoDAO($usuarioDao->getConexao());
					if (!$validacaoDao->verificaSeAtivo($usuario)) {
						echo '<div class="alerta-erro">
									<div class="icone icone-notification ix16"></div>
									<div class="titulo-alerta">Aten&ccedil&atildeo</div>
									<div class="subtitulo-alerta">Esse usuário possui um problema quanto ao status!</div>
								</div>';
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}

					$daqui3Meses = date('Y-m-d', strtotime("+60 days")) . 'T' . date('G:00:01');
					$vinculo->setFinalValidade($daqui3Meses);

					if ($vinculoDao->atualizaValidade($vinculo)) {
						echo '<div class="alerta-sucesso">
							<div class="icone icone-notification ix16"></div>
							<div class="titulo-alerta">Aten&ccedil&atildeo</div>
							<div class="subtitulo-alerta">Vínculo Atualizado com Sucesso!</div>
							</div>';
					} else {
						echo '<div class="alerta-erro">
									<div class="icone icone-notification ix16"></div>
									<div class="titulo-alerta">Aten&ccedil&atildeo</div>
									<div class="subtitulo-alerta">Erro ao tentar renovar vínculo.</div>
								</div>';
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}
			}
			$this->view->formIdentificacao($cartao, $usuario, $tipo, 'sem-imagem');
		}
	}
	public function recicleCard()
	{
		if (!isset($_GET['numero_cartao'])) {
			return;
		}
		if (strlen($_GET['numero_cartao']) < 3) {
			return;
		}
		if (!isset($_POST['certeza'])) {
			echo '<div class="alerta-ajuda">
			<div class="icone icone-notification ix16"></div>
			<div class="titulo-alerta">Aten&ccedil&atildeo</div>
			<div class="subtitulo-alerta">Tem certeza que deseja reciclar esse cartão?</div>
			</div>
			<form id="form-confirma-cartao" action="" method="post">
				<input type="submit" class="botao" value="certeza" name="certeza" />
			</form>';
			return;
		}

		$number = $_GET['numero_cartao'];
		$result = $this->dao->getConexao()->query("SELECT * FROM cartao WHERE cart_numero = '$number' LIMIT 1");
		$credits = 0;
		foreach ($result as $line) {
			$id = $line['cart_id'];
			$cartPreviousNumber =  $line['cart_numero'];
			$credits = $line['cart_creditos'];
		}
		if ($credits != 0) {
			echo '<div class="alerta-erro">
			<div class="icone icone-notification ix16"></div>
			<div class="titulo-alerta">Aten&ccedil&atildeo</div>
			<div class="subtitulo-alerta">O cartão tem créditos, por isso não pode ser reciclado!</div>
		</div>';
			return;
		}
		$newNumber = 'reciclado_'.date('Ymd').'_'.$cartPreviousNumber;
		$sql0 = "UPDATE cartao set cart_numero = '$newNumber' WHERE cart_id = $id";

		if (!$this->dao->getConexao()->exec($sql0)) {
			echo '<div class="alerta-erro">
			<div class="icone icone-notification ix16"></div>
			<div class="titulo-alerta">Aten&ccedil&atildeo</div>
			<div class="subtitulo-alerta">Erro ao tentar reciclar cartão!</div>
		</div>';
			echo '<meta http-equiv="refresh" content="2; url=?pagina=cartao">';
			return;
		} else {
			echo '<div class="alerta-sucesso">
				<div class="icone icone-notification ix16"></div>
				<div class="titulo-alerta">Aten&ccedil&atildeo</div>
				<div class="subtitulo-alerta">Cartão Reciclado com Sucesso!</div>
				</div>';
		}

	}
	public function telaCadastro()
	{
		$this->view->formBuscaUsuarios();

		if (isset($_GET['selecionado'])) {

			$idDoSelecionado = $_GET['selecionado'];

			$usuarioDao = new UsuarioDAO();



			$usuario = new Usuario();
			$usuario->setIdBaseExterna($idDoSelecionado);

			$usuarioDao->retornaPorIdBaseExterna($usuario);

			$this->view->mostraSelecionado($usuario);
			$vinculoDao = new VinculoDAO();

			if (isset($_GET['vinculo_cancelar'])) {
				$vinculo = new Vinculo();
				$vinculo->setId($_GET['vinculo_cancelar']);

				if (isset($_POST['certeza'])) {
					if ($vinculoDao->invalidarVinculo($vinculo)) {
						$this->view->formMensagem("-sucesso", "Vínculo Invalidado.");
					} else {
						$this->view->formMensagem("-erro", "Erro ao tentar invalidar vínculo.");
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}
				$this->view->formConfirmacaoEliminarVinculo($vinculo);
				return;
			}

			if (isset($_GET['vinculo_renovar'])) {
				$vinculo = new Vinculo();
				$vinculo->setId($_GET['vinculo_renovar']);
				$vinculoDao->vinculoPorId($vinculo);

				$daqui3Meses = date('Y-m-d', strtotime("+60 days")) . 'T' . date('G:00:01');
				$vinculo->setFinalValidade($daqui3Meses);

				if (isset($_POST['certeza'])) {
					if ($vinculoDao->usuarioJaTemVinculo($usuario)) {
						$this->view->formMensagem("-erro", "Esse usuário já possui vínculo válido.");
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}

					if ($vinculo->isAvulso()) {
						$this->view->formMensagem("-erro", "Não existe renovação de vínculos avulsos!");
						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
						return;
					}
					// 					$validacaoDao = new ValidacaoDAO($usuarioDao->getConexao());
					// 					if(!$validacaoDao->verificaSeAtivo($vinculo->getResponsavel())){
					// 						$this->view->formMensagem("-erro", 'Esse cartão não pode ser renovado!');
					// 						echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					// 						return;
					// 					}

					if ($vinculoDao->atualizaValidade($vinculo)) {
						$this->view->formMensagem("-sucesso", "Vínculo Atualizado com Sucesso!");
					} else {
						$this->view->formMensagem("-erro", "Erro ao tentar renovar vínculo.");
					}
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=cartao&selecionado=' . $usuario->getIdBaseExterna() . '">';
					return;
				}

				$this->view->formConfirmacaoRenovarVinculo();
				return;
			}

			$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);


			$validacaoDao = new ValidacaoDAO($vinculoDao->getConexao());
			$listaDeTipos = $validacaoDao->listaDeTipos($usuario);
			$podeComer = false;
			if (count($listaDeTipos) > 0) {
				$podeComer = true;
			}
			if (!$vinculoDao->usuarioJaTemVinculo($usuario) && $podeComer) {
				if (!isset($_GET['cartao'])) {
					echo '<a class="botao" href="?pagina=cartao&selecionado=' . $idDoSelecionado . '&cartao=add">Adicionar</a>';
				} else {


					if (isset($_GET['salvar'])) {
						foreach ($listaDeTipos as $tipo) {
							if ($tipo->getId() == $_GET['id_tipo'])
								$esseTipo = $tipo;
						}
						$vinculo = new Vinculo();
						$daqui3Meses = date('Y-m-d', strtotime("+60 days")) . 'T' . date('G:00:01');
						$vinculo->setFinalValidade($daqui3Meses);
						$vinculo->getCartao()->getTipo()->setId($esseTipo->getId());
						$vinculo->getCartao()->setNumero($_GET['numero_cartao2']);
						$vinculo->getResponsavel()->setIdBaseExterna(intval($usuario->getIdBaseExterna()));
						$vinculo->getResponsavel()->setNome($usuario->getNome());
						$vinculo->setInicioValidade(date("Y-m-d G:i:s"));
						if ($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())) {
							$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Inative o cartão atual para adicionar um novo.");
							//echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';
							return;
						}

						if ($vinculoDao->cartaoTemVinculo($vinculo->getCartao())) {
							$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '&cartao=add">';
							return;
						}

						if (isset($_POST['enviar_vinculo'])) {

							if ($vinculoDao->usuarioJaTemVinculo($vinculo->getResponsavel())) {
								$this->view->formMensagem("-erro", "Esse usuário já possui cartão. Invalide o cartão atual para adicionar um novo.");
								//echo '<a href="?pagina=cartao&cartaoselecionado=' .$vinculo->getCartao()->getId().'">Clique aqui para ver</a>';
								return;
							}

							if ($vinculoDao->cartaoTemVinculo($vinculo->getCartao())) {
								$this->view->formMensagem("-erro", "O numero do cartão digitado já possui vinculo, utilize outro cartão.");
								return;
							}
							$daoAutenticacao = new UsuarioDAO();

							$vinculoDao->verificarUsuario($vinculo->getResponsavel(), $daoAutenticacao->getConexao());

							if ($vinculoDao->adicionaVinculo($vinculo)) {

								$this->view->formMensagem("-sucesso", "Vinculo Adicionado Com Sucesso.");
							} else {
								$this->view->formMensagem("-erro", "Erro na tentativa de Adicionar Vínculo.");
							}
							echo '<meta http-equiv="refresh" content="3; url=.\?pagina=cartao&selecionado=' . $vinculo->getResponsavel()->getIdBaseExterna() . '">';
							return;
						}

						$this->view->formConfirmacaoEnvioVinculo($usuario, $_GET['numero_cartao2'], $esseTipo);
					} else {
						$this->view->mostraFormAdicionarVinculo($listaDeTipos, $idDoSelecionado);
					}
				}
			}

			foreach ($vinculos as $vinculoComIsencao) {
				$vinculoDao->isencaoValidaDoVinculo($vinculoComIsencao);
			}
			$podeRenovar = true;
			if (sizeof($vinculos)) {
				$podeRenovar = false;
			}
			$vinculosVencidos = $vinculoDao->retornaVinculosVencidos($usuario);
			$vinculosALiberar = $vinculoDao->retornaVinculosFuturos($usuario);

			if (sizeof($vinculos)) {
				echo '<h2 class="titulo">Vinculos ativos</h2>';
				$this->view->mostraVinculos($vinculos);
			}

			if (sizeof($vinculosVencidos)) {
				echo '<h2 class="titulo">Vinculos Vencidos</h2>';
				$this->view->mostraVinculos($vinculosVencidos, $podeRenovar);
			}

			if (sizeof($vinculosALiberar)) {
				echo '<h2 class="titulo">Vinculos A Liberar</h2>';
				$this->view->mostraVinculos($vinculosALiberar, false);
			}
		}

		if (isset($_GET['nome'])) {
			$mensagem = "";

			$usuarioDao = new UsuarioDAO();

			$listaDeUsuarios = $usuarioDao->pesquisaNoSigaa($_GET['nome']);

			$this->view->mostraResultadoBuscaDeUsuarios($listaDeUsuarios, $mensagem);
			$usuarioDao->fechaConexao();
		}
	}

	public function verificaSeAtivo(Usuario $usuario)
	{
		if (strtolower(trim($usuario->getStatusServidor())) == 'ativo') {
			return true;
		}
		if (trim($usuario->getStatusDiscente()) == 'CADASTRADO' || strtolower(trim($usuario->getStatusDiscente())) == 'ativo' || strtolower(trim($usuario->getStatusDiscente())) == 'ativo - formando' || strtolower(trim($usuario->getStatusDiscente())) == 'formando'  || strtolower(trim($usuario->getStatusDiscente())) == 'formado' || strtolower(trim($usuario->getStatusDiscente())) == 'ativo - graduando' || strtolower(trim($usuario->getIdStatusDiscente())) == self::ID_STATUS_DISCENTE_CONCLUIDO) {

			return true;
		}
		if (strtolower(trim($usuario->getTipodeUsuario())) == 'terceirizado' || strtolower(trim($usuario->getTipodeUsuario())) == 'outros') {
			return true;
		}
		if (strtolower(trim($usuario->getTipodeUsuario())) == 'docente externo' || substr(strtolower(trim($usuario->getTipodeUsuario())), 0, 2) == 'co') {
			return true;
		}
		return false;
	}
	const ID_STATUS_DISCENTE_ATIVO = 1;
	const ID_STATUS_DISCENTE_CADASTRADO = 3;
	const ID_STATUS_DISCENTE_FORMADO = 9;
	const ID_STATUS_DISCENTE_CONCLUIDO = 3; //



}
