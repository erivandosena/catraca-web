<?php
class TipoDAO extends DAO{

	/**
	 * Retorna Um vetor de unidades.
	 * @return multitype:Tipo
	 */
	public function retornaLista(){
		$lista = array();
		$result = $this->getConexao()->query("SELECT * FROM tipo LIMIT 10");

		foreach ($result as $linha){
			$tipo = new Tipo();
			$tipo->setId($linha['tipo_id']);
			$tipo->setNome($linha['tipo_nome']);
			$tipo->setValorCobrado($linha['tipo_valor']);
			$lista[] = $tipo;

		}
		return $lista;
	}
	

	public function retornaTipoPorId(Tipo $tipo){
	
		$idTipo = $tipo->getId();
		$sql = "SELECT * FROM tipo WHERE tipo_id = $idTipo";
		$result = $this->getConexao()->query($sql);
	
		foreach ($result as $linha){
			$tipo->setId($linha['tipo_id']);
			$tipo->setNome($linha['tipo_nome']);
			$tipo->setValorCobrado($linha['tipo_valor']);
		}
		return $tipo;
	}
	

	

}