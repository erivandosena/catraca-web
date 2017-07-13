<?php

/*********
  * Copyright (c) 12/07/2017 {INITIAL COPYRIGHT UNILAB} {OTHER COPYRIGHT LABPATI/DISUP/DTI}.
  * All rights reserved. This program and the accompanying materials
  * are made available under the terms of the Eclipse Public License v1.0
  * which accompanies this distribution, and is available at
  * http://www.eclipse.org/legal/epl-v10.html
  *
  * Contributors:
  *    Jefferson Uchôa Ponte - initial API and implementation and/or initial documentation
  *********/
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