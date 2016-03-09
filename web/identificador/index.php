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

<?php 
echo $html []='<!DOCTYPE html>
<html lang="pt-BR">
<head>

<meta charset="UTF-8">
<meta name="viewport"
	content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no" />

<title>Projeto Catraca</title>

<script type="text/javascript" src="js/simpletabs_1.3.js"></script>
<link rel="stylesheet" href="css/simpletabs.css" />
<link rel="stylesheet" href="http://spa.dsi.unilab.edu.br/spa/css/spa.css" />
<link rel="stylesheet" href="css/estilo.css" type="text/css" media="screen">
<link rel="stylesheet" href="css/estilo_responsivo.css" type="text/css" media="screen">
<script type="text/javascript" src="js/jquery.min.js"></script>
</head>'
?>
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
					
					if ($sessao->getNivelAcesso () == Sessao::NIVEL_SUPER) {						
						$dao = new DAO();
						$auditoria = new Auditoria($dao->getConexao());
						$auditoria->cadastrar($sessao->getIdUsuario());
				
 						echo '
							<div  class="doze colunas barra-menu">
								    <div class="menu-horizontal config">
								        <ol class="a-esquerda">';
								             
 						echo '<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
 						echo ' <li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
 						echo '<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
 						echo '<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
 						//echo ' <li><a href="?pagina=guiche" class="item"><span class="icone-user"></span> <span class="item-texto">Guichê</span></a></li>';
 						echo ' <li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
 						
						echo '</ol>
								        <ol class="a-direita" start="4">
								            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
								        </ol>
								    </div>
								</div>';
						
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
</body>
</html>