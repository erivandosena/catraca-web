<!DOCTYPE html>
<html lang="pt-BR">
	<head>

		<meta charset="UTF-8">
		<meta name="description" content="Curso Bootstrap - PontoCanal"/>
		<meta name="viewport" content="width=device-width, height=device-height, initial-scale=1, maximum-scale=1, user-scalable=no" />
		
		<title>Projeto Catraca</title>
		<link rel="stylesheet" href="http://spa.dsi.unilab.edu.br/spa/css/spa.css" />		
		<link rel="stylesheet" href="css/estilo.css" type="text/css" media="screen">
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
		<script type="text/javascript" src="js/javascript.js"></script>

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
				

							<div  class="doze colunas barra-menu">
								    <div class="menu-horizontal config">
								        <ol class="a-esquerda">';
								             
 						<li><a href="?pagina=inicio" class="item-ativo"><span class="icone-home3"></span> <span class="item-texto">Início</span></a></li>';
 						<li><a href="?pagina=catraca" class="item"><span class="icone-loop2"></span> <span class="item-texto">Catraca</span></a></li>';
 						<li><a href="?pagina=cartao" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Cartão</span></a></li>';
 						<li><a href="?pagina=gerador" class="item"><span class="icone-credit-card"></span> <span class="item-texto">Catraca Virtual</span></a></li>';
 						<li><a href="?pagina=guiche" class="item"><span class="icone-user"></span> <span class="item-texto">Guichê</span></a></li>';
 						<li><a href="?pagina=relatorio" class="item"><span class="icone-file-text2"></span> <span class="item-texto">Relatório</span></a></li>';
 						
						</ol>
								        <ol class="a-direita" start="4">
								            <li><a href="?sair=sair" class="item"><span class="icone-exit"></span> <span class="item-texto">Sair</span></a></li>
								        </ol>
								    </div>
								</div>

			</div>
					
			<div class="doze colunas">				
				<div class="resolucao config">	
					<div id="caixa"class="doze colunas borda">										
						<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Venda de Créditos</h2>																											
						<div class="sete colunas">											
							<div id="infovenda" class="fundo-cinza1">												
								<div class="doze colunas">													
									<h3 class="centralizado">Descição da Operação</h1><br>
										<table class="tabela quadro no-centro">													    
										    <thead>
												<tr>
												    <th>Cod</th>
												    <th>Valor</th>
												    <th>Descrição</th>
												    <th>Data</th>
													<th>Operador</th>
												</tr>
											</thead>
											<tbody>
											    <tr>
											        <td>1</td>
											        <td>30</td>
											        <td>Venda Credito</td>
											        <td>11/12/2015 14:36:00</td>
											        <td>Sena</td>
											    </tr>													        
											</tbody>
										</table>
									</div>
								</div>											
									<h2>Saldo em Caixa: 100,00</h1>
									<div class="sete borda">
										<span class="icone-user"> Operador: Sena</span>
										<span class="icone-clock"> Ultimo Acesso: 11/12/2015 9:00</span>
										<span class="icone-clock2"> Data/Hora: 11/12/2015 10:00</span>
									</div>																					
								</div>
									<div class="cinco colunas">
										<form class="formulario-organizado" action="#">
											<label for="cartao">
												Nº Cartão: <input type="text" name="cartao" id="cartao">													
											</label>
												<input type="submit" value="Pesquisar">
										</form>
										<hr>
										<span>Usuario: Alan Cleber Morais Gomes</span>
										<span>Tipo Usuario: Servidor</span>
										<span>Saldo: 0,00</span>
										<span>Valor Credito: 1,60</span>
										<hr>
										<form class="formulario-organizado" action="#">
											<label for="">
										        <object class="rotulo">Venda por: </object>
											    <select name="opcoes-1" id="opcoes-1">											            
											        <option value="opcoes-1.1">Valor</option>
											            <option value="opcoes-1.1">Crédito</option>									            										         
											        </select>
											    </label>

												<label for="credito">
													Qnt. de Crédito: <input type="text" name="credito" id="credito">
												</label>
												<label for="valor">
													Valor Recebido: <input type="text" name="valor" id="valor">
												</label>
												<hr>												
												<h2>Troco: R$ 0,00</h1>
												<input type="submit" value="Finalizar Venda" class="botao b-sucesso">
											</form>
											<hr class="solida">
											<a href="" class="botao b-erro">Sangria</a>
											<a href="" class="botao ">Encerrar Caixa</a>
										</div>
									</div>											
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