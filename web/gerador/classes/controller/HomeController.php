<?php


class HomeController{
	
	public static function main($nivelDeAcesso){
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				GeradorController::main();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
		
	}
	
	
}


?>