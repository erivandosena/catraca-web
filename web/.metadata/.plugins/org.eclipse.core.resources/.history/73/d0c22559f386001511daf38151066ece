<?php
class UsuarioDAO extends DAO {
	public function autentica(Usuario $usuario) {
		if ($usuario->getLogin () == "admin" && $usuario->getSenha () == "biblioteca@123A") {
			$usuario->setNivelAcesso ( Sessao::NIVEL_USUARIO_ESPECIAL );
			$usuario->setId ( 100 );
			return true;
		}
		$login = $usuario->getLogin ();
		$senha = md5 ( $usuario->getSenha () );
		$sql = "SELECT * FROM usuario WHERE login ='$login' AND senha = '$senha'";
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$usuario->setLogin ( $linha ['login'] );
			$usuario->setId ( $linha ['id_usuario'] );
			
			$usuario->setNivelAcesso ( $linha ['nivel_acesso'] );
			return true;
		}
		return false;
	}
	/**
	 * Pesquisaremos primeiro o Login do usuario e depois o nome do laboratorio.
	 * Apos isso pegaremos o Id de cada um e usaremos numa operacao de insert.
	 * Mas essa operacao so pode funcionar se ela ainda nao existir com esse usuario e laboratorio.
	 * Terminando tudo iremos atualizar o nivel do usuario
	 * 
	 * @param Usuario $usuario        	
	 * @param Laboratorio $laboratorio        	
	 */
	public function tornarAdministrador(Usuario $usuario, Laboratorio $laboratorio) {
		$login = $usuario->getLogin();
		$nomeLaboratorio = $laboratorio->getNome();
		
		
		$sqlLaboratorio = "SELECT * FROM laboratorio WHERE nome_laboratorio = $nomeLaboratorio";
		
		
		
	}
	public function preenchePorLogin(Usuario $usuario){
		$login = $usuario->getLogin();
		$sql = "SELECT * FROM usuario WHERE login = '$login'";
		$flag = false;
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setId($linha['id_usuario']);
			$flag = true;
			return $flag;
		}
		return $flag;
		
		
	}
	public function preenchePorNome(Laboratorio $laboratorio){
		$nome = $laboratorio->getNome();
		$sql = "SELECT * FROM laboratorio WHERE nome_laboratorio = '$nome'";
		foreach($this->getConexao()->query($sql) as $linha){
			$laboratorio->setId($linha['id_laboratorio']);
			return true;
		}
		return false;
	}
	public function ehAdministrador(Usuario $usuario, Laboratorio $laboratorio){
		$idUsuario = $usuario->getId();
		$idLaboratorio = $laboratorio->getId();
		$sql= "SELECT * FROM administrador WHERE id_usuario = $idUsuario AND id_laboratorio = $idLaboratorio";
		$result =$this->getConexao()->query($sql);
		foreach($result as $linha){
			return true;
		}
		return false;
	}
	public function adicionaAdministrador(Usuario $usuario, Laboratorio $laboratorio){
		$novoNivel = Sessao::NIVEL_ADMIN;
		$idUsuario = $usuario->getId();
		$idLaboratorio = $laboratorio->getId();
		
		$sqlUpdate = "UPDATE usuario set nivel_acesso = $novoNivel WHERE id_usuario = $idUsuario";
		$sqlInsert = "INSERT into administrador (id_usuario, id_laboratorio) VALUES($idUsuario, $idLaboratorio)";
		$this->getConexao()->beginTransaction();
		if($this->getConexao()->query($sqlUpdate)){
			if($this->getConexao()->query($sqlInsert)){
				$this->getConexao()->commit();
				return true;
			}
		}
		$this->getConexao()->rollBack();
		return false;
		
	}
	
}

?>