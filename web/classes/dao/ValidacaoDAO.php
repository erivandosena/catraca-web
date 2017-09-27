<?php 


class ValidacaoDAO extends DAO{
	
	public function retornaCampos(){		
		$sql = "SELECT
		c.relname, a.attname as column
		FROM pg_catalog.pg_attribute a
		INNER JOIN pg_stat_user_tables c on a.attrelid = c.relid
		WHERE c.relname = 'vw_usuarios_catraca' AND a.attnum > 0 AND NOT a.attisdropped	";
		$listaCampos = $this->getConexao()->query($sql);		
		return $listaCampos;		
	}
	
	public function inserirValidacao($campo, $valor, $tipo){
		
		if ($campo == null || $valor == null || $tipo == null){
			return false;
		}
		
		$sql = "INSERT INTO validacao(vali_campo, vali_valor, tipo_id) VALUES('$campo', '$valor', $tipo);";
		if ($this->getConexao()->exec($sql))			
			return true;		
		return false;
	}
	
	public function listaValidacao(){
		$lista = array();
		$sql = "SELECT * FROM validacao 
				INNER JOIN tipo ON validacao.tipo_id = tipo.tipo_id ";
		$result = $this->getConexao()->query($sql);
		foreach ($result as $linha){
			$validacao = new Validacao;
			$validacao->setId($linha['vali_id']);
			$validacao->setCampo($linha['vali_campo']);
			$validacao->setValor($linha['vali_valor']);
			$validacao->setTipoId($linha['tipo_id']);
			$validacao->setTipoNome($linha['tipo_nome']);
			$lista[] = $validacao;
		}
		return $lista;
	}
	
	public function excluirValidacao($id){
		$sql = "DELETE FROM validacao WHERE vali_id = $id";
		if ($this->getConexao()->exec($sql))
			return true;
		return false;		
		
	}
	
}

?>