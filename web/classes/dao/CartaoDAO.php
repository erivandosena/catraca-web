<?php
/**
 * Classe utilizada para conxão com o Bando de Dados.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */

/**
 * Nesta classe são realizadas as conexões com o Banco de Dados,
 * com referência ao tratamento de dados relativos a entidade Cartões.
 *
 * Nela é realizada Consulta, Inserção, Atualização e Exclusão dos cartões.
 */
class CartaoDAO extends DAO {
	
	/**
	 * Função utilizada para realizar pesquisa pelo número do cartão,
	 * retorna um array contendo os dados do usuários, relativo ao cartão consultado.
	 *
	 * @param string $numero
	 *        	Número do cartão.
	 * @return Cartao[] Array contendo a consulta.
	 */
	public function pesquisaPorNumero($numero) {
		$numero = preg_replace ( '/[^0-9]/', '', $numero );
		$lista = array ();
		
		$sql = "SELECT * FROM cartao 
		INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id 
		WHERE cart_numero = '$numero' LIMIT 100";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$cartao = new Cartao ();
			$cartao->setId ( $linha ['cart_id'] );
			$cartao->setCreditos ( $linha ['cart_creditos'] );
			$cartao->setNumero ( $linha ['cart_numero'] );
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
			$cartao->setTipo ( $tipo );
			$lista [] = $cartao;
		}
		return $lista;
	}
	
	/**
	 * Função utilizada para realizar pesquisa pelo número do cartão,
	 * retorna um Objeto Cartão contendo os dados do usuários, relativo ao cartão consultado.
	 *
	 * @param Cartao $cartao
	 *        	Objeto os dados do Cartão.
	 * @return Cartao Objeto Cartão contendo os dados do cartão consultado.
	 */
	public function preenchePorNumero(Cartao $cartao) {
		$numero = $cartao->getNumero ();
		$sql = "SELECT * FROM cartao
		INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		WHERE cart_numero = '$numero' LIMIT 100";
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			
			$cartao->setId ( $linha ['cart_id'] );
			$cartao->setCreditos ( $linha ['cart_creditos'] );
			$cartao->setNumero ( $linha ['cart_numero'] );
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
			$cartao->setTipo ( $tipo );
			return $cartao;
		}
		return null;
	}
	
	/**
	 * Função utilizada para consultar todos os tipos cadastrados,
	 * retorna um array contendo as informações.
	 *
	 * @return Tipo[] Array contendo os tipos.
	 */
	public function retornaTipos() {
		$lista = array ();
		$result = $this->getConexao ()->query ( "SELECT * FROM tipo" );
		
		foreach ( $result as $linha ) {
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$lista [] = $tipo;
		}
		return $lista;
	}
	
	/**
	 * Retorna uma lista de cartões.
	 *
	 * @return Cartao[] Array contendo todos os cartões e seus respectivos Tipos.
	 */
	public function retornaLista() {
		$lista = array ();
		$result = $this->getConexao ()->query ( "SELECT * FROM cartao INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id LIMIT 100" );
		
		foreach ( $result as $linha ) {
			$cartao = new Cartao ();
			$cartao->setId ( $linha ['cart_id'] );
			$cartao->setCreditos ( $linha ['cart_creditos'] );
			$cartao->setNumero ( $linha ['cart_numero'] );
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
			$cartao->setTipo ( $tipo );			
			$lista [] = $cartao;
		}
		return $lista;
	}
	
	/**
	 * Função utilizada para realizar a inserção de um cartão novo,
	 * retorna True caso a inserção seja realizada.
	 *
	 * @param Cartao $cartao
	 *        	Cartão sem venculo a ser cadastrado.
	 * @return boolean True caso a inserção seja bem sussedida.
	 */
	public function inserir(Cartao $cartao) {
		$numero = $cartao->getNumero ();
		$idTipo = $cartao->getTipo ()->getId ();
		
		if ($this->getConexao ()->query ( "INSERT INTO cartao(cart_numero, cart_creditos, tipo_id) VALUES($numero, 0, $idTipo)" ))
			return true;
		return false;
	}
	
	/**
	 * Função utilizada para deletar uma unidade,
	 * retorna True caso o delete seja realizado.
	 *
	 * @param Unidade $unidade
	 *        	Unidade a ser excluída.
	 * @return boolean True caso a exclusão seja bem sucedida.
	 */
	public function deletarUnidade(Unidade $unidade) {
		$id = $unidade->getId ();
		$sql = "DELETE FROM unidade WHERE unid_id = $id";
		if ($this->getConexao ()->query ( $sql ))
			return true;
		return false;
	}
	
	/**
	 * Passe um Objeto cartao com ID e receba-o preenchido.
	 *
	 * @param Cartao $cartao
	 *        	Cartão a ser consultado.
	 * @return Cartao Objeto Cartão contendo os dados do cartão consultado.
	 */
	public function selecionaPorId(Cartao $cartao) {
		$id = $cartao->getId ();
		$id = intval ( $id );
		$sql = "SELECT * FROM cartao INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE cart_id = $id LIMIT 1";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			
			$cartao->setId ( $linha ['cart_id'] );
			$cartao->setCreditos ( $linha ['cart_creditos'] );
			$cartao->setNumero ( $linha ['cart_numero'] );
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
			$cartao->setTipo ( $tipo );
			return $cartao;
		}
	}
}

?>