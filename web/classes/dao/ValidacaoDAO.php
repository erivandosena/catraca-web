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
	
	public function validacaoDoTipo(Tipo $tipo){
		$lista = array();
		$idTipo = $tipo->getId();
		$sql = "SELECT * FROM validacao
				INNER JOIN tipo ON validacao.tipo_id = tipo.tipo_id
				WHERE tipo.tipo_id = $idTipo
				";
		echo $sql;
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
	
	/**
	 * Retorna a lista de tipos válidos para este usuário.
	 * O usuário deve ter em sua instancia o id da base externa.
	 * @return array $listaDeTipos
	 * @param Usuario $usuario
	 *
	 */
	public function retornaTiposValidosUsuario(Usuario $usuario){
		$tipoDao = new TipoDAO($this->getConexao());
		$listaDeTipos = $tipoDao->retornaLista();
		foreach ($listaDeTipos as $chave => $tipo){
			if(!$this->tipoValido($usuario, $tipo)){
				unset($listaDeTipos[$chave]);
			}
		}
		return $listaDeTipos;
	}
	
	
	/**
	 * Esse método verifica se o tipo é válido para determinado usuário. 
	 * Deve ser usado sempre que for adicionar ou renovar um vínculo próprio para um usuário. 
	 *  
	 * @param Usuario $usuario
	 * @param Tipo $tipo
	 */
	public function tipoValido(Usuario $usuario, Tipo $tipo){
		$validacoes = $this->validacaoDoTipo($tipo);
		if(!count($validacoes)){
			return false;
		}
		$idUsuario = $usuario->getIdBaseExterna();
		$sqlUsuarios = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $idUsuario LIMIT 15";
		$result = $this->getConexao()->query($sqlUsuarios);
		$i = 0;
		foreach($result as $linha){
				
			$matrizValidacao = array();
			foreach($validacoes as $validacao){
				$matrizValidacao[$validacao->getCampo()] = false;
			}
			foreach($matrizValidacao as $campo => $validade){
				foreach($validacoes as $validacao){
					if($validacao->getCampo() == $campo && $validacao->getValor() == $linha[$campo]){
						$matrizValidacao[$campo] = true;
					}
				}
			}
			$valido = true;
			foreach($matrizValidacao as $validade){
				if(!$validade){
					$valido = false;
					break;
				}
			}
			if($valido){
				return true;
			}
		}
		return false;
	}
	
	
}

?>