<?php
class PessoalController {
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			default:	
				$controller = new PessoalController();
				$controller->telaPessoal();
				break;
		}
	}
	private $dao;
	
	public function telaPessoal(){
		
		echo '<div class="conteudo"> <div class = "simpleTabs">
		        <ul class = "simpleTabsNavigation">
		
					<li><a href="#">Meus Créditos</a></li>
					<li><a href="#">Minhas Transações</a></li>
			
		        </ul>
		        <div class = "simpleTabsContent">';
				$usuario = new Usuario();
				$sessao = new Sessao();
				$this->dao = new UsuarioDAO();
				$usuario->setId($sessao->getIdUsuario());
				$this->dao->preenchePorId($usuario);
				$this->telaDeCreditos($usuario);
		echo '	</div>	
				<div class = "simpleTabsContent">';
		
		$this->telaDeTransacoes($usuario);
		
		echo '	</div>
		    </div></div>';
		
		
	}
	public function telaDeTransacoes(Usuario $usuario){
		$idUsuario = $usuario->getId();
		$result = $this->dao->getConexao()->query("SELECT * FROM transacao 
				INNER JOIN usuario ON usuario.usua_id = transacao.usua_id
				WHERE usua_id1 = $idUsuario
				ORDER BY tran_id DESC LIMIT 100");
		echo '<p>&Uacute;ltimas 100 transa&ccedil;&otilde;es</p>';
		echo '<table class="tabela borda-vertical zebrada texto-preto">';
		echo '<thead>';
		echo '<tr><th>Data/Hora</th><th>Valor</th><th>Descrição</th><th>Operador</th></tr>';
		echo '</thead>';
		echo '<tbody>';
		foreach($result as $linha){
			$time = strtotime($linha['tran_data']);
			
			echo '<tr><td>'.date('d/m/Y H:i:s', $time).'</td><td>'.$linha['tran_valor'].'</td><td>'.$linha['tran_descricao'].'<td>'.$linha['usua_nome'].'</td></td></tr>';
			
		}
		echo '</tbody>';
		echo '</table>';
		
	}
	
	public function telaDeCreditos(Usuario $usuario){
		
		$vinculoDao = new VinculoDAO($this->dao->getConexao());
		
		$vinculos = $vinculoDao->retornaVinculosValidosDeUsuario($usuario);
		
		if(count($vinculos) < 1){
			echo "<p>Nenhum cartao ativo</p>";
		}
		else if(count($vinculos) == 1){
			echo '<p>Vínculo ativo:</p>';
			$this->exibirVinculos($vinculos);
			
			
		}else if(count($vinculos) > 1){
			echo '<p>Vínculos ativos</p>';
			$this->exibirVinculos($vinculos);
		}
		
		
		$vinculos = array();
		$vinculos = $vinculoDao->retornaVinculosVencidos($usuario);
		if(count($vinculos) < 1){
			echo "<p>Nenhum cartao Inativo</p>";
		}
		else if(count($vinculos) == 1 && $vinculos[0]->isActive()){
			echo '<p>Vínculo Inativo:</p>';
			
			$this->exibirVinculos($vinculos);
				
				
		}else if(count($vinculos) > 1){
			echo '<p>Vínculos Inativos</p>';
			$this->exibirVinculos($vinculos);
		}
		
	}
	public function exibirVinculos($vinculos){
		foreach($vinculos as $vinculo){
			$this->exibirVinculo($vinculo);
		}
	}
	
	public function exibirVinculo(Vinculo $vinculo){
		if($vinculo->isAvulso() && !$vinculo->isActive()){
			return;
		}
		echo '<div class="borda">';
		echo '<p>Créditos: R$ '.number_format ( $vinculo->getCartao()->getCreditos(), 2, ',', '.' ).'</p>';
		$time = strtotime($vinculo->getInicioValidade());
		echo '<p>Início da Validade: '.date('d/m/Y H:i:s', $time).'</p>';
		
		if($vinculo->isAvulso()){
			echo '<p>Cartão Avulso</p>';
			
		}else{
			echo '<p>Cartão Pessoal</p>';
				
			
		}
		
		if(isset($_GET['id_refeicoes'])){
			$idTransacao = intval($_GET['id_refeicoes']);
			if($vinculo->getId() == $idTransacao){
				$sql = "SELECT * FROM registro 
					INNER JOIN catraca ON registro.catr_id = catraca.catr_id
					INNER JOIN catraca_unidade ON catraca_unidade.catr_id = catraca.catr_id 
					INNER JOIN unidade ON catraca_unidade.unid_id = unidade.unid_id 
					WHERE vinc_id = $idTransacao ORDER BY regi_id DESC LIMIT 10";
				$result = $this->dao->getConexao()->query($sql);
				echo '<div class="borda">';
				echo '<p>&Uacute;ltimas 10 Refeições do Vínculo: ';
				echo '<table  class="tabela borda-vertical zebrada texto-preto">';
				foreach($result as $linha){
					$time = strtotime($linha['regi_data']);
					
					echo '<tr><td>'.date('d/m/Y H:i:s', $time).'</td><td>R$'.number_format ( $linha['regi_valor_pago'], 2, ',', '.' ).'</td><td>'.$linha['unid_nome'].'</td></tr>';
					
					
				}
				echo '</table>';
				echo '</div>';
			}
				
		}
		echo '<p><a href="?pagina=pessoal&id_refeicoes='.$vinculo->getId().'">Refeicoes</a></p>';
		
		echo '</div>';
	}

	
}

?>