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
	
	/**
	 * Retorna a lista de tipos válidos para este usuário. 
	 * O usuário deve ter em sua instancia o id da base externa.
	 * @return array $listaDeTipos 
	 * @param Usuario $usuario
	 *
	 */
	public function retornaTiposValidosUsuario(Usuario $usuario){
		$listaDeTipos = $this->retornaLista();
		foreach ($listaDeTipos as $chave => $tipo){
			if(!$this->tipoValido($usuario, $tipo)){
				unset($listaDeTipos[$chave]);
			}
		}
		return $listaDeTipos;
	}
	
	/**
	 * Retorna verdadeiro se o tipo for valido para este usuario.
	 * @return boolean
	 * @param Usuario $usuario
	 * @param Tipo $tipo
	 */
	public function tipoValido(Usuario $usuario, Tipo $tipo){

		$valido = false;
		$idTipo = $tipo->getId();
		$sql = "SELECT * FROM validacao INNER JOIN tipo ON validacao.tipo_id = tipo.tipo_id 
				WHERE validacao.tipo_id = $idTipo";
		$result = $this->getConexao()->query($sql);
		//Vetor onde o index é o nome do campo e o valor é o valor desejado. 
		$validacao = array();
		$i = 0; 
		foreach ($result as $linha){
			
			$i++;
			$validacao[$linha['vali_campo']] = $linha['vali_valor'];
		}
	
		if(!$i){
			return false;
		}

		$idUsuario = $usuario->getIdBaseExterna();
		$sqlVerifica = "SELECT * FROM vw_usuarios_catraca WHERE id_usuario = $idUsuario LIMIT 15";
		
		$result = $this->getConexao()->query($sqlVerifica);
		$i = 0;
		foreach ($result as $linha2){
			$valido = true;
			foreach($validacao as $chave => $valor){
				if($linha2[$chave] != $valor){
					$valido = false;
					break;
				}
			}
			if($valido){
				return $valido;
			}
		}
		return $valido;
		
	}
}