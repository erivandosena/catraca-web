<?php
class TipoDAO extends DAO{

	/**
	 * Retorna Um vetor de unidades.
	 * @return multitype:Unidade
	 */
	public function retornaLista(){
		$lista = array();
		$result = $this->getConexao()->query("SELECT * FROM tipo LIMIT 10");

		foreach ($result as $linha){
			$tipo = new Tipo();
			$tipo->setId($linha['tipo_id']);
			$tipo->setNome($linha['tipo_nome']);
			$lista[] = $tipo;

		}
		return $lista;
	}
	
	
}