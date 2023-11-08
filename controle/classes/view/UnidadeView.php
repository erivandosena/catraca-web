<?php


class UnidadeView{
	
	
	public function mostraFormulario(){
		echo '
			<form action="" method="post">
				<fieldset>
					<legend>Unidade Academica</legend>
					<label for="unid_nome">Nome da Unidade Academica</label><br>
					<input id="unid_nome" type="text" name="unid_nome"/>
					<br>
					<input type="submit" value="Enviar" />
			</fieldset>
	</form>';
	}
	public function mostraLista($lista){
		foreach($lista as $elemento){
			echo 'ID: '.$elemento->getId().'<br>';
			echo 'Nome: '.$elemento->getNome().'<br> ';
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