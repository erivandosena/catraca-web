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
				
				<div id="acessibilidade" class="">
				    <div class="resolucao config">
				        <a href="#conteudo" tabindex="1" accesskey="1">Ir para o conteúdo <b>1</b></a>
				        <a href="#menu" tabindex="2" accesskey="2">Ir para o menu <b>2</b></a>
				        <a href="#busca" tabindex="3" accesskey="3">Ir para a busca <b>3</b></a>
				        <a href="#rodape" tabindex="4" accesskey="4"><span>Ir para o rodapé <b>4</b></a>
				    </div>
				</div>

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
						            <li><a href="cadastro.php" class="item-vertical"><span class="icone-drawer"></span> <span class="item-vertical-texto">Cadastro</span></a></li>						            					            
						            <li><a href="cartao.php" class="item-vertical"><span class="icone-profile"></span> <span class="item-vertical-texto">Cartão</span></a></li>
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
								<li role="presentation" class="active"><a href="#tab1" data-toggle="tab">Relatórios</a></li>								
							</ul>
							<div class="tab-content">
								<div class="tab-pane active" id="tab1">									
									<div class="borda">
									<form action="" class="formulario sequencial">									
											<div id="data">
												<label for="opcoes-1">
													<object class="rotulo texto-preto">Unidade Acadêmica: </object>
													<select name="opcoes-1" id="opcoes-1" class="texto-preto">
														<option value="1">Liberdade</option>
														<option value="2">Auroras</option>
														<option value="3">Palmares</option>								            										            
												    </select>
												</label><br>
												<label for="opcoes-2">
													<object class="rotulo texto-preto">Turno: </object>
													<select name="opcoes-2" id="opcoes-2" class="texto-preto">
														<option value="1">Dejejum</option>
														<option value="2">Almoço</option>
														<option value="3">Jantar</option>								            										            
												    </select>
												</label><br>											    
												<label for="ini" class="texto-preto">
												    Data Inicial: <input id="ini" type="date" name="datainicio"/>
												</label><br>
												<label for="fim" class="texto-preto">
												    Data Final: <input id="fim" type="date" name="datafim"/>
												</label><br>
												<a href="#"><span class="icone-file-text2 botao" title=""> Gerar Relatório</span></a>
											</div>									    							
									</form>																			
									</div>
									
									<div class="doze colunas borda relatorio negrito centralizado">
										<h1>RESTAURANTE UNIVERSITÁRIO LIBERDADE</h1>
										<div class="quatro colunas">
											<hr class="solida" />
											<span>DATA:</span>
											<hr class="solida" /><br>
											<hr class="solida" />											
											<span>ALUNO:</span>
											<hr class="solida" />
											<span>PROFESSOR:</span>
											<hr class="solida" />
											<span>TÉCNICO:</span>
											<hr class="solida" />
											<span>VISITANTE:</span>
											<hr class="solida" />
											<span>TOTAL DE PRATOS:</span>
											<hr class="solida" />
										</div>
										<div class="quatro colunas">
											<hr class="solida" />
											<span class="centralizado">___/___/___</span>
											<hr class="solida" />
											<span class="centralizado">FICHAS</span>
											<hr class="solida" />
											<span>100</span>																						
											<hr class="solida" />
											<span>100</span>
											<hr class="solida" />
											<span>100</span>
											<hr class="solida" />
											<span>100</span>
											<hr class="solida" />
											<span>100</span>
											<hr class="solida" />										
											<span>VALOR TOTAL:</span>
											<hr class="solida" />
											<span>VALOR EXISTENTE:</span>
											<hr class="solida" />
											<span>VALOR DIFERENÇA:</span>
											<hr class="solida" />
										</div>
										<div class="quatro colunas">
											<hr class="solida" />
											<span class="centralizado">ALMOÇO</span>
											<hr class="solida" />
											<span class="centralizado">VALOR</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
											<span class="centralizado">R$ 100,00</span>
											<hr class="solida" />
										</div>
									</div>

									<div class=" doze colunas borda">
										<table class="tabela quadro no-centro fundo-branco">
										    <h1 class="centralizado">RESTAURANTE UNIVERSITÁRIO LIBERDADE</h1><br>
										    <thead>
										    	<tr class="centralizado">
										    		<th></th>
										    		<th>Almoço</th>
										    		<th></th>
										    		<th>Jantar</th>
										    		<th></th>
										    		<th>Total</th>
										    		<th></th>										 
										    	</tr>
										        <tr>
										            <th>Data</th>										            
										            <th>Usuários</th>
										            <th>Visitantes</th>
										            <th>Usuarios</th>
										            <th>Visitantes</th>
										            <th>Almoço</th>
										            <th>Jantar</th>										            
										        </tr>
										    </thead>
										    <tbody>
										        <tr>
										            <td>01/01/2015</td>
										            <td>100</td>
										            <td>100</td>
										            <td>100</td>
										            <td>100</td>
										            <td>100</td>
										            <td>100</td>
										        </tr>										        
										    </tbody>
										</table>
										<div class="dez colunas no-centro">
											<div class="cinco colunas esquerda">												
												<span>TOTAL MÊS ALMOÇO:</span>
												<span>CUSTO ALMOÇO:</span>
												<span>TOTAL:</span>
											</div>
											<div class="cinco colunas esquerda">
												<span>TOTAL MÊS JANTAR:</span>
												<span>CUSTO JANTAR:</span>
											</div>											
										</div>
									</div>																
								</div>								
							</div>
						</section>
					</div>
				</div>
			</div>
		</div>	
	</body>
</html>