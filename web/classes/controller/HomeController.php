<?php
/**
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */

class HomeController{
	
	public static function main($nivelDeAcesso){
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				//Acessa tudo. 
				CartaoController::main($nivelDeAcesso);
				break;
			case Sessao::NIVEL_ADMIN:
				//Acessa tudo que já foi homologado. 
				CartaoController::main($nivelDeAcesso);
				break;

			case Sessao::NIVEL_POLIVALENTE:
				//Acessa tudo que já foi homologado. 
				CartaoController::main($nivelDeAcesso);
				break;
			case Sessao::NIVEL_GUICHE:
				//Acessa cadastro e venda de creditos. 
				GuicheController::main($nivelDeAcesso);
				break;
			case Sessao::NIVEL_CATRACA_VIRTUAL:
				//Acessa catraca virtual. 
				CartaoController::main($nivelDeAcesso);
				break;
			case Sessao::NIVEL_CADASTRO:
				//So faz cadastro
				CartaoController::main($nivelDeAcesso);
				break;
			case Sessao::NIVEL_RELATORIO:
				//So faz cadastro
				RelatorioController::main($nivelDeAcesso);
				break;
				
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
		
	}
	
	
}


?>