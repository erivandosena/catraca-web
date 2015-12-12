<?php
class DefinicoesController {
	private $view;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$controller = new DefinicoesController ();
				$controller->telaDefinicoes ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function telaConfiguracaoUnidadeAcademica() {
		$this->view->formInserirUnidade ();
		$unidadeDao = new UnidadeDAO ( $this->dao->getConexao () );
		if (isset ( $_GET ['cadastrar_unidade'] )) {
			
			if ($_GET ['cadastrar_unidade'] != "") {
				
				echo '
						<div class="borda">
						<p>Você tem certeza que quer adicionar essa unidade acadêmica? </p><p>' . $_GET ['cadastrar_unidade'] . '</p><br>';
				echo '<form action="" method="post" class="formulario sequencial texto-preto">
							<input type="hidden" name="certeza_cadastrar_unidade" value="' . $_GET ['cadastrar_unidade'] . '" />
							<input  type="submit"  name="certeza" value="Tenho Certeza"/></form>';
				
				echo '</div>';
			}
		}
		if (isset ( $_POST ['certeza_cadastrar_unidade'] )) {
			$unidade = $_POST ['certeza_cadastrar_unidade'];
			$stmt = $this->dao->getConexao()->prepare("INSERT INTO unidade(unid_nome) VALUES(?);");
			$stmt->bindParam(1, $unidade);
			if ($stmt->execute()) {
				$this->view->mostraSucesso ( "Sucesso" );
			} else {
				$this->view->mostraSucesso ( "Erro ao tentar inserir unidade" );
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		} else {
			$unidadesAcademicas = $unidadeDao->retornaLista ();
			foreach ($unidadesAcademicas as $unidadeAcademica){
				$unidadeDao->turnosDaUnidade($unidadeAcademica);
				
			}
			$this->view->listarUnidadesAcademicas ( $unidadesAcademicas );
			
			if (isset ( $_GET ['turno_na_unidade'] )) {
				$unidade = new Unidade ();
				$unidade->setId ( $_GET ['turno_na_unidade'] );
				$unidadeDao->preenchePorId($unidade);
				
				$turnoDao = new TurnoDAO ( $unidadeDao->getConexao () );
				
				$listaDeTurnos = $turnoDao->retornaLista ();
				$this->view->formTurnoNaUnidade($unidade, $listaDeTurnos);
				if(isset($_POST['turno_na_unidade'])){
					$turno = new Turno();
					$unidade = new Unidade();
					$turno->setId($_POST['id_turno']);
					$unidade->setId($_POST['id_unidade']);
					if($unidadeDao->turnoNaUnidade($turno, $unidade))
						$this->view->mostraSucesso("Turno Adicionado com Sucesso");
					else
						$this->view->mostraSucesso("Erro ao tentar adicionar turno na Unidade");
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
					
				}
			}
			
			else if(isset($_GET['excluir_turno_da_unidade'])){
				$unidade = new Unidade ();
				$unidade->setId ( $_GET ['excluir_turno_da_unidade'] );
				$unidadeDao->preenchePorId($unidade);
				$unidadeDao->turnosDaUnidade($unidade);
				
				$turnoDao = new TurnoDAO ( $unidadeDao->getConexao () );
				
				$listaDeTurnos = $turnoDao->retornaLista ();
				$this->view->formExcluirTurnoDaUnidade($unidade);
				if(isset($_POST['excluir_turno_da_unidade'])){
					$turno = new Turno();
					$unidade = new Unidade();
					$turno->setId($_POST['id_turno']);
					$unidade->setId($_POST['id_unidade']);
					if($unidadeDao->excluirTurnoDaUnidade($turno, $unidade))
						$this->view->mostraSucesso("Turno excluído com Sucesso");
					else
						$this->view->mostraSucesso("Erro ao tentar excluir turno na Unidade");
					echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
						
				}
				
			}
		}
		
		// $this->view->formAdicionarTurnoNaUnidade();
	}
	
	public function telaCatracas(){
		$unidadeDao = new UnidadeDAO($this->dao->getConexao());
		$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade();
		$this->view->listarCatracas($listaDeCatracas);
	
		if(isset($_GET['editar_catraca'])){
			
			$catraca = new Catraca();
			$catraca->setId($_GET['editar_catraca']);
			$listaDeUnidades = $unidadeDao->retornaLista();

			
			
			$unidadeDao->preencheCatracaPorId($catraca);
			
			$this->view->formEditarCatraca($catraca, $listaDeUnidades);
			
			if(isset($_POST['salvar'])){
				$catraca->setId($_POST['id_catraca']);
				$catraca->setOperacao($_POST['operacao']);
				$catraca->setTempoDeGiro($_POST['tempo_giro']);
				$catraca->setUnidade(new Unidade());
				$catraca->getUnidade()->setId($_POST['id_unidade']);
				
				
				if($unidadeDao->atualizarCatraca($catraca))
					$this->view->mostraSucesso("Catraca editada com sucesso");
				else
					$this->view->mostraSucesso("Erro ao tentar editar catraca");
				echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes&lista_catracas=1">';
				
			}
		}
	
	
	}
	public function telaConfiguracaoDeTurnos() {
		$this->view->formAdicionarTurno ();
		$turnoDao = new TurnoDAO ( $this->dao->getConexao () );
		
		if (isset ( $_GET ['cadastrar_turno'] )) {
			
			echo '
					<div class="borda">
					<p>Você tem certeza que quer adicionar esse turno? </p><p>' . $_GET ['turno_nome'] . '</p><br>';
			echo '<form action="" method="post" class="formulario sequencial texto-preto">
						
					<input type="hidden" name="hora_inicio" value="' . $_GET ['hora_inicio'] . '" />
							<input type="hidden" name="hora_fim" value="' . $_GET ['hora_fim'] . '" />
									<input type="hidden" name="turno_nome" value="' . $_GET ['turno_nome'] . '" />
											
						<input  type="submit"  name="certeza_cadastrar_turno" value="Tenho Certeza"/></form>';
			
			echo '</div>';
		}
		if (isset ( $_POST ['certeza_cadastrar_turno'] )) {
			$turnoNome = $_POST ['turno_nome'];
			
			$horaInicio = $_POST ['hora_inicio'];
			$horaFim = $_POST ['hora_fim'];
			
			$stmt = $this->dao->getConexao()->prepare( "INSERT INTO turno(turn_hora_inicio,turn_hora_fim,turn_descricao) VALUES(?, ?, ?);");
			$stmt->bindParam(1, $horaInicio);
			$stmt->bindParam(2, $horaFim);
			$stmt->bindParam(3, $turnoNome);
			
			
			if ($stmt->execute()) {
				$this->view->mostraSucesso ( "Sucesso" );
			} else {
				$this->view->mostraSucesso ( "Erro ao tentar inserir unidade" );
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		} else {
			$turnos = $turnoDao->retornaLista ();
			$this->view->listarTurnos ( $turnos );
		}
		
		// $this->view->formAdicionarTurnoNaUnidade();
	}
	public function telaTiposDeUsuarios() {
		$this->view->formAdicionarTipoDeUsuario ();
		$tipoDao = new TipoDAO ( $this->dao->getConexao () );
		
		if (isset ( $_GET ['cadastrar_tipo'] )) {
			
			echo '
					<div class="borda">
					<p>Você tem certeza que quer adicionar esse tipo de usuário? </p><p>' . $_GET ['tipo_nome'] . '</p><br>';
			echo '<form action="" method="post" class="formulario sequencial texto-preto">
		
					<input type="hidden" name="tipo_nome" value="' . $_GET ['tipo_nome'] . '" />
							<input type="hidden" name="tipo_valor" value="' . $_GET ['tipo_valor'] . '" />
						<input  type="submit"  name="certeza_cadastrar_tipo" value="Tenho Certeza"/></form>';
			echo '</div>';
		}
		if (isset ( $_POST ['certeza_cadastrar_tipo'] )) {
			$tipoNome = $_POST ['tipo_nome'];
			$tipoValor = floatval ( $_POST ['tipo_valor'] );
			$stmt = $this->dao->getConexao()->prepare("INSERT INTO tipo(tipo_nome, tipo_valor) VALUES(?, ?);");
			$stmt->bindParam(1, $tipoNome);
			$stmt->bindParam(2, $tipoValor);
			
			
			if ($stmt->execute()) {
				
				$this->view->mostraSucesso ( "Sucesso" );
			} else {
				$this->view->mostraSucesso ( "Erro ao tentar inserir unidade" );
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		} else {
			$tipos = $tipoDao->retornaLista ();
			$this->view->listarTiposDeUsuarios ( $tipos );
		}
	}
	public function telaDeCustos() {
		$custoAtualRefeicao = 0;
		$result = $this->dao->getConexao ()->query ( "SELECT cure_valor FROM custo_refeicao ORDER BY cure_id DESC LIMIT 1 ;" );
		foreach ( $result as $linha ) {
			$custoAtualRefeicao = $linha ['cure_valor'];
			break;
		}
		$custoCartao = 0;
		$result = $this->dao->getConexao ()->query ( "SELECT cuca_valor  FROM custo_cartao ORDER BY cuca_id DESC LIMIT 1 ;" );
		foreach ( $result as $linha ) {
			$custoCartao = $linha ['cuca_valor'];
			break;
		}
		
		$this->view->formAlterarCustoRefeicao ( $custoAtualRefeicao );
		$this->view->formAlterarCustoCartao ( $custoCartao );
		
		if (isset ( $_GET ['custo_refeicao'] )) {
			$dataTimeAtual = date ( "Y-m-d G:i:s" );
			$valor = floatval ( $_GET ['custo_refeicao'] );
			if ($this->dao->getConexao ()->exec ( "INSERT into custo_refeicao(cure_valor, cure_data) VALUES($valor, '$dataTimeAtual')" ))
				$this->view->mostraSucesso ( "Custo Modificado Com Sucesso" );
			else
				$this->view->mostraSucesso ( "Erro" );
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
		}
		if (isset ( $_GET ['custo_cartao'] )) {
			$dataTimeAtual = date ( "Y-m-d G:i:s" );
			$valor = floatval ( $_GET ['custo_cartao'] );
			if ($this->dao->getConexao ()->exec ( "INSERT into custo_cartao(cuca_valor , cuca_data ) VALUES($valor, '$dataTimeAtual')" ))
				$this->view->mostraSucesso ( "Custo Modificado Com Sucesso" );
			else
				$this->view->mostraSucesso ( "Erro" );
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
		}
	}
	private $dao;
	

	
	
	public function telaDefinicoes() {
		$this->dao = new DAO ( null, DAO::TIPO_PG_LOCAL );
		$this->view = new DefinicoesView ();
		
		
		echo '<div class="borda conteudo"> <div class = "simpleTabs">
		        <ul class = "simpleTabsNavigation">
		            <li><a href="#">Unidades Acadêmicas</a></li>
					<li><a href="#">Turnos</a></li>
					<li><a href="#">Catracas</a></li>							
					<li><a href="#">Tipos de Usuários</a></li>
					<li><a href="#">Custos</a></li>
		        </ul>
		        
				
				<div class = "simpleTabsContent"> ';
		  $this->telaConfiguracaoUnidadeAcademica ();
		  
		  echo ' 
		  		</div>
		        <div class = "simpleTabsContent">';
		  		
		  
		  $this->telaConfiguracaoDeTurnos ();
		  
		  echo '</div>
		        <div class = "simpleTabsContent">';
		  $this->telaCatracas();
		  echo '</div>   		
		  		<div class = "simpleTabsContent">';
		   
		  $this->telaTiposDeUsuarios ();
		  		
		  echo '	</div>
		        	<div class = "simpleTabsContent">';
		  $this->telaDeCustos ();
		  
		 echo '
		 	 </div>
		 			
			</div>';
		
	}
}

?>