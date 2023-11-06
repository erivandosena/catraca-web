<?php
/**
 * Nesta Classe estão contidos os Códigos HTML, responsáveis pela geração das Telas.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package View
 */
/**
 * Nesta Classe estão contidos os Códigos HTML
 * responsáveis por gerar os elementos e as telas da página Turno.
 */
class TurnoView {
	
	/**
	 * Gera um formulário para inserir um novo Turno.
	 */
	public function mostraFormulario() {
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
	
	/**
	 * Exibe os dados referentes aos Turnos Cadastrados,
	 * é exibido tambem um botão para uma possível exclusão do Turno.
	 *
	 * @param array $lista
	 *        	Array com os dados dos Turnos.
	 */
	public function mostraLista($lista) {
		foreach ( $lista as $elemento ) {
			echo 'ID: ' . $elemento->getId () . '<br>';
			echo 'descricao: ' . $elemento->getDescricao () . '<br> ';
			echo '<a href="?delete_unidade=1&unid_id=' . $elemento->getId () . '"> Deletar</a><br>';
		}
	}
	
	/**
	 * Mostra mensagem de Cadastro com Sucesso.
	 */
	public function cadastroSucesso() {
		echo "Inserido com sucesso";
	}
	
	/**
	 * Mostra mensagem de Exclusão com Sucesso.
	 */
	public function deleteSucesso() {
		echo "Deletado com sucesso";
	}
	
	/**
	 * Mostra mensagem de Erro ao Deletar.
	 */
	public function deleteFracasso() {
		echo "Erro ao tentar deletar";
	}
	
	/**
	 * Mostra mensagem de Erro ao Cadastrar.
	 */
	public function cadastroFracasso() {
		echo "Erro ao tentar inserir";
	}
}

?>