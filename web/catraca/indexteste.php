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
			<?php include ("../templates/topo2.php") ?>			
			<div class="doze colunas">
				<div class="resolucao config ">
					<div class="duas colunas">						
						<?php include("../templates/menu.php") ?>
					</div>
					<div class="sete colunas">
						
						<div>
							<div>
								<ul>
									<li><a href="#tab1">Link1</a></li>
									<li><a href="#tab2">Link2</a></li>
								</ul>
							</div>
							<div>
								
							</div>
						</div>

					</div>
					<div class="tres colunas"></div>
				</div>
			</div>
			<?php include ("../templates/rodape.php") ?>			
		</div>		
	</body>
</html>