<?php
class DefinicoesController {
	
	private $view;
	private $dao;
	
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
		
		$dao = new DAO();
		$this->view->formAdicionarCatracaVirtual();
		
		if(isset($_GET['nome_catraca'])){
				
			$nomeCatraca = $_GET['nome_catraca'];
			$sql1 = "SELECT * FROM catraca WHERE catr_nome = '$nomeCatraca'";
			$result = $dao->getConexao()->query($sql1);
			$i = 0;
				
			foreach ($result as $linha){
				$i++;
			}
				
			if($i > 0){
				$this->view->formMensagem("-erro", "Esta catraca já existe!");
				echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
			}else{
				if(isset($_POST['confirmar'])){
					$sql = "INSERT INTO catraca (catr_nome) VALUES ('$nomeCatraca')";
					if($dao->getConexao()->exec($sql)){
						echo'<div class="borda">';
						$this->view->formMensagem("-sucesso", "Catraca adicionada com Sucesso!");
						echo '</div>';
					}else{
						echo'<div class="borda">';
						$this->view->formMensagem("-erro", "Não foi possível adicionar a catraca!");
						echo '</div>';
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
					return ;
				}
		
				echo '<div class="borda">';
				$this->view->formMensagem("-ajuda", "Tem certeza que deseja adicionar esta catraca?");
				echo '<form action="" method="post">
						<input type="hidden" value="'.$_GET['nome_catraca'].'" name="nome_catraca">
						<input type="submit" class="botao" value="Confirmar" name="confirmar" />
						</form>';
				echo '</div>';
			}
		}		
		
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
				$catraca->setNome($_POST['nome_catraca']);
				$catraca->setOperacao($_POST['operacao']);
				$catraca->setTempoDeGiro($_POST['tempo_giro']);
				$catraca->setInterfaceRede($_POST['interface']);
				$catraca->setFinanceiro($_POST['financeiro']);
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
		
		if (isset($_GET['editar'])){
			if (isset($_GET['id_turno'])){					
				$dao = new TurnoDAO();
				$turno = new Turno();
				$turno->setId($_GET['id_turno']);
				
				$dao->retornaTurnoPorId($turno);
				$this->view->formEditarTurno($turno);
			
				if (isset($_POST['confirmar'])){
					
					$turno->setHoraInicial($_POST['hora_inicio']);				
					$turno->setHoraFinal($_POST['hora_fim']);
					
					if ($dao->atualizaTurno($turno)){
						$this->view->formMensagem("-sucesso", "Turno alterado com sucesso!");
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
					}else{
						$this->view->formMensagem("-erro", "Erro ao editar o turno.");
						echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
					}
					return ;
				}
				return ;
			}		
		}
		
		// $this->view->formAdicionarTurnoNaUnidade();
				
	}
	
	public function telaTiposDeUsuarios() {
		$this->view->formAdicionarTipoDeUsuario ();
		$tipoDao = new TipoDAO ( $this->dao->getConexao () );
		
		if (isset ( $_GET ['cadastrar_tipo'] )) {
			
			echo '	<div class="borda">
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
		
		if (isset($_GET['editar_tipo'])){			
			$tipo = new Tipo();
			$tipo->setId($_GET['editar_tipo']);
			$idTipo = $tipo->getId();
			$tipoDao->retornaTipoPorId($tipo);
			$this->view->formEditarTipo($tipo);
			
			if (isset($_POST['alterar'])){				
				
				$novoValor = $_POST['valor_tipo'];				
				$sql = "UPDATE tipo SET tipo_valor=$novoValor WHERE tipo_id= $idTipo";
				
				if ($this->dao->getConexao()->exec($sql)){					
					$this->view->formMensagem("-sucesso", "Valor do ".$tipo->getNome()." foi alterado com sucesso!");					
				}else{					
					$this->view->formMensagem("-erro", "Não foi possivel altera o valor!");					
				}
				echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
				return ;
			}
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
		
		/*
		 * Inclui e altera o custo específico da unidade.
		 */		
		echo'	<div class="borda relatorio">
					<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">
					Adicionar um custo para Unidade.</h2>	
					<form action="" method="get" class="formulario-organizado">
						<label>
							<object class="rotulo">Unidade Academica: </object>
							<select name="unidade" id="unidade">';		
		$sql1 = "SELECT * FROM unidade";
		$result = $this->dao->getConexao()->query($sql1);
		foreach ($result as $linha){
		echo'					<option value="'.$linha['unid_id'].'">'.$linha['unid_nome'].'</option>';
		}
		echo'				</select>
						</label>
						<label>
							<object class="rotulo">Valor de Custo: </object>
							<select name="valor_custo" id="valor_custo">';		
		$sql2 = "SELECT * FROM custo_refeicao";
		$result2 = $this->dao->getConexao()->query($sql2);
		foreach ($result2 as $linha2){
		echo'				<option value="'.$linha2['cure_id'].'">'.$linha2['cure_valor'].'</option>';
		}		
		echo'
							</select>
						</label>
						<input type="hidden" name="pagina" value="definicoes" />
						<input type="submit" value="Salvar" name="salvar">
					</form>
				</div>';
		
		if (isset($_GET['unidade'])){			
			if (isset($_GET['valor_custo'])){
				if (isset($_POST['confirmar'])){
					$idUnidade = $_GET['unidade'];
					$idValorCusto = $_GET['valor_custo'];
					$consulta = "SELECT * FROM custo_unidade WHERE unid_id = $idUnidade";
					$result = $this->dao->getConexao()->query($consulta);
					$i = 0;
					
					foreach ($result as $linha){
						$i++;
					}
					
					if ($i == 0){					
						$sql = "INSERT INTO custo_unidade (unid_id, cure_id) VALUES ($idUnidade, $idValorCusto)";
						if($this->dao->getConexao()->exec($sql)){
							$this->view->formMensagem("-sucesso", "Custo inserido com sucesso!");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
						}else{
							$this->view->formMensagem("-erro", "Erro ao inserir o custo na unidade.");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
						}
						return ;
					}else{
						$sql = "UPDATE custo_unidade SET cure_id = $idValorCusto WHERE unid_id = $idUnidade";
						if ($this->dao->getConexao()->exec($sql)){
							$this->view->formMensagem("-sucesso", "Custo alterado com sucesso!");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
						}else{
							$this->view->formMensagem("-erro", "Erro durante a alteração!");
							echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
						}
						return ;
					}
					
				}
				
				echo '	<div class="borda relatorio">';
				$this->view->formMensagem("-ajuda", "Deseja incluir este custo na unidade?");			
				echo '		<form method="post" class="formulario-organizado">
								<input type="hidden" name="unidade" value="'.$_GET['unidade'].'">
								<input type="hidden" name="valor_custo" value="'.$_GET['valor_custo'].'">
								<input type="submit" name="confirmar" value="Confirmar">
							</form>
						</div>';
			}			
		}		
		
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
		
		$sql = "SELECT * FROM unidade
				LEFT JOIN custo_unidade ON custo_unidade.unid_id = unidade.unid_id
				LEFT JOIN custo_refeicao ON custo_refeicao.cure_id = custo_unidade.cure_id";		
		$result = $this->dao->getConexao()->query($sql);
		$custoRefeicao = "";
		
		echo'	<div class="borda relatorio">
					<table id="turno" class="tabela borda-vertical zebrada texto-preto no-centro">
						<thead>
							<tr>
								<th>ID</th>
								<th>Unidade</th>
								<th>Valor Custo</th>
								<th>Ação</th>
							</tr>
						</thead>
						<tbody>';
		$i = 0;
		foreach ($result as $linha){
			$i++;
			$custoRefeicao = $linha['cure_valor'];
			if (!$custoRefeicao){
				$custoRefeicao = "Valor padrão";
			}
			
		echo'				<tr>
								<td>'.$i.'</td>
								<td>'.$linha['unid_nome'].'</td>
								<td>'.$custoRefeicao.'</td>
								<td><a href="?pagina=definicoes&custo_unidade_id='.$linha['cuun_id'].'&excluir=1" class="botao">Excluir</a></td>
							</tr>';
		}
		echo'			</tbody>
				</div>';
		
		if (isset($_GET['excluir'])){
			
			$this->view->formMensagem("-ajuda", "Deseja excluir este registro?");
			echo'	<form method="post" class="formulario-organizado">
						<input type="submit" class="botao" value="Confirmar" name="confirmar">
					</form>';
			
			if (isset($_POST['confirmar'])){
				$idValorCusto = $_GET['custo_unidade_id'];
				$sql="DELETE FROM custo_unidade WHERE cuun_id = $idValorCusto";
				if ($this->dao->getConexao()->exec($sql)){
					$this->view->formMensagem("-sucesso", "Custo removido com sucesso!");
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
				}else{
					$this->view->formMensagem("-erro", "Erro ao Excluir o custo da unidade!");
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
				}
				return ;
			}
		}		
	}
	
	public function telaAdicionarAcatracaVirtual(){
		
		$dao = new DAO();
		$this->view->formAdicionarCatracaVirtual();	
		
		if(isset($_POST['nome_catraca'])){	
			
			$nomeCatraca = $_POST['nome_catraca'];
			$sql1 = "SELECT * FROM catraca WHERE catr_nome = '$nomeCatraca'";
			$result = $dao->getConexao()->query($sql1);
			$i = 0;
			
			foreach ($result as $linha){
				$i++;
			}
			
			if($i > 0){
				$this->view->formMensagem("-erro", "Esta catraca já existe!");
				echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
			}else{						
				if(isset($_POST['confirmar'])){				
					$sql = "INSERT INTO catraca (catr_nome) VALUES ('$nomeCatraca')";
					if($dao->getConexao()->exec($sql)){				
						echo'<div class="borda">';
						$this->view->formMensagem("-sucesso", "Catraca adicionada com Sucesso!");
						echo '</div>';					
					}else{
						echo'<div class="borda">';
						$this->view->formMensagem("-erro", "Não foi possível adicionar a catraca!");
						echo '</div>';
					}
					echo '<meta http-equiv="refresh" content="2; url=.\?pagina=definicoes">';
					return ;
				}
				
				echo '<div class="borda">';
				$this->view->formMensagem("-ajuda", "Tem certeza que deseja adicionar esta catraca?");
				echo '<form action="" method="post">
						<input type="hidden" value="'.$_POST['nome_catraca'].'" name="nome_catraca">
						<input type="submit" class="botao" value="Confirmar" name="confirmar" />				
						</form>';				
				echo '</div>';
			}			
		}		
		return ;
	}		
	
// 	public function telaMensagem(){
	
// 		$unidade = new Unidade();
// 		$catraca = new Catraca();
// 		$dao = new DAO();
// 		$unidadeDao = new UnidadeDAO();
// 		$unidades = $unidadeDao->retornaLista();
// 		$mensagem = new MensagensController();
	
// 		echo'	<div class="borda relatorio">
// 					<form action="" class="formulario-organizado" method="">
// 						<label for="">
// 							<object class="rotulo">Unidade Acadêmica: </object>
// 							<select name="unidade_id" id="unidade_id">';
// 		foreach ($unidades as $unidade){
// 			echo'				<option value="'.$unidade->getId().'">'.$unidade->getNome().'</option>';
// 		}
// 		echo'				</select>
// 						</label>
				
// 						<label for="">
// 							<object class="rotulo">Unidade Acadêmica: </object>
// 							<select name="unidade_id" id="unidade_id">';
		
// 		$idUnidade = $_GET['unidade_id'];
// 		$sql = "SELECT * FROM catraca
// 				INNER JOIN unidade_catraca ON unidade_catraca.catr_id = catraca.catr_id
// 				INNER JOIN unidade ON unidade.unid_id = unidade_catraca.unid_id
// 				WHERE unidade.unid_id = $idUnidade";
// 		$stm = $this->dao->getConexao()->prepare($sql);
		
// 		foreach ($stm as $linha){
// 			echo'				<option value="'.$linha['catr_id'].'">'.$linha['catr_nome'].'</option>';
// 		}
// 		echo'				</select>
// 						</label>
				
// 						<label for="">
// 							1ª Mensagem: <input type="text" name="msg_um">
// 						</label>
// 						<label for="">
// 							2ª Mensagem: <input type="text" name="msg_dois">
// 						</label>
// 						<label for="">
// 							3ª Mensagem: <input type="text" name="msg_tres">
// 						</label>
// 						<label for="unidade_id">
// 							4ª Mensagem: <input type="text" name="msg_quatro">
// 						</label>						
// 						<input type="hidden" name="pagina" value="definicoes" />
// 						<input type="submit" name="salvar" value="Salvar">
// 					</form>
				
// 				</div>';
		
		
		
// 		echo json_encode($stm->fetchAll(PDO::FETCH_ASSOC));
		
// 		if (isset($_GET['unidade_id'])){
// 			if (isset($_POST['confirmar'])){
// 				echo'ok';
// 			}
// 			echo'	<form class="formulario-organizado" method="post">
// 						<input type="submit" name="confirmar" value="Confirmar">
// 					</form>
// 					';
// 		}
	
	
// 		echo'	<div class="borda relatorio">
// 					<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Mensagens</h2>
// 					<table class="tabela borda-vertical zebrada no-centro">
// 						<thead>
// 							<tr class="centralizado">
// 								<th>Catraca</th>
// 								<th>Mesnagem 1</th>
// 								<th>Mesnagem 2</th>
// 								<th>Mesnagem 3</th>
// 								<th>Mesnagem 4</th>
// 								<th>-</th>
// 							</tr>
// 						</thead>
// 					<tbody>';
				
// 		$idUnidade = $unidade->setId($_GET['unidade_id']);
// 		$sql = "SELECT * FROM unidade				
// 				INNER JOIN catraca_unidade ON catraca_unidade.unid_id = unidade.unid_id
// 				INNER JOIN catraca ON catraca.catr_id = catraca_unidade.catr_id
// 				INNER JOIN mensagem ON catraca.catr_id = mensagem.catr_id
// 				WHERE unid_id = $idUnidade";
				
// 		$result = $dao->getConexao()->query($sql);
// 		foreach ($result as $linha){
					
// 		echo'				<tr>
// 								<td>'.$linha['mens_institucional1'].'</td>
// 								<td>'.$linha['mens_institucional1'].'</td>
// 								<td>'.$linha['mens_institucional2'].'</td>
// 								<td>'.$linha['mens_institucional3'].'</td>
// 								<td>'.$linha['mens_institucional4'].'</td>
// 								<td><a href="" class="botao">Editar</a></td>
// 							</tr>';
// 		}
// 		echo'			</tbody>
// 					</table>
// 				</div>';
				
				
// 	}
	
	
	
	public function telaDefinicoes() {
		$this->dao = new DAO ();
		$this->view = new DefinicoesView ();
		
		$selecaoUnidade = "active";
		$selecaoTurnos = "";
		$selecaoTipos = "";
		$selecaoCustos = "";
		$selecaoCatracas = "";
		if (isset ( $_GET ['cadastrar_unidade'] ) || isset ( $_POST ['certeza_cadastrar_unidade'] )) {
			$selecaoUnidade = "active";
			$selecaoTurnos = "";
			$selecaoTipos = "";
			$selecaoCatracas = "";
			$selecaoCustos = "";
		} else if (isset ( $_POST ['certeza_cadastrar_turno'] ) || isset ( $_GET ['cadastrar_turno'] )) {
			$selecaoUnidade = "";
			$selecaoTurnos = "active";
			$selecaoTipos = "";
			$selecaoCatracas = "";
			$selecaoCustos = "";
		} else if (isset ( $_GET ['cadastrar_tipo'] ) || isset ( $_POST ['certeza_cadastrar_tipo'] )) {
			$selecaoUnidade = "";
			$selecaoTurnos = "";
			$selecaoCatracas = "";
			$selecaoTipos = "active";
			$selecaoCustos = "";
		} else if (isset ( $_GET ['custo_cartao'] ) || isset ( $_GET ['custo_refeicao'] )) {
			$selecaoUnidade = "";
			$selecaoTurnos = "";
			$selecaoCatracas = "";
			$selecaoTipos = "";
			$selecaoCustos = "active";
		}
		
		else if(isset($_GET['editar_catraca']) || isset($_GET['lista_catracas'])){
			$selecaoUnidade = "";
			$selecaoTurnos = "";
			$selecaoCatracas = "active";
			$selecaoTipos = "";
			$selecaoCustos = "";
		}
		
		echo '<div class="navegacao"> <div class = "simpleTabs">
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
		  
// 		  $this->telaMensagem();
		 
// 		  echo '</div>
// 		  		<div class = "simpleTabsContent">';
		  
		  $this->telaTiposDeUsuarios ();
		  
		  echo '</div>
		  		<div class = "simpleTabsContent">';		 
		  
		  $this->telaDeCustos ();		  
		  
		  echo '	</div>		 			
				</div>';
		
	}
}

?>