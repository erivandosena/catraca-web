<!DOCTYPE html>
<html lang="pt-BR">
	<head>

		<meta charset="UTF-8">
		<meta name="description" content="Curso Bootstrap - PontoCanal"/>
		<meta name="viewport" content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no" />
		
		<title>Projeto Catraca</title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
		<link rel="stylesheet" href="http://spa.dsi.unilab.edu.br/spa/css/spa.css" />		
		<link rel="stylesheet" href="css/estilo.css" type="text/css" media="screen">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>		
		<script>window.jQuery || document.write('<script src="js/jquery-1.7.1.min.js"><\/script>')</script>
		<script src="js/bootstrap.js"></script>

	</head>

	<body >

		<div class="pagina fundo-cinza1">			

			<?php include ("templates/topo.php") ?>
			
			<div class="doze colunas">
				<div class="resolucao config">					

					<div class="nove colunas">
						<h1 class="texto-preto">Conteúdo</h1>						
					</div>

					<div id="login" class="tres colunas texto-preto">
						<h3>Acesso ao Sistema</h3>
						<form method="post" action="" class="formulario sequencial">
							<label for="campo-texto-2">
						        Usuario: <input type="text" name="usuario" id="campo-texto-2" />
						    </label>
						    <label for="campo-senha-2">
						        Senha: <input type="password" name="senha" id="campo-senha-2" />
						    </label>
						    <input type="submit" value="Entrar" />
						</form>
					</div>
				</div>
			</div>
			<div id="rodape" class="doze colunas fundo-azul1 centralizado rodape">
				<p>CATRACA todos os direitos reservados</p>
			</div>			
		</div>
	</body>
</html>