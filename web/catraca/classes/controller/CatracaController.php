<?php
class CatracaController {
	private $view;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				
				$controller = new CatracaController ();
				$controller->controlar ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function CatracaController() {
		$this->view = new CatracaView ();
	}
	public function controlar() {
		$unidadeDao = new UnidadeDAO ( null, DAO::TIPO_PG_LOCAL );
		if(!isset($_GET['unidade']) && !isset($_GET['completo']) && !isset($_GET['detalhe'])){
			$lista = $unidadeDao->retornaLista ();
			$this->view->listaDeUnidadesAcademicas ( $lista );
		}
		if(isset($_GET['unidade'])){
			$unidade = new Unidade();
			$unidade->setId(intval($_GET['unidade']));
			$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade($unidade);
			$this->view->listaDeCatracas($listaDeCatracas);
			
		}else if(isset($_GET['completo'])){
			$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade();
			$this->view->listaDeCatracas($listaDeCatracas);
		}
		else if(isset($_GET['detalhe'])){
			
			$catraca = new Catraca();
			$catraca->setId(intval($_GET['detalhe']));
			$unidadeDao->detalheCatraca($catraca);
			$this->view->detalheCatraca($catraca);
			
			
		}
		
		
		
	}
	
}

?>