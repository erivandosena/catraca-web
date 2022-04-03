<?php
            
/**
 * Classe feita para manipulação do objeto VaccineDeclarationController
 * feita automaticamente com programa gerador de software inventado por
 * @author Jefferson Uchôa Ponte <j.pontee@gmail.com>
 */

namespace Vacinometro\controller;
use Vacinometro\dao\VaccineDeclarationDAO;
use Vacinometro\model\VaccineDeclaration;
use Vacinometro\view\VaccineDeclarationView;
use Sessao;

class VaccineDeclarationController {

	protected  $view;
    protected $dao;

	public function __construct(){
		$this->dao = new VaccineDeclarationDAO();
		$this->view = new VaccineDeclarationView();
	}


    public function delete(){
	    if(!isset($_GET['delete'])){
	        return;
	    }
        $selected = new VaccineDeclaration();
	    $selected->setId($_GET['delete']);
        if(!isset($_POST['delete_vaccine_declaration'])){
            $this->view->confirmDelete($selected);
            return;
        }
        if($this->dao->delete($selected))
        {
			echo '

<div class="alert alert-success" role="alert">
  Sucesso ao excluir Vaccine Declaration
</div>

';
		} else {
			echo '

<div class="alert alert-danger" role="alert">
  Falha ao tentar excluir Vaccine Declaration
</div>

';
		}
    	echo '<META HTTP-EQUIV="REFRESH" CONTENT="2; URL=index.php?page=vaccine_declaration">';
    }



	public function fetch() 
    {
		$list = $this->dao->fetch();
		$this->view->showList($list);
	}


	public function add() {
            
        if(!isset($_POST['enviar_vaccine_declaration'])){
            $this->view->showInsertForm();
		    return;
		}
		if (! ( isset ( $_POST ['id_user_sig'] ) && isset ( $_POST ['dose_number'] ) && isset ( $_FILES ['card_file'] ) && isset ( $_POST ['status'] ) && isset ( $_POST ['created_at'] ))) {
			echo '
                <div class="alert alert-danger" role="alert">
                    Failed to register. Some field must be missing. 
                </div>

                ';
			return;
		}
		$vaccineDeclaration = new VaccineDeclaration ();
		$vaccineDeclaration->setIdUserSig ( $_POST ['id_user_sig'] );
		$vaccineDeclaration->setDoseNumber ( $_POST ['dose_number'] );

        if($_FILES['card_file']['name'] != null){

            if(!file_exists('uploads/vaccine_declaration/card_file/')) {
    		    mkdir('uploads/vaccine_declaration/card_file/', 0777, true);
    		}
    
    		if(!move_uploaded_file($_FILES['card_file']['tmp_name'], 'uploads/vaccine_declaration/card_file/'. $_FILES['card_file']['name']))
    		{
    		    echo '
                    <div class="alert alert-danger" role="alert">
                        Failed to send file.
                    </div>
    		        
                    ';
    		    return;
    		}
            $vaccineDeclaration->setCardFile ( "uploads/vaccine_declaration/card_file/".$_FILES ['card_file']['name'] );
        }
		$vaccineDeclaration->setStatus ( $_POST ['status'] );
		$vaccineDeclaration->setCreatedAt ( $_POST ['created_at'] );
            
		if ($this->dao->insert ($vaccineDeclaration ))
        {
			echo '

<div class="alert alert-success" role="alert">
  Sucesso ao inserir Vaccine Declaration
</div>

';
		} else {
			echo '

<div class="alert alert-danger" role="alert">
  Falha ao tentar Inserir Vaccine Declaration
</div>

';
		}
        echo '<META HTTP-EQUIV="REFRESH" CONTENT="3; URL=index.php?page=vaccine_declaration">';
	}



            
	public function addAjax() {
        
		$session = new Sessao();
		
        if(!isset($_POST['enviar_vaccine_declaration'])){
            return;    
        }
        
		    
		
		if (! ( isset ( $_POST ['dose_number'] ) && isset ( $_FILES ['card_file'] ))) {
			echo ':incompleto';
			return;
		}
            
		$vaccineDeclaration = new VaccineDeclaration ();
		$vaccineDeclaration->setIdUserSig ($session->getIdUserSig());
		$vaccineDeclaration->setDoseNumber ( $_POST ['dose_number'] );
        if($_FILES['card_file']['name'] != null){
    		if(!file_exists('uploads/vaccine_declaration/card_file/')) {
    		    mkdir('uploads/vaccine_declaration/card_file/', 0777, true);
    		}
    		        
    		if(!move_uploaded_file($_FILES['card_file']['tmp_name'], 'uploads/vaccine_declaration/card_file/'. $_FILES['card_file']['name']))
    		{
    		    echo ':falha';
    		    return;
    		}
            $vaccineDeclaration->setCardFile ( "uploads/vaccine_declaration/card_file/".$_FILES ['card_file']['name'] );
        }
		$vaccineDeclaration->setStatus (VaccineDeclaration::STATUS_SUBMITTED);
		$vaccineDeclaration->setCreatedAt ( date('Y-m-d H:i:s') );
            
		if ($this->dao->insert ( $vaccineDeclaration ))
        {
			$id = $this->dao->getConnection()->lastInsertId();
            echo ':sucesso:'.$id;
            
		} else {
			 echo ':falha';
		}
	}
            
            

            
    public function edit(){
	    if(!isset($_GET['edit'])){
	        return;
	    }
        $selected = new VaccineDeclaration();
	    $selected->setId($_GET['edit']);
	    $this->dao->fillById($selected);
	        
        if(!isset($_POST['edit_vaccine_declaration'])){
            $this->view->showEditForm($selected);
            return;
        }
            
		if (! ( isset ( $_POST ['id_user_sig'] ) && isset ( $_POST ['dose_number'] ) && isset ( $_POST ['card_file'] ) && isset ( $_POST ['status'] ) && isset ( $_POST ['created_at'] ))) {
			echo "Incompleto";
			return;
		}

		$selected->setIdUserSig ( $_POST ['id_user_sig'] );
		$selected->setDoseNumber ( $_POST ['dose_number'] );
		$selected->setCardFile ( $_POST ['card_file'] );
		$selected->setStatus ( $_POST ['status'] );
		$selected->setCreatedAt ( $_POST ['created_at'] );
            
		if ($this->dao->update ($selected ))
        {
			echo '

<div class="alert alert-success" role="alert">
  Sucesso 
</div>

';
		} else {
			echo '

<div class="alert alert-danger" role="alert">
  Falha 
</div>

';
		}
        echo '<META HTTP-EQUIV="REFRESH" CONTENT="3; URL=index.php?page=vaccine_declaration">';
            
    }
        

    public function main(){
        
        if (isset($_GET['select'])){
            echo '<div class="row">';
                $this->select();
            echo '</div>';
            return;
        }
        echo '
		<div class="row">';
        echo '<div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">';
        
        if(isset($_GET['edit'])){
            $this->edit();
        }else if(isset($_GET['delete'])){
            $this->delete();
	    }else{
            $this->add();
        }
        $this->fetch();
        
        echo '</div>';
        echo '</div>';
            
    }
    public function mainAjax(){

        $this->addAjax();
        
            
    }


            
    public function select(){
	    if(!isset($_GET['select'])){
	        return;
	    }
        $selected = new VaccineDeclaration();
	    $selected->setId($_GET['select']);
	        
        $this->dao->fillById($selected);

        echo '<div class="col-xl-7 col-lg-7 col-md-12 col-sm-12">';
	    $this->view->showSelected($selected);
        echo '</div>';
            

            
    }
}
?>