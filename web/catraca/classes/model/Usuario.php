<?php


class Usuario{
	private $id;
	private $nome;
	private $email;
	private $login;
	private $senha;
	private $nivelAcesso;
	
	
	
	public function setId($id){
		$this->id = $id;
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
	public function setEmail($email){
		$this->email = $email;
	}
	public function getEmail(){
		return $this->email;
	}
	public function setLogin($login){
		$this->login = $login;
	}
	public  function getLogin(){
		return $this->login;
	}
	public function setSenha($senha){
		$this->senha = $senha;
	}
        public function getSenha(){
            return $this->senha;
        }
	public function setNivelAcesso($nivelAcesso){
		$this->nivelAcesso = $nivelAcesso;
	}
	public function getNivelAcesso(){
		return $this->nivelAcesso;
	}
	
	public function __toString(){
		$strUsuario = ' Nome: '.$this->nome.' email: '.$this->email.' Login: '.$this->login;
		if($this->getNivelAcesso() == Sessao::NIVEL_COMUM){
			$strUsuario .= 'Nivel Default';
		}
		if($this->getNivelAcesso() == Sessao::NIVEL_ADMIN){
			$strUsuario .= 'Nivel Administrador';
		}
		if($this->getNivelAcesso() == Sessao::NIVEL_SUPER){
			$strUsuario .= 'Nivel Super';
		}
		return $strUsuario;
	}
	
	
	
}