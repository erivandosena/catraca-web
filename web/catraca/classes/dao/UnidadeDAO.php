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
			$catraca->setIp ( $linha ['catr_ip'] );
			return $catraca;
		}
		return false;
	}
	public function preenchePorId(Unidade $unidade) {
		$idUnidade = $unidade->getId ();
		if (! is_int ( $idUnidade ) && $idUnidade <= 0)
			return;
		$sql = "SELECT * FROM unidade WHERE unid_id = $idUnidade";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha )
			$unidade->setNome ( $linha ['unid_nome'] );
		return;
	}
	public function turnoNaUnidade(Turno $turno, Unidade $unidade) {
		$idTurno = $turno->getId ();
		$idUnidade = $unidade->getId ();
		if ($idUnidade <= 0 || $idTurno <= 0 || ! is_int ( $idUnidade ) || ! is_int ( $idTurno ))
			return;
			// Primeiro vamos ver se esse turno existe nessa unidade.
		
		$sqlExiste = "SELECT * FROM unidade_turno WHERE turn_id = $idTurno AND unid_id = $idUnidade";
		foreach ( $this->getConexao ()->query ( $sqlExiste ) as $linha )
			return false;
		
		$sqlInsert = "INSERT INTO unidade_turno(turn_id, unid_id) VALUES($idTurno, $idUnidade)";
		if ($this->getConexao ()->exec ( $sqlInsert ))
			return true;
		return false;
		
		// Caso contrário a gente insere.
	}
	
	public function excluirTurnoDaUnidade(Turno $turno, Unidade $unidade) {
		$idTurno = $turno->getId ();
		$idUnidade = $unidade->getId ();
		if ($idUnidade <= 0 || $idTurno <= 0 || ! is_int ( $idUnidade ) || ! is_int ( $idTurno ))
			return;
		$sqlInsert = "DELETE FROM unidade_turno WHERE unid_id = $idUnidade AND  turn_id = $idTurno";
		if ($this->getConexao ()->exec ( $sqlInsert ))
			return true;
		return false;
	
		// Caso contrário a gente insere.
	}
	
	public function turnosDaUnidade(Unidade $unidade) {
		$idUnidade = $unidade->getId ();
		$sql = "SELECT * FROM unidade 
				INNER JOIN 
				unidade_turno ON unidade.unid_id = unidade_turno.unid_id 
				INNER JOIN turno 
				ON turno.turn_id = unidade_turno.turn_id
				WHERE unidade.unid_id = $idUnidade";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			
			$turno = new Turno ();
			$turno->setId ( $linha ['turn_id'] );
			$turno->setDescricao ( $linha ['turn_descricao'] );
			$turno->setHoraFinal ( $linha ['turn_hora_fim'] );
			$turno->setHoraInicial ( $linha ['turn_hora_inicio'] );
			$unidade->adicionaTurno ( $turno );
		}
	}

}

?>