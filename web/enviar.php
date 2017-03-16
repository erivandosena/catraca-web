<?php


ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

date_default_timezone_set ( 'America/Araguaina' );


function __autoload($classe) {
	if (file_exists ( 'classes/dao/' . $classe . '.php' ))
		include_once 'classes/dao/' . $classe . '.php';
	if (file_exists ( 'classes/model/' . $classe . '.php' ))
		include_once 'classes/model/' . $classe . '.php';
	if (file_exists ( 'classes/controller/' . $classe . '.php' ))
		include_once 'classes/controller/' . $classe . '.php';
	if (file_exists ( 'classes/util/' . $classe . '.php' ))
		include_once 'classes/util/' . $classe . '.php';
	if (file_exists ( 'classes/view/' . $classe . '.php' ))
		include_once 'classes/view/' . $classe . '.php';
}

$sessao = new Sessao ();

if (isset ( $_GET ["sair"] )) {
	
	$sessao->mataSessao ();
	header ( "Location:./index.php" );
}

if($sessao->getNivelAcesso() != Sessao::NIVEL_SUPER)
	exit(0);


?>
<!DOCTYPE html>
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <?php

        
            
            define('UPLOAD_DIR', 'fotos/');
            $img = $_POST['img64'];
            $img = str_replace('data:image/png;base64,', '', $img);
            $img = str_replace(' ', '+', $img);
            $data = base64_decode($img);
            $file = UPLOAD_DIR .$_POST['id_usuario']. '.png';
            $success = file_put_contents($file, $data);
            print $success ? "Foto salva com sucesso!" : 'Erro ao tentar salvar arquivo.';
            echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $_POST['id_usuario'] . '">';
        
            
         ?>
    </body>
</html>

