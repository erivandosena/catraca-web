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
	 *
	 * @param unknown $nivelDeAcesso        	
	 */
	public static function gerenciaAdmin($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$usuarioController = new UsuarioController ();
				$usuarioController->gerenciamentoDeAdministrador ();
				break;
			default :
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
	
	/**
	 * 
	 * @ignore Atravez dessa aplicacao sera possivel definir um usuario para administrar um novo laboratorio.
	 */
	public function gerenciamentoDeAdministrador() {
		if (isset ( $_GET ['form_gerencia_adm'] )) {
			if ($_GET ['usuario'] && $_GET ['laboratorio']) {
				$usuario = new Usuario ();
				$usuario->setLogin ( $_GET ['usuario'] );
				$laboratorio = new Laboratorio ();
				$laboratorio->setNome ( $_GET ['laboratorio'] );
				$usuarioDao = new UsuarioDAO ();
				if (! $usuarioDao->preenchePorLogin ( $usuario )) {
					echo "Usuario Inexistente";
					return;
				}
				
				if (! $usuarioDao->preenchePorNome ( $laboratorio )) {
					echo "Laboratorio Inexistente";
					return;
				}
				
				if ($usuarioDao->ehAdministrador ( $usuario, $laboratorio )) {
					echo "Ele ja era administrador";
					return;
				}
				if (! $usuarioDao->adicionaAdministrador ( $usuario, $laboratorio )) {
					echo "Erro na transacao principal";
					return;
				}
				echo "Sucesso";
				return;
			}
		}
		
		echo '<div class="resolucao">
            <div class="doze colunas">
                <div class="conteudo fundo-branco">';
		echo '<form action="#" method="get" name="form_gerencia_adm" id="pesquisa" class="formulario-organizado">
                      <label for="usuario">
                      <object class="">Login do Usuario: </object>
		
                      <input type="text" name="usuario" id="usuario" />
                      </label>
					<label for="laboratorio">
                      <object class="">Laboratorio: </object>
		
                      <input type="text" name="laboratorio" id="laboratorio" />
                      </label>
						<input type="hidden" name="pagina" value="gerenciamento_administrador" />
                        <input type="submit" value="enviar" name="form_gerencia_adm" />
                    </form></div>
            </div>
        </div>';
	}
}
?>