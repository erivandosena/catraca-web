<?php
date_default_timezone_set ( 'America/Araguaina' );

ini_set ( 'display_errors', 1 );
ini_set ( 'display_startup_erros', 1 );
error_reporting ( E_ALL );
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
<link rel="stylesheet"
	href="http://spa.dsi.unilab.edu.br/spa/css/spa.css" />
<link rel="stylesheet" href="css/estilo.css" type="text/css"
	media="screen">

<script type="text/javascript" src="js/jquery.min.js"></script>
</head>

<body>
	<div class="pagina fundo-cinza1">
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

		<div class="doze colunas banner gradiente">

			<div id="topo" class="resolucao config">
				<div class="tres colunas">
					<a href="http://www.dti.unilab.edu.br"><img
						class="imagem-responsiva"
						src="http://dti.unilab.edu.br/wp-content/themes/dti/img/logo_h-site.png"
						alt=""></a>
				</div>
				<div class="seis colunas centralizado">
					<h1>
						CATRACA<br> <small class="texto-branco">Controle Administrativo de
							Tr&aacute;fego Acad&eacute;mico Automatizado</small>
					</h1>
				</div>
				<div class="tres colunas alinhado-a-direita">
					<a href="http://www.unilab.edu.br"><img
						class="imagem-responsiva centralizada"
						src="http://200.129.19.10/pub/templates_dti/img/logo-unilab-branco.png"
						alt=""></a>
				</div>
			</div>
		</div>

		<div id="barra" class="doze colunas fundo-azul3 alinhado-a-direita">
			<div class="config">
				<a href="#"><span>Perguntas frequentes |</span></a> <a href="#"><span>Contato
						|</span></a> <a href="#"><span>Servi&ccedil;os |</span></a> <a
					href="#"><span>Dados Abertos |</span></a> <a href="#"><span>&Aacute;rea
						de Imprensa |</span></a>
			</div>
		</div>

		<div class="doze colunas">
			<div class="resolucao config">
					<?php
					
					if ($sessao->getNivelAcesso () == Sessao::NIVEL_SUPER) {
						
						
						// exibir menu de usuario Super.
						echo '
							<div class="duas colunas">					
								<div class="padding">
								    <a href="#expandir_menu" title="Clique para expandir o menu" class="menu-resp icone-menu2"> Menu Catraca</a>
								    <div id="expandir_menu" class="menu-vertical">
								        <a href="#ocultar_menu" class="fechar-menu icone-cross"></a>
								        <ol>
		
										 <li><a href="?pagina=inicio" class="item-vertical-ativo"><span class="icone-home3"></span> <span class="item-vertical-texto">Início</span></a></li>
							            <li><a href="?pagina=definicoes" class="item-vertical"><span class="icone-cogs"></span> <span class="item-vertical-texto">Definições</span></a></li>';
						echo ' <li><a href="?pagina=catraca" class="item-vertical"><span class="icone-loop2"></span> <span class="item-vertical-texto">Catraca</span></a></li>';
						echo '          <li><a href="?pagina=cartao" class="item-vertical"><span class="icone-credit-card"></span> <span class="item-vertical-texto">Cartão</span></a></li>';
// 						echo ' <li><a href="?pagina=guiche" class="item-vertical"><span class="icone-user"></span> <span class="item-vertical-texto">Guichê</span></a></li>';
						echo ' <li><a href="?pagina=relatorio" class="item-vertical"><span class="icone-file-text2"></span> <span class="item-vertical-texto">Relatório</span></a></li>';
						echo '         	<li><a href="?sair=sair" class="item-vertical"><span class="icone-exit"></span> <span class="item-vertical-texto">Sair</span></a></li>';
						
						echo '
										</ol>
								    </div>
								</div>
							</div>';
						
					}
					?>
					
					<div class="dez colunas">
					
						
					<?php
					
					$nivelNovo = Sessao::NIVEL_SUPER;
					
					
					if (isset ( $_GET ['pagina'] )) {
						switch ($_GET ['pagina']) {
							case 'inicio' :
								HomeController::main ( $sessao->getNivelAcesso () );
								break;
							case 'definicoes' :
								DefinicoesController::main ( $sessao->getNivelAcesso () );
								break;
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
// 							case 'guiche' :
// 								echo '
								
									
// 										<div class="borda conteudo">
											
// 										<h2> Ainda não desenvolvida.</h2>
											
// 										</div>
			
			
// 									';
// 								break;
							case 'relatorio' :
								RelatorioController::main($sessao->getNivelAcesso());
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
			</div>
		</div>
	</div>
</body>
</html>