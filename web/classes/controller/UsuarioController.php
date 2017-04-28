<?php
/**
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */
class UsuarioController {
	
	/**
	 * Metodo principal utilizada para controlar o acesso a classe através do nível de acesso do usuario.
	 *
	 * @param Sessao $nivelDeAcesso
	 *        	Recebe uma Sessão que contém o nível de acesso do usuario,
	 *        	esta Sessão é iniciada na página principal, durante o login do usuario.
	 */
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			
			case Sessao::NIVEL_DESLOGADO :
				$usuarioController = new UsuarioController ();
				$usuarioController->telaLogin ();
				break;
			default :
				$sessao = new Sessao ();
				
				$usuario = new Usuario ();
				$usuario->setLogin ( $sessao->getLoginUsuario () );
				
				$usuarioDao = new UsuarioDAO ();
				
				$usuarioDao->preenchePorLogin ( $usuario );
				$nome = $usuario->getNome ();
				$lista = explode ( ' ', $nome );
				$nome = $lista [0];
				echo '<p>Olá, ' . ucfirst ( strtolower ( $nome ) ) . '!</p>
						<p>Visualize abaixo seus dados referentes ao Restaurante Universitário</p>';
				
				PessoalController::main ( $nivelDeAcesso );
				
				break;
		}
	}
	
	/**
	 * Função Utilizada para gerar a tela de login, e com os dados fornecidos por ela,
	 * atraves do usuário realizar a autenticação do usuário no sistema.
	 * 
	 * Nela será criada uma Sessão que será atribuido o nível de acesso do usuário, 
	 * de acordo com o banco de dados.
	 * 
	 * Por padrão, durante o primeiro acesso é fornecido o nivel padrão a todos os usuário.
	 */
	public function telaLogin() {
		$usuarioView = new UsuarioView ();
		$erro = FALSE;
		if (isset ( $_POST ['formlogin'] )) {
			
			$usuarioDAO = new UsuarioDAO ();
			$usuario = new Usuario ();
			$usuario->setLogin ( $_POST ['login'] );
			$usuario->setSenha ( $_POST ['senha'] );
			if ($usuarioDAO->autentica ( $usuario )) {
				
				$sessao2 = new Sessao ();
				$sessao2->criaSessao ( $usuario->getId (), $usuario->getNivelAcesso (), $usuario->getLogin () );
				echo '<meta http-equiv="refresh" content=1;url="./index.php">';
			} else {
				$msg_erro = "Senha ou usuário Inválido";
				$erro = true;
				
				$usuarioView->mostraFormularioLogin ( $erro, $msg_erro );
				return;
			}
		}
		$usuarioView->mostraFormularioLogin ();
	}	
	
}
?>