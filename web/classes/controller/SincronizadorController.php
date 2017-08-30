<?php



/**
 * Esse augorítmo precisa ser melhorado. 
 * @author Jefferson Ponte
 *
 */
class SincronizadorController{

	private $daoSigaa;
	private $daoComum;
	private $daoLocal;

	

	
	
	public function sincronizarSigaa(){
		
		$this->daoLocal = new DAO();
		$this->daoSigaa = new DAO(null, DAO::TIPO_USUARIOS);
		
		$this->daoLocal->getConexao()->beginTransaction();
		if(!$this->daoLocal->getConexao()->exec("DELETE FROM vw_usuarios_catraca")){
			$this->daoLocal->getConexao()->rollBack();
			$this->daoSigaa->fechaConexao();
			$this->daoLocal->fechaConexao();
			echo "Erro ao tentar apagar tudo";
			return false;
		}
		$sqlSigaa = "SELECT * FROM vw_usuarios_catraca";
		
		$result = $this->daoSigaa->getConexao()->query($sqlSigaa);
		foreach ($result as $linha){
			foreach($linha as $chave => $valor){
				$linha[$chave] = str_replace("'", "''", $valor);
			}
			$linha['nome'] = "'".$linha['nome']."'";
			$linha['identidade'] = "'".$linha['identidade']."'";
			$linha['passaporte'] = "'".$linha['passaporte']."'";
			$linha['email'] = "'".$linha['email']."'";
			$linha['login'] = "'".$linha['login']."'";
			$linha['senha'] = "'".$linha['senha']."'";
			$linha['nivel_discente'] = "'".$linha['nivel_discente']."'";
			$linha['status_discente'] = "'".$linha['status_discente']."'";
			$linha['status_servidor'] = "'".$linha['status_servidor']."'";
			$linha['tipo_usuario'] = "'".$linha['tipo_usuario']."'";
			$linha['categoria'] = "'".$linha['categoria']."'";
			$linha['turno'] = "'".$linha['turno']."'";
			$linha['nome_curso'] = "'".$linha['nome_curso']."'";
			foreach($linha as $chave => $valor){
				if(!$valor || $valor == "''"){
					$linha[$chave] = "null";
				}
			}
			
			
			$sqlInserir = "INSERT into vw_usuarios_catraca
			(
			id_usuario, nome,identidade, cpf_cnpj, passaporte,email,login,senha,matricula_disc,nivel_discente,id_status_discente,status_discente,siape,id_status_servidor,status_servidor,id_tipo_usuario,tipo_usuario,id_categoria,
			status_sistema,
			categoria,
			id_turno,
			turno,
			id_curso,
			nome_curso
			)
			VALUES(
			".$linha['id_usuario'].",
			".$linha['nome'].",
			".$linha['identidade'].",
			".$linha['cpf_cnpj'].",
			".$linha['passaporte'].",
			".$linha['email'].",
			".$linha['login'].",
			".$linha['senha'].",
			".$linha['matricula_disc'].",
			".$linha['nivel_discente'].",
			".$linha['id_status_discente'].",
			".$linha['status_discente'].",
			".$linha['siape'].",
			".$linha['id_status_servidor'].",
			".$linha['status_servidor'].",
			".$linha['id_tipo_usuario'].",
			".$linha['tipo_usuario'].",
			".$linha['id_categoria'].",
			".$linha['status_sistema'].",
			".$linha['categoria'].",
			".$linha['id_turno'].",
			".$linha['turno'].",
			".$linha['id_curso'].",
			".$linha['nome_curso']."
			);";
			
			if(!$this->daoLocal->getConexao()->exec($sqlInserir)){
				echo "Errei aqui: ".$sqlInserir."<br>";
				$this->daoLocal->getConexao()->rollBack();
				$this->daoSigaa->fechaConexao();
				$this->daoLocal->fechaConexao();
				return false;
			}
			
			
		}
		$this->daoLocal->getConexao()->commit();
		$this->daoSigaa->fechaConexao();
		$this->daoLocal->fechaConexao();
		return true;
	}
	
	public function sincronizarComum(){
	
		$this->daoLocal = new DAO();
		$this->daoLocal->getConexao()->beginTransaction();	
		
		if(!$this->daoLocal->getConexao()->exec("DELETE FROM vw_usuarios_autenticacao_catraca")){
			$this->daoLocal->getConexao()->rollBack();
			echo "Erro ao tentar deletar tudo";
			return false;
		}
		
		$this->daoComum = new DAO(null, DAO::TIPO_AUTENTICACAO);
		$sqlComum = "SELECT * FROM vw_usuarios_autenticacao_catraca";
		$result = $this->daoComum->getConexao()->query($sqlComum);
		$matriz = array();
		foreach ($result as $linha){
			foreach($linha as $chave => $valor){
				$linha[$chave] = str_replace("'", "''", $valor);
			}
			$linha['nome'] = "'".$linha['nome']."'";
			$linha['passaporte'] = "'".$linha['passaporte']."'";
			$linha['email'] = "'".$linha['email']."'";
			$linha['login'] = "'".$linha['login']."'";
			$linha['senha'] = "'".$linha['senha']."'";
			$linha['status_servidor'] = "'".$linha['status_servidor']."'";
			$linha['tipo_usuario'] = "'".$linha['tipo_usuario']."'";
			$linha['categoria'] = "'".$linha['categoria']."'";
			foreach($linha as $chave => $valor){
				if(!$valor || $valor == "''"){
					$linha[$chave] = "null";
				}
			}
			$sqlInserir = "INSERT into vw_usuarios_autenticacao_catraca
			(
			id_usuario,
			nome,
			cpf_cnpj,
			passaporte,
			email,
			login,
			senha,
			siape,
			id_status_servidor,
			status_servidor,
			id_tipo_usuario,
			id_categoria,
			categoria
			)
			VALUES(
			".$linha['id_usuario'].",
			".$linha['nome'].",
			".$linha['cpf_cnpj'].",
			".$linha['passaporte'].",
			".$linha['email'].",
			".$linha['login'].",
			".$linha['senha'].",
			".$linha['siape'].",
			".$linha['id_status_servidor'].",
			".$linha['status_servidor'].",
			".$linha['id_tipo_usuario'].",
			".$linha['id_categoria'].",
			".$linha['categoria']."
		
			
			);";
				
			
			if(!$this->daoLocal->getConexao()->exec($sqlInserir)){
				echo "Errei aqui no Comum: ".$sqlInserir;
				$this->daoLocal->getConexao()->rollBack();
				return false;
			}
			
			
		}
		$this->daoLocal->getConexao()->commit();
		$this->daoLocal->fechaConexao();
		$this->daoComum->fechaConexao();
		return true;
		
	}


	
	public function sincronizar(){
		
		
		if(!file_exists(self::ARQUIVO)){
			mkdir("config");
			$fp = fopen(self::ARQUIVO, "a");
			
			fwrite($fp, "ultima_atualizacao = 2017-04-25 11:35:00");
			fclose($fp);
			return;
		}
			
		$config = parse_ini_file ( self::ARQUIVO );
		$dataDaUltimaAtualizacao = $config ['ultima_atualizacao'];
		$dataDaUltimaAtualizacao = date ( "d/m/Y", strtotime ( $dataDaUltimaAtualizacao ) );
		$hoje = date ( "d/m/Y" );
		if ($dataDaUltimaAtualizacao == $hoje) {
			return;
		}
		if (! is_writable ( self::ARQUIVO )) {
			return;
		}


		if(!$this->sincronizarSigaa()){
			echo 'Errou no sigaa';
			return;
		}
		if(!$this->sincronizarComum()){
			echo "Errou no comum";
			return;
		}
		
		
		$escrever = fopen(self::ARQUIVO, "w");
		
		$hoje = date ( "Y-m-d G:i:s" );
		if(!fwrite($escrever, "ultima_atualizacao = ".$hoje)){
			
			return;
		}
		echo "Feito";
		fclose($escrever);
		
		
	}
	
	const ARQUIVO = "config/copia_base_sigaa.ini";
	
	
	
}
