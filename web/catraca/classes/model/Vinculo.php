<?php


class Vinculo{
	
	
	
	private $id;
	private $avulso;
	private $responsavel;
	private $inicioValidade;
	private $finalValidade;
	private $quantidadeDeAlimentosPorTurno;
	private $descricao;
	private $cartao;	

	public function Vinculo(){
		$this->setAvulso(false);
		$this->responsavel = new Usuario();
		$this->cartao= new Cartao();
		
	}
	
	public function setInicioValidade($inicioValidade){
		$this->inicioValidade = $inicioValidade;
	}
	public function getInicioValidade(){
		return $this->inicioValidade;
	}
	public function setFinalValidade($finalValidade){
		$this->finalValidade = $finalValidade;
	}
	public function getFinalValidade(){
		return $this->finalValidade;
	}
	public function setId($id){
		$this->id = $id;
	}
	public function getId(){
		return $this->id;
	}
	public function setAvulso($avulso){
		if($avulso)
			$this->avulso = true;
		else
			$this->avulso = false;
	}
	public function isAvulso(){
		return $this->avulso;
	}
	public function setResponsavel(Usuario $usuario){
		$this->responsavel = $usuario;
	}
	public function getResponsavel(){
		return $this->responsavel;
	}
	public function setQuantidadeDeAlimentosPorTurno($quantidade){
		$this->quantidadeDeAlimentosPorTurno = intval($quantidade);
	}
	public function getQuantidadeDeAlimentosPorTurno(){
		return $this->quantidadeDeAlimentosPorTurno;
	}
	public function setDescricao($descricao){
		$descricao = preg_replace ('/[^a-zA-Z0-9\s]/', '', $descricao);
		$this->descricao = $descricao;
	}
	public function getDescricao(){
		return $this->descricao;
		
	}
	public function setCartao(Cartao $cartao){
		$this->cartao = $cartao;
	}
	public function getCartao(){
		return $this->cartao;
	}
	
	
	
}


?>