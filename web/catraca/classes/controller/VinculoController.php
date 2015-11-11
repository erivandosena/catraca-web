<?php


class VinculoController{
	
	public static function main($tela){
		switch ($tela){
			case Sessao::NIVEL_SUPER:
				echo 'Vinculo controller';
				$controller = new VinculoController();
				$controller->telaVinculo();
				/*
				 * Queremos 
				 * um formulario de pesquisa. 
				 * Ao digitar um nome, vamos buscar. 
				 * Temos uma lista que tras SIAP, Matricula, Nome, documentos. 
				 * Vamos fazer o teste. 
				 * 
				 */
				
				break;
			case Sessao::NIVEL_DESLOGADO:
				break;
			default:
				break;
		}
		
		
	
	
	}
	public function telaVinculo(){
		echo '<form action=\'\' method=\'post\'>
				<input type="text" name="nome" placeholder="Pesquisar Pessoa">
				</form>';
		if(isset($_POST['nome'])){
			$pesquisa = preg_replace('/[^[:alnum:]]/', '',$_POST['nome']);
			$pesquisa = strtoupper($pesquisa);
			$sql = "SELECT * FROM vw_usuarios_catraca WHERE nome LIKE '%$pesquisa%'";
			$dao = new DAO(null, DAO::TIPO_PG_SIGAAA);
			$result = $dao->getConexao()->query($sql);
			
			echo '<table border="1">';
			echo '<tr>';
			echo '<th>Nome: </th>';
			echo '<th>CPF: </th>';
			echo '<th>Identidade: </th>';
				
			echo '<th>Tipo: </th>';
			echo '<th>SIAPE: </th>';
			echo '<th>Status Servidor: </th>';
			echo '<th>Matricula Discente: </th>';
			echo '<th>Status Discente: </th>';
			echo '<th>Passaporte: </th>';
				
			echo '</tr>';
			foreach($result as $linha){
				echo '<tr>';
				echo '<td><a href="?selecionado='.$linha['id_usuario'].'">'.$linha['nome'].'</a></td>';
				echo '<td>'.$linha['cpf_cnpj'].'</td>';
				echo '<td>'.$linha['identidade'].'</td>';
				echo '<td>'.$linha['tipo_usuario'].'</td>';
				echo '<td>'.$linha['siape'].'</td>';
				echo '<td>'.$linha['status_servidor'].'</td>';
				echo '<td>'.$linha['matricula_disc'].'</td>';
				echo '<td>'.$linha['status_discente'].'</td>';
				echo '<td>'.$linha['passaporte'].'</td>';
				echo '</tr>';
			}
			echo '</table>';
		}
		if(isset($_GET['selecionado'])){
			if(is_int(intval($_GET['selecionado'])))
			{
				echo 'Selecionou '.$_GET['selecionado'];
				/*
				 * Vamos aqui verificar os vinculos desse usuario. 
				 * 
				 */
			}
		}
	}

}


?>