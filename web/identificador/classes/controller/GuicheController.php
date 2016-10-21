<?php

class GuicheController{
	
	private $view;
	private $dao;
	public static function main($nivel){
		
		switch ($nivel) {
			case Sessao::NIVEL_SUPER :
				$controller = new GuicheController();
				$controller->telaGuiche();
				break;
			case Sessao::NIVEL_ADMIN :
				$controller = new GuicheController();
				$controller->telaGuiche();
				break;

			case Sessao::NIVEL_POLIVALENTE:
				$controller = new GuicheController();
				$controller->telaGuiche();
				break;
			case Sessao::NIVEL_GUICHE:
				$controller = new GuicheController();
				$controller->telaGuiche();
				break;
			case Sessao::NIVEL_CATRACA_VIRTUAL:
				$controller = new GuicheController();
				$controller->telaGuiche();
				break;
			default :
				UsuarioController::main ( $nivel );
				break;
		}
			
	}
	public function telaGuiche(){
	
		$controller = new GuicheController();
		$this->view = new GuicheView();
		$this->dao = new GuicheDAO();
		$unidade = new Unidade();
		$dao = new DAO();
		$sessao = new Sessao();
		$idDoUsuario = $sessao->getIdUsuario();

		/*
		 * Preenche a tabela 'Descrição da Operação'
		 * apenas com dados das operações realizadas no dia
		 * corrente do operador logado.		 *
		 */

		$dataInicio = date('Y-m-d');
		$dataFim = date('Y-m-d');

		$data1 = $dataInicio.' 00:00:00';
		$data2 = $dataFim.' 23:59:59';

		$sqlTransacao = "SELECT cliente.usua_nome cliente,* FROM transacao
		INNER JOIN usuario
		on transacao.usua_id = usuario.usua_id
		INNER JOIN usuario as cliente
		ON cliente.usua_id = transacao.usua_id1
		WHERE (tran_data BETWEEN '$data1' AND '$data2') 
		AND usuario.usua_id = $idDoUsuario ORDER BY tran_id DESC LIMIT 100 ";

		$listaDescricao = $dao->getConexao()->query($sqlTransacao);
		$this->view->formDescricao($listaDescricao);

		/*
		 * Soma os campos de valores.
		 */

		$valorTotal = 0;
		$result = $dao->getConexao()->query($sqlTransacao);
		foreach ($result as $linha){
			
			$valor = $linha['tran_valor'];
			floatval ($valor);
			if($linha){
				$valorTotal = $valorTotal + $valor;
			}
		}
		echo'					<h2>Saldo em Caixa: R$ '.number_format($valorTotal, 2,',','.').' </h1>
							<div class="sete borda">';

		$sqlUsuario = "SELECT * FROM usuario WHERE usua_id = '$idDoUsuario'";
		$result = $dao->getConexao()->query($sqlUsuario);
		foreach ($result as $linha){
			echo'	<span class="icone-user"> Operador: '.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</span>';
		}
		echo'	</div>
		</div>';

		$this->view->formBuscarCartao();

		/*
		 * Realiza a pesquisa pelo numero do cartão identificando se existe vinculo ativo.
		 */

		if(isset($_GET['cartao'])){
			$cartao = new Cartao();
			$cartao->setNumero($_GET['cartao']);
			$numeroCartao = $cartao->getNumero();
			$sqlVerificaNumero = "SELECT * FROM usuario
			INNER JOIN vinculo ON vinculo.usua_id = usuario.usua_id
			LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
			LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
			WHERE cartao.cart_numero = '$numeroCartao'";
			$result = $dao->getConexao()->query($sqlVerificaNumero);
			$usuario = new Usuario();
			$idCartao = 0;
			$tipo = new Tipo();
			$vinculoDao = new VinculoDAO($dao->getConexao());
			$vinculo = new Vinculo();
			foreach($result as $linha){
				$idDoVinculo = $linha['vinc_id'];
				$tipo->setNome($linha['tipo_nome']);
				$tipo->setValorCobrado($linha['tipo_valor']);
				$cartao->setId($linha['cart_id']);
				$cartao->setCreditos($linha['cart_creditos']);
				$usuario->setNome($linha['usua_nome']);
				$usuario->setId($linha['usua_id']);
				$usuario->setLogin($linha['usua_login']);
				$usuario->setIdBaseExterna($linha['id_base_externa']);
				$vinculo->setAvulso($linha['vinc_avulso']);
				$idCartao = $linha['cart_id'];
				$avulso = $linha['vinc_avulso'];
				if($avulso){
					$usuario->setNome('Avulso');
				}
				break;
			}
			
			if($idCartao && $_GET['cartao'] != ''){
				$idBeneficiado = $usuario->getId();
				$vinculo->setId($idDoVinculo);
				$cartao->setId($idCartao);
				$vinculoDao->vinculoPorId($vinculo);
					
				if(!$vinculo->isActive()){

					$this->view->mensagem('erro','O vinculo n&atildeo est&aacute ativo.');

				}else{
						
					$this->view->formConsulta($usuario, $tipo, $cartao);
					$this->view->formInserirValor();
						
					/*
					 * Insere ou estorna os creditos do usuario pesquisado com vinculo ativo.
					 */
						
					if(isset($_GET['valor'])){

						$cartao->setCreditos($_GET['valor']);
						$valorVendido = $cartao->getCreditos();
						$login = $usuario->getLogin();
						$valorAnt = $vinculo->getCartao()->getCreditos();
						$valorVendido = $cartao->getCreditos();
						$novoValor = $valorAnt + $valorVendido;
						$valor = number_format($valorVendido, 2,',','.');

						if ($valorVendido == 0){
							$this->view->mensagem("erro", "Valor Inválido! Digite novamente.");
							return ;
						}

						if($valorVendido < 0){
							if ($valorAnt <= 0){
								echo '<div id="msgconfirmado">';
								$this->view->mensagem("erro", "Saldo Insuficiente para realizar estorno!");
								echo '</div>';
								echo '<meta http-equiv="refresh" content="3; url=.\?pagina=guiche">';
								return;
							}else if ($novoValor < 0){
								echo '<div id="msgconfirmado">';
								$this->view->mensagem("erro", "Saldo Insuficiente para realizar estorno!");
								echo '</div>';
								echo '<meta http-equiv="refresh" content="3; url=.\?pagina=guiche">';
								return;
							}
							$estorno = true;
						}else{
							$this->view->mensagem("ajuda", "Deseja inserir R\$ $valor?");
							$tipoTransacao = 'Venda de Créditos';
							$tipo = "sucesso";
							$mensagem = "Valor inserido com sucesso.";
							$estorno = false;
						}

						if ($estorno){
							echo '	<div id="mascara"></div>
							<div class="window borda" id="janela1">
								<a href="#" class="fechar">X Fechar</a>
								<h2 class="titulo">Por Favor digite sua Senha para confirmar.</h2>
								<hr class="um">
								<form class="formulario sequencial " method="post" id="formIndentificacao">
									<label>
										Login<input type="text"  name="login" value="'.$login.'" class="doze"/>
									</label>
									<label>
										Senha<input type="password" placeholder="Senha Sig" name="senha" class="doze" autofocus />
									</label>
									<input type="submit" value="Confirmar" name="estornar" class="doze" />
								</form>';
							$this->view->mensagem("erro", "Deseja estornar R\$ $valor?");
							echo '	</div>';
						}else{
							echo ' 	<form method="post" class="formulario">
									<input type="submit" name="confirmar" value="Confirmar">
								</form>';
							if (isset($_POST['confirmar'])){
								$autorizado = true;
							}
						}

						if (isset($_POST['estornar'])){
							$usuarioDao = new UsuarioDAO();
							$usuario2 = new Usuario();
							$usuario2->setLogin($login = $_POST['login']);
							$usuario2->setSenha($senha = $_POST['senha']);
							if ($usuarioDao->autentica($usuario2)){
								$idUsuario1 = $usuario->getId();
								$idUsuario2 = $usuario2->getId();
								if ($idUsuario1 == $idUsuario2 || $usuario2->getNivelAcesso() >= 2){
									$tipo = "ajuda";
									$mensagem = "Valor estornado com sucesso!";
									$tipoTransacao = 'Estorno de valores';
									$autorizado = true;
								}else{
									echo '<div id="msgconfirmado">';
									$this->view->mensagem("erro", "Este cartão não pertence a este usuario!");
									echo '</div>';
									echo '<meta http-equiv="refresh" content="3; url=.\?pagina=guiche">';
								}
							}else{
								echo '<div id="msgconfirmado">';
								$this->view->mensagem("erro", "Usuario ou Senha Inválidos!");
								echo '</div>';
								echo '<meta http-equiv="refresh" content="3; url=.\?pagina=guiche">';
								return;
							}
						}

						if(isset($autorizado)){
								
							$idCartao = $vinculo->getCartao()->getId();
							$idUsuario = $usuario->getId();
							$dataTimeAtual = date ( "Y-m-d G:i:s" );
								
							$dao->getConexao()->beginTransaction();

							$sql = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";

							$sql2 = "INSERT into transacao(tran_valor, tran_descricao, tran_data, usua_id,usua_id1)
							VALUES($valorVendido, '$tipoTransacao' ,'$dataTimeAtual', $idDoUsuario, $idBeneficiado)";

							//echo $sql;
							if(!$dao->getConexao()->exec($sql)){
								$dao->getConexao()->rollBack();
								$this->view->mensagem('erro','Erro ao inserir os creditos.');
								return false;
							}
							if(!$dao->getConexao()->exec($sql2)){
								$dao->getConexao()->rollBack();
								$this->view->mensagem('erro','Erro ao inserir os creditos.');
								return false;
							}

							$dao->getConexao()->commit();
							echo '<div id="msgconfirmado">';
							$this->view->mensagem($tipo,$mensagem);
							echo '</div>';
							echo '<meta http-equiv="refresh" content="3; url=.\?pagina=guiche">';

						}
					}
				}
			}else{
				$this->view->mensagem('erro','Cart&atildeo sem vinculo v&aacutelido.');
			}
		}
	}

}
	
	
	?>