<?php
class DAO {
	protected $conexao;
	private $tipoDeConexao;
	
	public function DAO($conexao = null, $tipo = self::TIPO_DEFAULT) {
		$this->tipoDeConexao = $tipo;
		if ($conexao != null) {
			$this->conexao = $conexao;
		} else {
			
			$this->fazerConexao();
		}
	}
	public function fazerConexao(){
		switch ($this->tipoDeConexao) {
			case self::TIPO_PG_TESTE :
				$this->conexao = new PDO ( "pgsql:host=10.5.1.8 dbname=unicafe user=unicafe password=unicafe@unilab" );
				break;
			case self::TIPO_PG_SIMULACAO_SIGAA :
				$this->conexao = new PDO ( "pgsql:host=10.5.1.8 dbname=sistemas_comum user=unicafe password=unicafe@unilab" );
				break;
			case self::TIPO_UNICAFE :
				$this->conexao = new UniCafe ();
				break;
			case self::TIPO_SQLITE :
				$this->conexao = new PDO ( 'sqlite:dados/banco.bd' );
				break;
			case self::TIPO_PG_PRODUCAO :
				$this->conexao = new PDO ( "pgsql:host=localhost dbname=unicafe user=unicafe password=unicafe" );
				break;
			case self::TIPO_PG_SIGAA :
				$this->conexao = new PDO ( "pgsql:host=200.129.19.80 dbname=sistemas_comum user=unicafe password=unicafe" );
				break;
			case self::TIPO_PG_CAMILA :
				$this->conexao = new PDO ( "pgsql:host=localhost dbname=unicafe_definitivo user=postgres password=99557722" );
				break;
			default :
				$this->conexao = new PDO ( "pgsql:host=10.5.1.8 dbname=unicafe user=unicafe password=unicafe@unilab" );
				break;
		}
	}
	public function setConexao($conexao) {
		$this->conexao = $conexao;
	}
	public function getConexao() {
		return $this->conexao;
	}
	public function fechaConexao() {
		$this->conexao = null;
	}
	public function getTipoDeConexao(){
		return $this->tipoDeConexao;
	}
	public function setTipoDeConexao($tipo){
		$this->tipoDeConexao = $tipo;
	}
	const TIPO_UNICAFE = 0;
	const TIPO_PG_TESTE = 1;
	const TIPO_DEFAULT = self::TIPO_PG_TESTE;
	const TIPO_SQLITE = 2;
	const TIPO_PG_CAMILA = 3;
	const TIPO_PG_PRODUCAO = 4;
	const TIPO_PG_SIGAA = 5;
	const TIPO_PG_SIMULACAO_SIGAA = 6;
	
}

?>