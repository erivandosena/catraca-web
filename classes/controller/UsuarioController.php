<?php

<<<<<<<< HEAD:web/classes/controller/UsuarioController.php
class UsuarioController{
	
	public static function main($nivelDeAcesso, $loginComLdap = false){
		switch ($nivelDeAcesso){

========




class UsuarioController{
	
	public static function main($nivelDeAcesso){
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				break;
>>>>>>>> origin/artificio_para_controle:web/controle/classes/controller/UsuarioController.php
			case Sessao::NIVEL_DESLOGADO:
				$usuarioController = new UsuarioController();
				$usuarioController->telaLogin($loginComLdap);
				break;
			default:
				$sessao = new Sessao();
<<<<<<<< HEAD:web/classes/controller/UsuarioController.php
				$usuario = new Usuario();
				$usuario->setLogin($sessao->getLoginUsuario());
				$usuarioDao = new UsuarioDAO();
				$usuarioDao->preenchePorLogin($usuario);
				$nome = $usuario->getNome();
				$lista = explode(' ', $nome);
				$nome = $lista[0];
				echo '<p>Olá, '.ucfirst  ( strtolower ($nome)).'!</p>
						<p>Visualize abaixo seus dados referentes ao Restaurante Universitário</p>';
				
				PessoalController::main($nivelDeAcesso);		
========
				
				$usuario = new Usuario();
				$usuario->setLogin($sessao->getLoginUsuario());
				
				$usuarioDao = new UsuarioDAO();
				
				$usuarioDao->preenchePorLogin($usuario);
				
				echo '<div class="borda"><br><br><p>Olá, '.lcfirst ( strtolower ($usuario->getNome())).'! O seu usuário é de nível padrão. Infelizmente a página de usuário padrão só será concluída no dia 22/12/2015. <br>
				
						Até lá temos apenas página de usuário administrador. Caso queira se tornar um usuário administrador peça para que o um usuário que já seja administrador mude o seu nível de acesso para usuário administrador utilizando a interface administrativa. <br>
				
						Caso não exista nenhum usuário administrador, peça a um administrador do banco de dados que passe a seguinte instrução SQL:
						"UPDATE usuario set usua_nivel = '.Sessao::NIVEL_SUPER.' WHERE usua_login = \''.$usuario->getLogin().'\';".</p>
						<br>
								Depois clique em sair logo abaixo:  </p><h1><a href="?sair=1">sair</a></h1> e tente logar novamente.
								</div>
						';
>>>>>>>> origin/artificio_para_controle:web/controle/classes/controller/UsuarioController.php
				break;
		}

		
	}
	
	public static function gerenciaAdmin($nivelDeAcesso){
		switch ($nivelDeAcesso)
		{
			case Sessao::NIVEL_SUPER:
				$usuarioController = new UsuarioController();
				$usuarioController->gerenciamentoDeAdministrador();
				break;
			default:
				break;
		}
	}
	public function telaLogin($loginComLdap = false){
		$usuarioView = new UsuarioView();
		$erro=FALSE;
<<<<<<<< HEAD:web/classes/controller/UsuarioController.php
		if(!isset($_POST['formlogin'])){
			$usuarioView->mostraFormularioLogin();
			return;
		}
========
		if(isset($_POST['formlogin']))
		
		{
			$usuarioDAO = new UsuarioDAO(null, DAO::TIPO_PG_LOCAL);
			$usuario = new Usuario();
			$usuario->setLogin($_POST['login']);
			$usuario->setSenha($_POST['senha']);
			if($usuarioDAO->autentica($usuario)){
>>>>>>>> origin/artificio_para_controle:web/controle/classes/controller/UsuarioController.php
		
	
		$usuarioDAO = new UsuarioDAO();
		$usuario = new Usuario();
		$usuario->setLogin($_POST['login']);
		$usuario->setSenha($_POST['senha']);
		if($loginComLdap){
			if($usuarioDAO->autenticaLdap($usuario)){
				$sessao2 = new Sessao();
				$sessao2->criaSessao($usuario->getId(), $usuario->getNivelAcesso(), $usuario->getLogin());
				echo '<meta http-equiv="refresh" content=1;url="./index.php">';
				return;
			}
			$msg_erro= "Senha ou usuário Inválido";
			$erro=true;
			$usuarioView->mostraFormularioLogin($erro, $msg_erro);
			return;
		}
		if($usuarioDAO->autentica($usuario)){
	
			$sessao2 = new Sessao();
			$sessao2->criaSessao($usuario->getId(), $usuario->getNivelAcesso(), $usuario->getLogin());
			echo '<meta http-equiv="refresh" content=1;url="./index.php">';
			return;
		}else{
			$msg_erro= "Senha ou usuário Inválido";
			$erro=true;
			$usuarioView->mostraFormularioLogin($erro, $msg_erro);
			return;
	
		}
	
		
	}
	/**
	 * Atravez dessa aplicacao sera possivel definir um usuario para administrar um novo laboratorio. 
	 */
	public function gerenciamentoDeAdministrador(){
		
		if(isset($_GET['form_gerencia_adm'])){
			if($_GET['usuario'] && $_GET['laboratorio'])
			{
				$usuario = new Usuario();
				$usuario->setLogin($_GET['usuario']);
				$laboratorio = new Laboratorio();
				$laboratorio->setNome($_GET['laboratorio']);
				$usuarioDao = new UsuarioDAO();
				if(!$usuarioDao->preenchePorLogin($usuario)){
					echo "Usuario Inexistente";
					return;
				}
				
				if(!$usuarioDao->preenchePorNome($laboratorio)){
					echo "Laboratorio Inexistente";
					return;
				}
				
				if($usuarioDao->ehAdministrador($usuario, $laboratorio)){
					echo "Ele ja era administrador";
					return;
				}
				if(!$usuarioDao->adicionaAdministrador($usuario, $laboratorio)){
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