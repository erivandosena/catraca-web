<?php
/**
 * Classe utilizada para instanciar o Objeto Catraca.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
/**
 * 
 * Classe utilizada para intaciar objetos do tipo Catraca.
 *
 */
class Catraca {
	
	/**
	 * Variável que recebe o Id da Catraca.
	 *
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe Nome da Catraca.
	 *
	 * @access private
	 * @var string
	 */
	private $nome;
	
	/**
	 * Variável que recebe o Ip da Catraca.
	 *
	 * @access private
	 * @var string
	 */
	private $ip;
	
	/**
	 * Variável que recebe o Tempo de Giro da Catraca.
	 *
	 * @access private
	 * @var int
	 */
	private $tempoDeGiro;
	
	/**
	 * Variável que recebe a Operacao da Catraca, que corresponde ao sentido de giro.
	 *
	 * @access private
	 * @var int
	 */
	private $operacao;
	
	/**
	 * Variável que recebe o Mac da Catraca, referente a conexao Lan.
	 *
	 * @access private
	 * @var string
	 */
	private $macLan;
	
	/**
	 * Variável que recebe o Mac da Catraca, referente conexao Wifi.
	 *
	 * @access private
	 * @var string
	 */
	private $macWlan;
	
	/**
	 * Variável que recebe o tipo de Interface de rede que será utilizado pela Catraca,
	 * recebe os valores "eth0" ou "wlan0".
	 *
	 * @access private
	 * @var string
	 */
	private $interfaceRede;
	
	/**
	 * Recebe um Objeto Unidade.
	 *
	 * @access private
	 * @var Unidade
	 */
	private $unidade;
	
	/**
	 * Variável recebe um boolean que habilita ou desabilita o Módulo Financeiro da Catraca
	 * True - habilita, False - desabilita.
	 *
	 * @access private
	 * @var boolean
	 */
	private $financeiro;
	
	/**
	 * Função Construtora da Classe Catraca.
	 * Para cada Catraca será instaciado uma Unidade.
	 */
	public function Catraca() {
		$this->unidade = new Unidade ();
	}
	
	/**
	 * Retorna uma string contendo a informação do Status do Módulo Financeiro da Catraca,
	 * podendo está Habilitado ou Desabilitado, de acordo com o valor recebido na variável $financeiro.
	 *
	 * @return string
	 */
	public function getStrFincaneito() {
		$financeiro = "";
		switch ($this->financeiroAtivo ()) {
			case true :
				$financeiro = "Habilitado";
				break;
			case false :
				$financeiro = "Desabilitado";
				break;
			default :
				$financeiro = "Não Identificado";
				break;
		}
		return $financeiro;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $unidade.
	 * Recebe um Objeto Unidade.
	 *
	 * @param Unidade $unidade        	
	 */
	public function setUnidade(Unidade $unidade) {
		$this->unidade = $unidade;
	}
	
	/**
	 * Retorna o objeto Unidade.
	 *
	 * @return Unidade
	 */
	public function getUnidade() {
		return $this->unidade;
	}
	
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
	 * Função utilizada para encapsular o valor da variável $nome.
	 *
	 * @param string $ip        	
	 */
	public function setIp($ip) {
		$this->ip = $ip;
	}
	
	/**
	 * Retorna o valor da variável $ip.
	 *
	 * @return string
	 */
	public function getIp() {
		return $this->ip;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $tempoDeGiro.
	 *
	 * @param int $tempoDeGiro        	
	 */
	public function setTempoDeGiro($tempoDeGiro) {
		$this->tempoDeGiro = $tempoDeGiro;
	}
	
	/**
	 * Retorna o valor da variável $tempoDeGiro.
	 *
	 * @return int
	 */
	public function getTempodeGiro() {
		return $this->tempoDeGiro;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $operacao.
	 *
	 * @param int $operacao        	
	 */
	public function setOperacao($operacao) {
		$this->operacao = $operacao;
	}
	
	/**
	 * Retorna o valor da variável $operacao.
	 *
	 * @return int
	 */
	public function getOperacao() {
		return $this->operacao;
	}
	
	/**
	 * Retorna uma string de acordo com o valor recebido na variável $operacao, que pode ser:
	 *
	 * 1 = Horario Validado -> Anti-horário Bloqueado;
	 * 2 = Anti-horário Validado -> Horario Bloqueado;
	 * 3 = Anti-horário Livre -> Horario Validado;
	 * 4 = Hoário Livre -> Anti-horário Validado;
	 * 5 = Livre em abos os sentidos.
	 *
	 * @return string
	 */
	public function getStrOperacao() {
		$strOperacao = "Não Listado";
		switch ($this->getOperacao ()) {
			case self::GIRO_ANTI_VAL_HOR_BLOQ :
				$strOperacao = "Giro Anti-Horário";
				break;
			case self::GIRO_HOR_VAL_ANTI_BLOQ :
				$strOperacao = "Giro Horário";
				break;
			case self::GIRO_LIVRE :
				$strOperacao = "Giro Livre";
				break;
			case self::GIRO_ANTI_LIVRE_HOR_VAL :
				$strOperacao = "Anti-Horário(LIVRE) / Horário(VALIDADO)";
				break;
			case self::GIRO_HOR_LIVRE_ANTI_VAL :
				$strOperacao = "Horário(LIVRE) / Anti-Horário(VALIDADO)";
				break;
			default :
				$strOperacao = "Não Listado";
				break;
		}
		return $strOperacao;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $macLan.
	 *
	 * @param string $macLan        	
	 */
	public function setMacLan($macLan) {
		$this->macLan = $macLan;
	}
	
	/**
	 * Retorna o valor da variável $macLan.
	 *
	 * @return string
	 */
	public function getMacLan() {
		return $this->macLan;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $macWlan.
	 *
	 * @param string $macWlan        	
	 */
	public function setMacWlan($macWlan) {
		$this->macWlan = $macWlan;
	}
	
	/**
	 * Retorna o valor da variável $macWlan.
	 *
	 * @return string
	 */
	public function getMacWlan() {
		return $this->macWlan;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $InterfaceRede.
	 *
	 * @param string $InterfaceRede        	
	 */
	public function setInterfaceRede($InterfaceRede) {
		$this->interfaceRede = $InterfaceRede;
	}
	
	/**
	 * Retorna o valor da variável $InterfaceRede.
	 *
	 * @return string
	 */
	public function getInterfaceRede() {
		return $this->interfaceRede;
	}
	
	/**
	 * Retorna uma string de acordo com o valor recebido na váriável $InterfaceRede, que pode ser:
	 * "eth0" - Rede Cabeada;
	 * "wlan0" - Rede Sem Fio.
	 *
	 * @return string
	 */
	public function getStrIterfaceRede() {
		$interface = "Não Identificado";
		switch ($this->getInterfaceRede ()) {
			case 'eth0' :
				$interface = "Rede Cabeada";
				break;
			case 'wlan0' :
				$interface = "Rede Sem Fio";
				break;
			default :
				$interface = "Não Identificado";
				break;
		}
		return $interface;
	}
	
	/**
	 * Retorna uma string que concatena o retorno da Função getStrOperacao(),
	 * com o Status do Módulo Financeiro, que pode ser:
	 *
	 * True - Financeiro Ativo;
	 * False - Sem financeiro.
	 *
	 * @return string
	 */
	public function __toString() {
		$str = $this->getStrOperacao ();
		$str .= $this->getUnidade ()->getNome ();
		if ($this->financeiroAtivo ())
			$str .= "Financeiro Ativo";
		else
			$str .= "Sem financeiro";
		return $str;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $financeiro.
	 *
	 * @param boolean $financeiro        	
	 */
	public function setFinanceiro($financeiro) {
		if ($financeiro)
			$this->financeiro = true;
		else
			$this->financeiro = false;
	}
	
	/**
	 * Retona True quando o Módulo estiver ativo.
	 *
	 * @return boolean
	 */
	public function financeiroAtivo() {
		if ($this->financeiro)
			return true;
		return false;
	}
	const GIRO_HOR_VAL_ANTI_BLOQ = 1;
	const GIRO_ANTI_VAL_HOR_BLOQ = 2;
	const GIRO_ANTI_LIVRE_HOR_VAL = 3;
	const GIRO_HOR_LIVRE_ANTI_VAL = 4;
	const GIRO_LIVRE = 5;
}

?>