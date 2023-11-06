<?php
/**
 * Classe utilizada para centralizar as demais Classes(DAO, Model, View, Util).
 * Esta classe será instaciada no index.php.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */
/**
 * 
 * Esta Classe fará o direcionamento do usuário de acordo com o nível do usuário.
 *
 */
class HomeController {
	
	/**
	 * Metodo principal utilizada para controlar o acesso a classe através do nível de acesso do usuario.
	 *
	 * @param Sessao $nivelDeAcesso
	 *        	Recebe uma Sessão que contém o nível de acesso do usuario,
	 *        	esta Sessão é iniciada na página principal, durante o login do usuario.
	 */
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				// Acessa tudo.
				CartaoController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_ADMIN :
				// Acessa tudo que já foi homologado.
				CartaoController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_POLIVALENTE :
				// Acessa tudo que já foi homologado.
				CartaoController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_GUICHE :
				// Acessa cadastro e venda de creditos.
				GuicheController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_CATRACA_VIRTUAL :
				// Acessa catraca virtual.
				CartaoController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_CADASTRO :
				// So faz cadastro
				CartaoController::main ( $nivelDeAcesso );
				break;
			case Sessao::NIVEL_RELATORIO :
				// So faz cadastro
				RelatorioController::main ( $nivelDeAcesso );
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
}

?>