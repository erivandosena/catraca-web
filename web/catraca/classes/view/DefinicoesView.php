<?php


class DefinicoesView{
	
	public function formInserirUnidade(){
		echo '<div class="borda">							
										<form method="get" action="" class="formulario sequencial" >										
											<label for="cadastrar_unidade" class="texto-preto">
										        Unidade Acadêmica: <input type="text" name="cadastrar_unidade" id="cadastrar_unidade" />
										    </label>										    
										    <input type="submit" name="pagina" value="definicoes" />
										</form>
									</div>';
		
	}
	public function listarUnidadesAcademicas($unidadesAcademicas){
		echo '		
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
												<tbody>';
		
		foreach ($unidadesAcademicas as $unidade){
			$this->linhaUnidadeAcademica($unidade);
		}
		

		echo '
											        								        
											    </tbody>
											</table>												
										</div>';
		
		
	}
	public function linhaUnidadeAcademica(Unidade $unidade){
		echo '
											        <tr>
											            <td>'.$unidade->getId().'</td>
											            <td>'.$unidade->getNome().'</td>

											            		<td>';

		$i = 0;
		foreach ($unidade->getTurnosValidos() as $turno){
			if($i)
				echo '\ ';
			echo $turno->getDescricao();
			$i++;
		}
		echo '											</td>
											            <td class="centralizado">
											            	<a href="?pagina=definicoes&turno_na_unidade='.$unidade->getId().'"><span class="icone-plus texto-verde2 botao" title="Editar"></span></a>
											            	<a href="?pagina=definicoes&excluir_turno_da_unidade='.$unidade->getId().'"><span class="icone-cross botao texto-vermelho2" title="Excluir"></span></a>

											            </td>
				</tr>';
	}
	public function formAdicionarTurnoNaUnidade(){
		echo '
					
		
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
										</div>';
	}

	public function listarTurnos($turnos){
		
		
		echo '
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
											<tbody>';
		
		foreach($turnos as $turno){
			$this->mostraLinhaTurno($turno);
		}
		
		
		echo '									       
										    </tbody>
										</table>																			
									</div>';
	}
	public function mostraLinhaTurno(Turno $turno){
		echo '
										        <tr>
										            <td>'.$turno->getId().'</td>
										            <td>'.$turno->getDescricao().'</td>
										            <td>'.$turno->getHoraInicial().'</td>
										            <td>'.$turno->getHoraFinal().'</td>
										            <td class="centralizado">
										            	<a href=""><span class="icone-pencil2 botao texto-amarelo2" title="Editar"></span></a>
										            	<a href=""><span class="icone-cross botao texto-vermelho2" title="Excluir"></span></a>
										            </td>
										        </tr>';
		
	}
	
	public function formAdicionarTurno(){
		echo '
									<div class="borda">
											<form method="get" action="" class="formulario" >										
											<label for="turno_nome" class="">
										        Turno: <input type="text" name="turno_nome" id="turno" required />
										    </label><br>
										    <label for="hora_inicio" class="">
										        Hora Inicio: <input type="time" name="hora_inicio" id="hora_inicio" required />
										    </label><br>
										    <label for="hora_fim" class="">
										        Hora Fim: <input type="time" name="hora_fim" id="hora_fim" required />
										    </label><br>
										    <input type="hidden" name="pagina" value="definicoes" />
										    <input type="submit" name="cadastrar_turno" value="Salvar" />
											</form>
										</div>';
	}
	
	
	
	public function formAdicionarTipoDeUsuario(){
		echo '<div class="borda">
									<form method="get" action="" class="formulario sequencial">
										<label for="tipo_nome" class="">
										    Tipo Usuario: <input type="text" name="tipo_nome" id="tipo_nome" />
										</label>
										<label for="tipo_valor" class="">
										    Valor por Refeição : <input type="number"  max="100"  step="0.01" value="1.6" name="tipo_valor" id="tipo_valor" />
										</label>
				    					<input type="hidden" name="pagina"  value="definicoes" />
										<input type="submit" name="cadastrar_tipo" value="Salvar" />
									</form>
								</div>';
	}
	public function listarTiposDeUsuarios($tipos){
		
		echo '
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
										<tbody>';
		foreach($tipos as $tipo){
			$this->mostrarLinhaTipo($tipo);
		}
		echo '
									        								       
									    </tbody>
									</table>																			
								</div>';
	}
	public function mostrarLinhaTipo(Tipo $tipo){
		echo '<tr>
				<td>'.$tipo->getId().'</td>
									            <td>'.$tipo->getNome().'</td>
									            <td>R$' . number_format($tipo->getValorCobrado(), 2, ',', '.').'</td>
									            <td>Ativado</td>								           					            
									            <td class="centralizado">
									            	<a href=""><span class="icone-pencil2 botao texto-amarelo2" title="Editar"></span></a>
									            	<a href=""><span class="icone-checkmark botao texto-verde2" title="Ativar"></span></a>
									            </td>
									        </tr>	';
		
	}
	
	public function formAlterarCustoRefeicao($custoAtualRefeicao){
		$custoAtualRefeicao = floatval($custoAtualRefeicao);
		echo '<div class="borda">
							Custo Atual da Refeição Pago à empresa por prato servido: R$' . number_format($custoAtualRefeicao, 2, ',', '.').'
									<form action="" class="formulario sequencial">
										<label for="custo_refeicao" class="">
										    Valor de Custo Refeição:  <input type="number"  max="100"  step="0.01" name="custo_refeicao" id="custo_refeicao" value="'.$custoAtualRefeicao.'" />
										</label>
										<input type="submit" name="pagina" value="definicoes" />
									</form>
								</div>';
		
	}
	
	public function formAlterarCustoCartao($custoAtualCartao){
		$custoAtualCartao= floatval($custoAtualCartao);
		echo '<div class="borda">
							Custo do cartão: R$' . number_format($custoAtualCartao, 2, ',', '.').'
									<form action="" class="formulario sequencial">
										<label for="custo_cartao" class="">
										    Valor de Custo Refeição: <input type="number"  max="100"  step="0.01" name="custo_cartao" id="custo_cartao" value="'.$custoAtualCartao.'" />
										</label>
										<input type="submit" name="pagina" value="definicoes" />
									</form>
								</div>';
	
	}
	public function mostraSucesso($mensagem){
		echo '<div class="borda"><p>'.$mensagem.'</p></div>';
	
	}
	public function formTurnoNaUnidade(Unidade $unidade, $listaDeTurnos){
		
		echo '<div class="borda">
						Deseja adicionar um turno na unidade: '.$unidade->getNome().'
						<form action="" method="post" class="formulario sequencial">
								<select name="id_turno">';
		foreach ( $listaDeTurnos as $turno ) {
			echo '<option value="'.$turno->getId().'">' . $turno->getDescricao () . '</option>';
		}
		echo '<input type="hidden" name="id_unidade" value="' . $unidade->getId () . '">';
		echo '</select><input type="submit" name="turno_na_unidade"></form></div>';
		
		
	}
	public function formExcluirTurnoDaUnidade(Unidade $unidade){
		$listaDeTurnos = $unidade->getTurnosValidos();
	
		echo '<div class="borda">
						Deseja remover um turno na unidade: '.$unidade->getNome().'
						<form action="" method="post" class="formulario sequencial">
								<select name="id_turno">';
		foreach ( $listaDeTurnos as $turno ) {
			echo '<option value="'.$turno->getId().'">' . $turno->getDescricao () . '</option>';
		}
		echo '<input type="hidden" name="id_unidade" value="' . $unidade->getId () . '">';
		echo '</select><input type="submit" name="excluir_turno_da_unidade"></form></div>';
	
	
	}
}


?>