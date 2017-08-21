<?php 

class ValidacaoView{
	
	public function formValidacao($listaTipos, $listaCampos){		
				
		echo '			<div class="borda">
							<form class="formulario-organizado" method="get">
								<input type="hidden" name="pagina" value="validacao">
				 				<label for="" class="cinco">
									<object class="rotulo tres ">Tipo: </object>
							        <select name="tipo" class="seis">
									<option selected="selected" value="">Selecione um Tipo</option>';
										foreach ($listaTipos as $tipo){
										echo '<option value="'.$tipo->getId().'">'.$tipo->getNome().'</option>';
										}							            	            						            
		echo '				        </select>
							    </label>
				
								<label for="" class="cinco linha" >
									<object class="rotulo tres">Campo: </object>
							        <select name="campo" class="seis" id="campo">
										<option selected="selected" value="">Selecione um Campo</option>';
										foreach ($listaCampos as $campos){
							            echo '<option value="'.$campos['column'].'">'.$campos['column'].'</option>';
										}
		echo '				        </select>
							    </label>
				
								<label for="" class="cinco linha">
									<object class="rotulo tres ">Valor: </object>
							        <select name="valor" class="seis" id="valor">
							            <option selected="selected" value="">Selecione um Valor</option> 			            
							        </select>
							    </label>								
								<input type="submit" value="Salvar" name="salvar">
							</form>					
						</div>';		
		
	}
	
	public function formConfirmar(){
		echo '	<form method="post" class="formulario-organizado">
					<input type="submit" name="confirmar" value="Confirmar">
				</form>';
	}
	
	public function tabelaCampos($listaValidacao){		
		echo '			<div class="borda doze colunas">
							<table class="tabela borda-vertical zebrada no-centro">
								<thead>
									<tr>
										<th>Id</th>
										<th>Tipo</th>
										<th>Campo</th>
										<th>Valor</th>
										<th>Excluir</th>
									</tr>
								</thead>
								<tbody>';
								foreach ($listaValidacao as $validacao){
								echo '	<tr>
											<td>'.$validacao->getId().'</td>
											<td>'.$validacao->getTipoNome().'</td>
											<td>'.$validacao->getCampo().'</td>
											<td>'.$validacao->getValor().'</td>
											<td><a href="?pagina=validacao&excluir=ok&validacao_id='.$validacao->getId().'" class="icone-cross botao b-erro centralizado"></a></td>
										</tr>';
								}								
		echo '					</tbody>
							</table>
						</div>';
	}
	
	public function mensagem($tipo, $texto){
		//Tipo = sucesso, erro, ajuda		
				
		echo '			<div class="alerta-'.$tipo.'">
					    	<div class="icone icone-notification ix16"></div>
					    	<div class="titulo-alerta">Aten&ccedil&atildeo</div>
					    	<div class="subtitulo-alerta">'.$texto.'</div>
						</div>';
		
// 		echo '		</div>
// 				</div>';
		
		if ($tipo == 'sucesso' || $tipo == 'erro'){
			echo '<meta http-equiv="refresh" content="2; url=.\?pagina=validacao">';
		}		

	}
	
}

?>