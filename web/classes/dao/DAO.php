 <?php
/**
 * Classe utilizada para conxão com o Bando de Dados.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */
/**
 */
/*
 * Esse era producao
 * Descomente esta e comente a de baixo para colocar em produção.
 */
class DAO {
	
	/**
	 * Recebe uma conexao do tipo PDO
	 *
	 * @var PDO $conexao
	 */
	protected $conexao;
	
	/**
	 * Variável utilizada para rececer o tipo de conexão com o Banco.
	 *
	 * @var string
	 */
	private $tipoDeConexao;
	
	/**
	 * Função construtora da Classe DAO, caso não seja definido o Tipo de conexão
	 * o tipo definido como Default será utilizado.
	 *
	 * @param PDO $conexao
	 *        	PDO é uma classe desenvolvida especificamente para trabalhar com procedimentos relacionados a Banco de Dados.
	 *        	O interessante em utilizar este tipo de classe é a abstração de qual banco utilizamos e a segurança extra que esta classe nos oferece.
	 * @param int $tipo
	 *        	A variável $tipo irá especificar qual tipo de Banco será utilizada, caso não seja especificado o Banco Default será utilizado.
	 */
	public function DAO($conexao = null, $tipo = self::TIPO_DEFAULT) {
		$this->tipoDeConexao = $tipo;
		if ($conexao != null) {
			$this->conexao = $conexao;
		} else {
			$this->fazerConexao ();
		}
	}
	
	/**
	 * Realiza a conexão com o Banco, de acordo com o tipo de conexão especificado no contrutor da classe.
	 */
	public function fazerConexao() {
		switch ($this->tipoDeConexao) {
			case self::TIPO_PG_DESENVOLVIMENTO :
				$this->conexao = new PDO ( "pgsql:host=localhost dbname=homologacao user=catraca password=CaTraCa@unilab2015" );
				break;
			case self::TIPO_PG_PRODUCAO_LOCAL :
				$this->conexao = new PDO ( "pgsql:host=localhost dbname=homologacao user=catraca password=CaTraCa@unilab2015" );
				// $this->conexao = new PDO ( "pgsql:host=localhost dbname=treinamento user=catraca password=CaTraCa@unilab2015" );
				break;
			case self::TIPO_PG_PRODUCAO_BAHIA :
				$this->conexao = new PDO ( "pgsql:host=200.128.19.11 dbname=producao user=catraca password=CaTraCa@unilab2015" );
				break;
			case self::TIPO_PG_SIGAAA : // Produ��o do SIG.
				$this->conexao = new PDO ( "pgsql:host=200.129.19.80 dbname=sigaa user=catraca password=c4Tr@3a" );
				break;
			case self::TIPO_PG_SISTEMAS_COMUM : // Produ��o do SIG.
				$this->conexao = new PDO ( "pgsql:host=200.129.19.80 dbname=sistemas_comum user=catraca password=c4Tr@3a" );
				break;
			default :
				$this->conexao = new PDO ( "pgsql:host=localhost dbname=desenvolvimento user=catraca password=CaTraCa@unilab2015" );
				break;
		}
	}
	
	/**
	 *
	 * @ignore
	 *
	 * @param unknown $conexao        	
	 */
	public function setConexao($conexao) {
		$this->conexao = $conexao;
	}
	
	/**
	 * Função que estabelece uma conexão com o Banco,
	 * utilizada para fazer acessos ao Banco através de Select, Insert, Update e Delete.
	 */
	public function getConexao() {
		return $this->conexao;
	}
	
	/**
	 * Classe utilizada para fechar a conexão com o Banco.
	 */
	public function fechaConexao() {
		$this->conexao = null;
	}
	
	/**
	 * @ignore
	 *
	 * @return unknown
	 */
	public function getTipoDeConexao() {
		return $this->tipoDeConexao;
	}
	
	/**
	 * @ignore
	 *
	 * @param unknown $tipo        	
	 */
	public function setTipoDeConexao($tipo) {
		$this->tipoDeConexao = $tipo;
	}
	const TIPO_PG_SIGAAA = 4;
	const TIPO_PG_SISTEMAS_COMUM = 6;
	const TIPO_PG_PRODUCAO_LOCAL = 7;
	const TIPO_PG_DESENVOLVIMENTO = 8;
	const TIPO_PG_PRODUCAO_BAHIA = 9;
	const TIPO_DEFAULT = self::TIPO_PG_PRODUCAO_LOCAL;
}
	
?>

 