<?php

class AberturaGuicheController{
	
	public static function main($nivel){
		
		switch ($nivel) {
			case Sessao::NIVEL_SUPER :
				$controller = new AberturaGuicheController();
				$controller->telaAbertura();
				break;
			default :
				UsuarioController::main ( $nivel );
				break;
		}		
	}
	
	public function telaAbertura(){
		
		$dao = new DAO();
		$unidadeDao = new UnidadeDAO();
		$unidade = new Unidade();
		$lista = $unidadeDao->retornaLista();
		
		echo '	<div class="borda relatorio">         
			        <h1>Abertura de Caixa</h1>
				
			        <form action="" class="formulario  sequencial">
												
				        <label for="data_abertura" class="quatro colunas">
				        	Data da Abertura: <input type="date" name="data_abertura">
				        </label>				
						<label for="hora_abertura" class="quatro colunas">
				        	Hora da Abertura: <input type="time" name="hora_abertura">
				        </label>				
				
						<label for="data_fechamento" class="linha quatro colunas">
				        	Data do Fechamento: <input type="date" name="data_fechamento">
				        </label>
				
						<label for="hora_fechamento" class="quatro colunas">
				        	Hora do Fechamento: <input type="time" name="hora_fechamento">
				        </label>
				
						<label for="" class="linha">
					        <object class="rotulo">Unidade Acadêmica:</object>
					        <select name="" id="">';
		
		foreach ($lista as $unidade){
			echo '	    		<option value="">'.$unidade->getNome().'</option>';
		}
		
		echo'		        </select>
					    </label>
				
						<label for="">
					        <object class="rotulo">Operador:</object>
					        <select name="" id="">';
		
		$sql = "SELECT * FROM usuario WHERE usua_nivel > 1";
		$result =  $dao->getConexao()->query($sql);		
		foreach ($result as $linha){			
			echo '				<option value="'.$linha['usua_id'].'">'.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</option>';
		}		
		echo'			        </select>
					    </label>
						<input type="submit" name="abrir" value="Abrir Guichê">
			        </form>
				</div>
					
				<div class="borda">
			        <table class="tabela borda-vertical zebrada no-centro centralizado">
				        <thead>
					        <tr>
						        <th>ID</th>
						        <th>Hora de Abertura</th>
						        <th>Hora de Fechamento</th>
						        <th>Status</th>
						        <th>Unidade</th>
						        <th>Operador</th>
					        </tr>
				        </thead>
				        <tbody>';
		
		$sql = "SELECT * FROM guiche
				INNER JOIN unidade ON unidade.unid_id = guiche.unid_id
				INNER JOIN usuario ON usuario.usua_id = guiche.usua_id";
		$result = $dao->getConexao()->query($sql);
		foreach ($result as $linha){		
			echo '		    <tr>
						        <td>'.$linha['guic_id'].'</td>
						        <td>'.$linha['guic_abertura'].'</td>
						        <td>'.$linha['guic_encerramento'].'</td>
						        <td></td>
						        <td>'.$linha['unid_nome'].'</td>
						        <td>'.$linha['usua_nome'].'</td>						        
					        </tr>';			
		}		
		echo '	        </tbody>
			        </table>		
		      	</div>';
		
	}
	
}

?>