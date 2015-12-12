<?php


class RelatorioController{
	private $view;
	public static function main($nivelDeAcesso){
	
		switch ($nivelDeAcesso){
			case Sessao::NIVEL_SUPER:
				$controller = new RelatorioController();
				$controller->relatorio();
				break;
			default:
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	
	public function relatorio(){
		echo '<div class="borda">
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
												<a href="?pagina=relatorio&gerar=1"><span class="icone-file-text2 botao" title=""> Gerar Relatório</span></a>
											</div>									    							
									</form>																			
									</div>';
		
		if(isset($_GET['gerar']))
					echo '
									
									<div class="doze colunas borda relatorio negrito centralizado">
										<h1>RELATÓRIO MERAMENTE ILUSTRATIVO - AINDA TEMOS A TRABALHAR NESTA PÁGINA</h1>
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
						</section>';
			
	}
	
	
}


?>