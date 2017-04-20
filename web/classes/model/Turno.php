<?php
/**
 * Classe utilizada para instanciar o Objeto Turno.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
class Turno {
	
	/**
	 * Variável que recebe o Id do Turno.
	 * 
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe a Hora de Inicio do Turno.
	 * 
	 * @access private
	 * @var DateTime
	 */
	private $horaInicial;
	
	/**
	 * Variável que recebe a Hora de Termino do Turno.
	 * 
	 * @access private
	 * @var DateTime
	 */
	private $horaFinal;
	
	/**
	 * Variável que recebe a Descrição dada para o turno.
	 * 
	 * @access private
	 * @var string
	 */
	private $descricao;
	
	/**
	 * Função utilizada para encapsular o valor da variável $id.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 * 
	 * @param int $id        	
	 */
	public function setId($id) {
		$this->id = intval ( $id );
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
	 * Função utilizada para encapsular o valor da variável $horaInicial.
	 *
	 * @param DateTime $horaInicial        	
	 */
	public function setHoraInicial($horaInicial) {
		$this->horaInicial = $horaInicial;
	}
	
	/**
	 * Retorna o valor da variável $horaInicial.
	 *
	 * @return DateTime
	 */
	public function getHoraInicial() {
		return $this->horaInicial;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $horaFinal.
	 *
	 * @param DateTime $horaFinal        	
	 */
	public function setHoraFinal($horaFinal) {
		$this->horaFinal = $horaFinal;
	}
	
	/**
	 * Retorna o valor da variável $horaFinal.
	 *
	 * @return DateTime
	 */
	public function getHoraFinal() {
		return $this->horaFinal;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $descricao.
	 *
	 * @param string $descricao        	
	 */
	public function setDescricao($descricao) {
		$this->descricao = $descricao;
	}
	
	/**
	 * Retorna o valor da variável $descricao.
	 *
	 * @return string
	 */
	public function getDescricao() {
		return $this->descricao;
	}
}

?>