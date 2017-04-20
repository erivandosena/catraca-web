<?php
/**
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */

class SincronizadorController{
	private $dadosSigaa;
	private $dadosComum;
	private $daoSigaa;
	private $daoComum;
	private $daoLocal;

	

	public function carregarDados(){
		$this->daoSigaa = new DAO(null, DAO::TIPO_PG_SIGAAA);
		$sqlSigaa = "SELECT * FROM vw_usuarios_catraca";
		$result = $this->daoSigaa->getConexao()->query($sqlSigaa);
		$matriz = array();
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
			foreach($linha as $chave => $valor){
				if(!$valor || $valor == "''"){
					$linha[$chave] = "null";
				}
			}
			$matriz[] = $linha;
		}
		$this->dadosSigaa = $matriz;
		$this->daoComum = new DAO(null, DAO::TIPO_PG_SISTEMAS_COMUM);
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
			$matriz[$linha['id_usuario']] = $linha;
		}
		$this->dadosComum = $matriz;
		
	}
	public function deletarDadosLocais(){
		$this->daoLocal = new DAO();
		$this->daoLocal->getConexao()->exec("DELETE FROM vw_usuarios_catraca");
		$this->daoLocal->getConexao()->exec("DELETE FROM vw_usuarios_autenticacao_catraca");	
		
		
	}
	
	public function inserirOsDoSigaa(){
		foreach($this->dadosSigaa as $idUsuario => $linha){
			$sqlInserir = "INSERT into vw_usuarios_catraca
			(
			id_usuario,
			nome,identidade,
			cpf_cnpj,
			passaporte,
			email,
			login,
			senha,
			matricula_disc,
			nivel_discente,
			id_status_discente,
			status_discente,
			siape,
			id_status_servidor,
			status_servidor,
			id_tipo_usuario,
			tipo_usuario,
			id_categoria,
			status_sistema,
			categoria
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
			".$linha['categoria']."
			);";
		
			
			if(!$this->daoLocal->getConexao()->exec($sqlInserir)){
				echo "Errei aqui: ".$sqlInserir."<br>";
				return false;
			}
		}
		$this->dadosSigaa = null;
		return true;
		
	}
	public function inserirOsDoComum(){
		
		foreach($this->dadosComum as $idUsuario => $linha){	
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
				return false;
			}
		}
		return true;
		
	}
	
	public function sincronizar(){

		$tempoA = round(microtime(true) * 1000);
//		echo 'Vou carregar os dados.<br>';
		
		$this->carregarDados();
		$tempoB = round(microtime(true) * 1000);
//		echo "Carreguei! Levei: <br>";
//		echo $tempoB-$tempoA;
//		echo " Mili segundos.<br>";
//		echo '<br>Agora vou deletar os dados da tabela local<br>';
		
		$this->deletarDadosLocais();
//		echo '<br>Pronto! Levei: ';
		
		$tempoC = round(microtime(true) * 1000);
//		echo $tempoC-$tempoB;
//		echo " Milisegundos<br>";
//		echo "Vou inserir os dados do SIGAA na base local";
		
		if($this->inserirOsDoSigaa()){
			echo "";
			//echo '<h1>Deu tudo certo INSERINDO SIGAA</h1>';
			//$tempoD = round(microtime(true) * 1000);
			//echo 'Inseri tudo em: ';
			//echo $tempoD-$tempoC;
			//echo ' Milisegundos';
		}else{
			echo "";
			//echo 'Retornou Um falso';
		}
		if($this->inserirOsDoComum()){
			echo "";
			//echo '<h1>Deu tudo certo INSERINDO COMUM</h1>';
			//$tempoE = round(microtime(true) * 1000);
			//echo 'Inseri tudo em: ';
			//echo $tempoE-$tempoD;
			//echo ' Milisegundos';
		}else{
			echo "";
			//echo 'Retornou Um falso no COmum';
		}
	}
	
	
	
}
