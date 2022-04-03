<?php
            
/**
 * Classe feita para manipulação do objeto VaccineDeclarationController
 * @author Jefferson Uchôa Ponte <j.pontee@gmail.com>
 */

namespace Vacinometro\controller;
use Vacinometro\dao\VaccineDeclarationDAO;
use Vacinometro\model\VaccineDeclaration;
use Vacinometro\view\VaccineDeclarationView;
use Sessao;
use Usuario;
use UsuarioDAO;

class VaccineDeclarationController {

	protected  $view;
    protected $dao;

	public function __construct(){
		$this->dao = new VaccineDeclarationDAO();
		$this->view = new VaccineDeclarationView();
	}


	public function fetch() 
    {
		$vaccineDeclaration = new VaccineDeclaration();
		$vaccineDeclaration->setStatus(VaccineDeclaration::STATUS_SUBMITTED);
		$list = $this->dao->fetchByStatus($vaccineDeclaration);
		$this->view->showList($list);
	}

	public function addAjax() {
        
		$session = new Sessao();
		if($session->getNivelAcesso() === Sessao::NIVEL_DESLOGADO){
			return '';
		}
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
		if($_FILES['card_file']['name'] == null){
			echo ':falha';
			return;
		}
		if(!file_exists('../uploads_card_vaccine/')) {
			mkdir('../uploads_card_vaccine/', 0777, true);
		}
		$fileExp = explode(".", $_FILES['card_file']['name']);
		$fileExtension = end($fileExp);
		if(strtolower($fileExtension) != 'pdf') {
			return ':falha';
		}
		$newFileName = $session->getIdUserSig().'.pdf';

		if(!move_uploaded_file($_FILES['card_file']['tmp_name'], '../uploads_card_vaccine/'. $newFileName))
		{
			echo ':falha';
			return;
		}
		$vaccineDeclaration->setCardFile ( "../uploads_card_vaccine/".$newFileName );
        
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
	    $usuarioDao = new UsuarioDAO($this->dao->getConnection());
		$usuario = new Usuario();
		$usuario->setIdBaseExterna($selected->getIdUserSig());
		$usuarioDao->preenchePorIdBaseExterna($usuario);

        if(!isset($_POST['edit_vaccine_declaration'])){
            $this->view->showEditForm($selected, $usuario);
            return;
        }
            
		if (! (isset ( $_POST ['status'] ))) {
			echo "Incompleto";
			return;
		}

		$selected->setStatus ( $_POST ['status'] );

            
		if ($this->dao->update ($selected ))
        {
			echo '

<div class="alert alert-success" role="alert">
  Avaliação realizada com sucesso!
</div>

';
		} else {
			echo '

<div class="alert alert-danger" role="alert">
  Falha na tentativa de atualizar avaliação. 
</div>

';
		}
        echo '<META HTTP-EQUIV="REFRESH" CONTENT="3; URL=index.php?pagina=vaccine_declaration">';
            
    }
        

    public function main(){
		$this->mainAdmin();
		$session = new Sessao();
		if($session->getNivelAcesso() === Sessao::NIVEL_DESLOGADO){
			return;
		}
		$vaccineDeclaration = new VaccineDeclaration();
		$vaccineDeclaration->setIdUserSig($session->getIdUserSig());
		$list = $this->dao->fetchByIdUserSig($vaccineDeclaration);
		foreach($list as $key => $element)  {
			if($element->getStatus() === VaccineDeclaration::STATUS_DISAPPROVED) {
				unset($list[$key]);
			}
		}
        echo '
		<div class="row">';
        echo '<div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">';
        
		
		if(count($list) === 0){
			if(!isset($_POST['enviar_vaccine_declaration'])){
				$this->view->showInsertForm();
				return;
			}
		} else {
			echo '<div class="alert alert-primary m-3" role="alert">
			O seu cartão de vacinação foi enviado.
		  </div>';
		}
		$list2 = $this->dao->fetchByIdUserSig($vaccineDeclaration);
		$this->view->showListMy($list2);

        echo '</div>';
        echo '</div>';
            
    }
	public function mainAdmin() {
		$session = new Sessao();
		if(
			!(
				$session->getNivelAcesso() === Sessao::NIVEL_ADMIN || 
				$session->getNivelAcesso() === Sessao::NIVEL_POLIVALENTE  || 
				$session->getNivelAcesso() === Sessao::NIVEL_GUICHE  || 
				$session->getNivelAcesso() === Sessao::NIVEL_CADASTRO 
			)
		) {
				return;
		}

		echo '
		<div class="row">';
        echo '<div class="col-xl-12 col-lg-12 col-md-12 col-sm-12">';
        

				
		if(isset($_GET['edit'])){
			$this->edit();
		}
		$this->fetch();

		echo '</div>';
        echo '</div>';
	}
	
    public function mainAjax(){
        $this->addAjax();
    }
}
?>