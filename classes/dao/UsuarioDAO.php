<?php
/*********
  * Copyright (c) 12/07/2017 {INITIAL COPYRIGHT UNILAB} {OTHER COPYRIGHT LABPATI/DISUP/DTI}.
  * All rights reserved. This program and the accompanying materials
  * are made available under the terms of the Eclipse Public License v1.0
  * which accompanies this distribution, and is available at
  * http://www.eclipse.org/legal/epl-v10.html
  *
  * Contributors:
  *    Jefferson Uchôa Ponte - initial API and implementation and/or initial documentation
  *********/

class UsuarioDAO extends DAO {
	

	
	public function loginExisteLdap($login, $config) {
		
		
		$ldap_server = $config['servidor'].":".$config['porta'];
		$auth_user = $config['usuario_consulta'].'@'.$config['dominio'];
		$auth_pass = $config['senha'];
		$base_dn = $config['base_dn'];
		$campo_filtro = $config['campo_filtro'];
		// Tenta se conectar com o servidor
		if (! ($connect = @ldap_connect ( $ldap_server ))) {
			return FALSE;
		}
		// Tenta autenticar no servidor
		if (! ($bind = @ldap_bind ( $connect, $auth_user, $auth_pass ))) {
			return FALSE;
		} else {
			$result = ldap_search($connect,$base_dn, "($campo_filtro=$login)") or die ("Error in search query: ".ldap_error($connect));
			$data = ldap_get_entries($connect, $result);
			
			if(!isset($data[0]['employeenumber'])){
				return false;
			}
			if($data[0]['employeenumber'][0]){
				return true;
			}
			return false;
		}
		
	}
	public function logarLdap(Usuario $usuario, $config){
		$ldap_server = $config['servidor'].":".$config['porta'];
		$auth_user = $usuario->getLogin().'@'.$config['dominio'];
		$auth_pass = $usuario->getSenha();
		$login = $usuario->getLogin();
		$base_dn =  $config['base_dn'];
		$campo_filtro = $config['campo_filtro'];
		
		if($auth_pass == ""){
			return false;
		}
		
		// Tenta se conectar com o servidor
		if (! ($connect = @ldap_connect ( $ldap_server ))) {
			return FALSE;
		}
		// Tenta autenticar no servidor
		if (! ($bind = @ldap_bind ( $connect, $auth_user, $auth_pass ))) {
			return FALSE;
		} else {
			$result = ldap_search($connect,$base_dn, "($campo_filtro=$login)") or die ("Error in search query: ".ldap_error($connect));
			$data = ldap_get_entries($connect, $result);
						
			if(!isset($data[0]['employeenumber'])){
				return false;
			}
			if(!isset($data[0]['employeenumber'][0])){
				return false;
			}
			$usuario->setIdBaseExterna($data[0]['employeenumber'][0]);
			$usuario->setCpf($data[0]['employeenumber'][0]);
			return true;
		}
	}
	
	
	/**
	 * Vamos autenticar usando LDAP. 
	 * Caso usuáservidor = 200.129.22.43
porta = 3268 
dominio = testes.funece.br
usuario_consulta = consulta.base
senha = AlguemSabe@senha7
campo_filtro = sAMAccountName
base_dn = "dc=testes,dc=funece,dc=br"rio exista, nós pegamos seu CPF no LDAP e o buscamos na tabela usuário. Para posterior criação da sessão. 
	 * Caso não exista na tabela usuario, significa que é o primeiro login, copiamos da tabela cash. Vw_usuarios_catraca com nivel de acesso padrao. 
	 * Caso nem exista na tabela vw_usuarios_catraca, significa uma inconsistência e retornemos falso, login não poderá ser feito.  
	 * 
	 * @param Usuario $usuario
	 * 
	 */
	const ARQUIVO_LDAP_CONFIG =  "/dados/config/catraca_ldap.ini";
	
	public function autenticaLdap(Usuario $usuario){
		$config_ldap = parse_ini_file (self::ARQUIVO_LDAP_CONFIG);
	
		if(!$this->loginExisteLdap($usuario->getLogin(), $config_ldap)){
			return false;
		}
		
		if(!$this->logarLdap($usuario, $config_ldap)){
			return false;
		}
		$loginVelho = $usuario->getLogin();
		if($this->preenchePorIdBaseExterna($usuario)){
			return true;
		}
		// Se vier pra ca significa que usuario nao existe na tabela usuario. 
		//Vamos buscar na tabela cash e inserir com nivel default, sem login e sem senha. 
		
		$this->retornaPorIdBaseExterna($usuario);
		
		$usuario->setNivelAcesso(Sessao::NIVEL_COMUM);
		$nome = $usuario->getNome();
		$email = $usuario->getEmail();
		$nivel = $usuario->getNivelAcesso();
		$usuario->setLogin($loginVelho);
		
		$idBaseExterna = $usuario->getIdBaseExterna();
		$sqlInsert = "INSERT into usuario(usua_nome, usua_login,usua_email, usua_nivel, id_base_externa)
				VALUES	('$nome', '$loginVelho','$email', $nivel, $idBaseExterna)";

		$inseriu = false;
		if($this->getConexao()->exec($sqlInsert)){
			$inseriu = true;
		}
		if($this->getConexao()->lastInsertId() == 1){
			$nivelAdm = Sessao::NIVEL_ADMIN;
			$this->getConexao()->exec("UPDATE usuario set usua_nivel = 1 WHERE usua_id = $nivelAdm;");
		}
		return $inseriu;
	}
	
	/**
	 * Vamos verificar dois bancos. 
	 * Primeiro no Banco Local. Se ele n�o existir olhamos no SIG. 
	 * Se existir no SIG copiamos para o local com n�vel Default. 
	 * @param Usuario $usuario
	 * @return boolean
	 */
	public function autentica(Usuario $usuario) {
		
		/*
		 * Primeiro vou verificar no banco local . 
		 * Deu certo?
		 * Define nivel na session e deixa o cara logado. 
		 * 
		 */
		
		
		$login = $usuario->getLogin();
		$senha = md5 ( $usuario->getSenha() );
		$sql = "SELECT * FROM usuario WHERE usua_login ='$login' AND usua_senha = '$senha' LIMIT 1";
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$usuario->setLogin ( $linha ['usua_login'] );
			$usuario->setId ( $linha ['usua_id'] );
			$usuario->setNivelAcesso ( $linha ['usua_nivel'] );
			
			return true;
		}
		//N�o deu. 
		//Vou verificar na base do SIG. 
		$result2 = 	$this->getConexao()->query("SELECT login, senha, id_usuario FROM vw_usuarios_autenticacao_catraca WHERE LOWER(login) = LOWER('$login') AND senha = '$senha' LIMIT 1");
		foreach($result2 as $linha){
			
			//Se eu to procurando aqui � pq houve algo errado no banco local. 
			//2 n�o tinha. -- nesse caso fazemos um insert. 
			//Vamos verificar isso agora. 
			//Existe esse login?
			
			$idBaseExterna = $linha['id_usuario'];
			//1 Minha senha est� desatualizada no local. -- Nesse caso fazemos update na senha e tentamos autenticar de novo com o Nivel que tenho.
			$result3 = $this->getConexao()->query("SELECT usua_id, usua_login, usua_senha, id_base_externa FROM usuario WHERE id_base_externa = $idBaseExterna LIMIT 1");
			foreach($result3 as $outraLinha){
				//Vamos atualizar sua senha, meu filho. 
				
				$this->getConexao()->query("UPDATE usuario set usua_senha = '$senha', set usua_login = '$login' WHERE id_base_externa = $idBaseExterna");
				//Caso isso aconteceu, podemos logar de novo. Mesmo augoritimo de antes.  Fa�amos recursividade? N�o, � meio arriscado, Vamos repetir mesmo. 
				foreach ( $this->getConexao ()->query ( $sql ) as $linha2 ) {
					$usuario->setLogin ( $linha2 ['usua_login'] );
					$usuario->setId ( $linha2 ['usua_id'] );
					$usuario->setNivelAcesso ( $linha2 ['usua_nivel'] );
					return true;
				}
				
			}
			//Vish, o cara n�o existia na base local. O que faremos? 
			//Num tem pobrema! Nois adiciona! N�is rai farr� um incerte. 		
			$nivel = Sessao::NIVEL_COMUM;
			$nome = $linha['nome'];
			$email = $linha['email'];
			
			$this->getConexao()->query("INSERT into usuario(usua_login,usua_senha, usua_nome,usua_email, usua_nivel, id_base_externa) 
										VALUES	('$login', '$senha', '$nome','$email', $nivel, $idBaseExterna)");
			$usuario->setNivelAcesso ( $nivel);
			return true;
			
		}
		 
		
		
		return false;
	}

	public function pesquisaNoSigaa($pesquisa){
		$lista = array();
		$pesquisa = strtoupper ( $pesquisa );
		$pesquisa = "%".$pesquisa."%";
		
		$sql = "SELECT * FROM vw_usuarios_catraca WHERE 
				TRANSLATE(UPPER(nome), 'áéíóúàèìòùãõâêîôôäëïöüçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜÇ','aeiouaeiouaoaeiooaeioucAEIOUAEIOUAOAEIOOAEIOUC')
				LIKE TRANSLATE(:pesquisa, 'áéíóúàèìòùãõâêîôôäëïöüçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜÇ','aeiouaeiouaoaeiooaeioucAEIOUAEIOUAOAEIOOAEIOUC') LIMIT 150";

		try{
			$stmt = $this->getConexao()->prepare($sql);
			$stmt->bindParam(":pesquisa", $pesquisa, PDO::PARAM_STR);
			$stmt->execute();
			$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
			
		}catch (PDOException $e){
			echo '{"erro":{"text":'. $e->getMessage() .'}}';
		}
		foreach($result as $linha){
			$usuario = new Usuario();
			$usuario->setNome($linha['nome']);
			$usuario->setEmail($linha['email']);
			$usuario->setLogin($linha['login']);
			$usuario->setIdBaseExterna($linha['id_usuario']);
			$usuario->setCpf($linha['cpf_cnpj']);
			$usuario->setIdentidade($linha['identidade']);
			$usuario->setPassaporte($linha['passaporte']);
			$usuario->setSiape($linha['siape']);
			$usuario->setTipoDeUsuario($linha['tipo_usuario']);
			$usuario->setMatricula($linha['matricula_disc']);
			$usuario->setStatusDiscente($linha['status_discente']);
			$usuario->setNivelDiscente($linha['nivel_discente']);
			$usuario->setCategoria($linha['categoria']);
			$usuario->setStatusServidor($linha['status_servidor']);
			$lista[] = $usuario;
		}
		
		return $lista;
		
	}
	public function pesquisaTesteNoSigaa($pesquisa){
		$lista = array();
		$pesquisa = strtoupper ( $pesquisa );
		$pesquisa = "%".$pesquisa."%";
		
		$sql = "SELECT * FROM vw_usuarios_catraca WHERE 
				TRANSLATE(UPPER(nome), 'áéíóúàèìòùãõâêîôôäëïöüçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜÇ','aeiouaeiouaoaeiooaeioucAEIOUAEIOUAOAEIOOAEIOUC')
				LIKE TRANSLATE(:pesquisa, 'áéíóúàèìòùãõâêîôôäëïöüçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜÇ','aeiouaeiouaoaeiooaeioucAEIOUAEIOUAOAEIOOAEIOUC') LIMIT 150";

		try{
			$stmt = $this->getConexao()->prepare($sql);
			$stmt->bindParam(":pesquisa", $pesquisa, PDO::PARAM_STR);
			$stmt->execute();
			$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
			
		}catch (PDOException $e){
			echo '{"erro":{"text":'. $e->getMessage() .'}}';
		}
		foreach($result as $linha){
			$usuario = new Usuario();
			$usuario->setNome($linha['nome']);
			$usuario->setEmail($linha['email']);
			$usuario->setLogin($linha['login']);
			$usuario->setIdBaseExterna($linha['id_usuario']);
			$usuario->setCpf($linha['cpf_cnpj']);
			$usuario->setIdentidade($linha['identidade']);
			$usuario->setPassaporte($linha['passaporte']);
			$usuario->setSiape($linha['siape']);
			$usuario->setTipoDeUsuario($linha['tipo_usuario']);
			$usuario->setMatricula($linha['matricula_disc']);
			$usuario->setStatusDiscente($linha['status_discente']);
			$usuario->setNivelDiscente($linha['nivel_discente']);
			$usuario->setCategoria($linha['categoria']);
			$usuario->setStatusServidor($linha['status_servidor']);
			$lista[] = $usuario;
		}
	
		return $lista;
		
	
	}
	public function retornaPorIdBaseExterna(Usuario $usuario){
		$id = $usuario->getIdBaseExterna();
		$sql = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $id ORDER BY status_discente, status_servidor ASC LIMIT 1";
		
		foreach ($this->getConexao ()->query ( $sql ) as $linha){
			$usuario->setNome($linha['nome']);
			$usuario->setEmail($linha['email']);
			$usuario->setLogin($linha['login']);
			$usuario->setCpf($linha['cpf_cnpj']);
			$usuario->setIdBaseExterna($linha['id_usuario']);
			$usuario->setIdentidade($linha['identidade']);
			$usuario->setPassaporte($linha['passaporte']);
			$usuario->setTipoDeUsuario($linha['tipo_usuario']);
			$usuario->setMatricula($linha['matricula_disc']);
			$usuario->setStatusDiscente($linha['status_discente']);
			$usuario->setIdStatusDiscente($linha['id_status_discente']);
			$usuario->setNivelDiscente($linha['nivel_discente']);
			$usuario->setCategoria($linha['categoria']);
			$usuario->setIDCategoria($linha['id_categoria']);
			$usuario->setSiape($linha['siape']);
			$usuario->setStatusServidor($linha['status_servidor']);
			return $usuario;
			
		}
		return false;
		
	}
	

	/**
	 * @param Usuario $usuario
	 * @return array:Usuario
	 */
	public function retornaListaPorIdBaseExterna(Usuario $usuario){
		$lista = array();
		$id = $usuario->getIdBaseExterna();
		$sql = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $id ORDER BY status_discente, status_servidor ASC LIMIT 15";
	
		foreach ($this->getConexao ()->query ( $sql ) as $linha){
			$usuarioLista = new Usuario();
			
			$usuarioLista->setNome($linha['nome']);
			$usuarioLista->setEmail($linha['email']);
			$usuarioLista->setLogin($linha['login']);
			$usuarioLista->setCpf($linha['cpf_cnpj']);
			$usuarioLista->setIdBaseExterna($linha['id_usuario']);
			$usuarioLista->setIdentidade($linha['identidade']);
			$usuarioLista->setPassaporte($linha['passaporte']);
			$usuarioLista->setStatusSistema($linha['status_sistema']);
			$usuarioLista->setIdTipoUsuario($linha['id_tipo_usuario']);
			$usuarioLista->setTipoDeUsuario($linha['tipo_usuario']);
			$usuarioLista->setMatricula($linha['matricula_disc']);
			$usuarioLista->setStatusDiscente($linha['status_discente']);
			$usuarioLista->setIdStatusDiscente($linha['id_status_discente']);
			$usuarioLista->setNivelDiscente($linha['nivel_discente']);
			$usuarioLista->setCategoria($linha['categoria']);
			$usuarioLista->setIDCategoria($linha['id_categoria']);
			$usuarioLista->setSiape($linha['siape']);
			$usuarioLista->setIdStatusServidor($linha['id_status_servidor']);
			$usuarioLista->setStatusServidor($linha['status_servidor']);
			
			//Vamos deixar o usuário passado por parametro editado também. 
			$usuario->setNome($linha['nome']);
			$usuario->setEmail($linha['email']);
			$usuario->setLogin($linha['login']);
			$usuario->setCpf($linha['cpf_cnpj']);
			$usuario->setIdBaseExterna($linha['id_usuario']);
			$usuario->setIdentidade($linha['identidade']);
			$usuario->setPassaporte($linha['passaporte']);
			$usuario->setTipoDeUsuario($linha['tipo_usuario']);
			$usuario->setMatricula($linha['matricula_disc']);
			$usuario->setStatusDiscente($linha['status_discente']);
			$usuario->setIdStatusDiscente($linha['id_status_discente']);
			$usuario->setNivelDiscente($linha['nivel_discente']);
			$usuario->setCategoria($linha['categoria']);
			$usuario->setIDCategoria($linha['id_categoria']);
			$usuario->setSiape($linha['siape']);
			$usuario->setIdStatusServidor($linha['id_status_servidor']);
			$usuario->setStatusServidor($linha['status_servidor']);
			
			$lista[] = $usuarioLista;
		}
		return $lista;
	
	}
	
	const ID_STATUS_DISCENTE_ATIVO = 1;
	const ID_STATUS_DISCENTE_CADASTRADO = 3;
	const ID_STATUS_DISCENTE_FORMANDO = 8;
	const ID_STATUS_DISCENTE_FORMADO = 9;
	const ID_STATUS_DISCENTE_CONCLUIDO = 3;
	const ID_TIPO_USUARIO_TERCERIZADO = 12;
	const ID_TIPO_USUARIO_OUTROS = 4;
	const ID_CATEGORIA_DOCENTE = 1;
	const ID_CATEGORIA_TAE = 2;
	const ID_STATUS_SERVIDOR_ATIVO = 1;
	
	

	public function preenchePorLogin(Usuario $usuario){
		
		$login = $usuario->getLogin();
		$sql = "SELECT * FROM usuario WHERE usua_login = '$login'";
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setId($linha['usua_id']);
			$usuario->setNome($linha['usua_nome']);
			return true;
		}
		return false;
		
	}
	public function preenchePorId(Usuario $usuario){
	
		$id = intval($usuario->getId());
		
		$sql = "SELECT * FROM usuario WHERE usua_id = $id";
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setNome($linha['usua_nome']);
			$usuario->setNivelAcesso($linha['usua_nivel']);
			$usuario->setIdBaseExterna($linha['id_base_externa']);
			return true;
		}
		return false;
	
	
	}
	/**
	 * Diferente do outro este está preparado para olhar na base própria
	 * @param Usuario $usuario
	 */
	public function preenchePorIdBaseExterna(Usuario $usuario){	
		$id = $usuario->getIdBaseExterna();
		$sql = "SELECT * FROM usuario WHERE id_base_externa  = $id";
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setId($linha['usua_id']);
			$usuario->setNome($linha['usua_nome']);
			$usuario->setNivelAcesso($linha['usua_nivel']);
			return true;
		}
		return false;
	
	
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
	/**
	 * Passe o usuario com id da base externa. 
	 * @param Usuario $usuario
	 */
	public function alteraNivelDeAcesso(Usuario $usuario){
		
		$idBaseExterna = $usuario->getIdBaseExterna();
		$novoNivel = $usuario->getNivelAcesso();
		$update = "UPDATE usuario set usua_nivel = $novoNivel WHERE id_base_externa = $idBaseExterna";
		return $this->getConexao()->exec($update);
		
		
	}
	
	
}

?>