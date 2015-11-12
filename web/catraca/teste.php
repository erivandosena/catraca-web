<?php  

$opcao = $_REQUEST['radio-1'];

if($opcao == "sim"){
	header("location:incluir_cartao.php?info=sim");
}else{
	header("location:incluir_cartao.php");
}

?>