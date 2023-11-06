<?php
/**
 * Classe utilizada para instanciar o Objeto Vinculo.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * Classe utilizada para intaciar objetos do tipo Vínculo.
 */
class Vinculo {
	
	/**
	 * Variável que recebe o Id do Vínculo.
	 *
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável utilizada para verificar se o Vínculo é avulso.
	 *
	 * @access private
	 * @var boolean
	 */
	private $avulso;
	
	/**
	 * Recebe um Objeto Usuario.
	 *
	 * @access private
	 * @var Usuario
	 */
	private $responsavel;
	
	/**
	 * Variável que recebe a Data de Inicio do Vínculo.
	 *
	 * @access private
	 * @var DateTime
	 */
	private $inicioValidade;
	
	/**
	 * Variável que recebe a Data Final do Vinculo.
	 *
	 * @access private
	 * @var DateTime
	 */
	private $finalValidade;
	
	/**
	 * Recebe a quantidade de Alimentos por Turno
	 * 
	 * @access private
	 * @var int
	 */
	private $quantidadeDeAlimentosPorTurno;
	
	/**
	 * Variável que recebe a Descrição do Vinculo.
	 *
	 * @access private
	 * @var string
	 */
	private $descricao;
	
	/**
	 * Recebe um Objeto Cartão.
	 *
	 * @access private
	 * @var Cartao
	 */
	private $cartao;
	
	/**
	 * Variável que recebe as Refeições Restantes para o Vínculo.
	 *
	 * @access private
	 * @var int
	 */
	private $refeicoesRestantes;
	
	/**
	 * Variável utilizada para verifica se o vinculo é isento.
	 *
	 *
	 * @access private
	 * @var boolean
	 */
	private $isento;
	
	/**
	 * Recebe um Objeto Isencao.
	 *
	 * @access public
	 * @var Isencao
	 */
	public $isencao;
	
	/**
	 * Função Construtora da Classe Vinculo.
	 * O vinculo por padrão não é Isento nem Avulso, recebendo False em ambas.
	 */
	public function Vinculo() {
		$this->setIsento ( false );
		$this->isencao = new Isencao ();
		$this->setAvulso ( false );
		$this->responsavel = new Usuario ();
		$this->cartao = new Cartao ();
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $refeicoesRestantes.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 *
	 * @param int $refeicoesRestantes        	
	 */
	public function setRefeicoesRestantes($refeicoesRestantes) {
		$this->refeicoesRestantes = intval ( $refeicoesRestantes );
	}
	
	/**
	 * Retorna o valor da variável $refeicoesRestantes.
	 *
	 * @return int
	 */
	public function getRefeicoesRestantes() {
		return $this->refeicoesRestantes;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $isento.
	 * Retorna True caso o Vinculo seja Isento.
	 *
	 * @param boolean $isento        	
	 */
	public function setIsento($isento) {
		if ($isento)
			$this->isento = true;
		else
			$this->isento = false;
	}
	
	/**
	 * Função utilizada para encapsular os valores do Objeto Isenção.
	 *
	 * @param Isencao $isencao        	
	 */
	public function setIsencao(Isencao $isencao) {
		$this->isencao = $isencao;
	}
	
	/**
	 * Retorna o valor do Objeto Isenção.
	 *
	 * @return Isencao
	 */
	public function getIsencao() {
		return $this->isencao;
	}
	
	/**
	 * Verifica se o Vinculo é isento retornando True caso seja verdadeiro.
	 *
	 * @return boolean
	 */
	public function ehIsento() {
		if ($this->isento)
			return true;
		return false;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $inicioValidade.
	 *
	 * @param DateTime $inicioValidade        	
	 */
	public function setInicioValidade($inicioValidade) {
		$this->inicioValidade = $inicioValidade;
	}
	
	/**
	 * Retorna o valor da variável $inicioValidade.
	 *
	 * @return DateTime
	 */
	public function getInicioValidade() {
		return $this->inicioValidade;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $finalValidade.
	 *
	 * @param DateTime $finalValidade        	
	 */
	public function setFinalValidade($finalValidade) {
		$this->finalValidade = $finalValidade;
	}
	
	/**
	 * Retorna o valor da variável $finalValidade.
	 *
	 * @return DateTime
	 */
	public function getFinalValidade() {
		return $this->finalValidade;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $id.
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
	 * Função utilizada para encapsular o valor da variável $avulso.
	 *
	 * @param boolean $avulso        	
	 */
	public function setAvulso($avulso) {
		if ($avulso)
			$this->avulso = true;
		else
			$this->avulso = false;
	}
	
	/**
	 * Retorna o valor da variável $avulso.
	 *
	 * @return boolean
	 */
	public function isAvulso() {
		return $this->avulso;
	}
	
	/**
	 * Função utilizada para encapsular o valor o Objeto responsavel que é um Usuario.
	 *
	 * @param Usuario $usuario        	
	 */
	public function setResponsavel(Usuario $usuario) {
		$this->responsavel = $usuario;
	}
	
	/**
	 * Retorna o valor do Objeto responsável.
	 *
	 * @return Usuario
	 */
	public function getResponsavel() {
		return $this->responsavel;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $quantidadeDeAlimentosPorTurno.
	 *
	 * @param int $quantidade        	
	 */
	public function setQuantidadeDeAlimentosPorTurno($quantidade) {
		$this->quantidadeDeAlimentosPorTurno = intval ( $quantidade );
	}
	
	/**
	 * Retorna o valor da variável $quantidadeDeAlimentosPorTurno.
	 *
	 * @return int
	 */
	public function getQuantidadeDeAlimentosPorTurno() {
		return $this->quantidadeDeAlimentosPorTurno;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $descricao.
	 *
	 * @param string $descricao        	
	 */
	public function setDescricao($descricao) {
		$descricao = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $descricao );
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
	
	/**
	 * Função utilizada para encapsular o valor do Objeto $cartao.
	 *
	 * @param Cartao $cartao        	
	 */
	public function setCartao(Cartao $cartao) {
		$this->cartao = $cartao;
	}
	
	/**
	 * Retorna o valor do Objeto $cartao.
	 *
	 * @return Cartao
	 */
	public function getCartao() {
		return $this->cartao;
	}
	
	/**
	 * Verifica, de acordo com os valores das variáveis $inicioDaValidade e $fimDaValidade,
	 * se o vincuo está ativo, retornando True.
	 *
	 * @return boolean
	 */
	public function isActive() {
		$tempoA = strtotime ( $this->getInicioValidade () );
		$tempoB = strtotime ( $this->getFinalValidade () );
		$tempoAgora = time ();
		if ($tempoAgora > $tempoA && $tempoAgora < $tempoB)
			return true;
		return false;
	}
	
	/**
	 * 
	 * @return boolean
	 */
	public function invalidoParaAdicionar() {
		$time = strtotime ( date ( "Y-m-d 01:00:00" ) );
		$tempo1 = strtotime ( $this->getInicioValidade () );
		$tempo2 = strtotime ( $this->getFinalValidade () );
		if ($time > $tempo1 || $time > $tempo2)
			return true;
		return false;
	}
}

?>