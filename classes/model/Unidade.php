<?php
/**
 * Classe utilizada para instanciar o Objeto Unidade.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * Unidade Academica.
 *
 * Será usada em muitos lugares.
 * Turno tem unidade academica, catraca tem unidade, etc.
 */
class Unidade {
	
	/**
	 * Variável que recebe o Id da Unidade.
	 * 
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe o Nome da Unidade.
	 * 
	 * @access private
	 * @var string
	 */
	private $nome;
	
	/**
	 * Variável que recebe os Turnos da Unidade.
	 * 
	 * @access private
	 * @var Turno[]
	 */
	private $turnosValidos;
	
	/**
	 * Recebe um Objeto Catraca.
	 * 
	 * @access private
	 * @var Catraca
	 */
	private $catracas;
	
	/**
	 * Variável que recebe o Custo da Unidade.
	 * 
	 * @access private
	 * @var float
	 */
	private $custoUnidade;
	
	/**
	 * Função Construtora da Classe Unidade.
	 * Ao ser instaciada é gerada um array com os Turnos Válidos.
	 */
	public function Unidade() {
		$this->turnosValidos = array ();
	}
	
	/**
	 * Retorna um array com os Turnos Válidos.
	 * 
	 * @return array
	 */
	public function getTurnosValidos() {
		return $this->turnosValidos;
	}
	
	/**
	 *
	 * @param Turno $turno        	
	 */
	public function adicionaTurno(Turno $turno) {
		$this->turnosValidos [] = $turno;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $id
	 *
	 * @param int $id        	
	 */
	public function setId($id) {
		$this->id = intval ( $id );
	}
	
	/**
	 * Retorna o valor da variável $id
	 *
	 * @return int
	 */
	public function getId() {
		return $this->id;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $nome.
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
	 * Retorna o valor da variável $custoUnidade.
	 *
	 * @return float
	 */
	public function getCustoUnidade() {
		return $this->custoUnidade;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $custoUnidade.
	 *
	 * @param float $custoUnidade        	
	 */
	public function setCustoUnidade($custoUnidade) {
		$this->custoUnidade = $custoUnidade;
	}
}