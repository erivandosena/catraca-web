<?php


class CartaoController{
	private $dao;
	private $view;

	public function CartaoController(){
		$this->dao = new CartaoDAO();
		$this->view = new CartaoView();
	}
	
	
	public static function main(){
		
		$controller = new CartaoController();
		$controller->listagem();
		$controller->cadastro();
// 		$controller->delete();
		
		
		
	}
	
	
	
	
	
	
	
	public function listagem(){
		
		$lista = $this->dao->retornaLista();
		$this->view->mostraLista($lista);
		
		
	}
	public function cadastro(){
		
		$this->view->mostraFormulario($this->dao->retornaTipos());
		if(isset($_POST['cart_numero']))
			if($_POST['cart_numero'] != null && $_POST['cart_numero'] != "")
			{
				$cartao = new Cartao();
				$cartao->setNumero($_POST['cart_numero']);
				$cartao->setTipo(new Tipo());
				$cartao->getTipo()->setId($_POST['tipo_id']);
				
				if($this->dao->inserir($cartao))
					$this->view->cadastroSucesso();
				else
					$this->view->cadastroFracasso();
				echo '<meta http-equiv="refresh" content="2; url=/interface/index.php">';
			}
	}
	
	public function delete(){

		if(isset($_GET['delete_unidade'])){
			if(isset($_GET['unid_id'])){
				if(is_int(intval($_GET['unid_id']))){
					$id = intval($_GET['unid_id']);
					$unidade = new Unidade();
					$unidade->setId($id);
		
					if($this->dao->deletarUnidade($unidade))
						$this->view->deleteSucesso();
					else
						$this->view->deleteFracasso();
		
				}
			}
			echo '<meta http-equiv="refresh" content="2; url=/interface/index.php">';
		
		}
	}

	
	
	
}



?>