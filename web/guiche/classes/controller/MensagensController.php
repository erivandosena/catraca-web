<?php

class MensagensController{
	
	public static function main($nivel){
		
		$mensagem = new MensagensController();
		$mensagem->telaMensagem();
		
	}
	
	public function telaMensagem(){
		
		$unidade = new Unidade();
		$catraca = new Catraca();
		$dao = new DAO();
		$unidadeDao = new UnidadeDAO();
		$unidades = $unidadeDao->retornaLista();
		$mensagem = new MensagensController();
		
		echo'	<div class="borda relatorio">						
						<form action="" class="formulario em-linha" method="post">						
							<label for="">
								<object class="rotulo">Selecione a Unidade: </object>
								<select name="unidade" id="unidade">';		
		
		$unidades = $unidadeDao->retornaLista();
		foreach ($unidades as $unidade){		
		echo'						<option value="'.$unidade->getId().'">'.$unidade->getNome().'</option>';				
				}
		echo'					</select>
							</label>
							<input type="submit" name="buscar" value="Buscar">
						</form>';
		
		if(isset($_POST['buscar'])){		
			
			echo'	<div class="borda relatorio">
						<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Mensagens</h2>
						<table class="tabela borda-vertical zebrada no-centro">
							<thead>
								<tr class="centralizado">
									<th>Mesnagem 1</th>
									<th>Mesnagem 2</th>
									<th>Mesnagem 3</th>
									<th>Mesnagem 4</th>
									<th>-</th>
								</tr>
							</thead>
							<tbody>';
			
			$idUnidade = $unidade->setId($_POST['unidade']);
			$sql = "SELECT * FROM mensagem
					LEFT JOIN catraca ON catraca.catr_id = mensagem.catr_id
					LEFT JOIN catraca_unidade ON catraca_unidade.
					WHERE unid_id = $idUnidade";
					
			$result = $dao->getConexao()->query($sql);
			foreach ($result as $linha){
			
				echo'					<tr>
									<td>'.$linha['mens_institucional1'].'</td>
									<td>'.$linha['mens_institucional2'].'</td>
									<td>'.$linha['mens_institucional3'].'</td>
									<td>'.$linha['mens_institucional4'].'</td>
									<td><a href="" class="botao">Editar</a></td>
								</tr>';
			}
			echo'					</tbody>
						</table>
					</div>';
			
			
		}		
		
	}
	
	public function formEditar(){
		
		echo'			<form action="" class="formulario em-linha" method="post">
							<input name="catraca" type="hidden" value="'.$_POST['catraca'].'">
							<label for="">
								1ª Mensagem: <input type="text" name="msg_um">
							</label>
							<label for="">
								2ª Mensagem: <input type="text" name="msg_dois">
							</label>
							<label for="">
								3ª Mensagem: <input type="text" name="msg_tres">
							</label>
							<label for="">
								4ª Mensagem: <input type="text" name="msg_quatro">
							</label>
							<input type="submit" name="salvar" value="Salvar">
						</form>
					</div>	';
		
	}
	
	
}

?>