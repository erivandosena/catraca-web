<?php



/**
 * 
 * Esta classe gerencia as telas e eventos para configuração de validações. 
 * 
 * @author Jefferson Uchoa Ponte
 *
 */
class ValidacoesController{
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$controller = new ValidacoesController();
				$controller->telaDefinicoes ();
				break;
			case Sessao::NIVEL_ADMIN:
				$controller = new ValidacoesController();
				$controller->telaDefinicoes ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
		
	}
	public function telaDefinicoes(){
		
		echo "Preciamos ver as validações. <br>";
		echo "Precisamos eliminar validações<br>";
		
	}
}


?>