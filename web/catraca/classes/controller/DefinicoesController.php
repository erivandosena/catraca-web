<?php


class DefinicoesController{
	
	private $view;
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new DefinicoesController();
				$controller->telaDefinicoes();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function telaConfiguracaoUnidadeAcademica(){
		$this->view->formInserirUnidade();
		$unidadeDao = new UnidadeDAO($this->dao->getConexao());
		if(isset($_GET['cadastrar_unidade']))
		{

			echo '
					<div class="borda">
					<p>Você tem certeza que quer adicionar essa unidade acadêmica? </p><p>'.$_GET['cadastrar_unidade'].'</p><br>';
			echo '<form action="" method="post" class="formulario sequencial texto-preto">
						<input type="hidden" name="certeza_cadastrar_unidade" value="'.$_GET['cadastrar_unidade'].'" />
						<input  type="submit"  name="certeza" value="Tenho Certeza"/></form>';
			
			echo '</div>';
				
		}
		if(isset($_POST['certeza_cadastrar_unidade'])){
			$unidade = $_POST['certeza_cadastrar_unidade'];
			$unidade = preg_replace ('/[^a-zA-Z0-9\s]/', '', $unidade);
			if($this->dao->getConexao()->exec("INSERT INTO unidade(unid_nome) VALUES('$unidade');")){
				$this->view->mostraSucesso("Sucesso");
			}
			else{
				$this->view->mostraSucesso("Erro ao tentar inserir unidade");
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		}else{
			$unidadesAcademicas = $unidadeDao->retornaLista();
			$this->view->listarUnidadesAcademicas($unidadesAcademicas);
		}
		
		
		
		//$this->view->formAdicionarTurnoNaUnidade();
	}
	public function telaConfiguracaoDeTurnos(){
		$this->view->formAdicionarTurno();
		$turnoDao = new TurnoDAO($this->dao->getConexao());
		
		
		
		if(isset($_GET['cadastrar_turno']))
		{
		
			
			echo '
					<div class="borda">
					<p>Você tem certeza que quer adicionar esse turno? </p><p>'.$_GET['turno_nome'].'</p><br>';
			echo '<form action="" method="post" class="formulario sequencial texto-preto">
						
					<input type="hidden" name="hora_inicio" value="'.$_GET['hora_inicio'].'" />
							<input type="hidden" name="hora_fim" value="'.$_GET['hora_fim'].'" />
									<input type="hidden" name="turno_nome" value="'.$_GET['turno_nome'].'" />
											
						<input  type="submit"  name="certeza_cadastrar_turno" value="Tenho Certeza"/></form>';
				
			echo '</div>';
		
		}
		if(isset($_POST['certeza_cadastrar_turno'])){
			$turnoNome = $_POST['turno_nome'];
			$turnoNome = preg_replace ('/[^a-zA-Z0-9\s]/', '', $turnoNome);
			$horaInicio = $_POST['hora_inicio'];
			$horaFim = $_POST['hora_fim'];
			
			if($this->dao->getConexao()->exec("INSERT INTO turno(turn_hora_inicio,turn_hora_fim,turn_descricao) VALUES('$horaInicio', '$horaFim', '$turnoNome');")){
				$this->view->mostraSucesso("Sucesso");
			}
			else{
				$this->view->mostraSucesso("Erro ao tentar inserir unidade");
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		}else{
			$turnos = $turnoDao->retornaLista();
			$this->view->listarTurnos($turnos);
		}
		
		
		
		//$this->view->formAdicionarTurnoNaUnidade();
		
		
	}
	
	public function telaTiposDeUsuarios(){
		
		$this->view->formAdicionarTipoDeUsuario();
		$tipoDao = new TipoDAO($this->dao->getConexao());
		
		
		
		if(isset($_GET['cadastrar_tipo']))
		{
		
				
			echo '
					<div class="borda">
					<p>Você tem certeza que quer adicionar esse tipo de usuário? </p><p>'.$_GET['tipo_nome'].'</p><br>';
			echo '<form action="" method="post" class="formulario sequencial texto-preto">
		
					<input type="hidden" name="tipo_nome" value="'.$_GET['tipo_nome'].'" />
							<input type="hidden" name="tipo_valor" value="'.$_GET['tipo_valor'].'" />
						<input  type="submit"  name="certeza_cadastrar_tipo" value="Tenho Certeza"/></form>';
			echo '</div>';
		
		}
		if(isset($_POST['certeza_cadastrar_tipo'])){
			$tipoNome = $_POST['tipo_nome'];
			
			$tipoNome = preg_replace ('/[^a-zA-Z0-9\s]/', '', $tipoNome);
			$tipoValor = floatval($_POST['tipo_valor']);
			
				
			if($this->dao->getConexao()->exec("INSERT INTO tipo(tipo_nome, tipo_valor) VALUES('$tipoNome', $tipoValor);")){
				$this->view->mostraSucesso("Sucesso");
			}
			else{
				$this->view->mostraSucesso("Erro ao tentar inserir unidade");
			}
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			return;
		}else{
			$tipos = $tipoDao->retornaLista();
			$this->view->listarTiposDeUsuarios($tipos);
		}
		
		
		
	}
	
	
	
	public function telaDeCustos(){
		$custoAtualRefeicao = 0;
		$result = $this->dao->getConexao()->query("SELECT cure_valor FROM custo_refeicao ORDER BY cure_id DESC LIMIT 1 ;");
		foreach ($result as $linha){
			$custoAtualRefeicao = $linha['cure_valor'];
			break;
		}
		$custoCartao = 0;
		$result = $this->dao->getConexao()->query("SELECT cuca_valor  FROM custo_cartao ORDER BY cuca_id DESC LIMIT 1 ;");
		foreach ($result as $linha){
			$custoCartao = $linha['cuca_valor'];
			break;
		}
		
		
		$this->view->formAlterarCustoRefeicao($custoAtualRefeicao);
		$this->view->formAlterarCustoCartao($custoCartao);
		
		if(isset($_GET['custo_refeicao'])){
			$dataTimeAtual = date ( "Y-m-d G:i:s" );
			$valor = floatval($_GET['custo_refeicao']);
			if($this->dao->getConexao()->exec("INSERT into custo_refeicao(cure_valor, cure_data) VALUES($valor, '$dataTimeAtual')"))
				$this->view->mostraSucesso("Custo Modificado Com Sucesso");
			else
				$this->view->mostraSucesso("Erro");
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
			
		}
		if(isset($_GET['custo_cartao'])){
			$dataTimeAtual = date ( "Y-m-d G:i:s" );
			$valor = floatval($_GET['custo_cartao']);
			if($this->dao->getConexao()->exec("INSERT into custo_cartao(cuca_valor , cuca_data ) VALUES($valor, '$dataTimeAtual')"))
				$this->view->mostraSucesso("Custo Modificado Com Sucesso");
			else
				$this->view->mostraSucesso("Erro");
			echo '<meta http-equiv="refresh" content="4; url=.\?pagina=definicoes">';
		}
		
		
	}
	private $dao;
	public function telaDefinicoes(){
		
		$this->dao = new DAO(null, DAO::TIPO_PG_LOCAL);
		$this->view = new DefinicoesView();
		echo '<section id="navegacao">
				<ul class="nav nav-tabs">';
		$selecaoUnidade = "active";
		$selecaoTurnos = "";
		$selecaoTipos = "";
		$selecaoCustos = "";
		if(isset($_GET['cadastrar_unidade']) || isset($_POST['certeza_cadastrar_unidade'])){
			$selecaoUnidade = "active";
			$selecaoTurnos = "";
			$selecaoTipos = "";
			$selecaoCustos = "";
		}else if(isset($_POST['certeza_cadastrar_turno']) || isset ( $_GET['cadastrar_turno'])){
			$selecaoUnidade = "";
			$selecaoTurnos = "active";
			$selecaoTipos = "";
			$selecaoCustos = "";
		}else if(isset($_GET['cadastrar_tipo']) || isset ( $_POST['certeza_cadastrar_tipo']) ){
			$selecaoUnidade = "";
			$selecaoTurnos = "";
			$selecaoTipos = "active";
			$selecaoCustos = "";
		}else if(isset($_GET['custo_cartao']) || isset ($_GET['custo_refeicao'])){
			$selecaoUnidade = "";
			$selecaoTurnos = "";
			$selecaoTipos = "";
			$selecaoCustos = "active";
		}
		echo '
					<li role="presentation" class="'.$selecaoUnidade.'"><a href="#tab1" data-toggle="tab">Unidades Acadêmicas</a></li>
					<li role="presentation" class="'.$selecaoTurnos.'"><a href="#tab2" data-toggle="tab">Turnos</a></li>
					<li role="presentation" class="'.$selecaoTipos.'"><a href="#tab3" data-toggle="tab">Tipos de Usuários</a></li>
					<li role="presentation" class="'.$selecaoCustos.'"><a href="#tab4" data-toggle="tab">Custos</a></li>
				
							';
		
		
		
		echo '
				</ul><div class="tab-content">';
		echo '<div class="tab-pane '.$selecaoUnidade.'" id="tab1">';
		$this->telaConfiguracaoUnidadeAcademica();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoTurnos.'" id="tab2">';
		$this->telaConfiguracaoDeTurnos();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoTipos.'" id="tab3">';
		$this->telaTiposDeUsuarios();
		echo '</div>';
		echo '<div class="tab-pane '.$selecaoCustos.'" id="tab4">';
		$this->telaDeCustos();
		echo '</div>';
		echo '</section>';
		
		
	}
	
}


?>