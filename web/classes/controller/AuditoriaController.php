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
 * Classe resposável por auditar todos os acessos ao sistema Catraca,
 * é capturado a URL acessada e posteriormente inserida no Banco.
 */
class AuditoriaController {
	
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
				$controller = new AuditoriaController ();
				$controller->telaAuditoria ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	/**
	 * Função utilizada para gerar a tela responsável por exibir todos os acessos dos usuário no sistema.
	 */
	public function telaAuditoria() {
		echo '	<div class="doze colunas borda">
					<div class="resolucao config">
						<form action="">
							<input type="datetime-local" name="data_inicial" />
							<input type="datetime-local" name="data_final" />
							<input type="text" name="id_usuario" />
							<input type="hidden" name="pagina" value="auditoria" />
							<input type="submit" />
						</form>';
		
		if (isset ( $_GET ['data_inicial'] ) && isset ( $_GET ['data_final'] ) && isset ( $_GET ['id_usuario'] )) {
			$dataInicial = $_GET ['data_inicial'];
			$dataFinal = $_GET ['data_final'];
			$nome = $_GET ['id_usuario'];
			$dao = new DAO ();
			Auditoria::mostrar ( $dao->getConexao (), $nome, $dataInicial, $dataFinal );
		} else {
			$dao = new DAO ();
			Auditoria::mostrar ( $dao->getConexao () );
		}
		echo '	</div>
				</div>';
	}
}