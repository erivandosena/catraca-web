<?php

class IdentificadorController{
	
	
	private $dao;
	private $view;
	
	public function CatracaVirtual(){
		$this->view = new CatracaVirtualView();
	}
	
	public static function main($nivel){
		
		if($nivel == Sessao::NIVEL_SUPER){

			$identificador = new IdentificadorController();
			$identificador->verificarSelecaoRU();
		}
		
		
	}
	
	public function verificarSelecaoRU(){
		$this->dao = new DAO();
		
		if(isset($_SESSION['catraca_id'])){
			$this->telaIdentificador();
		}
		else{
			if(isset($_POST['catraca_id'])){
				$_SESSION['catraca_id'] = intval($_POST['catraca_id']);
				echo '<meta http-equiv="refresh" content="0; url=?pagina=identificador">';
			}
			$this->selecionarRU();
		}	
		
	}
	
	public function selecionarRU(){
		
		$unidadeDao = new UnidadeDAO($this->dao->getConexao());
		$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade();
		
		echo '
				<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">
						<li><a href="#" class="current">Cadastro</a></li>
			        </ul>
			        <div class = "simpleTabsContent currentTab">		
						<div class="doze colunas borda">';
		
		echo '<form action="" method="post">
				<label for="catraca_id">Selecione o Restaurante:</label><br>
			        <select name="catraca_id" id="catraca_id">';
		
		foreach ($listaDeCatracas as $catraca){
			
			echo '<option value="'.$catraca->getId().'">'.$catraca->getNome().'</option>';
						
		}		                
			            
		echo '       </select><br>
					<input type="submit" class="botao" VALUE="Selecionar" />
				</form>	';
		

		echo '</div>
				</div>
				</div>
				';
		
		
	}
	
	public function telaIdentificador(){
		
		$_SESSION['nome_usuario'] = "";
		$_SESSION['tipo_usuario'] = "";
		$_SESSION['numero_cartao'] = "";
		$_SESSION['confirmado'] = "";
		
		echo '	<div class="doze colunas borda relatorio">
						
						<div class="doze colunas">
							<div class="duas colunas">
								<a href="http://www.unilab.edu.br">
									<img class="imagem-responsiva centralizada" src="img/logo-unilab.png" alt="">
								</a>
							</div>
							<div class="dez colunas">
								<h2 id="titulo-um">Restaurante Universitário</h2>
							</div>
							<hr class="um"><br>
						</div>
						
						<div class="doze colunas dados-usuario">					

							<h3 id="titulo-dois" class="centralizado">Identificação do Usuario</h1><br>			
							
							<hr class="um">							
							<div class="oito colunas">													
								<div id="informacao" class="fundo-cinza1">									
									<form action="" class="formulario-organizado">							
										<label for="numero_cartao">
											Cartão: <input type="number" id="numero_cartao" name="numero_cartao" autofocus>
										</label>										
										<input type="hidden" name="pagina" value="identificador" />
									</form><br><br><br><br>									
									<span id="aproxime">Por favor, aproxime o seu cartão.</span>';
									
								
		$this->dao = new DAO();
		$tipoDao = new TipoDAO($this->dao->getConexao());
		$data = date ( "Y-m-d G:i:s" );
		if(isset($_GET['numero_cartao'])){
			if($_GET['numero_cartao'] == NULL || $_GET['numero_cartao'] == "")
				return;				
				$i = 0;
				$turnoAtual = new Turno();				
				$selectTurno = "Select * FROM turno
				WHERE '$data' BETWEEN turno.turn_hora_inicio AND turno.turn_hora_fim";
				$result = $this->dao->getConexao()->query($selectTurno);
				foreach($result as $linha){
					$turnoAtual->setHoraInicial($linha['turn_hora_inicio']);
					$turnoAtual->setHoraFinal($linha['turn_hora_fim']);
					$i++;
					break;
				}
				if($i == 0){
					$this->mensagemErro("Fora do hor&aacute;rio de refei&ccedil;&atilde;o");
					echo '<meta http-equiv="refresh" content="1; url=?pagina=identificador">';
					return;
				}					
					
				$cartao = new Cartao();
				$cartao->setNumero($_GET['numero_cartao']);				
				$cartaoDao = new CartaoDAO($tipoDao->getConexao());
				$verifica = $cartaoDao->preenchePorNumero($cartao);
				$idCartao = $cartao->getId();
				$imagem = $cartao->getNumero();			
				
				if (!file_exists('img/'.$imagem.'.jpg')){
					$imagem = "sem-imagem";
				}							
				
				if($verifica == NULL){
					$this->mensagemErro("Cartão não cadastrado!");
					echo '<meta http-equiv="refresh" content="1; url=?pagina=identificador">';
					return;
				}
					
				$vinculoDao = new VinculoDAO($cartaoDao->getConexao());
				$vinculo = $vinculoDao->retornaVinculoValidoDeCartao($cartao);
				if($vinculo == NULL)
				{
					$this->mensagemErro("Verifique o vínculo deste cartão!");
					echo '<meta http-equiv="refresh" content="1; url=?pagina=identificador">';
					return;
		
				}
				//Vamos ver se ele pode mesmo comer. Coloque o código aqui.
				$data1 = date("Y-m-d").' '.$turnoAtual->getHoraInicial();
				$data2 = date("Y-m-d").' '.$turnoAtual->getHoraFinal();
					
				$sqlVerRegistros = "SELECT * FROM registro WHERE (registro.regi_data  BETWEEN '$data1' AND '$data2')
				AND (registro.cart_id = $idCartao) ORDER BY registro.regi_id DESC";
				$i = 0;
				foreach($this->dao->getConexao()->query($sqlVerRegistros) as $linha){
					$i++;
					if($vinculo->isAvulso())
						break;
						if($i >= $vinculo->getQuantidadeDeAlimentosPorTurno()){
							$this->mensagemErro("Usuário já passou neste turno!");
							echo '<meta http-equiv="refresh" content="3; url=?pagina=identificador">';
							return;
						}
				}				
				
				$strNome = $vinculo->getResponsavel()->getNome();
				if($vinculo->isAvulso()){
					$strNome = " Avulso ";
				}
				
				$_SESSION['numero_cartao'] = $_GET['numero_cartao'];
				$_SESSION['nome_usuario'] = $strNome;
				$_SESSION['tipo_usuario'] = $cartao->getTipo()->getNome();
				$_SESSION['confirmado'] = "aguarde";
				
				echo	'			<div id="dados" class="dados">
										<span>Nº Cartão: '.$cartao->getNumero().'</span><br>
										<span>Nome: '.$strNome.'</span><br>
										<span>Tipo: '.$cartao->getTipo()->getNome().'</span><br>
										<span>Matrícula: </span>
									</div>
								</div>										
							</div>
							<div class="quatro colunas">
								<img id="imagem" src="img/'.$imagem.'.jpg" alt="">
							</div>
						</div>		
						
						<form method="post" class="formulario organizado centralizado">
							<input type="submit" id="confirmado" name="confirmado" class="oito" value="Confirmar">						
						</form>
												
						';
				
				if(isset($_POST['confirmado'])){
					
					$custo = 0;
					$idCatraca = $_SESSION['catraca_id'];
		
					$verificaCusto = "SELECT * FROM custo_refeicao
					INNER JOIN custo_unidade ON custo_unidade.cure_id = custo_refeicao.cure_id
					INNER JOIN unidade ON unidade.unid_id = custo_unidade.unid_id
					INNER JOIN catraca_unidade ON catraca_unidade.unid_id = unidade.unid_id
					WHERE catraca_unidade.catr_id = $idCatraca";
		
					$result = $this->dao->getConexao()->query($verificaCusto);
					foreach ($result as $linha){
						$custo = $linha['cure_valor'];
					}
		
					if (!$custo){
						$sql = "SELECT cure_valor FROM custo_refeicao ORDER BY cure_id DESC LIMIT 1";
						foreach($tipoDao->getConexao()->query($sql) as $linha){
							$custo = $linha['cure_valor'];
						}
					}
		
					$numeroCartao = $_GET['numero_cartao'];
					$idVinculo= $vinculo->getId();
					$valorPago = $vinculo->getCartao()->getTipo()->getValorCobrado();
		
					$sqlVerificaNumero = "SELECT * FROM cartao WHERE cart_numero = '$numeroCartao'";
		
					$result = $this->dao->getConexao()->query($sqlVerificaNumero);
					foreach($result as $linha){
						$saldoCartao = ($linha['cart_creditos']);
					}
		
					$novoSaldo = $saldoCartao - $valorPago;
		
					if($novoSaldo <= 0){
						$novoSaldo = null;
					}
					
					
					
// 					$this->dao->getConexao()->beginTransaction();
						
// 					$sql1 = "UPDATE cartao SET cart_creditos = '$novoSaldo' WHERE cart_numero = '$numeroCartao'";
						
// 					$sql2 = "INSERT into registro(regi_data, regi_valor_pago, regi_valor_custo, catr_id, cart_id, vinc_id)
// 					VALUES('$data', $valorPago, $custo, $idCatraca, $idCartao, $idVinculo)";
						
// 					if(!$this->dao->getConexao()->exec($sql1)){
// 						$this->dao->getConexao()->rollBack();
// 						$this->view->formMensagem("-erro", "Saldo insuficiente, recarregue seu cartão!");
// 						return false;
// 					}
		
// 					if(!$this->dao->getConexao()->exec($sql2)){
// 						$this->dao->getConexao()->rollBack();
// 						$this->view->formMensagem("-erro", "Erro ao inserir o registro!");
// 						return false;
// 					}
		
// 					$this->dao->getConexao()->commit();

					$this->mensagemSucesso();
					$_SESSION['confirmado'] = "confirmado";
					echo '<meta http-equiv="refresh" content="2; url=?pagina=identificador">';					
		
					// 				if($this->dao->getConexao()->exec($sql))
						// 						$this->mensagemSucesso();
						// 					else
							// 						$this->mensagemErro();
		
		
				} 
				
		}
			echo'			</div>
						</div>		
					</div>
				
				';
		
		
	}
	
	public function mensagemSucesso(){
		echo '	<div class="doze colunas centralizado">
					<br>
					<div class="alerta-sucesso dez no-centro">
					<div class="icone icone-checkmark ix24"></div>
					<div class="titulo-alerta">Ok!</div>
					<div class="subtitulo-alerta">Acesso Liberado!.</div>
				</div>
			</div>';
	
	}
	
	public function mensagemErro($strMensagem = null){
		if($strMensagem == null)
			$strMensagem = "Erro na tentativa de inserir os dados!";
			echo '<div class="doze colunas borda centralizado">
	
										<div class="alerta-erro">
										    <div class="icone icone-fire ix24"></div>
										    <div class="titulo-alerta">'.$strMensagem.'</div>
										    <div class="subtitulo-alerta">Erro!</div>
										</div>
	
									</div>';
	
	}
	
	
}

?>