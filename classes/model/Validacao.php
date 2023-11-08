<?php 

class Validacao {
	
	private $id;
	private $campo;
	private $valor;
	private $tipoId;
	private $tipoNome;
	
	public function getId(){
		return $this->id;
	}
	
	public function setId($id){
		$this->id = $id;
	}
	
	public function getCampo(){
		return $this->campo;	
	}
	
	public function setCampo($campo){
		$this->campo = $campo;
	}
	
	public function getValor(){
		return $this->valor;
	}
	
	public function setValor($valor){
		$this->valor = $valor;
	}
	
	public function getTipoId(){
		return $this->tipoId;
	}
	
	public function setTipoId($tipoId){
		$this->tipoId = $tipoId;
	}
	
	public function setTipoNome($tipoNome){
		$this->tipoNome = $tipoNome;
	}
	
	public function getTipoNome(){
		return $this->tipoNome;
	}
	
	
	
}

?>