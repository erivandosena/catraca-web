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
			default :
				UsuarioController::main ($nivel);
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
		
		$sqlTransacao = "SELECT * FROM transacao as trans 
				LEFT JOIN usuario as usuario
				on trans.usua_id = usuario.usua_id				
				WHERE (tran_data BETWEEN '$data1' AND '$data2') AND usuario.usua_id = $idDoUsuario";
		
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
		echo'					<h2>Saldo em Caixa: R$ '.number_format($valorTotal, 2).' </h1>
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
		
		if(isset($_POST['cartao'])){
			$cartao = new Cartao();
			$cartao->setNumero($_POST['cartao']);
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
				$usuario->setIdBaseExterna($linha['id_base_externa']);				
				$vinculo->setAvulso($linha['vinc_avulso']);
				$idCartao = $linha['cart_id'];
				$avulso = $linha['vinc_avulso'];
				if($avulso){
					$usuario->setNome('Avulso');
				}
				break;
			}
			
 			if($idCartao){ 				
 				
 				$vinculo->setId($idDoVinculo);
 				$cartao->setId($idCartao);
 				$vinculoDao->vinculoPorId($vinculo);
 				
 				if(!$vinculo->isActive()){
 					
 					$this->view->mensagem('-erro','O vinculo n&atildeo est&aacute ativo.');
 					
 				}else{			
									
				$this->view->formConsulta($usuario, $tipo, $cartao);		
				$this->view->formInserirValor();						
				
				/*
				 * Insere os estorna os creditos no usuario pesquisado com vinculo ativo.
				 */
				
				if(isset($_POST['valor'])){
					if(isset($_POST['finalizar'])){	
					
						$valorAnt = $vinculo->getCartao()->getCreditos();
						$idCartao = $vinculo->getCartao()->getId();					
						$cartao->setCreditos($_POST['valor']);
						$valorVendido = $cartao->getCreditos();					
						$idUsuario = $usuario->getId();						
						$dataTimeAtual = date ( "Y-m-d G:i:s" );
						$novoValor = $valorAnt + $valorVendido;					
						$tipoTransacao = 'Venda de Créditos';										
						$tipo = "-sucesso";
						$mensagem = "Valor inserido com sucesso.";
						
						if ($valorVendido == 0){
							$this->view->mensagem("-erro", "Valor Inválido!");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=guiche">';
							return ;
						}
						
						if($valorVendido < 0){
							$tipo = "-ajuda";
							$mensagem = "Valor estornado com sucesso!";
							$tipoTransacao = 'Estorno de valores';							
						}
						
						$dao->getConexao()->beginTransaction();
							
						$sql = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";
							
						$sql2 = "INSERT into transacao(tran_valor, tran_descricao, tran_data, usua_id)
						VALUES($valorVendido, '$tipoTransacao' ,'$dataTimeAtual', $idDoUsuario)";
							
						//echo $sql;
						if(!$dao->getConexao()->exec($sql)){
							$dao->getConexao()->rollBack();
							$this->view->mensagem('-erro','Erro ao inserir os creditos.');
							return false;
						}
						if(!$dao->getConexao()->exec($sql2)){
							$dao->getConexao()->rollBack();
							$this->view->mensagem('-erro','Erro ao inserir os creditos.');
							return false;
						}
							
						$dao->getConexao()->commit();
						$this->view->mensagem($tipo,$mensagem);
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=guiche">';
						}
						
					}
 				
				}
				
 			}else{
 				
 				$this->view->mensagem('-erro','Cart&atildeo sem vinculo v&aacutelido.');				
				
 			}			
		}
				
 	}	

}


?>