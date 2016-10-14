<?php

/**
 * 
 * @author Jefferson Uchoa Ponte
 * 
 * Como usar
 * Para começar a usar chame o metodo estático da seguinte forma: 
 * 
 * Auditoria::criarTabela(new PDO("pgsql:host=localhost dbname=nome_do_banco user=usuario_do_banco password=senhaDoBanco"));
 * 
 * Após a tabela criada
 * Inclua a classe auditoria no arquivo PHP da pagina que deseja auditar. 
 * 
 * $auditoria1 = new Auditoria(new PDO("pgsql:host=localhost dbname=nome_do_banco user=usuario_do_banco password=senhaDoBanco"));
 * 
 * $auditoria1->cadastrar(12);//Ou $auditoria1->cadastrar(12, "Alterando tabela endereco");
 */
class Auditoria {
	private $conexao;
	public function Auditoria(PDO $conexao = NULL) {
		if ($conexao != null) {
			$this->conexao = $conexao;
		} else {
			$this->conexao = new PDO ( "pgsql:host=localhost dbname=nome_do_banco user=usuario_do_banco password=senhaDoBanco" );
		}
	}
	public function cadastrar($idDoUsuario, $obs = "-") {
		$url = $_SERVER ['REQUEST_URI'];
		$idDoUsuario = intval ( $idDoUsuario );
		$data = date ( "Y-m-d H:i:s" );
		$sql = "INSERT INTO auditoria(audi_pagina, audi_data, usua_id, audi_observacao) VALUES('$url', '$data', $idDoUsuario, '$obs');";
		$this->conexao->exec ( $sql );
	}
	/**
	 * Caso queira criar a tabela no banco local passe uma conexão PDO.
	 *
	 * @param PDO $conexao        	
	 */
	public static function criarTabela(PDO $conexao) {
		$conexao->exec ( "CREATE TABLE auditoria(audi_id serial NOT NULL,
				audi_pagina character varying(200),audi_data timestamp without time zone,  
				usua_id integer,  audi_observacao character varying(200),  CONSTRAINT auditoria_pkey PRIMARY KEY (audi_id));" );
	}
	public static function mostrar(PDO $conexao) {
		$sql = "SELECT * FROM auditoria 
				INNER JOIN usuario 
				ON auditoria.usua_id = usuario.usua_id 
				ORDER BY audi_id DESC LIMIT 3000";
		$result = $conexao->query ( $sql );
		foreach ( $result as $linha ) {
			echo $linha ['audi_id'] . ' - ' . $linha ['usua_nome'] . ' - ' . $linha ['audi_pagina'] . ' - ' . date ( "d/m/Y H:i:s", strtotime ( $linha ['audi_data'] ) );
			if ($linha ['usua_nivel'] > 1)
				echo ' <b> ' . $linha ['usua_nivel'] . '</b>';
			else
				echo ' Comum';
			echo '<hr>';
		}
	}
}

?>