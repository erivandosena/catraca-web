
<?php


ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

date_default_timezone_set ( 'America/Araguaina' );


function __autoload($classe) {
	if (file_exists ( 'classes/dao/' . $classe . '.php' ))
		include_once 'classes/dao/' . $classe . '.php';
	if (file_exists ( 'classes/model/' . $classe . '.php' ))
		include_once 'classes/model/' . $classe . '.php';
	if (file_exists ( 'classes/controller/' . $classe . '.php' ))
		include_once 'classes/controller/' . $classe . '.php';
	if (file_exists ( 'classes/util/' . $classe . '.php' ))
		include_once 'classes/util/' . $classe . '.php';
	if (file_exists ( 'classes/view/' . $classe . '.php' ))
		include_once 'classes/view/' . $classe . '.php';
}

$sessao = new Sessao ();

if (isset ( $_GET ["sair"] )) {
	
	$sessao->mataSessao ();
	header ( "Location:./index.php" );
}




?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>

<meta charset="UTF-8">
<meta name="viewport"
	content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no" />

<title>Projeto Catraca</title>

<script type="text/javascript" src="js/simpletabs_1.3.js"></script>
<link rel="stylesheet" href="css/simpletabs.css" />
<link rel="stylesheet" href="css_spa/spa.css" />
<link rel="stylesheet" href="css/estilo.css" type="text/css" media="screen">
<link rel="stylesheet" href="css/estilo_responsivo.css" type="text/css" media="screen">
<script type="text/javascript" src="js/jquery.min.js"></script>

</head>

<body>




	<div class="pagina fundo-cinza1">
	
		<div class="acessibilidade">
			<div class="config">
				<div class="a-esquerda">
<!-- 					<a href="#conteudo" tabindex="1" accesskey="1">Ir para o conteúdo <b>1</b></a> -->
<!-- 					<a href="#menu" tabindex="2" accesskey="2"><span>Ir para o</span> menu <b>2</b></a> -->
<!-- 					<a href="#busca" tabindex="3" accesskey="3"><span>Ir para a</span> busca <b>3</b></a> -->
<!-- 					<a href="#rodape" tabindex="4" accesskey="4"><span>Ir para o</span> rodapé <b>4</b></a> -->
					</div>
					<div class="a-direita">
<!-- 					<a href="#" id="alto-contraste">ALTO <b>CONTRASTE</b></a> -->
<!-- 					<a href="#" id="mapa-do-site"><b>MAPA DO SITE</b></a> -->
				</div>
			</div>
		</div>
	
		<div id="barra-governo">
			<div class="resolucao config">
				<div class="a-esquerda">
					<a href="http://brasil.gov.br/" target="_blank"><span id="bandeira"></span><span>BRASIL</span></a>
					<a href="http://acessoainformacao.unilab.edu.br/" target="_blank">Acesso
						&agrave;  informa&ccedil;&atilde;o</a>
				</div>
				<div class="a-direita">
					<a href="#"><i class="icone-menu"></i></a>
				</div>
				<ul>
					<li><a href="http://brasil.gov.br/barra#participe" target="_blank">Participe</a></li>
					<li><a href="http://www.servicos.gov.br/" target="_blank">Servi&ccedil;os</a></li>
					<li><a href="http://www.planalto.gov.br/legislacao" target="_blank">Legisla&ccedil;&atilde;o</a></li>
					<li><a href="http://brasil.gov.br/barra#orgaos-atuacao-canais"
						target="_blank">Canais</a></li>
				</ul>
			</div>
		</div>

		<div class="doze colunas gradiente">

			<div id="topo" class="resolucao config">
				<div class="tres colunas">
					<a href="http://www.dti.unilab.edu.br"><img
						class="imagem-responsiva"
						src="img/logo_h-site.png"
						alt=""></a>
				</div>
				<div class="seis colunas centralizado">
					<h1>
						CATRACA<br> <small class="texto-branco">Controle Administrativo de
							Tr&aacute;fego Acadêmico Automatizado</small>
					</h1>
				</div>
				<div class="tres colunas alinhado-a-direita">
					<a href="http://www.unilab.edu.br"><img
						class="imagem-responsiva centralizada"
						src="img/logo-unilab-branco.png"
						alt=""></a>
				</div>
			</div>
		</div>

		
				
				<?php
				
				function auditar(){
					$dao = new DAO();
					$sessao = new Sessao();
					$auditoria = new Auditoria($dao->getConexao());
					
					$obs = " - ";
					if(isset($_POST['catraca_virtual']) && isset($_POST['catraca_id'])){
						$obs = "Selecionou Catraca virtual: ".$_POST['catraca_id'];
							
					}
					
					$auditoria->cadastrar($sessao->getIdUsuario(), $obs);
					$dao->fechaConexao();
					
				}
				
				
				switch ($sessao->getNivelAcesso()){
					case Sessao::NIVEL_SUPER:
					
						auditar();
						echo '
							<div  class="doze colunas barra-menu">
								    <div class="menu-horizontal config">
								        <ol class="a-esquerda">';
							
						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
						echo ' <li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a>
			
									<ul>
										<li><a href="?pagina=cartao">Próprio</a></li>
										<li><a href="?pagina=avulso">Avulso</a></li>
										<li><a href="?pagina=isento">Isento</a></li>
									</ul>
			
			
						</li>';
						
						
						echo '<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
						echo ' <li><a href="?pagina=guiche" class="item"><span class="icone-user"></span> <span class="item-texto">Guichê</span></a></li>';
						echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a>

				
						</li>';
						echo ' <li><a href="?pagina=nivel_acesso" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Nivel de Acesso</span></a></li>';

							
						echo '</ol>
								        <ol class="a-direita" start="4">
											<li><a href="" class="item"><span class="item-texto">Status: Super</span></a></li>
											<li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
		
								        </ol>
								    </div>
								</div>';
						break;
					case Sessao::NIVEL_ADMIN:
						auditar();
						echo '
							<div  class="doze colunas barra-menu">
								    <div class="menu-horizontal config">
								        <ol class="a-esquerda">';
						 
						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
						echo ' <li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
						echo '<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
						
						echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
						//echo ' <li><a href="?pagina=nivel_acesso" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Nivel de Acesso</span></a></li>';
						
						echo '</ol>
								        <ol class="a-direita" start="4">

											<li><a href="" class="item"><span class="item-texto">Status: Adm</span></a></li>
											<li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
								        </ol>
								    </div>
								</div>';
						break;
					
					case Sessao::NIVEL_GUICHE:
						auditar();
						echo '
							<div  class="doze colunas barra-menu">
								    <div class="menu-horizontal config">
								        <ol class="a-esquerda">';
						 
						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
						echo ' <li><a href="?pagina=guiche" class="item"><span class="icone-user"></span> <span class="item-texto">Guichê</span></a></li>';						
						echo '</ol>
								        <ol class="a-direita" start="4">
											<li><a href="" class="item"><span class="item-texto">Status: Guiche</span></a></li>
								            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
								        </ol>
								    </div>
								</div>';
						break;
					case Sessao::NIVEL_CATRACA_VIRTUAL:
					
						auditar();
						echo '
						<div  class="doze colunas barra-menu">
							    <div class="menu-horizontal config">
							        <ol class="a-esquerda">';
							
						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
						echo ' <li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
						
						echo '<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
						echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
					
						echo '</ol>
							        <ol class="a-direita" start="4">
										<li><a href="" class="item"><span class="item-texto">Status: Catraca Virtual</span></a></li>
							            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
							        </ol>
							    </div>
							</div>';
						break;
					case Sessao::NIVEL_CADASTRO:
							
						auditar();
						echo '
					<div  class="doze colunas barra-menu">
						    <div class="menu-horizontal config">
						        <ol class="a-esquerda">';
							
						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';

							
						echo '</ol>
						        <ol class="a-direita" start="4">
									<li><a href="" class="item"><span class="item-texto">Status: Cadastro</span></a></li>
						            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
						        </ol>
						    </div>
						</div>';
						break;
						
						case Sessao::NIVEL_CATRACA_VIRTUAL:
								
							auditar();
							echo '
						<div  class="doze colunas barra-menu">
							    <div class="menu-horizontal config">
							        <ol class="a-esquerda">';
								
							echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
							echo ' <li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
							echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
							echo '<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
							echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
								
							echo '</ol>
							        <ol class="a-direita" start="4">
										<li><a href="" class="item"><span class="item-texto">Status: Catraca Virtual</span></a></li>
							            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
							        </ol>
							    </div>
							</div>';
							break;
						case Sessao::NIVEL_RELATORIO:
								
							auditar();
							echo '
								<div  class="doze colunas barra-menu">
									    <div class="menu-horizontal config">
									        <ol class="a-esquerda">';
								
							echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
							echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
							
								
							echo '</ol>
						        <ol class="a-direita" start="4">
									<li><a href="" class="item"><span class="item-texto">Status: Relatorio</span></a></li>
						            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
						        </ol>
						    </div>
						</div>';
							break;
					default:
						break;
						
				}
					
					
					
					?>
				
			

		<div class="doze colunas">
			<div class="resolucao config">					
						
					<?php

					
					if (isset ( $_GET ['pagina'] )) {
						switch ($_GET ['pagina']) {
							case 'inicio' :
								HomeController::main ( $sessao->getNivelAcesso () );
								break;
// 							case 'definicoes' :
// 								DefinicoesController::main ( $sessao->getNivelAcesso () );
// 								break;
							case 'catraca' :
								
								$filtroIdCatraca = "";
								if(isset($_GET['unidade'])){
									$filtroIdCatraca = "unidade=".$_GET['unidade'];
								}
								else if(isset($_GET['completo'])){
									$filtroIdCatraca = "completo=1";
								}
								echo '
		
										<script>
											var auto_refresh = setInterval (
												function () {
													$.ajax({
														url: \'catracas.php?'.$filtroIdCatraca.'\',
														success: function (response) {
														$(\'#olinda\').html(response);
													}
												});
											}, 1000);
										</script>
								';
								CatracaController::main($sessao->getNivelAcesso());
								break;
							case 'cartao' :
								CartaoController::main ( $sessao->getNivelAcesso () );
								break;
							case 'gerador' :
								CatracaVirtual::main( $sessao->getNivelAcesso () );
								break;
							case 'relatorio' :
								RelatorioController::main($sessao->getNivelAcesso());
								break;
							case 'guiche' :
								GuicheController::main($sessao->getNivelAcesso());
								break;
							case 'definicoes' :
								DefinicoesController::main($sessao->getNivelAcesso());
								break;
							case 'nivel_acesso' :
								NivelAcessoController::main($sessao->getNivelAcesso());
								break;
							case 'avulso' :
								CartaoAvulsoController::main($sessao->getNivelAcesso());
								break;
							case 'isento' :
								CartaoIsentoController::main($sessao->getNivelAcesso());
								break;
							case 'relatorio_guiche' :
								RelatorioControllerGuiche::main($sessao->getNivelAcesso());
								break;
							default :
								echo '404 NOT FOUND';
								break;
						}
					} else {
						
						HomeController::main ( $sessao->getNivelAcesso () );
					}
					
					?>
										
			</div>
 			<script type="text/javascript">
        	var img;

        	navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
        	
            var canvas = document.getElementById("canvas"),
                context = canvas.getContext("2d"),
                video = document.getElementById("video"),
                btnStart = document.getElementById("btnStart"),
                btnStop = document.getElementById("btnStop"),
                btnPhoto = document.getElementById("btnPhoto"),
                videoObj = {
                    video: true,
                    audio: false
                };
            
	        
				 //Compatibility
	            
	
	            btnStart.addEventListener("click", function() {
	                var localMediaStream;
	
	                if (navigator.getUserMedia) {
	                    navigator.getUserMedia(videoObj, function(stream) {              
	                        video.src = (navigator.webkitGetUserMedia) ? window.webkitURL.createObjectURL(stream) : stream;
	                        localMediaStream = stream;
	                        
	                    }, function(error) {
	                        console.error("Video capture error: ", error.code);

	                    });
	                	
	                    btnStop.addEventListener("click", function() {
	                        localMediaStream.stop();
	                        
	                    });
	
	                    btnPhoto.addEventListener("click", function() {
	                        context.drawImage(video, 0, 0, 320, 240);

	                        img = canvas.toDataURL("image/png");
	                        formulario.img64.value = img;

							
	                    });

	                    
	                }
	            });
			
	       

        </script>
		</div>		
	</div>
</body>
</html>