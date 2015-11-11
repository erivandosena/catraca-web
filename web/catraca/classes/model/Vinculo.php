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
		$this->quantidadeDeAlimentosPorTurno = $quantidade;
	}
	public function getQuantidadeDeAlimentosPorTurno(){
		return $this->quantidadeDeAlimentosPorTurno;
	}
	public function setDescricao($descricao){
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