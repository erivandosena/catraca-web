<?php
/**
 * Classe utilizada para instanciar o Objeto Isencao.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * 
 * Classe utilizada para intaciar objetos do tipo Isenção.
 *
 */
class Isencao {
	
	/**
	 * Variável que recebe o Id da Isenção.
	 *
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe a Data de Inicio da Isenção.
	 *
	 * @access private
	 * @var DateTime
	 */
	private $dataDeInicio;
	
	/**
	 * Variável que recebe a Data Final da Isenção.
	 *
	 * @access private
	 * @var DateTime
	 */
	private $dataFinal;
	
	/**
	 * Função Construtora da Classe Isenção.
	 */
	public function Isencao() {
		$this->id = 0;
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
	 * Função utilizada para encapsular o valor da variável $dataInicio.
	 *
	 * @param DateTime $dataInicio        	
	 */
	public function setDataDeInicio($dataInicio) {
		$this->dataDeInicio = $dataInicio;
	}
	
	/**
	 * Retorna o valor da variável $dataInicio.
	 *
	 * @return DateTime
	 */
	public function getDataDeInicio() {
		return $this->dataDeInicio;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $dataFinal.
	 *
	 * @param DateTime $dataFinal        	
	 */
	public function setDataFinal($dataFinal) {
		$this->dataFinal = $dataFinal;
	}
	
	/**
	 * Retorna o valor da variável $dataFinal.
	 *
	 * @return DateTime
	 */
	public function getDataFinal() {
		return $this->dataFinal;
	}
	
	/**
	 * Verifica se a Isenção ainda está válida,
	 * Comparando a Data Final a Data e Hora correntes.
	 * Restorna True caso a isenção ainda esteja válida.
	 *
	 * @return boolean
	 */
	public function isActive() {
		$tempoA = strtotime ( $this->getDataDeInicio () );
		$tempoB = strtotime ( $this->getDataFinal () );
		$tempoAgora = time ();
		if ($tempoAgora < $tempoB)
			return true;
		return false;
	}
}

?>