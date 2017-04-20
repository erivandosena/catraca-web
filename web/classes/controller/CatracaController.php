<?php
/**
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */

class CatracaController {
	private $view;
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new CatracaController ();
				$controller->controlar ();
				break;
			case Sessao::NIVEL_ADMIN:
				$controller = new CatracaController ();
				$controller->controlar ();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	public function CatracaController() {
		$this->view = new CatracaView ();
	}
	public function controlar() {
		
		$unidadeDao = new UnidadeDAO ();
		if(!isset($_GET['unidade']) && !isset($_GET['completo']) && !isset($_GET['detalhe'])){
			$this->view->abreContainer("Selecione uma Unidade Acadêmica");
			$lista = $unidadeDao->retornaLista ();
			foreach ($lista as $unidadeAcademica){
				$catracasDessaUnidade = $unidadeDao->retornaCatracasPorUnidade($unidadeAcademica);
				$i = 0;
				$j = 0;
				foreach ($catracasDessaUnidade as $catracaDessaUnidade){
					$i += $unidadeDao->totalDeGirosDaCatraca($catracaDessaUnidade);
					$j += $unidadeDao->totalDeGirosDaCatracaTurnoAtual($catracaDessaUnidade);				
				}
				$this->view->mostrarUnidade($unidadeAcademica, count($catracasDessaUnidade) , $i);
				
			}
			$this->view->fechaContainer();
		}
		if(isset($_GET['unidade'])){
			$this->view->abreContainer();
			
			$unidade = new Unidade();
			$unidade->setId(intval($_GET['unidade']));
			$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade($unidade);
			foreach ($listaDeCatracas as $catraca){
				$valor = $unidadeDao->totalDeGirosDaCatraca($catraca);
				$outroValor = $unidadeDao->totalDeGirosDaCatracaTurnoAtual($catraca);
				$this->view->mostraCatraca($catraca, $outroValor, $valor);
				
			}
			$this->view->fechaContainer();
			
		}else if(isset($_GET['completo'])){
			$this->view->abreContainer();
			//Script do Ajax pra atualizar a lista de catracas.
			$listaDeCatracas = $unidadeDao->retornaCatracasPorUnidade();
			
			foreach ($listaDeCatracas as $catraca){
				$valor = $unidadeDao->totalDeGirosDaCatraca($catraca);
				$outroValor = $unidadeDao->totalDeGirosDaCatracaTurnoAtual($catraca);
				$this->view->mostraCatraca($catraca, $outroValor, $valor);
				
			}
			$this->view->fechaContainer();
		}
		else if(isset($_GET['detalhe'])){
			$catraca = new Catraca();
			$catraca->setId(intval($_GET['detalhe']));
			$unidadeDao->preencheCatracaPorId($catraca);
			$valor = $unidadeDao->totalDeGirosDaCatraca($catraca);
			$outroValor = $unidadeDao->totalDeGirosDaCatracaTurnoAtual($catraca);
			$this->view->detalheCatraca($catraca, $outroValor, $valor);
			
		}
		
		
		
	}
	
}

?>