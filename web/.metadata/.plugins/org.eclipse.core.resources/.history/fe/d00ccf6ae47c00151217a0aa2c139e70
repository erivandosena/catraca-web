<?php


class UsuarioController{
	
	public static function main($tela){
		switch ($tela){
			case Sessao::NIVEL_SUPER:
				echo 	'<meta http-equiv="refresh" content=1;url="index.php">';
				break;
			case Sessao::NIVEL_DESLOGADO:
				$usuarioController = new UsuarioController();
				$usuarioController->telaLogin();
				break;
			default:
				echo 	'<meta http-equiv="refresh" content=1;url="index.php">';
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
	public function telaLogin(){
		$usuarioView = new UsuarioView();
		$erro=FALSE;
		if(isset($_POST['formlogin']))
		
		{
			$usuarioDAO = new UsuarioDAO();
			$usuario = new Usuario();
			$usuario->setLogin($_POST['login']);
			$usuario->setSenha($_POST['senha']);
			if($usuarioDAO->autentica($usuario)){
		
				$sessao2 = new Sessao();
				$sessao2->criaSessao($usuario->getId(), $usuario->getNivelAcesso(), $usuario->getLogin());
				echo '<meta http-equiv="refresh" content=1;url="index.php">';
			}else{
				$msg_erro= "Senha ou usuário Inválido";
				$erro=true;
				
				$usuarioView->mostraFormularioLogin($erro, $msg_erro);
				return;
		
			}
		}
		$usuarioView->mostraFormularioLogin();
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