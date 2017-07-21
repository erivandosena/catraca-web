<?php

/**
 * 
 * @author Jefferson Uchôa Ponte
 * 
 * Essa classe sincroniza tabelas de dois bancos de dados distintos. 
 *
 */
class Sincronizador {
	private $conexaoOrigem;
	private $conexaoDestino;
	private $entidadeOrigem;
	private $entidadeDestino;
	private $campos;
	/**
	 * Construtor do Sincronizador
	 *
	 * @param PDO $conexaoOrigem        	
	 * @param PDO $conexaoDestino        	
	 * @param string $entidadeOrigem
	 *        	tabela ou view que terá informações replicadas.
	 * @param string $entidadeDestino
	 *        	tabela que receberá informações da view ou tabela de origem.
	 */
	public function __construct(PDO $conexaoOrigem, PDO $conexaoDestino, $entidadeOrigem, $entidadeDestino) {
		$this->conexaoOrigem = $conexaoOrigem;
		$this->conexaoDestino = $conexaoDestino;
		$this->entidadeOrigem = $entidadeOrigem;
		$this->entidadeDestino = $entidadeDestino;
		$campos = array ();
	}
	/**
	 * Adiciona um campo a ser replicado
	 *
	 * @param string $campoOrigem
	 *        	campo da tabela ou view de origem que vai corresponder a um campo da tabela de destino.
	 * @param string $campoDestino
	 *        	campo da tabela de destino que vai corresponder a um campo da tabela ou view de origem.
	 */
	public function addCampo($campoOrigem, $campoDestino) {
		$this->campos [$campoOrigem] = $campoDestino;
	}
	/**
	 * Atribui o vetor de campos que serão sincronizados.
	 * O vetor será indexado com os campos da entidade
	 * de origem e os valores serão os campos da entidade de destino.
	 *
	 * @param array $campos        	
	 */
	public function setCampos($campos) {
		$this->campos = $campos;
	}
	
	/**
	 * Metodo que faz uso da classe.
	 */
	public static function main() {
		if (self::jaTenteiAtualizar ()) {
			return;
		}
		$daoUsuarios = new DAO ( null, DAO::TIPO_USUARIOS );
		$entidadeOrigem = $daoUsuarios->getEntidadeUsuarios ();
		$conexaoOrigem = $daoUsuarios->getConexao ();
		$dao = new DAO ();
		$conexaoDestino = $dao->getConexao ();
		
		$entidadeDestino = "vw_usuarios_catraca";
		$sincronizador = new Sincronizador ( $conexaoOrigem, $conexaoDestino, $entidadeOrigem, $entidadeDestino );
		
		$campos = [ 
				"cpf" => "id_usuario",
				"NOME" => "nome",
				"categoria" => "categoria",
				"tipo_usuario" => "tipo_usuario",
				"identidade" => "identidade",
				"status_discente" => "status_discente",
				"id_status_discente" => "id_status_discente" 
		]
		;
		$sincronizador->setCampos ( $campos );
		$sincronizador->sincronizar ();
		
		echo "<br><hr>";
		$campos = array ();
		$campos = [ 
				"cpf" => "id_usuario",
				"NOME" => "nome",
				"email" => "email" 
		]
		;
		$entidadeDestino = "vw_usuarios_autenticacao_catraca";
		$sincronizador = new Sincronizador ( $conexaoOrigem, $conexaoDestino, $entidadeOrigem, $entidadeDestino );
		$sincronizador->setCampos ( $campos );
		$sincronizador->sincronizar ();
	}
	/**
	 * Executa sincronização.
	 */
	public function sincronizar() {
		$this->conexaoDestino->beginTransaction ();
		$sqlDelete = "DELETE FROM " . $this->entidadeDestino;
		$b = $this->conexaoDestino->exec ( $sqlDelete );
		echo "Excluido " . $b . " linhas da entidade de destino<br>";
		$sql = "SELECT * FROM " . $this->entidadeOrigem;
		$result = $this->conexaoOrigem->query ( $sql );
		foreach ( $result as $linha ) {
			
			$sql = "INSERT INTO " . $this->entidadeDestino . " (";
			$i = 0;
			foreach ( $this->campos as $chave => $valor ) {
				$i ++;
				if ($i != count ( $this->campos )) {
					$sql .= $valor . ", ";
				}
			}
			$sql .= $valor . ") VALUES(";
			$i = 0;
			foreach ( $this->campos as $chave => $valor ) {
				$i ++;
				if ($linha [$chave] == null || $linha [$chave] == '') {
					$sql .= "null";
				} else {
					$sql .= ":" . $valor;
				}
				
				if ($i != count ( $this->campos )) {
					$sql .= ", ";
				}
			}
			$sql .= "); ";
			
			try {
				$stmt = $this->conexaoDestino->prepare ( $sql );
				$h = 0;
				foreach ( $this->campos as $chave => $valor ) {
					$$valor = $linha [$chave];
					$conteudo = $linha [$chave];
					
					if ($valor == "id_usuario" || $valor == "id_status_discente") {
						$$valor = intval ( $$valor );
					}
					if (is_string ( $conteudo )) {
						
						$$valor = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $$valor );
						$stmt->bindParam ( $valor, $$valor, PDO::PARAM_STR );
					} else if (is_int ( $conteudo )) {
						$stmt->bindParam ( $valor, $$valor, PDO::PARAM_INT );
					} else if (is_bool ( $conteudo )) {
						$$valor = intval ( $$valor );
						$stmt->bindParam ( $valor, $$valor, PDO::PARAM_INT );
					}
				}
				
				if (! $stmt->execute ()) {
					$this->conexaoDestino->rollBack ();
					return;
				}
			} catch ( PDOException $e ) {
				echo '{"error":{"text":' . $e->getMessage () . '}}';
			}
		}
		$this->conexaoDestino->commit ();
		return;
	}
	public static function jaTenteiAtualizar() {
		if (! file_exists ( self::ARQUIVO )) {
			$fp = fopen ( self::ARQUIVO, "a" );
			fwrite ( $fp, "ultima_atualizacao = 2017-04-25 11:35:00" );
			fclose ( $fp );
		}
		$config = parse_ini_file ( self::ARQUIVO );
		$dataDaUltimaAtualizacao = $config ['ultima_atualizacao'];
		$hoje = date ( "Y-m-d G:i:s" );
		if ($dataDaUltimaAtualizacao == $hoje) {
			return true;
		}
		if (! is_writable ( self::ARQUIVO )) {
			return true;
		}
		$escrever = fopen ( self::ARQUIVO, "w" );
		
		$hoje = date ( "Y-m-d G:i:s" );
		if (! fwrite ( $escrever, "ultima_atualizacao = " . $hoje )) {
			return true;
		}
		fclose ( $escrever );
		return false;
	}
	const ARQUIVO = "/dados/sites/adm/catraca/config/ultima_sincronizacao.ini";
}

?>