<?php

/**
 * Classe utilizada para conxão com o Bando de Dados.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */

/**
 * UnidadeDAO alterações do banco de dados referentes à entidade unidade.
 *
 * Gera pesistencia da classe unidade.
 * a unidade academica.
 * 
 * @author jefponte
 *        
 */
class TurnoDAO extends DAO {
	
	/**
	 * Retorna Um vetor de unidades.
	 *
	 * @return Turno[]
	 */
	public function retornaLista() {
		$lista = array ();
		$result = $this->getConexao ()->query ( "SELECT * FROM turno" );
		
		foreach ( $result as $linha ) {
			$turno = new Turno ();
			$turno->setId ( $linha ['turn_id'] );
			$turno->setDescricao ( $linha ['turn_descricao'] );
			$turno->setHoraFinal ( $linha ['turn_hora_fim'] );
			$turno->setHoraInicial ( $linha ['turn_hora_inicio'] );
			$lista [] = $turno;
		}
		return $lista;
	}
	
	/**
	 * Função Utilizada para Inserir um turno. 
	 * @param Turno $turno Objeto Turno contendo os dados do turno.
	 */
	public function inserir(Turno $turno) {
		$descricao = $turno->getDescricao ();
		$horaInicial = $turno->getHoraInicial ();
		$horaFinal = $turno->getHoraFinal ();
		
		if ($this->getConexao ()->query ( "INSERT INTO turno (turn_hora_inicio, turn_hora_fim, turn_descricao) VALUES('$horaInicial', '$horaFinal','$descricao')" ))
			return true;
		return false;
	}
	
	/**
	 * Realiza um pesquisa pelo Id do turno.
	 * @param Turno $turno
	 */
	public function retornaTurnoPorId(Turno $turno) {
		$idTurno = $turno->getId ();
		$sql = "SELECT * FROM turno WHERE turn_id = $idTurno";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			$turno->setId ( $linha ['turn_id'] );
			$turno->setHoraInicial ( $linha ['turn_hora_inicio'] );
			$turno->setHoraFinal ( $linha ['turn_hora_fim'] );
			$turno->setDescricao ( $linha ['turn_descricao'] );
		}
	}
	
	/**
	 * Realiza a atualização do 
	 * @param Turno $turno
	 */
	public function atualizaTurno(Turno $turno) {
		$idTurno = $turno->getId ();
		$novaHoraIni = $turno->getHoraInicial ();
		$novaHoraFim = $turno->getHoraFinal ();
		
		$sql = "UPDATE turno SET
		turn_hora_inicio = '$novaHoraIni', turn_hora_fim = '$novaHoraFim'
		WHERE turn_id = $idTurno";
		if ($this->getConexao ()->exec ( $sql ))
			return true;
		return false;
	}
}

?>