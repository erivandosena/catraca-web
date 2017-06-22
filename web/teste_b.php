<?php





date_default_timezone_set ( 'America/Araguaina' );
ini_set('display_errors',1);
ini_set('display_startup_erros',1);
error_reporting(E_ALL);

function __autoload($classe) {
	if (file_exists ( 'classes/dao/' . $classe . '.php' )){
		include_once 'classes/dao/' . $classe . '.php';
	}
	if (file_exists ( 'classes/model/' . $classe . '.php' )){
		include_once 'classes/model/' . $classe . '.php';
	}
	if (file_exists ( 'classes/controller/' . $classe . '.php' )){
		include_once 'classes/controller/' . $classe . '.php';
	}
	if (file_exists ( 'classes/util/' . $classe . '.php' )){
		include_once 'classes/util/' . $classe . '.php';
	}
	if (file_exists ( 'classes/view/' . $classe . '.php' )){
		include_once 'classes/view/' . $classe . '.php';
	}
}


include_once "classes/util/NotificacaoApp.php";
use FireBase\NotificacaoApp;



$n = new NotificacaoApp();
$n->envia_notificacao("App Catraca UNILAB", 'Ola, Jeff', "cJMV66p0l14:APA91bHKhuw1iMdpdwHpp3_iRc4o5rogpMzmE-0bDnoXh-YdUgkiFctwneS1ZCAfaiCgg7g4Jv8AFHdVNch0n2Ck0N7iCHY_h8VT3Gm6401dY6nGdKtTKVSj0gMRcGfjFq9E0c5VQWpO");



?>