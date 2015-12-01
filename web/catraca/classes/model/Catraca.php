<?php

class Catraca{
	
	private $id;
	private $nome;
	private $ip;
	
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
	
}


?>