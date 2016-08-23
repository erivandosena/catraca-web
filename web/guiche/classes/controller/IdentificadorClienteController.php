<?php

class IdentificadorClienteController{
	
	public static function main($nivel){
	
		if($nivel == Sessao::NIVEL_SUPER){	
			$identificadorCliente = new IdentificadorClienteController();
			$identificadorCliente->telaCliente();
		}
	
	
	}
	
	public function telaCliente(){
				
		if (!isset($_SESSION['numero_cartao'])){
			echo '	<div class="doze colunas borda relatorio">
						<div class="alerta-ajuda dez no-centro">
							<div class="icone icone-warning ix24"></div>
							<div class="titulo-alerta">Atenção!</div>
							<div class="subtitulo-alerta">Inicie a catraca vitual, antes de iniciar o Cliente!</div>
						</div>				
					</div>';
			echo '<meta http-equiv="refresh" content="3; url=?pagina=identificador">';
			return false;
		}else {
			$numeroCartao = $_SESSION['numero_cartao'];
			$nome = $_SESSION['nome_usuario'];
			$tipo = $_SESSION['tipo_usuario'];
			$confirma = $_SESSION['confirmado'];
			$imagem = $numeroCartao;
		}
		
		if (!file_exists('img/'.$imagem.'.jpg')){
			$imagem = "sem-imagem";
		}		
		
		echo'			<div id="usuario">
				
							<div class="doze colunas borda relatorio">
				
								<div class="doze colunas">
									<div class="duas colunas">
										<a href="http://www.unilab.edu.br">
											<img class="imagem-responsiva centralizada" src="img/logo-unilab.png" alt="">
										</a>
									</div>
									<div class="oito colunas">
										<h2 style="font-size:55px">Restaurante Universitário</h2>
									</div>
									<div class="duas colunas">
										<img class="imagem-responsiva centralizada" src="img/pp.jpg" alt="">
									</div>
									<hr class="um"><br>
								</div>			
				
								<div class="doze colunas dados-usuario">
				
									<h1 id="titulo-dois" class="centralizado" style="font-size:48px">Identificação do Usuario</h1><br>
				
									<hr class="um">
									<div>
										<div id="imagem" class="quatro colunas">
											<img id="img" src="img/'.$imagem.'.jpg" alt="" style="width:16cm;height:18cm">
										</div>
					
										<div class="oito colunas">											
											<div id="informacao" class="fundo-cinza1" style="padding: 113px">											
												<br><br><br><br>
												<div id="dados" class="dados" style="font-size:46px">';											
		if ($numeroCartao == ""){			
			echo '<span id="aproxime">Por favor, aproxime o seu cartão.</span>';		
		}else {
			echo'									
													<span id="cart">Nº Cartão: '.$numeroCartao.'</span><br>
													<span >Nome: '.$nome.'</span><br>
													<span >Tipo: '.$tipo.'</span><br>
													<span >Matrícula: </span>';
		}
		echo'									</div>
											</div>
										</div>
									</div>
								</div>
				
								<div class="doze colunas">
									<br>';
			
		if ($confirma == "confirmado"){				
		echo'						<div class="alerta-sucesso dez no-centro">
										<div class="icone icone-warning ix24"></div>
										<div class="titulo-alerta">Ok!</div>
										<div class="subtitulo-alerta">Acesso Liberado!</div>
									</div>';		
		}elseif ($confirma == "aguarde"){
		echo'						<div class="alerta-ajuda dez no-centro">
										<div class="icone icone-checkmark ix24"></div>
										<div class="titulo-alerta">Aguarde!</div>
										<div class="subtitulo-alerta">Estamos liberando seu acesso!</div>
									</div>';
		}
		echo'					</div>
				
							</div>
							</div>		
						</div>				
					</div>
				</div>';		
	}
	
}

?>