<?php

/**
* Conexao com o BD.
*
* Classe para conexao com o Banco de Dados PostgreSQL com acesso nativo PHP/PDO.
* Constantes necessarias: HOST, PORTA, BD, USUARIO, SENHA.
*
* PHP versao 5
*
* LICENCA: Este arquivo fonte esta sujeito a versao 3.01 da licença PHP 
* que esta disponivel atraves da world-wide-web na seguinte URI:
* Http://www.php.net/license/3_01.txt. Se você não recebeu uma copia da 
* Licenca PHP e nao consegue obte-la atraves da web, por favor, envie uma 
* nota para license@php.net para que possamos enviar-lhe uma copia imediatamente.
*
* @category   CategoryName
* @package    PackageName
* @author     Erivando Sena <erivandoramos@unilab.edu.br>, demais participantes
* @copyright  2015-2015 Unilab
* @license    http://www.php.net/license/3_01.txt PHP License 3.01
* @version    SVN: $Id$
* @link       http://www.unilab.edu.br
* @see        NetOther, Net_Sample::Net_Sample()
* @since      File available since Release 1.2.0
* @deprecated File deprecated in Release 2.0.0
*/

function getDB() {

	define('HOST','localhost');	#(localhost)200.129.19.65
	define('PORTA','5432');
	define('BD','desenvolvimento');
	define('USUARIO','catraca');	#catraca
	define('SENHA','CaTraCa@unilab2015');	#CaTraCa@unilab2015

	$conexao = 'pgsql:dbname='.BD.';host='.HOST.';port='.PORTA;

	try{
		$dbConnection = new PDO($conexao,USUARIO,SENHA);
		$dbConnection->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
		return $dbConnection;
	}catch(PDOexception $error_conecta){
		echo htmlentities('Erro conectando no PostgreSQL: '.$error_conecta->getMessage());
	}
}
?>