<?php


/**
 * 
 * @author Jefferson Uchôa Ponte
 * 
 *
 */
class Sincronizador{
	
	private $conexaoOrigem;
	private $conexaoDestino;
	private $entidadeOrigem;
	private $entidadeDestino;
	private $campos; 
	
	public function __construct(PDO $conexaoOrigem, PDO $conexaoDestino, $entidadeOrigem, $entidadeDestino){
		$this->conexaoOrigem = $conexaoOrigem;
		$this->conexaoDestino = $conexaoDestino;
		$this->entidadeOrigem = $entidadeOrigem;
		$this->entidadeDestino = $entidadeDestino;
		$campos = array();
		
	}
	
	public function addCampo($campoOrigem, $campoDestino){
		
		$this->campos[$campoOrigem] = $campoDestino;
		
		
	}
	public function sincronizar(){
		
		$this->conexaoDestino->beginTransaction();
		$sqlDelete = "DELETE FROM ".$this->entidadeDestino;
		$b = $this->conexaoDestino->exec($sqlDelete);
		echo "Deletei ".$b." linhas da entidade de destino<br>";
		
		
		$sql = "SELECT * FROM ".$this->entidadeOrigem;
		$result = $this->conexaoOrigem->query($sql);
		
		foreach($result as $linha){
			
			$sql = "INSERT INTO ".$this->entidadeDestino." (";
			$i = 0;
			foreach($this->campos as $chave => $valor){
				$i++;
				if($i != count($this->campos)){
					$sql .= $valor.", ";
				}
				else{
					$sql .= $valor.") VALUES(";
				}
			}
			$i = 0;
			foreach($this->campos as $chave => $valor){
				$i++;
				if(is_string($linha[$chave]))
				{
					$sql .= "'";
					$sql .= $linha[$chave];
					$sql .= "'";
				}
				else
				{
					if(!($linha[$chave]) || ($linha[$chave]) == "''"){
						$sql .=  "null";
					}else{
						$sql .= $linha[$chave];
					}
					
				}
				if($i != count($this->campos))
				{
					$sql .= ", ";
				}
				else
				{
					$sql .= ");";
				}
				
			}
			
			
			echo $sql;
			return;


		}

		
	}
	public function setCampos($campos){
		$this->campos = $campos;
	}
	
	public static function main(){
		$dao = new DAO(null, DAO::TIPO_USUARIOS);
		$entidadeOrigem = $dao->getEntidadeUsuarios();
		$conexaoOrigem = $dao->getConexao();
		$dao = new DAO();
		$conexaoDestino = $dao->getConexao();
		$entidadeDestino = "vw_usuarios_catraca";
		$sincronizador = new Sincronizador($conexaoOrigem, $conexaoDestino, $entidadeOrigem, $entidadeDestino);
		$campos = ["id_usuario" => "status_discente", "NOME" => "nome", "identidade" => "identidade", "email" => "email", "login" => "login", "senha" => "senha", "cpf" => "cpf_cnpj", "categoria" => "categoria"];
		$sincronizador->setCampos($campos);
		$sincronizador->sincronizar();
	}
	
}



?>