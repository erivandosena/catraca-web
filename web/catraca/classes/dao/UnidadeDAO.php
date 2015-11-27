<?php
/**
 * UnidadeDAO altera��es do banco de dados referentes � entidade unidade. 
 * Gera pesistencia da classe unidade. 
 * � a unidade academica. 
 * @author jefponte
 *
 */
class UnidadeDAO extends DAO{

	/**
	 * Retorna Um vetor de unidades. 
	 * @return multitype:Unidade
	 */
	public function retornaLista(){
		$lista = array();
		$result = $this->getConexao()->query("SELECT * FROM unidade LIMIT 100");

		foreach ($result as $linha){
			$unidade = new Unidade();
			$unidade->setId($linha['unid_id']);
			$unidade->setNome($linha['unid_nome']);
			$lista[] = $unidade;
				
		}
		return $lista;
	}

	

	public function inserirUnidade(Unidade $unidade){
		$nome = $unidade->getNome();
		if($this->getConexao()->query("INSERT INTO unidade (unid_nome) VALUES('$nome')"))
			return true;
		return false;
		
		
	}
	public function deletarUnidade(Unidade $unidade){
		$id = $unidade->getId();
		$sql = "DELETE FROM unidade WHERE unid_id = $id";
		if($this->getConexao()->query($sql))
			return true;
		return false;
	}
	
	
	
	
}


?>