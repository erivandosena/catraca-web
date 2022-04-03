<?php
            
/**
 * Classe feita para manipulação do objeto VaccineDeclaration
 * feita automaticamente com programa gerador de software inventado por
 * @author Jefferson Uchôa Ponte <j.pontee@gmail.com>
 */

namespace Vacinometro\model;

class VaccineDeclaration {
	private $id;
	private $idUserSig;
	private $doseNumber;
	private $cardFile;
	private $status;
	private $createdAt;
    public function __construct(){

    }
	public function setId($id) {
		$this->id = $id;
	}
		    
	public function getId() {
		return $this->id;
	}
	public function setIdUserSig($idUserSig) {
		$this->idUserSig = $idUserSig;
	}
		    
	public function getIdUserSig() {
		return $this->idUserSig;
	}
	public function setDoseNumber($doseNumber) {
		$this->doseNumber = $doseNumber;
	}
		    
	public function getDoseNumber() {
		return $this->doseNumber;
	}
	public function setCardFile($cardFile) {
		$this->cardFile = $cardFile;
	}
		    
	public function getCardFile() {
		return $this->cardFile;
	}
	public function setStatus($status) {
		$this->status = $status;
	}
		    
	public function getStatus() {
		return $this->status;
	}
	public function setCreatedAt($createdAt) {
		$this->createdAt = $createdAt;
	}
		    
	public function getCreatedAt() {
		return $this->createdAt;
	}
	public function __toString(){
	    return $this->id.' - '.$this->idUserSig.' - '.$this->doseNumber.' - '.$this->cardFile.' - '.$this->status.' - '.$this->createdAt;
	}
	const STATUS_SUBMITTED = 'submitted';

}
?>