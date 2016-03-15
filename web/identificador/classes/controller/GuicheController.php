<?php




class GuicheController{
	
	
	public static function main($nivel){
		
		$controller = new GuicheController();
		$controller->telaGuiche();
		
	}
	
	
	public function telaGuiche(){
		echo '<div id="caixa"class="doze colunas borda">										
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
									</div>		';
		
	
	}
	
	
}


?>