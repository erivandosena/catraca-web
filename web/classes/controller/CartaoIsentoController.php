<?php
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */

class CartaoIsentoController{
	private $view;
	public static function main($nivelDeAcesso){
		
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new CartaoIsentoController();
				$controller->telaCartao();
				break;
			case Sessao::NIVEL_ADMIN:
				$controller = new CartaoIsentoController();
				$controller->telaCartao();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	
	public function telaCartao(){
		$this->view = new CartaoIsentoView();
		echo '<div class="conteudo">
				<div class = "simpleTabs">';
		$this->telaIdentificacao();
		echo '</div>
			</div>';
		
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
				
				echo '<div class="borda"><h1>'.ucwords(strtolower(htmlentities($usuario->getNome()))).'. Tipo: '.$tipo->getNome();
				
				echo '</h1>';
				
				if(file_exists('fotos/'.$usuario->getIdBaseExterna().'.png')){
						
					echo '<img width="300" src="fotos/'.$usuario->getIdBaseExterna().'.png" />';
						
				}
				
				if(!$vinculo->isActive()){
					echo '<p>O vinculo não está ativo </p><br>
							<a href="?pagina=cartao&numero_cartao='.$_GET['numero_cartao'].'&cartao_renovar=1" class="botao">Renovar</a> ';
				
					
				}else{
					
					//Aqui a gente da a opção de adicionar a isenção. 
					$vinculoDao->isencaoValidaDoVinculo($vinculo);
					if($vinculo->ehIsento()){
						echo '<p>Usuário Isento até: '.date("d/m/Y", strtotime($vinculo->getIsencao()->getDataFinal())).'</p>';
						if(!(isset($_GET['cancelar_isencao']) && isset($_GET['numero_cartao']))){
							
							echo '<br><a href="?pagina=isento&numero_cartao='.$_GET['numero_cartao'].'&cancelar_isencao=1" class="botao">Cancelar Isenção</a>';
							
						}
						else if(!(isset($_POST['confirmar']) && isset($_POST['numero_cartao']))){
							
							
							$this->view->formCancelarIsencao($_GET['numero_cartao']);
						}else{
							if($vinculoDao->invalidarIsencaoVinculo($vinculo)){
								$this->view->mostraSucesso("Isenção adicionada Com Sucesso");
								
							}else{
								$this->view->mostraSucesso("Erro");
							}
	
							echo '<meta http-equiv="refresh" content="4; url=.\?pagina=isento&numero_cartao='.$_GET['numero_cartao'].'">';
							
						}
						
					
					}
					else{
						if(!isset($_GET['add_isencao'])){
							echo '<a href="?pagina=isento&numero_cartao='.$_GET['numero_cartao'].'&add_isencao=1" class="botao">Adicionar Isenção</a>';
						}else{
							if(isset($_POST['isen_inicio']) && isset($_POST['isen_fim']) && isset($_POST['id_card'])){
								$vinculo->setIsencao(new Isencao());
								$vinculo->getIsencao()->setDataDeInicio($_POST['isen_inicio']);
								$vinculo->getIsencao()->setDataFinal($_POST['isen_fim']);
								if($vinculoDao->adicionarIsencaoNoVinculo($vinculo)){
									$this->view->mostraSucesso("Isenção adicionada Com Sucesso");
									
								}else{
									$this->view->mostraSucesso("Erro ao tentar adicionar isenção. ");
									
								}
								echo '<meta http-equiv="refresh" content="4; url=.\?pagina=isento&numero_cartao='.$_GET['numero_cartao'].'">';
								
							}
							$this->view->formAdicionarIsencao($_GET['numero_cartao']);
							
							
						}
						
					}
						
					
				}
				echo '
						
						
						</div>';
			}else
			{

				echo '<div class="borda"><h1>Cartão Não possui Vínculo Válido.</h1></div>';
				
			}
			
			
			
		}
		
		
	}
	
	public function verificaSeAtivo(Usuario $usuario){
		if(strtolower (trim($usuario->getStatusServidor())) == 'ativo'){
			
			return true;
		}
		if(strtolower (trim($usuario->getStatusDiscente())) == 'ativo' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - formando' || strtolower (trim($usuario->getStatusDiscente())) == 'ativo - graduando'){
			return true;	
		}
		
		if(strtolower (trim($usuario->getTipodeUsuario())) == 'terceirizado' || strtolower (trim($usuario->getTipodeUsuario())) == 'outros'){
			return true;
		}

		return false;
	}
	
	
	
	
}



?>