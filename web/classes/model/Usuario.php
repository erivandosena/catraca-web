<?php
/**
 * Classe utilizada para instanciar o Objeto Usuario.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Modelo
 */
class Usuario {
	
	/**
	 * Variável que recebe o Id do Usuário.
	 * 
	 * @access private
	 * @var int
	 */
	private $id;
	
	/**
	 * Variável que recebe o Nome do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $nome;
	
	/**
	 * Variável que recebe o Email do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $email;
	
	/**
	 * Variável que recebe o Login do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $login;
	
	/**
	 * Variável que recebe a Senha do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $senha;
	
	/**
	 * Variável que recebe o Nivel de Acesso do Usuário.
	 * 
	 * @access private
	 * @var int
	 */
	private $nivelAcesso;
	
	/**
	 * Variável que recebe a Categoria do Usuário.
	 * 
	 * @access private
	 * @var int
	 */
	private $idCategoria;
	
	// Documentos
	/**
	 * Variável que recebe o Id do bando de Dados do Sigaa.
	 * 
	 * @access private
	 * @var int
	 */
	private $idBaseExterna;
	
	/**
	 * Variável que recebe o Número do CPF do Usuário
	 * 
	 * @access private
	 * @var string
	 */
	private $cpf;
	
	/**
	 * Variável que recebe o Número da Identidade do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $identidade;
	
	/**
	 * Variável que recebe o Número do Passaporte do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $passaporte;
	
	/**
	 * Variável que recebe o Número da Mátricula do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $matricula;
	
	/**
	 * Variável que recebe o Nível do Discente.
	 * 
	 * @access private
	 * @var string
	 */
	private $nivelDiscente;
	
	/**
	 * Variável que recebe o Status do Discente.
	 * 
	 * @access private
	 * @var string
	 */
	private $statusDiscente;
	
	/**
	 * Variável que recebe o Número do Siape do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $siape;
	
	/**
	 * Variável que recebe a Categoria do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $categoria;
	
	/**
	 * Variável que recebe o Tipo do Usuário.
	 * 
	 * @access private
	 * @var string
	 */
	private $tipoDeUsuario;
	
	/**
	 * Variável que recebe o Status do Servidor.
	 * 
	 * @access private
	 * @var string
	 */
	private $statusServidor;
	
	/**
	 * Função Construtora da Classe Usuário.
	 */
	public function Usuario() {
		$this->id = 0;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $idCategoria.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 *
	 * @param int $idCategoria        	
	 */
	public function setIDCategoria($idCategoria) {
		$idBaseExterna = intval ( $idCategoria );
		if (is_int ( $idCategoria ))
			$this->idCategoria = $idCategoria;
	}
	
	/**
	 * Retorna o valor da variável $idCategoria.
	 *
	 * @return int
	 */
	public function getIDCategoria() {
		return $this->idCategoria;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $id.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 *
	 * @param int $id        	
	 */
	public function setId($id) {
		$idBaseExterna = intval ( $id );
		if (is_int ( $id ))
			$this->id = $id;
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
	 * Função utilizada para encapsular o valor da variável $email.
	 *
	 * @param string $email        	
	 */
	public function setEmail($email) {
		$this->email = $email;
	}
	
	/**
	 * Retorna o valor da variável $email.
	 *
	 * @return string
	 */
	public function getEmail() {
		return $this->email;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $login.
	 *
	 * @param string $login        	
	 */
	public function setLogin($login) {
		$this->login = $login;
	}
	
	/**
	 * Retorna o valor da variável $login.
	 *
	 * @return string
	 */
	public function getLogin() {
		return $this->login;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $senha.
	 *
	 * @param string $senha        	
	 */
	public function setSenha($senha) {
		$this->senha = $senha;
	}
	
	/**
	 * Retorna o valor da variável $senha.
	 *
	 * @return string
	 */
	public function getSenha() {
		return $this->senha;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $nivelAcesso.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 *
	 * @param int $nivelAcesso        	
	 */
	public function setNivelAcesso($nivelAcesso) {
		$nivelAcesso = intval ( $nivelAcesso );
		if (is_int ( $nivelAcesso ))
			$this->nivelAcesso = $nivelAcesso;
	}
	
	/**
	 * Retorna o valor da variável $nivelAcesso.
	 *
	 * @return int
	 */
	public function getNivelAcesso() {
		return $this->nivelAcesso;
	}
	
	/**
	 * Retona uma string contendo uma concatenação dos dados do usuário,
	 * é retornado também o nível de acesso ao sistema do usuário.
	 *
	 * @return string
	 */
	public function __toString() {
		$strUsuario = ' Nome: ' . $this->nome . ' email: ' . $this->email . ' Login: ' . $this->login;
		if ($this->getNivelAcesso () == Sessao::NIVEL_COMUM) {
			$strUsuario .= 'Nivel Default';
		}
		if ($this->getNivelAcesso () == Sessao::NIVEL_ADMIN) {
			$strUsuario .= 'Nivel Administrador';
		}
		if ($this->getNivelAcesso () == Sessao::NIVEL_SUPER) {
			$strUsuario .= 'Nivel Super';
		}
		return $strUsuario;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $statusServidor
	 *
	 * @param string $statusServidor        	
	 */
	public function setStatusServidor($statusServidor) {
		$this->statusServidor = $statusServidor;
	}
	
	/**
	 * Retorna o valor da variável $statusServidor.
	 *
	 * @return string
	 */
	public function getStatusServidor() {
		return $this->statusServidor;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $idBaseExterna,
	 * que é o Id do Banco de Dados do Sigaa.
	 * Caso seja recebido outro tipo de variável será convertido para inteiro.
	 *
	 * @param int $idBaseExterna        	
	 */
	public function setIdBaseExterna($idBaseExterna) {
		$idBaseExterna = intval ( $idBaseExterna );
		if (is_int ( $idBaseExterna ))
			$this->idBaseExterna = $idBaseExterna;
	}
	
	/**
	 * Retorna o valor da variável $idBaseExterna.
	 *
	 * @return unknown
	 */
	public function getIdBaseExterna() {
		return $this->idBaseExterna;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $cpf
	 *
	 * @param string $cpf        	
	 */
	public function setCpf($cpf) {
		$this->cpf = $cpf;
	}
	
	/**
	 * Retorna o valor da variável $cpf.
	 *
	 * @return string
	 */
	public function getCpf() {
		return $this->cpf;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $identidade.
	 *
	 * @param string $identidade        	
	 */
	public function setIdentidade($identidade) {
		$this->identidade = $identidade;
	}
	
	/**
	 * Retorna o valor da variável $identidade.
	 *
	 * @return string
	 */
	public function getIdentidade() {
		return $this->identidade;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $passaporte.
	 *
	 * @param string $passaporte        	
	 */
	public function setPassaporte($passaporte) {
		$this->passaporte = $passaporte;
	}
	
	/**
	 * Retorna o valor da variável $passaporte.
	 *
	 * @return string
	 */
	public function getPassaporte() {
		return $this->passaporte;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $matricula.
	 *
	 * @param string $matricula        	
	 */
	public function setMatricula($matricula) {
		$this->matricula = $matricula;
	}
	
	/**
	 * Retorna o valor da variável $matricula.
	 *
	 * @return string
	 */
	public function getMatricula() {
		return $this->matricula;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $nivelDiscente
	 *
	 * @param string $nivelDiscente        	
	 */
	public function setNivelDiscente($nivelDiscente) {
		$this->nivelDiscente = $nivelDiscente;
	}
	
	/**
	 * Retorna o valor da variável $nivelDiscente.
	 *
	 * @return string
	 */
	public function getNivelDiscente() {
		return $this->nivelDiscente;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $statusDiscente.
	 *
	 * @param string $statusDiscente        	
	 */
	public function setStatusDiscente($statusDiscente) {
		$this->statusDiscente = $statusDiscente;
	}
	
	/**
	 * Retorna o valor da variável $statusDiscente.
	 *
	 * @return string
	 */
	public function getStatusDiscente() {
		return $this->statusDiscente;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $siape.
	 *
	 * @param string $siape        	
	 */
	public function setSiape($siape) {
		$this->siape = $siape;
	}
	
	/**
	 * Retorna o valor da variável $siape.
	 *
	 * @return string
	 */
	public function getSiape() {
		return $this->siape;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $categoria.
	 *
	 * @param string $categoria        	
	 */
	public function setCategoria($categoria) {
		$this->categoria = $categoria;
	}
	
	/**
	 * Retorna o valor da variável $categoria.
	 *
	 * @return string
	 */
	public function getCategoria() {
		return $this->categoria;
	}
	
	/**
	 * Função utilizada para encapsular o valor da variável $tipoDeUsuario.
	 *
	 * @param string $tipoDeUsuario        	
	 */
	public function setTipoDeUsuario($tipoDeUsuario) {
		$this->tipoDeUsuario = $tipoDeUsuario;
	}
	
	/**
	 * Retorna o valor da variável $tipoDeUsuario.
	 *
	 * @return string
	 */
	public function getTipodeUsuario() {
		return $this->tipoDeUsuario;
	}
	
	/**
	 * Nesta função é feita uma verificação do usuário de acordo com os dados encapsulados,
	 * nela é verifica o tipo de Usuário: Servidor, Aluno, Terceirizado.
	 *
	 * E suas variações: ativo, inativo, etc.
	 *
	 * É retornada um string com todas as informações relativas ao Tipo do Usuário.
	 *
	 * @return string
	 */
	public function strTipo() {
		$usuario = $this;
		$tipo = "";
		if (strtolower ( trim ( $usuario->getTipodeUsuario () ) ) == 'servidor') {
			if (strtolower ( trim ( $usuario->getStatusServidor () ) ) == 'ativo' && strtolower ( trim ( $usuario->getCategoria () ) ) == 'docente') {
				$tipo .= "Servidor Docente";
			} else if (strtolower ( trim ( $usuario->getCategoria () ) ) == 'docente') {
				$tipo .= "Servidor Docente Inativo";
			}
			if (strtolower ( trim ( $usuario->getStatusServidor () ) ) == 'ativo' && strpos ( strtolower ( trim ( $usuario->getCategoria () ) ), 'administrativo' )) {
				$tipo .= "Servidor TAE";
			} else if (strpos ( strtolower ( trim ( $usuario->getCategoria () ) ), 'administrativo' )) {
				$tipo .= "Servidor TAE Inativo";
			}
			$tipo .= '. SIAPE: ' . $usuario->getSiape ();
		}
		
		if (strtolower ( trim ( $usuario->getTipodeUsuario () ) ) == 'aluno') {
			if (strtolower ( trim ( $usuario->getStatusDiscente () ) ) == 'ativo') {
				$tipo .= 'Aluno Ativo ';
			} else {
				$tipo .= 'Aluno Inativo. ';
			}
			echo 'Nivel Discente: ' . $usuario->getNivelDiscente ();
			$tipo .= ' Matricula: ' . $usuario->getMatricula ();
		}
		
		if (strtolower ( trim ( $usuario->getTipodeUsuario () ) ) == 'terceirizado') {
			$tipo .= 'Terceirizado Sem Informação de Status<br>';
		}
		return $tipo;
	}
	
	/**
	 * Retorna o Nivel de Acesso ao Sistema do Usuário, que pode ser:
	 *
	 * 0 - NIVEL_DESLOGADO
	 * 1 - NIVEL_COMUM (Padrão)
	 * 2 - NIVEL_SUPER (Super Admin)
	 * 3 - NIVEL_ADMIN (Admin)
	 * 4 - NIVEL_GUICHE
	 * 5 - NIVEL_POLIVALENTE
	 * 6 - NIVEL_CATRACA_VIRTUAL
	 * 7 - NIVEL_CADASTRO
	 * 8 - NIVEL_RELATORIO
	 * 9 - NIVEL_USUARIO_ESPECIAL
	 *
	 * @return string
	 */
	public function toStrNivel() {
		switch ($this->getNivelAcesso ()) {
			case Sessao::NIVEL_ADMIN :
				$strNivelAcesso = " Administrador";
				break;
			case Sessao::NIVEL_SUPER :
				$strNivelAcesso = "Super Usu&aacute;rio";
				break;
			case Sessao::NIVEL_GUICHE :
				$strNivelAcesso = "Guich&ecirc;";
				break;
			case Sessao::NIVEL_COMUM :
				$strNivelAcesso = "Padr&atilde;o";
				break;
			case Sessao::NIVEL_POLIVALENTE :
				$strNivelAcesso = "Polivalente";
				break;
			default :
				$strNivelAcesso = "Nao Listado: " . $this->getNivelAcesso ();
				break;
		}
		return $strNivelAcesso;
	}
	
	/**
	 * Verifica o Status do Usuário e retorna True, caso o usuário esteja Ativo.
	 *
	 * @return boolean
	 */
	public function verificaSeAtivo() {
		if (strtolower ( trim ( $this->getStatusServidor () ) ) == 'ativo') {
			return true;
		}
		if (strtolower ( trim ( $this->getStatusDiscente () ) ) == 'ativo' || strtolower ( trim ( $this->getStatusDiscente () ) ) == 'formando' || strtolower ( trim ( $this->getStatusDiscente () ) ) == 'ativo - formando' || strtolower ( trim ( $this->getStatusDiscente () ) ) == 'ativo - graduando') {
			return true;
		}
		if (strtolower ( trim ( $this->getTipodeUsuario () ) ) == 'terceirizado' || strtolower ( trim ( $this->getTipodeUsuario () ) ) == 'outros') {
			return true;
		}
		return false;
	}
}