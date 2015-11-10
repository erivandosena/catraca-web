<?php

class Isencao{
	private $id;
	private $dataDeInicio;
	private $dataFinal;
	private $cartao;
	
	public function setId($id){
		$this->id = $id;
	}
	public function getId(){
		return $this->id;
	}
	public function setDataDeInicio($dataInicio){
		$this->dataDeInicio = $dataInicio;
	}
	public function getDataDeInicio(){
		return $this->dataDeInicio;
		
	}
	public function setCartao(Cartao $cartao){
		$this->cartao = $cartao;
	}
	public function getCartao(){
		return $this->cartao;
	}
	
	
	
	
}

?>