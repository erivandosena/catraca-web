<?php

class GuicheController{
		
	public static function main($nivel){
		
		$controller = new GuicheController();
		$controller->telaGuiche();
		
	}
		
	public function telaGuiche(){
		
		$controller = new GuicheController();
		
		$dao = new DAO();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sessao = new Sessao();
		$user = $sessao->getLoginUsuario();
		$idDoUsuario= $sessao->getIdUsuario();
		echo '	<div id="caixa"class="doze colunas borda">										
					<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Venda de Cr&eacuteditos</h2>																											
						<div class="sete colunas">											
							<div id="infovenda" class="fundo-cinza1">

								<div class="doze colunas">													
									<h3 class="centralizado">Desci&ccedil&atildeo da Opera&ccedil&atildeo</h1><br>
										<table class="tabela quadro no-centro">													    
										    <thead>
												<tr>
												    <th>Cod</th>
												    <th>Valor</th>
												    <th>Descri&ccedil&atildeo</th>
												    <th>Data</th>
													<th>Cliente</th>
												</tr>
											</thead>
											<tbody>';		
		
		$sqlTransacao = "SELECT * FROM transacao as trans 
				LEFT JOIN usuario as usuario
				on trans.usua_id = usuario.usua_id 
				WHERE usuario.usua_id = $idDoUsuario";
		$result = $dao->getConexao()->query($sqlTransacao);
		$i = 1;
		foreach ($result as $linha){
			
				echo'	
												<tr>
											        <td>'.$i.'</td>
											        <td>R$ '.$linha['tran_valor'].'</td>
											        <td>'.$linha['tran_descricao'].'</td>
											        <td>'.date("d/m/Y H:i:s", strtotime($linha['tran_data'])).'</td>
											        <td>'.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</td>
											    </tr>';
				$i++;
		}
		
		echo'
											</tbody>											
										</table>
									</div>
								</div>';	
		
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
		
		$sqlUsuario = "SELECT * FROM usuario WHERE usua_login = '$user'";
		$result = $dao->getConexao()->query($sqlUsuario);
		foreach ($result as $linha){
			echo'	<span class="icone-user">Operador: '.ucwords(strtolower(htmlentities(substr($linha['usua_nome'], 0, 15)))).'</span>';			
		}
		
		echo'		<span id="ultAcesso" class="icone-clock"> Ultimo Acesso: '.$date = date('d/m/Y H:i:s').'</span>
				</div>																					
			</div>';
		
		echo'		<div class="cinco colunas">								
						<form method="post" class="formulario-organizado" >								
							<label for="cartao">
								N&uacutemero Cart&atildeo: <input type="number" name="cartao" id="cartao" autofocus>													
							</label>
								<input type="submit" value="Pesquisar">								
							<hr>
						</form>';
		
		if(isset($_POST['cartao'])){
			$cartao = new Cartao();
			$cartao->setNumero($_POST['cartao']);
			$numeroCartao = $cartao->getNumero();			
			$sqlVerificaNumero = "SELECT * FROM usuario 
				INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
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
			
				echo '	<span>Usuario 12: '.ucwords(strtolower(htmlentities($usuario->getNome()))).'</span>						
						<span>Tipo Usuario: '.$tipo->getNome().'</span>						
						<span>Saldo: '.$cartao->getCreditos().'</span>
						<span>Valor Credito: '.$tipo->getValorCobrado().'</span>
						<hr>
					
						
						<form method="post" class="formulario-organizado" >
						<label for="valor">								
							Valor: <input type="number" name="valor" id="valor" step="0.01">
						</label>
						<label for="valorrec">
							Valor Recebido: <input type="number" name="valorrec" id="valorrec" step="0.01">
						</label>
						<hr>
						<h2>Troco: <output id="troco"></output></h2>						
						<input type="hidden" name="cartao" value="'.$_POST['cartao'].'" />
						<input type="submit" value="finalizar" class="botao b-sucesso" name="finalizar">
					</form>';				
				
				if(isset($_POST['valor'])){
					if(isset($_POST['finalizar'])){					
					
						$valorAnt = $vinculo->getCartao()->getCreditos();
						$idCartao = $vinculo->getCartao()->getId();					
						$cartao->setCreditos($_POST['valor']);
						$valorVendido = $cartao->getCreditos();					
						$idUsuario = $usuario->getId();						
						$dataTimeAtual = date ( "Y-m-d G:i:s" );
						$novoValor = $valorAnt + $valorVendido;					
						
						if($valorVendido <= 0){
							$controller->mensagem('-erro','Valor inv&aacutelido.');
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=guiche">';
						}else{
							
						$dao->getConexao()->beginTransaction();
					
						$sql = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";
							
						$sql2 = "INSERT into transacao(tran_valor, tran_descricao, tran_data, usua_id)
						VALUES($valorVendido, 'Venda de Créditos','$dataTimeAtual', $idDoUsuario)";					
					
						//echo $sql;
						if(!$dao->getConexao()->exec($sql)){
							$dao->getConexao()->rollBack();
							$controller->mensagem('-erro','Erro ao inserir os creditos.');
							return false;
						}
						if(!$dao->getConexao()->exec($sql2)){
							$dao->getConexao()->rollBack();
							$controller->mensagem('-erro','Erro ao inserir os creditos.');
							return false;
						}
							
						$dao->getConexao()->commit();
						$controller->mensagem('-sucesso','Valor inserido com sucesso.');
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=guiche">';
					
						}				
					
					if(!$vinculo->isActive()){
						
						$controller->mensagem('-erro','O vinculo n&atildeo est&aacute ativo.');
						
					}
				}
			}
				
 			}else{
 				
 				$controller->mensagem('-erro','Cart&atildeo sem vinculo v&aacutelido.');				
				
 				}			
		}
		echo'
								<hr class="solida">
				
								<a href="" class="botao b-erro">Sangria 123</a>
								<a href="" class="botao ">Encerrar Caixa</a>
							</div>
						</div>
					</div>';
		
 	}
 	
 	public function mensagem($tipo, $texto){
 		//Tipo = -sucesso, -erro, -ajuda
 		echo '	<div class="alerta'.$tipo.'">
				    	<div class="icone icone-warning ix16"></div>
				    	<div class="titulo-alerta">Aten&ccedil&atildeo</div>
				    	<div class="subtitulo-alerta">'.$texto.'</div>
				</div>';
 		
 	}
 	
}


?>