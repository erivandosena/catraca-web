<?php

	/**
	 * Notiticacoes FireBase Server.
	 *
	 * Script de envio de notiticacoes via api firebase.
	 * 
	 * PHP versao 5
	 *
	 * LICENCA: Este arquivo fonte esta sujeito a versao 3.01 da licenï¿½a PHP
	 * que esta disponivel atraves da world-wide-web na seguinte URI:
	 * Http://www.php.net/license/3_01.txt. Se vocï¿½ nï¿½o recebeu uma copia da
	 * Licenca PHP e nao consegue obte-la atraves da web, por favor, envie uma
	 * nota para license@php.net para que possamos enviar-lhe uma copia imediatamente.
	 *
	 * @category   Aplicacao Web
	 * @package    util
	 * @author     Erivando Sena <erivandoramos@unilab.edu.br> 
	 * @copyright  2010-2017 UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
	 * @license    http://www.php.net/license/3_01.txt  PHP License 3.01
	 *
	 */
	
	namespace FireBase;

	
	
	/**
	 * Classe de envio de mensagens para o aplicativo
	 */
	class NotificacaoApp {
		
		/**
		 * Envia as notificacoes para o aplicativo do usuario
		 * 
		 * @param string $titulo O titulo da mensagem
		 * @param string $mensagem A mensagem a ser enviada
		 * @param string $token O TOKEN obtido a apartir do aplicativo do usuario
		 */
		function envia_notificacao($titulo, $mensagem, $token) {
			
			define( 'API_ACCESS_KEY', 'AIzaSyAGsra0IfOxKCAu6N9j7LFC4QqS9733Ysg');
			
			$msg = array(
				'body' 	=> $mensagem,//'Atualize seu App ao receber notificaÃ§Ãµes.',
				'title'	=> $titulo //'App Catraca Unilab',
				);
			
			$fields = array(
						'to'			=> $token,//"eNgXbsTXOMs:APA91bFUDqyiTC3pUYv-OxCuJUmrfFvQfUVKGX9Y_NbJx8nBZ6Brx5RidKZTX8hR2KNKGOXlOuUad1TKFtVk1262nZTkBa-bRibZUcGw5E2camIXS_xnXgL5RcYvATHkn4DDeR-6ehCO",//$_REQUEST['token'],
						'notification'	=> $msg
					
			);
			
			$headers = array
					(
						'Authorization: key=' . API_ACCESS_KEY,
						'Content-Type: application/json'
							
			);
			
			//Envio de resposta ao servidor FireBase
			$ch = curl_init();
			curl_setopt( $ch,CURLOPT_URL, 'https://fcm.googleapis.com/fcm/send' );
			curl_setopt( $ch,CURLOPT_POST, true );
			curl_setopt( $ch,CURLOPT_HTTPHEADER, $headers );
			curl_setopt( $ch,CURLOPT_RETURNTRANSFER, true );
			curl_setopt( $ch,CURLOPT_SSL_VERIFYPEER, false );
			curl_setopt( $ch,CURLOPT_POSTFIELDS, json_encode($fields));
			$result = curl_exec($ch );
			echo $result;
			curl_close( $ch );
		}
	}
	
?>