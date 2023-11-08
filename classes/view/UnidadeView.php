<?php
/**
 * Nesta Classe estão contidos os Códigos HTML, responsáveis pela geração das Telas.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package View
 */
/**
 * 
 * Nesta Classe estão contidos os Códigos HTML
 * responsáveis por gerar os elementos e as telas da página Unidade Acadêmicas.
 *
 */
class UnidadeView {
	
	/**
	 * Gera um formulário para inserir uma nova Unidade Acadêmica.
	 */
	public function mostraFormulario() {
		echo '
			<form action="" method="post">
				<fieldset>
					<legend>Unidade Academica</legend>
					<label for="unid_nome">Nome da Unidade Academica</label><br>
					<input id="unid_nome" type="text" name="unid_nome"/><br>
					<input type="submit" value="Enviar" />
				</fieldset>
			</form>';
	}
	
	/**
	 * Exibe os dados referentes as Unidades Acadêmicas,
	 * é exibido tambem um botão para uma possível exclusão da Unidade.
	 *
	 * @param array $lista
	 *        	Array com os dados das Unidades Acadêmicas.
	 */
	public function mostraLista($lista) {
		foreach ( $lista as $elemento ) {
			echo 'ID: ' . $elemento->getId () . '<br>';
			echo 'Nome: ' . $elemento->getNome () . '<br> ';
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