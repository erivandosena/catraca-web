<?php

/**
 * Dao Referente a Entidade Unidade.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */

/**
 * UnidadeDAO alterações do banco de dados referentes à entidade unidade. 
 * Gera pesistencia da classe unidade. 
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
		$sql = "SELECT * FROM unidade LIMIT 100";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$unidade = new Unidade ();
			$unidade->setId ( $linha ['unid_id'] );
			$unidade->setNome ( $linha ['unid_nome'] );
			$lista [] = $unidade;
		}
		return $lista;
	}
	
	/**
	 * Função utilidada para Inserir uma Unidade.
	 * @param Unidade $unidade
	 */
	public function inserirUnidade(Unidade $unidade) {
		$nome = $unidade->getNome ();
		if ($this->getConexao ()->query ( "INSERT INTO unidade (unid_nome) VALUES('$nome')" ))
			return true;
		return false;
	}
	
	/**
	 * Função utilizada para Deletar uma Unidade.
	 * @param Unidade $unidade
	 */
	public function deletarUnidade(Unidade $unidade) {
		$id = $unidade->getId ();
		$sql = "DELETE FROM unidade WHERE unid_id = $id";
		if ($this->getConexao ()->query ( $sql ))
			return true;
		return false;
	}
	
	/**
	 * Função utilizada para realizar uma constulta,retornando uma array de catracas da unidade consultada. 
	 * @param Unidade $unidade
	 */
	public function retornaCatracasPorUnidade(Unidade $unidade = null) {
		$lista = array ();
		if ($unidade != null) {
			$id = $unidade->getId ();
			$sql = "SELECT 
			
					*, catraca.catr_id as catraca_id
					 
					FROM catraca 
					INNER JOIN catraca_unidade
					ON catraca.catr_id = catraca_unidade.catr_id
					INNER JOIN unidade
					ON unidade.unid_id = catraca_unidade.unid_id
					WHERE unidade.unid_id = $id";
		} else {
			$sql = "SELECT *, catraca.catr_id as 
					catraca_id
					 FROM catraca
					LEFT JOIN catraca_unidade
					ON catraca.catr_id = catraca_unidade.catr_id
					LEFT JOIN unidade
					ON unidade.unid_id = catraca_unidade.unid_id
					ORDER BY catraca.catr_id ASC
					";
		}
		
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$catraca = new Catraca ();
			$catraca->setNome ( $linha ['catr_nome'] );
			$catraca->setOperacao($linha['catr_operacao']);
			$catraca->setTempoDeGiro($linha['catr_tempo_giro']);
			$catraca->setIp($linha['catr_ip']);
			$catraca->setId($linha['catraca_id']);
			$catraca->setMacLan($linha['catr_mac_lan']);
			$catraca->setMacWlan($linha['catr_mac_wlan']);
			$catraca->setInterfaceRede($linha['catr_interface_rede']);
			$catraca->setUnidade(new Unidade());
			$catraca->getUnidade()->setNome($linha['unid_nome']);
			$catraca->setFinanceiro($linha['catr_financeiro']);
			
			
			$lista [] = $catraca;
		}
		return $lista;
	}
	
	/**
	 * Retona a quantidade de giros efetuados pela catraca consultada.
	 * @param Catraca $catraca
	 * @return number|PDOStatement
	 */
	public function totalDeGirosDaCatraca(Catraca $catraca){
		$idCatraca = $catraca->getId();
		$filtro = "";
		
		$sql = "SELECT sum(1) as resultado 
				FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
				WHERE catraca.catr_id = $idCatraca $filtro";
		
		$resultado = 0;
		foreach ($this->getConexao()->query($sql) as $linha){
			$resultado = $linha['resultado'];
			
		}
		return $resultado;
	}
	
	/**
	 * Retorna a total de giro da catraca por turno em andamento,
	 * separando-os elo tipo de usuario que utilizou a catraca.
	 * @param Catraca $catraca
	 * @param Tipo $tipo
	 */
	public function totalDeGirosDaCatracaTurnoAtual(Catraca $catraca, Tipo $tipo = null){
		$resultado = 0;
		$idCatraca = $catraca->getId();
		$turno = $this->pegaTurnoAtualSeExistir();
		if($turno){
			$horaInicial = date("Y-m-d ").$turno->getHoraInicial();
			$horaFinal = date("Y-m-d ").$turno->getHoraFinal();
			if($tipo == null){
				
				$sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
			WHERE catraca.catr_id = $idCatraca AND registro.regi_data BETWEEN '$horaInicial' AND '$horaFinal' ";
				
			
			}
			else{
				$idTipo = $tipo->getId();
				$sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
				INNER JOIN cartao ON cartao.cart_id = registro.cart_id
				WHERE catraca.catr_id = $idCatraca AND registro.regi_data BETWEEN '$horaInicial' AND '$horaFinal' AND cartao.tipo_id = $idTipo";
				
			}

			foreach ($this->getConexao()->query($sql) as $linha){
				$resultado = $linha['resultado'];
			}			
		}		
		return $resultado;
	}

	/**
	 * Retorna a total de giro da catraca por turno em andamento,
	 * filtrando pelos registros de usuario pagantes.
	 * @param Catraca $catraca
	 * @param Tipo $tipo
	 */
	public function totalGiroTurnoAtualNaoIsento(Catraca $catraca, Tipo $tipo = null){
		$resultado = 0;
		$idCatraca = $catraca->getId();
		$turno = $this->pegaTurnoAtualSeExistir();
		if($turno){
			$horaInicial = date("Y-m-d ").$turno->getHoraInicial();
			$horaFinal = date("Y-m-d ").$turno->getHoraFinal();
			if($tipo == null){
	
				$sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
				WHERE (catraca.catr_id = $idCatraca) AND (registro.regi_data BETWEEN '$horaInicial' AND '$horaFinal') AND 
				(regi_valor_pago > 0)
				";
	
					
			}
			else{
				$idTipo = $tipo->getId();
				$sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
				INNER JOIN cartao ON cartao.cart_id = registro.cart_id
				WHERE (catraca.catr_id = $idCatraca) AND (registro.regi_data BETWEEN '$horaInicial' AND '$horaFinal') AND (cartao.tipo_id = $idTipo) AND 
				(regi_valor_pago > 0)
				";
	
			}
	
			foreach ($this->getConexao()->query($sql) as $linha){
				$resultado = $linha['resultado'];
			}
		}
		return $resultado;
	}
	
	/**
	 * Retorna a total de giro da catraca por turno em andamento,
	 * filtrando pelos registros de usuario isentos.
	 * @param Catraca $catraca
	 * @param Tipo $tipo
	 */
	public function totalGiroTurnoAtualIsento(Catraca $catraca, Tipo $tipo = null){
		$resultado = 0;
		$idCatraca = $catraca->getId();
		$turno = $this->pegaTurnoAtualSeExistir();
		if($turno){
			$horaInicial = date("Y-m-d ").$turno->getHoraInicial();
			$horaFinal = date("Y-m-d ").$turno->getHoraFinal();
	
			$sql = "SELECT sum(1) as resultado FROM registro INNER JOIN catraca ON registro.catr_id = catraca.catr_id
			WHERE catraca.catr_id = $idCatraca AND registro.regi_data BETWEEN '$horaInicial' AND '$horaFinal'
			AND (regi_valor_pago = 0)
			";
	
					
	
			foreach ($this->getConexao()->query($sql) as $linha){
				$resultado = $linha['resultado'];
			}
		}
		return $resultado;
	}
	
	/**
	 * Retorna um array de turnos no periodo corrente.
	 * @return NULL|Turno
	 */
	public function pegaTurnoAtualSeExistir(){
		$dataTimeAtual = date ( "G:i:s" );
		$sql = "Select * FROM turno WHERE '$dataTimeAtual' BETWEEN turno.turn_hora_inicio AND turno.turn_hora_fim";
		$result = $this->conexao->query($sql);
		$turno = null;
		foreach ($result as $linha){
			$turno = new Turno();
			$turno->setHoraInicial($linha['turn_hora_inicio']);
			$turno->setHoraFinal($linha['turn_hora_fim']);
			
		}
		return $turno;
	}
	
	/**
	 * Consulta a Catraca pelo seu Id
	 * @param Catraca $catraca
	 */
	public function preencheCatracaPorId(Catraca $catraca){
		$idCatraca = $catraca->getId();
		$sql = "
				SELECT *, catraca.catr_id as catraca_id FROM catraca
		LEFT JOIN catraca_unidade
		ON catraca.catr_id = catraca_unidade.catr_id
		LEFT JOIN unidade
		ON unidade.unid_id = catraca_unidade.unid_id
		WHERE catraca.catr_id = $idCatraca";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha ) {
			$catraca->setNome ( $linha ['catr_nome'] );
			$catraca->setId ( $linha ['catraca_id'] );
			$catraca->setOperacao($linha['catr_operacao']);
			$catraca->setTempoDeGiro($linha['catr_tempo_giro']);
			$catraca->setIp($linha['catr_ip']);
			$catraca->setInterfaceRede($linha['catr_interface_rede']);
			$catraca->setFinanceiro($linha['catr_financeiro']);
			
			$catraca->setUnidade(new Unidade());
			$catraca->getUnidade()->setNome($linha['unid_nome']);
			$catraca->getUnidade()->setId($linha['unid_id']);
				
		}
		
	}
	/**
	 * Realiza o Update dos dados Catraca selecionada.
	 * @param Catraca $catraca
	 */
	public function atualizarCatraca(Catraca $catraca){
		$giro = $catraca->getTempodeGiro();
		$id = $catraca->getId();
		$nomeCatraca = $catraca->getNome();
		$operacao = $catraca->getOperacao();
		$idUnidade= $catraca->getUnidade()->getId();
		$interface = $catraca->getInterfaceRede();
		
		if($catraca->financeiroAtivo()){
			$financeiro = 'TRUE';
		}else{
			$financeiro = 'FALSE';
		}		
		
		$this->getConexao()->beginTransaction();
		$sqlUpdate = "UPDATE catraca SET catr_tempo_giro = $giro,						
						catr_operacao = $operacao,
						catr_nome = '$nomeCatraca',
						catr_interface_rede = '$interface',
						catr_financeiro = '$financeiro'
						WHERE catr_id = $id";
		
		if(!$this->getConexao()->exec($sqlUpdate))
		{
			$this->getConexao()->rollBack();
			echo $sqlUpdate;
			echo 'Foi aqui Nao consegui Atualizar';
			return false;
		}
 		$this->getConexao()->exec("DELETE FROM catraca_unidade WHERE catr_id = $id");
		
		if(!$this->getConexao()->exec("INSERT into catraca_unidade(catr_id, unid_id) VALUES($id, $idUnidade)"))
		{
			$this->getConexao()->rollBack();
			return false;
		}
		
		$this->getConexao()->commit();
		return true;
		
		
		
	}
	
	/**
	 * ??????
	 */
	function inserirRegistro() {
		$request = \Slim\Slim::getInstance()->request();
		$body = $request->getBody();
		$dados = json_decode($body);
	
		$sql = "INSERT INTO registro(regi_data, regi_valor_pago, regi_valor_custo, cart_id, catr_id, vinc_id)
	VALUES (:data, :pago, :custo, :cartao, :catraca, :vinculo);";
	
		try {
			$db = getDB();
			$stmt = $db->prepare($sql);
			$stmt->bindParam("data", ($dados->regi_data == '') ? NULL : $dados->regi_data ); //NULL if $dados->regi_data == NULL else $dados->regi_data );
			$stmt->bindParam("pago", $dados->regi_valor_pago);
			$stmt->bindParam("custo", $dados->regi_valor_custo);
			$stmt->bindParam("cartao", $dados->cart_id);
			$stmt->bindParam("catraca", $dados->catr_id);
			$stmt->bindParam("vinculo", $dados->vinc_id);
			$stmt->execute();
			$db = null;
		} catch(PDOException $e) {
			echo '{"erro":{"text":'. $e->getMessage() .'}}';
		}
	}
	
	/**
	 * Consulta a Unidade pos Id.
	 * @param Unidade $unidade
	 */
	public function preenchePorId(Unidade $unidade) {
		$idUnidade = $unidade->getId ();
		if (! is_int ( $idUnidade ) && $idUnidade <= 0)
			return;
		$sql = "SELECT * FROM unidade WHERE unid_id = $idUnidade";
		foreach ( $this->getConexao ()->query ( $sql ) as $linha )
			$unidade->setNome ( $linha ['unid_nome'] );
		return;
	}
	
	/**
	 * Retorna os turnos contidos na unidade.
	 * @param Turno $turno
	 * @param Unidade $unidade
	 */
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
	
	/**
	 * Exclui um turno da unidade.
	 * @param Turno $turno
	 * @param Unidade $unidade
	 */
	public function excluirTurnoDaUnidade(Turno $turno, Unidade $unidade) {
		$idTurno = $turno->getId ();
		$idUnidade = $unidade->getId ();
		if ($idUnidade <= 0 || $idTurno <= 0 || ! is_int ( $idUnidade ) || ! is_int ( $idTurno ))
			return;
		$sqlInsert = "DELETE FROM unidade_turno WHERE unid_id = $idUnidade AND  turn_id = $idTurno";
		if ($this->getConexao ()->exec ( $sqlInsert ))
			return true;
		return false;
	
		// Caso contrÃ¡rio a gente insere.
	}
	
	/**
	 * Retorna os turnos da unidade.
	 * @param Unidade $unidade
	 */
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
	
	/**
	 * retorna um array contendo os custos das Unidades.
	 */
	public function custosDaUnidade(){
	
		$lista = array ();
		$sql = "SELECT * FROM unidade
				LEFT JOIN custo_unidade ON custo_unidade.unid_id = unidade.unid_id
				LEFT JOIN custo_refeicao ON custo_refeicao.cure_id = custo_unidade.cure_id";
		$result = $this->getConexao()->query($sql);
		foreach ($result as $linha){
			$unidade = new Unidade();
			$unidade->setId($linha['unid_id']);
			$unidade->setNome($linha['unid_nome']);
			$unidade->setCustoUnidade($linha['cure_valor']);
			$lista[] = $unidade;
		}
		return $lista;
	}
}

?>