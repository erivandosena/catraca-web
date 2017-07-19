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
				
			}
			$sql .= $valor.") VALUES(";
			$i = 0;
			foreach($this->campos as $chave => $valor){
				$i++;
				if($linha[$chave] == null || $linha[$chave] == ''){
					$sql .= "null";
				}else{
					$sql .= ":".$valor;
				}
				
				if($i != count($this->campos)){
					$sql .= ", ";
				}
			}
			$sql .= "); ";
			
			
			try {
				$stmt = $this->conexaoDestino->prepare($sql);
				$h = 0;
				foreach($this->campos as $chave => $valor){
					$$valor = $linha[$chave];
					$conteudo = $linha[$chave];
					if(is_string($conteudo)){
						
						
						
						$$valor = preg_replace ('/[^a-zA-Z0-9\s]/', '', $$valor);
						
						$stmt->bindParam($valor, $$valor, PDO::PARAM_STR);						
					}
					else if(is_int($conteudo)){
						$stmt->bindParam($valor, $$valor, PDO::PARAM_INT);
					}


				}
				
				if(!$stmt->execute()){
					$this->conexaoDestino->rollBack();
					echo "Errei aqui: ". $sql;
					print_r($linha);
					return;
				}
					
				
			
			} catch(PDOException $e) {
				echo '{"error":{"text":'. $e->getMessage() .'}}';
			}
			

		}
		
		$this->conexaoDestino->commit();

		
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
		$campos = ["NOME" => "nome", "categoria" => "categoria"];
		$sincronizador->setCampos($campos);
		$sincronizador->sincronizar();
	}
	
}



?>