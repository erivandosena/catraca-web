<?php

class Catraca{
	
	private $id;
	private $nome;
	private $ip;
	private $tempoDeGiro;
	private $operacao;
	private $unidade;
	public function Catraca(){
		$this->unidade = new Unidade();
	}
	
	public function setUnidade(Unidade $unidade){
		$this->unidade = $unidade;
	}
	public function getUnidade(){
		return $this->unidade;
	}
	
	
	public function setId($id){
		$this->id = intval($id);
	}
	public function getId(){
		return $this->id;
	}
	
	public function setNome($nome){
		$this->nome = $nome;
	}
	public function getNome(){
		return $this->nome;
	}
	
	public function setIp($ip){
		$this->ip = $ip;
	}
	public function getIp(){
		return $this->ip;
	}
	public function setTempoDeGiro($tempoDeGiro){
		$this->tempoDeGiro = $tempoDeGiro;
	}
	public function getTempodeGiro(){
		return $this->tempoDeGiro;
	}
	public function setOperacao($operacao){
		$this->operacao = $operacao;
	}
	public function getOperacao(){
		return $this->operacao;
	}
	
	public function getStrOperacao(){
		$strOperacao = "Não Listado";
		switch ($this->getOperacao()){
			case self::GIRO_ANTI_HORARIO:
				$strOperacao = "Giro Anti Horário";
				break;
			case self::GIRO_HORARIO:
				$strOperacao = "Giro Horário";
			break;
			case self::GIRO_LIVRE:
				$strOperacao = "Giro Livre";
				break;
			default:
				$strOperacao = "Não Listado";
			break;	
		}
		return $strOperacao;
	}
	
	const GIRO_HORARIO = 1;
	const GIRO_ANTI_HORARIO = 2;
	const GIRO_LIVRE = 3;
	
}


?>