<?php
/**
 * Classe utilizada para instanciar o Objeto Tipo.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * 
 * Classe utilizada para intaciar objetos do tipo Tipo.
 *
 */
class Tipo {
	
	/**
	 * Variável que recebe o Id do Tipo.
	 * 
	 * @var $id
	 */
	private $id;
	
	/**
	 * Variável que recebe o Nome do Tipo.
	 * 
	 * @var $nome
	 */
	private $nome;
	
	/**
	 * Variável que recebe o Valor Cobrado para o Tipo.
	 * 
	 * @var $valorCobrado
	 */
	private $valorCobrado;
	
	/**
	 * Função utilizada para encapsular o valor da variável $id.
	 * 
	 * @param int $id        	
	 */
	public function setId($id) {
		$this->id = $id;
	}
	
	/**
	 * Retorna o valor da variável $id.
	 * 
	 * @return int
	 */
	public function getId() {
		return $this->id;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $nome
	 * 
	 * @param string $nome        	
	 */
	public function setNome($nome) {
		$this->nome = $nome;
	}
	
	/**
	 * Retorna o valor da variável $nome.
	 * 
	 * @return string
	 */
	public function getNome() {
		return $this->nome;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $valorCobrado
	 * 
	 * @param float $valorCobrado        	
	 */
	public function setValorCobrado($valorCobrado) {
		$this->valorCobrado = $valorCobrado;
	}
	
	/**
	 * Retorna o valor da variável $valorCobrado.
	 * 
	 * @return float
	 */
	public function getValorCobrado() {
		return $this->valorCobrado;
	}
}
?>