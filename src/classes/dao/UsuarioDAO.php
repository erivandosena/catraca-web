<?php
class UsuarioDAO extends DAO {
	
	
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


        $url = "https://api.unilab.edu.br/api/authenticate";
        
        $data = ['login' =>  $usuario->getLogin(), 'senha' => $usuario->getSenha()];
        

        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($curl);
        curl_close($curl);
        $responseJ = json_decode($response);
		$idUsuario  = 0;
		if(isset($responseJ->id)) {
			$idUsuario = intval($responseJ->id);
		}
		if($idUsuario === 0) {
			return false;
		}
		
		$sql = "SELECT * FROM usuario WHERE id_base_externa = $idUsuario LIMIT 1";
		$usuario->setIdBaseExterna($idUsuario);
		try {
		    $stmt = $this->conexao->prepare($sql);
		    $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $linha ) {
		        $usuario->setLogin ( $linha ['usua_login'] );
		        $usuario->setId ( $linha ['usua_id'] );
		        $usuario->setNivelAcesso ( $linha ['usua_nivel'] );
		        return true;
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
		    return false;
		
		}
		$vinculoDao = new VinculoDAO($this->getConexao());
		$idUsuario = $vinculoDao->verificarUsuario($usuario, $this->getConexao());
		if($idUsuario === 0) {
			return false;
		} else {
			return true;
		}
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
		
		$sql = "SELECT * FROM vw_usuarios_catraca 
                WHERE id_usuario = $id 
                ORDER BY status_discente, status_servidor 
                ASC LIMIT 1";
		
		
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
		
	}
	public function listaPorIdBaseExterna(Usuario $usuario){
	    $lista = array();
	    $id = $usuario->getIdBaseExterna();
	    
	    $sql = "SELECT * FROM vw_usuarios_catraca
                WHERE id_usuario = $id
                ORDER BY status_discente, status_servidor
                ASC LIMIT 100";
	    
	    
	    foreach ($this->getConexao ()->query ( $sql ) as $linha){
	        
	        $usuario = new Usuario();
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
	        $lista[] = $usuario;
	        
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
	
	/**
	 * @deprecated
	 * @param Vinculo $vinculo
	 * @return boolean
	 */
	public function vinculoRenovavel(Vinculo $vinculo){
		$id = $vinculo->getResponsavel()->getIdBaseExterna();
		$sql = "SELECT id_status_discente, id_categoria, id_status_servidor,tipo_usuario, id_tipo_usuario
		FROM vw_usuarios_catraca WHERE id_usuario = $id ORDER BY status_discente, status_servidor ASC LIMIT 10";
		if($vinculo->isAvulso() || $vinculo->getCartao()->getTipo()->getNome() == 'Visitante'){
			return false;
		}
		foreach ($this->getConexao ()->query ( $sql ) as $linha){
			if(strtolower($vinculo->getCartao()->getTipo()->getNome()) == 'aluno'){
				if($linha['id_status_discente'] == self::ID_STATUS_DISCENTE_ATIVO){
					$vinculo->getResponsavel()->setStatusDiscente("Ativo");
					return true;
				}
				if($linha['id_status_discente'] == self::ID_STATUS_DISCENTE_FORMANDO){
					$vinculo->getResponsavel()->setStatusDiscente("Formando");
					return true;
				}
			}
			if((strtolower($vinculo->getCartao()->getTipo()->getNome()) == 'terceirizado') && $linha['id_tipo_usuario'] == self::ID_TIPO_USUARIO_TERCERIZADO){
				return true;
			}
			if((strtolower($vinculo->getCartao()->getTipo()->getNome()) == 'terceirizado') && $linha['id_tipo_usuario'] == self::ID_TIPO_USUARIO_OUTROS){
				return true;
			}
			if(strtolower($vinculo->getCartao()->getTipo()->getNome()) == 'servidor tae'){
				if($linha['id_categoria'] == self::ID_CATEGORIA_TAE && $linha['id_status_servidor'] == self::ID_STATUS_SERVIDOR_ATIVO){
					return true;
				}
			}
			if(strtolower($vinculo->getCartao()->getTipo()->getNome()) == 'servidor docente'){
				if($linha['id_categoria'] == self::ID_CATEGORIA_DOCENTE  && $linha['id_status_servidor'] == self::ID_STATUS_SERVIDOR_ATIVO){
					return true;
				}
			}
		}
		return false;	
	}

	public function preenchePorLogin(Usuario $usuario){
		
		$login = $usuario->getLogin();
		$login = preg_replace ('/[^a-zA-Z0-9\s]/', '', $login);
		$sql = "SELECT * FROM usuario WHERE usua_login = '$login'";
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setId($linha['usua_id']);
			$usuario->setNome($linha['usua_nome']);
			$usuario->setIdBaseExterna($linha['id_base_externa']);
			return true;
		}
		return false;
		
		
	}
	
	public function preenchePorId(Usuario $usuario){
	
		$id = intval($usuario->getId());
		
		$sql = "SELECT * FROM usuario WHERE usua_id = $id";
		foreach($this->getConexao()->query($sql) as $linha){
			$usuario->setNome($linha['usua_nome']);
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