<?php
echo'
<!DOCTYPE html>
<html lang="pt-br">
	<head>

		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no" />

		<title>Projeto Catraca</title>

		<script type="text/javascript" src="js/simpletabs_1.3.js"></script>
		<link rel="stylesheet" href="css/simpletabs.css" />
		<link rel="stylesheet" href="http://spa.dsi.unilab.edu.br/spa/css/spa.css" />
		<link rel="stylesheet" href="css/estilo.css" type="text/css" media="screen">
		<link rel="stylesheet" href="css/estilo_responsivo.css" type="text/css" media="screen">
		<script type = "text/javascript" src="js/jquery-1.12.0.min.js"></script>
		<script type="text/javascript" src="js/javascript.js"></script>
	
	</head>

	<body>
		<div class="pagina fundo-cinza1">
			<div id="barra-governo">
				<div class="resolucao config">
					<div class="a-esquerda">
						<a href="http://brasil.gov.br/" target="_blank"><span id="bandeira"></span><span>BRASIL</span></a>
						<a href="http://acessoainformacao.unilab.edu.br/" target="_blank">Acesso &agrave;  informa&ccedil;&atilde;o</a>
					</div>
					<div class="a-direita">
						<a href="#"><i class="icone-menu"></i></a>
					</div>
					<ul>
						<li><a href="http://brasil.gov.br/barra#participe" target="_blank">Participe</a></li>
						<li><a href="http://www.servicos.gov.br/" target="_blank">Servi&ccedil;os</a></li>
						<li><a href="http://www.planalto.gov.br/legislacao" target="_blank">Legisla&ccedil;&atilde;o</a></li>
						<li><a href="http://brasil.gov.br/barra#orgaos-atuacao-canais" target="_blank">Canais</a></li>
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

			<div  class="doze colunas barra-menu">
			    <div class="menu-horizontal config">
			        <ol class="a-esquerda">
			        	<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>
	 					<li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>
	 					<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>
	 					<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>								
	 					<li><a href="?pagina=guiche" class="item"><span class="icone-user"></span> <span class="item-texto">Guichê</span></a></li>
	 					<li><a href="" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a>
							<ul>
								<li><a href="?pagina=relatorio">Relatorio RU</a></li>
								<li><a href="">Relatorio Guichê</a></li>
							</ul>
	 					</li>
	 				</ol>
	 				<ol class="a-direita" start="4">
						<li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
					</ol>
				</div>
			</div>			

			<div class="doze colunas">

				<div class="resolucao config">					
				
					<div class="doze colunas borda relatorio no-centro">
						
						<div class="doze colunas">
							<div class="duas colunas">
								<a href="http://www.unilab.edu.br">
									<img class="imagem-responsiva centralizada" src="img/logo-unilab.png" alt="">
								</a>
							</div>
							<div class="oito colunas">
								<h2>Restaurante Universitário</h2>
							</div>
							<div class="duas colunas">
								<img class="imagem-responsiva centralizada" src="img/pp.jpg" alt="">
							</div>
							<hr class="um"><br>
						</div>
						
						<div class="doze colunas dados-usuario">					

							<h1 class="centralizado">Identificação do Usuario</h1><br>					

							<hr class="um">
							<div class="quatro colunas">
								<img src="img/gio.jpg" alt="">
							</div>

							<div class="oito colunas">													
								<div id="informacao" class="fundo-cinza1">
									
									<form action="" class="formulario-organizado">							
										<label for="">
											Cartão: <input type="number" autofocus>
										</label>
									</form><br><br><br>
									
									<span >Nº Cartão:</span><br>
									<span >Nome: Giovanildo Teixeira</span><br>
									<span >Aluno</span><br>
									<span >Matrícula: 123456789</span>					
								</div>
							</div>
						</div>				

						<div class="doze colunas">
							<br>
							<form action="" class="formulario centralizado">
								<input type="submit" value="Aguarde" class="oito">
							</form>

							<div class="alerta-sucesso dez no-centro">
								<div class="icone icone-checkmark ix24"></div>
								<div class="titulo-alerta">Ok!</div>
								<div class="subtitulo-alerta">Acesso Liberado!.</div>
							</div>
															
						</div>

					</div>	
													
				</div>

			</div>
		</div>
	</body>
</html>';

?>