<?php 

class ValidacaoController{
	
	private $view;
	private $dao;
	
	public static function main($nivelAcesso){
		
		$valida = new ValidacaoController();
		$valida->telaValidacao();	
		
	}
	
	public function telaValidacao(){
		
		echo '	<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">
			            <li><a href="#">Autenticação</a></li>
			        </ul>
					<div class = "simpleTabsContent">';
		$this->Validacao();
		echo '		</div>
				</div>';
		
	}
	
	
	public function Validacao(){
		
		$this->view = new ValidacaoView();
		
		$tipoDao = new TipoDAO();
		$validaDao = new ValidacaoDAO();
		
		$listaTipos = $tipoDao->retornaLista();
		$listaCampos = $validaDao->retornaCampos();
		$listaValidacao = $validaDao->listaValidacao();
			
		$this->view->formValidacao($listaTipos, $listaCampos);
		
		
		if (isset($_GET['salvar'])){			
			if (isset($_POST['confirmar'])){
				if ($validaDao->inserirValidacao($_GET['campo'], $_GET['valor'], $_GET['tipo'])){
					$this->view->mensagem('sucesso', 'Dados inseridos com sucesso!');
					return;
				}else{
					$this->view->mensagem('erro', 'Erro ao inserir os dados!');
					return;
				}
			}
			$this->view->mensagem('ajuda', 'Deseja salvar estes dados?');
			$this->view->formConfirmar();
			return ;
		}		
		
		if (isset($_GET['excluir'])){
			if (isset($_POST['confirmar'])){
				if ($validaDao->excluirValidacao($_GET['validacao_id'])){
					$this->view->mensagem('sucesso', 'Dados excluídos com sucesso!');
					return;
				}else {
					$this->view->mensagem('erro', 'Erro ao excluir os dados!');
					return;
				}
			}
			$this->view->mensagem('ajuda', 'Deseja excluir estes dados?');
			$this->view->formConfirmar('concluir');
			return ;
		}
		
		$this->view->tabelaCampos($listaValidacao);
	}	
}

?>