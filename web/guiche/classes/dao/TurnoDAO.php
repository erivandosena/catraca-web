<?php
/**
 * UnidadeDAO altera��es do banco de dados referentes � entidade unidade. 
 * Gera pesistencia da classe unidade. 
 * � a unidade academica. 
 * @author jefponte
 *
 */
class TurnoDAO extends DAO{

	/**
	 * Retorna Um vetor de unidades. 
	 * @return multitype:Turno
	 */
	public function retornaLista(){
		$lista = array();
		$result = $this->getConexao()->query("SELECT * FROM turno");

		foreach ($result as $linha){
			$turno = new Turno();
			$turno->setId($linha['turn_id']);
			$turno->setDescricao($linha['turn_descricao']);
			$turno->setHoraFinal($linha['turn_hora_fim']);
			$turno->setHoraInicial($linha['turn_hora_inicio']);
			$lista[] = $turno;
				
		}
		return $lista;
	}

	public function inserir(Turno $turno){
		$descricao = $turno->getDescricao();
		$horaInicial = $turno->getHoraInicial();
		$horaFinal = $turno->getHoraFinal();
		

		if($this->getConexao()->query("INSERT INTO turno (turn_hora_inicio, turn_hora_fim, turn_descricao) VALUES('$horaInicial', '$horaFinal','$descricao')"))
			return true;
		return false;
		
		
	}
	
	public function retornaTurnoPorId(Turno $turno){
		
		$idTurno = $turno->getId();
		$sql = "SELECT * FROM turno WHERE turn_id = $idTurno";
		$result = $this->getConexao()->query($sql);
		foreach ($result as $linha){
			$turno->setId($linha['turn_id']);
			$turno->setHoraInicial($linha['turn_hora_inicio']);
			$turno->setHoraFinal($linha['turn_hora_fim']);
			$turno->setDescricao($linha['turn_descricao']);			
		}
	}
	
	public function atualizaTurno(Turno $turno){
		
		$idTurno = $turno->getId();
		$novaHoraIni = $turno->getHoraInicial();
		$novaHoraFim = $turno->getHoraFinal();
		
		$sql = "UPDATE turno SET 
				turn_hora_inicio = '$novaHoraIni', turn_hora_fim = '$novaHoraFim'
				WHERE turn_id = $idTurno";		
		if($this->getConexao()->exec($sql))
			return true;
		return false;
		
	}
	
}


?>