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
		<link rel="stylesheet" href="css/bootstrap.css" type="text/css" media="screen">
		<link rel="stylesheet" href="css/bootstrap.min.css" type="text/css" media="screen">
		<link rel="stylesheet" href="css/bootstrap-theme.min.css" type="text/css" media="screen">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>		
		<script>window.jQuery || document.write('<script src="js/jquery-1.7.1.min.js"><\/script>')</script>		
		<script type="text/javascript" src="js/bootstrap.js"></script>
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		

	</head>

	<body >
		<div class="pagina fundo-cinza1">
			<div id="barra-governo">
			    <div class="resolucao config">
			       <div class="a-esquerda">
			          <a href="http://brasil.gov.br/" target="_blank"><span id="bandeira"></span><span>BRASIL</span></a>
			          <a href="http://acessoainformacao.unilab.edu.br/" target="_blank">Acesso à informação</a>
			       </div>
			       <div class="a-direita"><a href="#"><i class="icone-menu"></i></a></div>
			       <ul>
			          <li><a href="http://brasil.gov.br/barra#participe" target="_blank">Participe</a></li>
			          <li><a href="http://www.servicos.gov.br/" target="_blank">Serviços</a></li>
			          <li><a href="http://www.planalto.gov.br/legislacao" target="_blank">Legislação</a></li>
			          <li><a href="http://brasil.gov.br/barra#orgaos-atuacao-canais" target="_blank">Canais</a></li>
			       </ul>
			    </div>
			</div>

			<div class="doze colunas banner gradiente">			

				<div id="topo" class="resolucao config">
					<div class="tres colunas">
						<a href="http://www.dti.unilab.edu.br"><img class="imagem-responsiva" src="img/logo_h-site.png" alt=""></a>				
					</div>
					<div class="seis colunas centralizado">
						<h1>CATRACA<br><small class="texto-branco">Controle Administrativo de Tráfego Acadêmico Automatizado</small></h1>
					</div>
					<div class="tres colunas alinhado-a-direita">
						<a href="http://www.unilab.edu.br"><img class="imagem-responsiva centralizada" src="img/logo-unilab-branco.png" alt=""></a>
					</div>			
				</div>
			</div>

			<div id="barra" class="doze colunas fundo-azul3 alinhado-a-direita">
				<div class="config">
					<a href="#"><span>Perguntas frequentes |</span></a>
					<a href="#"><span>Contato |</span></a>
					<a href="#"><span>Serviços |</span></a>
					<a href="#"><span>Dados Abertos |</span></a>
					<a href="#"><span>Área de Imprensa |</span></a>
				</div>
			</div>
					
			<div class="doze colunas">				
				<div class="resolucao config">
					<div class="duas colunas">					
						<div class="padding">
						    <a href="#expandir_menu" title="Clique para expandir o menu" class="menu-resp icone-menu2"> Menu vertical</a>
						    <div id="expandir_menu" class="menu-vertical">
						        <a href="#ocultar_menu" class="fechar-menu icone-cross"></a>
						        <ol>
						            <li><a href="index.php" class="item-vertical-ativo"><span class="icone-home3"></span> <span class="item-vertical-texto">Início</span></a></li>
						            <li><a href="cadastro.php" class="item-vertical"><span class="icone-cogs"></span> <span class="item-vertical-texto">Definições</span></a></li>						            					            
						            <li><a href="cartao.php" class="item-vertical"><span class="icone-profile"></span> <span class="item-vertical-texto">Catraca</span></a></li>
						            <li><a href="relatorios.php" class="item-vertical"><span class="icone-loop2"></span> <span class="item-vertical-texto">Cartão</span></a></li>
						            <li><a href="relatorios.php" class="item-vertical"><span class="icone-user"></span> <span class="item-vertical-texto">Guichê</span></a></li>
						            <li><a href="relatorios.php" class="item-vertical"><span class="icone-file-text2"></span> <span class="item-vertical-texto">Relatório</span></a></li>
						         	<li><a href="" class="item-vertical"><span class="icone-exit"></span> <span class="item-vertical-texto">Sair</span></a></li>
						        </ol>
						    </div>
						</div>
					</div>
					<div class="dez colunas">
						
						<section id="navegacao">							
							<!--Tabs-->	
							<ul class="nav nav-tabs">
								<li role="presentation" class="active"><a href="#tab1" data-toggle="tab">Unidades Acadêmicas</a></li>
								<li role="presentation" class=""><a href="#tab2" data-toggle="tab">Turnos</a></li>
								<li role="presentation" class=""><a href="#tab3" data-toggle="tab">Tipos de Usuários</a></li>								
								<li role="presentation" class=""><a href="#tab4" data-toggle="tab">Custos</a></li>															
							</ul>
							<div class="tab-content">
								<div class="tab-pane active" id="tab1">
									<div class="borda">							
										<form method="post" action="" class="formulario sequencial" >										
											<label for="campo-texto-2" class="texto-preto">
										        Unidade Acadêmica: <input type="text" name="unidade" id="unidade" />
										    </label>										    
										    <input type="submit" value="Salvar" />
										</form>
									</div>
										<div class="doze linhas borda">										
											<table id="turno" class="tabela borda-vertical zebrada texto-preto no-centro">
												<thead>
											        <tr>
											            <th>ID</th>
											            <th>Unidade Acadêmica</th>
											            <th>Turnos</th>						            
											            <th class="centralizado">Ações</th>				            
											        </tr>
											    </thead>				
												<tbody>
											        <tr>
											            <td>1</td>
											            <td>Liberdade</td>
											            <td></td>									            
											            <td class="centralizado">
											            	<a href=""><span class="icone-pencil2 texto-amarelo2 botao" title="Editar"></span></a>
											            	<a href=""><span class="icone-cross botao texto-vermelho2" title="Excluir"></span></a>
											            	<a href=""><span class="icone-plus botao texto-verde2" title="Adicionar Turno"></span></a>											            	
											            </td>
											        </tr>								        
											    </tbody>
											</table>												
										</div>
										<div class="formulario sequencial borda">
											<form action="">
												<label for="opcoes-1">
												<object class="rotulo texto-preto">Turno: </object>
												<select name="opcoes-1" id="opcoes-1" class="texto-preto">
													<option value="1">Almoço</option>												
												</select>																					    
											</label>
											<input type="submit" value="Adicionar" />
											</form>
										</div>						
								</div>
									<div class="tab-pane" id="tab2">
										<div class="borda">
											<form method="post" action="" class="formulario" >										
											<label for="campo-texto-2" class="">
										        Turno: <input type="text" name="turno" id="turno" />
										    </label><br>
										    <label for="campo-texto-2" class="">
										        Hora Inicio: <input type="time" name="horaini" id="horaini" />
										    </label><br>
										    <label for="campo-texto-2" class="">
										        Hora Fim: <input type="time" name="horafim" id="horafim" />
										    </label><br>
										    <input type="submit" value="Salvar" />
											</form>
										</div>						

									<div class="doze linhas borda">										
										<table class="tabela borda-vertical zebrada texto-preto no-centro">
											<thead>
										        <tr>
										            <th>ID</th>
										            <th>Turno</th>
										            <th>Início</th>
										            <th>Fim</th>
										            <th>Ações</th>				            				            
										        </tr>
										    </thead>				
											<tbody>
										        <tr>
										            <td>1</td>
										            <td>Almoço</td>
										            <td>11:00</td>
										            <td>13:30</td>						            
										            <td class="centralizado">
										            	<a href=""><span class="icone-pencil2 botao texto-amarelo2" title="Editar"></span></a>
										            	<a href=""><span class="icone-cross botao texto-vermelho2" title="Excluir"></span></a>
										            </td>
										        </tr>									       
										    </tbody>
										</table>																			
									</div>
																															
							</div>
							<div class="tab-pane" id="tab3">

								<div class="borda">
									<form action="" class="formulario sequencial">
										<label for="campo-texto-2" class="">
										    Tipo Usuario: <input type="text" name="tipo_usuario" id="tipo_usuario" />
										</label>
										<label for="campo-texto-2" class="">
										    Valor por Refeição : <input type="text" name="valor_refeicao" id="valor_refeicao" />
										</label>
										<input type="submit" value="Salvar" />
									</form>
								</div>				

								<div class="doze linhas borda">										
									<table class="tabela borda-vertical zebrada texto-preto no-centro">
										<thead>
									        <tr>
									            <th>ID</th>
									            <th>Tipo de Usuario</th>
									            <th>Vavor por refeição</th>
									            <th>Status</th>							            
									            <th>Ações</th>				            				            
									        </tr>
									    </thead>				
										<tbody>
									        <tr>
									            <td>1</td>
									            <td>Aluno</td>
									            <td>$R 1,10</td>
									            <td>Desativado</td>								           					            
									            <td class="centralizado">
									            	<a href=""><span class="icone-pencil2 botao texto-amarelo2" title="Editar"></span></a>
									            	<a href=""><span class="icone-checkmark botao texto-verde2" title="Ativar"></span></a>
									            </td>
									        </tr>									       
									    </tbody>
									</table>																			
								</div>
							</div>
							<div class="tab-pane" id="tab4">
								<div class="borda">
									<form action="" class="formulario sequencial">
										<label for="campo-texto-2" class="">
										    Valor de Custo Refeição: <input type="text" name="custo_refeicao" id="tipo_usuario" />
										</label>
										<label for="campo-texto-2" class="">
										    Valor de Custo Cartão: <input type="text" name="valor_refeicao" id="valor_refeicao" />
										</label>
										<input type="submit" value="Salvar" />
									</form>
								</div>	
							</div>							
						</section>
					
					</div>
				</div>
			</div>
			
		</div>
		<footer>
			<div id="rodape" class="doze colunas fundo-azul1 centralizado">
				<p>CATRACA todos os direitos reservados</p>
			</div>
		</footer>	
	</body>
</html>