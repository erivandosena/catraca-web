<?php
/**
 * UnidadeDAO altera��es do banco de dados referentes � entidade unidade. 
 * Gera pesistencia da classe unidade. 
 * � a unidade academica. 
 * @author jefponte
 *
 */
class UnidadeDAO extends DAO {
	
	/**
	 * Retorna Um vetor de unidades.
	 *
	 * @return multitype:Unidade
	 */
	public function retornaLista() {
		$lista = array ();
		$result = $this->getConexao ()->query ( "SELECT * FROM unidade LIMIT 100" );
		
		foreach ( $result as $linha ) {
			$unidade = new Unidade ();
			$unidade->setId ( $linha ['unid_id'] );
			$unidade->setNome ( $linha ['unid_nome'] );
			$lista [] = $unidade;
		}
		return $lista;
	}
	public function inserirUnidade(Unidade $unidade) {
		$nome = $unidade->getNome ();
		if ($this->getConexao ()->query ( "INSERT INTO unidade (unid_nome) VALUES('$nome')" ))
			return true;
		return false;
	}
	public function deletarUnidade(Unidade $unidade) {
		$id = $unidade->getId ();
		$sql = "DELETE FROM unidade WHERE unid_id = $id";
		if ($this->getConexao ()->query ( $sql ))
			return true;
		return false;
	}
	public function retornaCatracasPorUnidade(Unidade $unidade = null) {
		$lista = array ();
		if ($unidade != null) {
			$id = $unidade->getId ();
			$sql = "SELECT * FROM catraca 
					INNER JOIN catraca_unidade
					ON catraca.catr_id = catraca_unidade.catr_id
					INNER JOIN unidade
					ON unidade.unid_id = catraca_unidade.unid_id
					WHERE unidade.unid_id = $id";
		} else {
			$sql = "SELECT * FROM catraca";
		}
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$catraca = new Catraca ();
			$catraca->setNome ( $linha ['catr_nome'] );
			$catraca->setId ( $linha ['catr_id'] );
			$lista [] = $catraca;
		}
		return $lista;
	}
	public function detalheCatraca(Catraca $catraca) {
		$idCatraca = $catraca->getId ();
		$sql = "SELECT * FROM catraca WHERE catr_id = $idCatraca";
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$catraca->setNome ( $linha ['catr_nome'] );
			$catraca->setId ( $linha ['catr_id'] );
			$catraca->setIp($linha['catr_ip']);
			return $catraca;
		}
		return false;
	}
}

?>