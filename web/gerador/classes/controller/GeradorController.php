<?php


class GeradorController{
	
	
	
	public static function main(){
		
		
		
		$gerador = new GeradorController();
		$gerador->paginaRegistroManual();
	}
	public function paginaRegistroManual(){
		
		echo '<div class="navegacao"> 
				<div class = "simpleTabs">
			        <ul class = "simpleTabsNavigation">					
						<li><a href="#">Cadastro</a></li>						
			        </ul>
				
			        <div class = "simpleTabsContent">
				
						<div class="alerta-sucesso">
						    <div class="icone icone-download ix24"></div>
						    <div class="titulo-alerta">Ok</div>
						    <div class="subtitulo-alerta">Dados enviados com sucesso!</div>
						</div>
				
						<div class="doze colunas borda">
							
							<table class="tabela borda-vertical zebrada no-centro centralizado">							    
							    <thead>
							        <tr>
										<th>Unidade</th>
							            <th>Estudantes</th>
										<th>TAEs</th>
										<th>Docentes</th>
										<th>Terceirizados</th>
										<th>Visitantes</th>
							        </tr>
							    </thead>
							    <tbody>
							        <tr>
										<th>Liberdade</th>										
							            <td>1</td>
							            <td>2</td>
							            <td>3</td>
							            <td>4</td>
										<td>5</td>
							        </tr>
									<tr>
										<th>Palmares</th>										
							            <td>1</td>
							            <td>2</td>
							            <td>3</td>
							            <td>4</td>
										<td>5</td>
							        </tr>
									<tr>
										<th>Selecionar</th>										
							            <td><a href="#" class="botao b-primario icone-checkmar">Enviar</a></td>
							            <td><a href="#" class="botao b-secundario icone-checkmar">Enviar</a></td>
							            <td><a href="#" class="botao b-sucesso icone-checkmar">Enviar</a></td>
							            <td><a href="#" class="botao b-aviso icone-checkmar">Enviar</a></td>
										<td><a href="#" class="botao b-erro icone-checkmar">Enviar</a></td>
							        </tr>
							    </tbody>
							</table>				
						</div>
				
						<div class="doze colunas borda centralizado">
							<h3>Confirmar Envio de Dados?</h3>
							<a href="#" class="botao b-sucesso">Confimar</a>
						</div>
					</div>
				</div>';
		        
		
		
	}
	
}

?>