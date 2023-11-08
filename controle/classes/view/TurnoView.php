<?php


class TurnoView{
	
	
	public function mostraFormulario(){
		echo '
			<form action="" method="post">
				<fieldset>
					<legend>Novo Turno</legend>
					<label for="unid_nome">Descricao</label><br>
					<input id="unid_nome" type="text" name="turno_descricao"/><br>
					<input name="turno_hora_inicial" type=time min=9:00 max=22:00><br>
					<input name="turno_hora_final" type=time min=9:00 max=22:00>
					<br>
					<input type="submit" value="Enviar" />
			</fieldset>
	</form>';
	}
	public function mostraLista($lista){
		foreach($lista as $elemento){
			echo 'ID: '.$elemento->getId().'<br>';
			echo 'descricao: '.$elemento->getDescricao().'<br> ';
			echo '<a href="?delete_unidade=1&unid_id='.$elemento->getId().'"> Deletar</a><br>';
		}
		
	}
	public function cadastroSucesso(){
		echo "Inserido com sucesso";
	}
	public function deleteSucesso(){
		echo "Deletado com sucesso";
	}
	public function deleteFracasso(){
		echo "Erro ao tentar deletar";
	}
	public function cadastroFracasso(){
		echo "Erro ao tentar inserir";
	}
	
}


?>