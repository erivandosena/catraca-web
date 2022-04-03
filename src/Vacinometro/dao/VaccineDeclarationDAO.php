<?php
            
/**
 * Classe feita para manipulação do objeto VaccineDeclaration
 * @author Jefferson Uchôa Ponte
 */
     
namespace Vacinometro\dao;
use PDO;
use PDOException;
use Vacinometro\model\VaccineDeclaration;

class VaccineDeclarationDAO extends DAO {
    
    

            
            
    public function update(VaccineDeclaration $vaccineDeclaration)
    {
        $id = $vaccineDeclaration->getId();
            
            
        $sql = "UPDATE vaccine_declaration
                SET
                id_user_sig = :idUserSig,
                dose_number = :doseNumber,
                card_file = :cardFile,
                status = :status,
                created_at = :createdAt
                WHERE vaccine_declaration.id = :id;";
			$idUserSig = $vaccineDeclaration->getIdUserSig();
			$doseNumber = $vaccineDeclaration->getDoseNumber();
			$cardFile = $vaccineDeclaration->getCardFile();
			$status = $vaccineDeclaration->getStatus();
			$createdAt = $vaccineDeclaration->getCreatedAt();
            
        try {
            
            $stmt = $this->getConnection()->prepare($sql);
			$stmt->bindParam(":id", $id, PDO::PARAM_INT);
			$stmt->bindParam(":idUserSig", $idUserSig, PDO::PARAM_INT);
			$stmt->bindParam(":doseNumber", $doseNumber, PDO::PARAM_INT);
			$stmt->bindParam(":cardFile", $cardFile, PDO::PARAM_STR);
			$stmt->bindParam(":status", $status, PDO::PARAM_STR);
			$stmt->bindParam(":createdAt", $createdAt, PDO::PARAM_STR);
            
            return $stmt->execute();
        } catch (PDOException $e) {
            echo $e->getMessage();
        }
            
    }
            
            

    public function insert(VaccineDeclaration $vaccineDeclaration){
        $sql = "INSERT INTO vaccine_declaration(id_user_sig, dose_number, card_file, status, created_at) VALUES (:idUserSig, :doseNumber, :cardFile, :status, :createdAt);";
		$idUserSig = $vaccineDeclaration->getIdUserSig();
		$doseNumber = $vaccineDeclaration->getDoseNumber();
		$cardFile = $vaccineDeclaration->getCardFile();
		$status = $vaccineDeclaration->getStatus();
		$createdAt = $vaccineDeclaration->getCreatedAt();
		try {
			$db = $this->getConnection();
			$stmt = $db->prepare($sql);
			$stmt->bindParam(":idUserSig", $idUserSig, PDO::PARAM_INT);
			$stmt->bindParam(":doseNumber", $doseNumber, PDO::PARAM_INT);
			$stmt->bindParam(":cardFile", $cardFile, PDO::PARAM_STR);
			$stmt->bindParam(":status", $status, PDO::PARAM_STR);
			$stmt->bindParam(":createdAt", $createdAt, PDO::PARAM_STR);
			return $stmt->execute();
		} catch(PDOException $e) {
			echo '{"error":{"text":'. $e->getMessage() .'}}';
		}
            
    }
    public function insertWithPK(VaccineDeclaration $vaccineDeclaration){
        $sql = "INSERT INTO vaccine_declaration(id, id_user_sig, dose_number, card_file, status, created_at) VALUES (:id, :idUserSig, :doseNumber, :cardFile, :status, :createdAt);";
		$id = $vaccineDeclaration->getId();
		$idUserSig = $vaccineDeclaration->getIdUserSig();
		$doseNumber = $vaccineDeclaration->getDoseNumber();
		$cardFile = $vaccineDeclaration->getCardFile();
		$status = $vaccineDeclaration->getStatus();
		$createdAt = $vaccineDeclaration->getCreatedAt();
		try {
			$db = $this->getConnection();
			$stmt = $db->prepare($sql);
			$stmt->bindParam(":id", $id, PDO::PARAM_INT);
			$stmt->bindParam(":idUserSig", $idUserSig, PDO::PARAM_INT);
			$stmt->bindParam(":doseNumber", $doseNumber, PDO::PARAM_INT);
			$stmt->bindParam(":cardFile", $cardFile, PDO::PARAM_STR);
			$stmt->bindParam(":status", $status, PDO::PARAM_STR);
			$stmt->bindParam(":createdAt", $createdAt, PDO::PARAM_STR);
			return $stmt->execute();
		} catch(PDOException $e) {
			echo '{"error":{"text":'. $e->getMessage() .'}}';
		}
            
    }

	public function delete(VaccineDeclaration $vaccineDeclaration){
		$id = $vaccineDeclaration->getId();
		$sql = "DELETE FROM vaccine_declaration WHERE id = :id";
		    
		try {
			$db = $this->getConnection();
			$stmt = $db->prepare($sql);
			$stmt->bindParam(":id", $id, PDO::PARAM_INT);
			return $stmt->execute();
			    
		} catch(PDOException $e) {
			echo '{"error":{"text":'. $e->getMessage() .'}}';
		}
	}


	public function fetch() {
		$list = array ();
		$sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration LIMIT 1000";

        try {
            $stmt = $this->connection->prepare($sql);
            
		    if(!$stmt){   
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		        return $list;
		    }
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row) 
            {
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $list [] = $vaccineDeclaration;

	
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
        return $list;	
    }
        
                
    public function fetchById(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $id = $vaccineDeclaration->getId();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.id = :id";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":id", $id, PDO::PARAM_INT);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fetchByIdUserSig(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $idUserSig = $vaccineDeclaration->getIdUserSig();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.id_user_sig = :idUserSig";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":idUserSig", $idUserSig, PDO::PARAM_INT);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fetchByDoseNumber(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $doseNumber = $vaccineDeclaration->getDoseNumber();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.dose_number = :doseNumber";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":doseNumber", $doseNumber, PDO::PARAM_INT);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fetchByCardFile(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $cardFile = $vaccineDeclaration->getCardFile();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.card_file like :cardFile";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":cardFile", $cardFile, PDO::PARAM_STR);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fetchByStatus(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $status = $vaccineDeclaration->getStatus();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.status like :status";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":status", $status, PDO::PARAM_STR);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fetchByCreatedAt(VaccineDeclaration $vaccineDeclaration) {
        $lista = array();
	    $createdAt = $vaccineDeclaration->getCreatedAt();
                
        $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
            WHERE vaccine_declaration.created_at like :createdAt";
                
        try {
                
            $stmt = $this->connection->prepare($sql);
            $stmt->bindParam(":createdAt", $createdAt, PDO::PARAM_STR);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
            foreach ( $result as $row ){
		        $vaccineDeclaration = new VaccineDeclaration();
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                $lista [] = $vaccineDeclaration;

	
		    }
    			    
        } catch(PDOException $e) {
            echo $e->getMessage();
    			    
        }
		return $lista;
    }
                
    public function fillById(VaccineDeclaration $vaccineDeclaration) {
        
	    $id = $vaccineDeclaration->getId();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.id = :id
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":id", $id, PDO::PARAM_INT);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
                
    public function fillByIdUserSig(VaccineDeclaration $vaccineDeclaration) {
        
	    $idUserSig = $vaccineDeclaration->getIdUserSig();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.id_user_sig = :idUserSig
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":idUserSig", $idUserSig, PDO::PARAM_INT);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
                
    public function fillByDoseNumber(VaccineDeclaration $vaccineDeclaration) {
        
	    $doseNumber = $vaccineDeclaration->getDoseNumber();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.dose_number = :doseNumber
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":doseNumber", $doseNumber, PDO::PARAM_INT);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
                
    public function fillByCardFile(VaccineDeclaration $vaccineDeclaration) {
        
	    $cardFile = $vaccineDeclaration->getCardFile();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.card_file = :cardFile
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":cardFile", $cardFile, PDO::PARAM_STR);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
                
    public function fillByStatus(VaccineDeclaration $vaccineDeclaration) {
        
	    $status = $vaccineDeclaration->getStatus();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.status = :status
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":status", $status, PDO::PARAM_STR);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
                
    public function fillByCreatedAt(VaccineDeclaration $vaccineDeclaration) {
        
	    $createdAt = $vaccineDeclaration->getCreatedAt();
	    $sql = "SELECT vaccine_declaration.id, vaccine_declaration.id_user_sig, vaccine_declaration.dose_number, vaccine_declaration.card_file, vaccine_declaration.status, vaccine_declaration.created_at FROM vaccine_declaration
                WHERE vaccine_declaration.created_at = :createdAt
                 LIMIT 1000";
                
        try {
            $stmt = $this->connection->prepare($sql);
                
		    if(!$stmt){
                echo "<br>Mensagem de erro retornada: ".$this->connection->errorInfo()[2]."<br>";
		    }
            $stmt->bindParam(":createdAt", $createdAt, PDO::PARAM_STR);
            $stmt->execute();
		    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
		    foreach ( $result as $row )
            {
                $vaccineDeclaration->setId( $row ['id'] );
                $vaccineDeclaration->setIdUserSig( $row ['id_user_sig'] );
                $vaccineDeclaration->setDoseNumber( $row ['dose_number'] );
                $vaccineDeclaration->setCardFile( $row ['card_file'] );
                $vaccineDeclaration->setStatus( $row ['status'] );
                $vaccineDeclaration->setCreatedAt( $row ['created_at'] );
                
                
		    }
		} catch(PDOException $e) {
		    echo $e->getMessage();
 		}
		return $vaccineDeclaration;
    }
}