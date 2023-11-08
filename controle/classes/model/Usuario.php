<?php


class Usuario{
	private $id;
	
	private $nome;
	
	private $email;
	private $login;
	private $senha;
	private $nivelAcesso;
	
	public function Usuario(){
		$this->id = 0;
	}
	
	
	
	
	public function setId($id){
		$idBaseExterna = intval ( $id) ;
		if(is_int($id))
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
	
	
	//Documentos
	private $idBaseExterna;
	private $cpf;
	private $identidade;
	private $passaporte;
	
	
	private $matricula;
	private $nivelDiscente;
	private $statusDiscente;
	
	
	private $siape;
	private $categoria;
	private $tipoDeUsuario;
	private $statusServidor;
	
	public function setStatusServidor($statusServidor){
		$this->statusServidor = $statusServidor;
	}
	public function getStatusServidor(){
		return $this->statusServidor;
	}
	
	public function setIdBaseExterna($idBaseExterna){
		$idBaseExterna = intval ( $idBaseExterna ) ;
		if(is_int($idBaseExterna))
			$this->idBaseExterna = $idBaseExterna;
	}
	public function  getIdBaseExterna(){
		return $this->idBaseExterna;
	}
	public function setCpf($cpf){
		$this->cpf = $cpf;
	}
	public function getCpf(){
		return $this->cpf;
	}
	public function setIdentidade($identidade){
		$this->identidade = $identidade;
	}
	public function getIdentidade(){
		return $this->identidade;
	}
	public function setPassaporte($passaporte){
		$this->passaporte = $passaporte;
	}
	public function getPassaporte(){
		return $this->passaporte;
	}
	public function setMatricula($matricula){
		$this->matricula = $matricula;
	}
	public function getMatricula(){
		return $this->matricula;
	}
	public function setNivelDiscente($nivelDiscente){
		$this->nivelDiscente = $nivelDiscente;
	}
	public function getNivelDiscente(){
		return $this->nivelDiscente;
		
	}
	
	public function setStatusDiscente($statusDiscente){
		$this->statusDiscente = $statusDiscente;
	}
	public function getStatusDiscente(){
		return $this->statusDiscente;
		
	}
	public function setSiape($siape){
		$this->siape = $siape;
	}
	public function getSiape(){
		return $this->siape;
	}
	public function setCategoria($categoria){
		$this->categoria = $categoria;
	}
	public function getCategoria(){
		return $this->categoria;
	}
	public function setTipoDeUsuario($tipoDeUsuario){
		$this->tipoDeUsuario = $tipoDeUsuario;
	}
	public function getTipodeUsuario(){
		return $this->tipoDeUsuario;
	}
	
	
}