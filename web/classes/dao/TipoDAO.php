<?php
/**
 * Classe utilizada para conxão com o Bando de Dados.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */
class TipoDAO extends DAO {
	
	/**
	 * Retorna um array contendo todos os tipos cadastrados.
	 * 
	 * @return Tipo[] Array de contendo os Tipos
	 */
	public function retornaLista() {
		$lista = array ();
		$result = $this->getConexao ()->query ( "SELECT * FROM tipo LIMIT 10" );
		
		foreach ( $result as $linha ) {
			$tipo = new Tipo ();
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
			$lista [] = $tipo;
		}
		return $lista;
	}
	
	/**
	 * Consulta o Tipo pelo ID.
	 * 
	 * @param Tipo $tipo        	
	 * @return Tipo
	 */
	public function retornaTipoPorId(Tipo $tipo) {
		$idTipo = $tipo->getId ();
		$sql = "SELECT * FROM tipo WHERE tipo_id = $idTipo";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$tipo->setId ( $linha ['tipo_id'] );
			$tipo->setNome ( $linha ['tipo_nome'] );
			$tipo->setValorCobrado ( $linha ['tipo_valor'] );
		}
		return $tipo;
	}
}