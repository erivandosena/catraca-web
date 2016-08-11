<?php


class CatracaVirtualController{
	
	private $dao;
	private $view;
	private $catracaSelecionada;
	
	public function CatracaVirtual(){
		$this->view = new CatracaVirtualView();
		
	}
	
	public static function main($nivel){

		switch ($nivel){
			case Sessao::NIVEL_SUPER:
				$gerador = new CatracaVirtualController();
				$gerador->verificarSelecaoRU();
				break;
			case Sessao::NIVEL_ADMIN:
				$gerador = new CatracaVirtualController();
				$gerador->verificarSelecaoRU();
				break;
			case Sessao::NIVEL_CATRACA_VIRTUAL:
				$gerador = new CatracaVirtualController();
				$gerador->verificarSelecaoRU();
				break;
			default:
				UsuarioController::main ( $nivel );
				break;
		}
		
		
		
		
	}
	
	public function verificarSelecaoRU(){
		$this->dao = new DAO();
		
		if(isset($_SESSION['catraca_id'])){
			$this->paginaRegistroManual();
		}
		else{
			if(isset($_POST['catraca_id'])){
				$_SESSION['catraca_id'] = intval($_POST['catraca_id']);
				echo '<meta http-equiv="refresh" content="0; url=?pagina=gerador">';
			}
			$this->selecionarRU();
		} 
			
		
	}
	public function selecionarRU(){
		$unidadeDao = new UnidadeDAO($this->dao->getConexao());
		$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade();
		$this->view->formSelecionarRu($listaDeCatracas);		
		
	}

	
	public function paginaRegistroManual(){
		
		$tipoDao = new TipoDAO($this->dao->getConexao());
		$catracaVirtualDao = new CatracaVirtualDAO($this->dao->getConexao());
		$listaDeTipos = $tipoDao->retornaLista();
		
		$unidadeDao = new UnidadeDAO($this->dao->getConexao());
		$catraca = new Catraca();
		$catraca->setId($_SESSION['catraca_id']);
		$unidadeDao->preencheCatracaPorId($catraca);
		
		
		echo '<div class="navegacao"> 
				<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">					
						<li><a href="#">Cadastro</a></li>	
			        </ul>
				
			        <div class = "simpleTabsContent">
				
						<div class="doze colunas borda">';
		$turnoAtivo = false;
		$data = date ( "Y-m-d G:i:s" );
		$selectTurno = "Select * FROM turno WHERE '$data' BETWEEN turno.turn_hora_inicio AND turno.turn_hora_fim";
		$result = $this->dao->getConexao()->query($selectTurno);
		$descricao = "Turno Não Iniciado";
		foreach($result as $linha){
			$turnoAtivo = true;
			$descricao = $linha['turn_descricao'];
			break;
		}
		
		echo '<p>'.date('d/m/Y H:i:s').'/';
		if($catraca->financeiroAtivo()){
			echo ' modulo financeiro ativo/';
		}
		else{
			echo ' Financeiro desativado /';
		}
		echo 'turno '.$descricao.' iniciado</p>';
		
		
		$somatorio = 0;
		foreach ($listaDeTipos as $tipo){
			$quantidades[] = $unidadeDao->totalDeGirosDaCatracaTurnoAtual($catraca, $tipo);	
		}
		$this->view = new CatracaVirtualView();
		$this->view->exibirQuantidadesDeCadaTipo($listaDeTipos, $quantidades, $catraca);
		
		
		$this->view->formBuscaCartao();
		$idCatraca = $_SESSION['catraca_id'];
		$custo = 0;
		$custo = $catracaVirtualDao->custoDaRefeicao($catraca);
		
		echo '
				
						</div>';
		
		if(isset($_GET['numero_cartao'])){
			if($_GET['numero_cartao'] == NULL || $_GET['numero_cartao'] == "")
				return;
			
			if(!($turnoAtual = $catracaVirtualDao->retornaTurnoAtual())){
				$this->mensagemErro("Fora do hor&aacute;rio de refei&ccedil;&atilde;o");
				echo '<meta http-equiv="refresh" content="1; url=?pagina=gerador">';
				return;
			}
			
			
			
			$cartao = new Cartao();
			$cartao->setNumero($_GET['numero_cartao']);
			
			$vinculo = new Vinculo();
			$vinculo->setCartao($cartao);
			
			
			if(!$catracaVirtualDao->verificaVinculo($vinculo)){
				//Aqui a gente tenta renovar se tiver vinculo proprio nesse cartao. 
				
				$this->mensagemErro("Verifique o vinculo deste cartão!");
				echo '<meta http-equiv="refresh" content="1; url=?pagina=gerador">';
				return;
			}
			
			
			
			if(!$catracaVirtualDao->podeContinuarComendo($vinculo, $turnoAtual)){
				$this->mensagemErro("Usuário já passou neste turno!");
				echo '<meta http-equiv="refresh" content="3; url=?pagina=gerador">';
				return;
			}
				
			
			if($catracaVirtualDao->vinculoEhIsento($vinculo)){
				$valorPago = 0;
				
			}else{
				$valorPago = $vinculo->getCartao()->getTipo()->getValorCobrado();
			}
			
			$idCartao = $cartao->getId();
				
				
			
			
			if(isset($_GET['confirmado'])){
				
				
				$idCatraca = $_SESSION['catraca_id'];
				$idVinculo= $vinculo->getId();
				
				
				
				
				$sql = "INSERT into registro(regi_data, regi_valor_pago, regi_valor_custo, catr_id, cart_id, vinc_id)
				VALUES('$data', $valorPago, $custo, $idCatraca, $idCartao, $idVinculo)";
				//echo $sql;
				if($this->dao->getConexao()->exec($sql))
						$this->mensagemSucesso();
					else
						$this->mensagemErro();
				echo '<meta http-equiv="refresh" content="1; url=?pagina=gerador">';
			}
			
			else{
				
				$strNome = $vinculo->getResponsavel()->getNome();
				if($vinculo->isAvulso()){
					$strNome = " Avulso ";
				}
				
				echo '<div class="doze colunas borda centralizado">';
				
				echo '<p>Confirmar Cadastro de refeição para '.$strNome.' - '.$cartao->getTipo()->getNome().'?</p>';
				if($vinculo->getIsencao()->isActive())
						echo '<p>Usuário Isento</p>';
				else
					echo '<p>Cobrar R$'.number_format($valorPago, 2, ',', '.').'.</p>';
				echo '<a href="?pagina=gerador&numero_cartao='.$_GET['numero_cartao'].'&confirmado=1" class="botao b-sucesso">Confimar</a>';
				echo '</div>';
			}
		}
		
		
		
		
		
				
		echo '</div>
				</div>';
		        
		
		
	}
	
	
	
	public function mensagemSucesso(){
		echo '<div class="doze colunas borda centralizado">
		
										<div class="alerta-sucesso">
										    <div class="icone icone-download ix24"></div>
										    <div class="titulo-alerta">Ok</div>
										    <div class="subtitulo-alerta">Dados enviados com sucesso!</div>
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