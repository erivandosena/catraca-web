<?php


class AuditoriaController{
	
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new AuditoriaController();
				$controller->telaAuditoria();		
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	public function telaAuditoria(){
		$dao = new DAO();
		Auditoria::mostrar($dao->getConexao());
		
		
	}
	
	
}