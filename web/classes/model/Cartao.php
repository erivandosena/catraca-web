<?php
/**
 * Classe utilizada para instanciar o Objeto Cartão.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * 
 * Classe utilizada para intaciar objetos do tipo Cartão
 *
 */
class Cartao {
	
	/**
	 * Variável que recebe o Id do Cartão.
	 *
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe o Número do Cartão.
	 *
	 * @access private
	 * @var string
	 */
	private $numero;
	
	/**
	 * Variável que recebe os Créditos do Cartão.
	 *
	 * @access private
	 * @var int
	 */
	private $creditos;
	
	/**
	 * Variável que rece o Tipo do Cartão.
	 *
	 * @access private
	 * @var Tipo
	 */
	private $tipo;
	
	/**
	 * Função construtora da Classe Cartão.
	 * Para cada Cartão será instaciado um Tipo para ele.
	 */
	public function Cartao() {
		$this->tipo = new Tipo ();
		$this->creditos = 0;
	}
	
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
	 * Função utilizada para encapsular o valor da variável $numero.
	 * 
	 * @param string $numero        	
	 */
	public function setNumero($numero) {
		$this->numero = preg_replace ( '/[^0-9]/', '', $numero );
	}
	
	/**
	 * Retorna o número do cartão.
	 * 
	 * @return string
	 */
	public function getNumero() {
		return $this->numero;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $creditos.
	 * 
	 * @param float $creditos        	
	 */
	public function setCreditos($creditos) {
		$this->creditos = $creditos;
	}
	
	/**
	 * Retorna a quantidade de créditos.
	 * 
	 * @return float
	 */
	public function getCreditos() {
		return $this->creditos;
	}
	
	/**
	 * Função utilizada para encapsular do Objeto Tipo.
	 * 
	 * @param Tipo $tipo        	
	 */
	public function setTipo(Tipo $tipo) {
		$this->tipo = $tipo;
	}
	
	/**
	 * Retorna o tipo.
	 * 
	 * @return Tipo
	 */
	public function getTipo() {
		return $this->tipo;
	}
	
	/**
	 *
	 * @ignore
	 *
	 * @param float $creditos        	
	 */
	public function adicionaCreditos($creditos) {
		if (is_numeric ( $creditos )) {
			$this->setCreditos ( $this->getCreditos () + $creditos );
		}
	}
}

?>