<?php
/** 
 * Classe utilizada para centralizar as demais Classes(DAO, Model, View, Util).
 * Esta classe será instaciada no index.php.
 * 
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */
/**
 * Esta classe é utilizada para a importação dos quandos
 * quando ocorrer a falta de conexão com o servidor.
 * 
 * Através do Bloco de Notas criado o arquivo .csv contendo
 * os números dos cartões que utilizaram o RU.
 * 
 * O valor da refeição será creditado de cada cartão.
 */
class ImportarCSVController {
	
	/**
	 * Metodo principal utilizada para controlar o acesso a classe através do nível de acesso do usuario.
	 *
	 * @param Sessao $nivelDeAcesso
	 *        	Recebe uma Sessão que contém o nível de acesso do usuario,
	 *        	esta Sessão é iniciada na página principal, durante o login do usuario.
	 */
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_ADMIN :
				$controller = new ImportarCSVController ();
				$controller->importar ();
				break;
			
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	/**
	 * Importa o arquivo para processar os dados e debitar os valores de cada
	 * cartão.
	 */
	public function importar() {
		echo '<h1>Importar</h1>';
		$row = 1;
		$cartoes = array ();
		if (($handle = fopen ( "almoco2.csv", "r" )) !== FALSE) {
			while ( ($data = fgetcsv ( $handle, 1000, "," )) !== FALSE ) {
				$num = count ( $data );
				$row ++;
				for($c = 0; $c < $num; $c ++) {
					$cartao = new Cartao ();
					$cartao->setNumero ( $data [$c] );
					$cartoes [] = $cartao;
				}
			}
			fclose ( $handle );
		}
		$dao = new CatracaVirtualDAO ();
		$dao->getConexao ()->beginTransaction ();
		
		$i = 0;
		echo '<table border=1>';
		echo '<tr><th>Cartao</th><th>Usuario</th><th>Creditos</th><th>Tipo</th></tr>';
		foreach ( $cartoes as $cartao ) {
			$vinculo = new Vinculo ();
			$vinculo->setCartao ( $cartao );
			
			$dao->verificaVinculo ( $vinculo );
			if ($cartao->getCreditos () == 0) {
				$i ++;
			}
			$isento = false;
			$valorPago = $vinculo->getCartao ()->getTipo ()->getValorCobrado ();
			if ($dao->vinculoEhIsento ( $vinculo )) {
				$valorPago = 0;
				$isento = true;
			}
			
			echo '<tr>';
			echo '<td>' . $cartao->getNumero () . '</td><td>' . $vinculo->getResponsavel ()->getNome () . ' </td><td>' . $cartao->getCreditos () . ' </td><td>' . $vinculo->getCartao ()->getTipo ()->getNome () . ' ' . $valorPago . '</td>';
			echo '</tr>';
			
			$data = '2016-12-02 12:00:00';
			
			$custo = 9.5;
			$idCatraca = 3;
			$idCartao = $cartao->getId ();
			$idVinculo = $vinculo->getId ();
			
			$sql = "INSERT into registro(regi_data, regi_valor_pago, regi_valor_custo, catr_id, cart_id, vinc_id)
			VALUES('$data', $valorPago, $custo, $idCatraca, $idCartao, $idVinculo)";
			
			$novoValor = floatval ( $vinculo->getCartao ()->getCreditos () ) - floatval ( $valorPago );
			$sqlUpdate = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";
			
			// echo '<tr>';
			// echo '<td colspan=3>';
			
			// echo $sql;
			// echo '</td>';
			// if($dao->getConexao()->exec($sql)){
			// echo '<td>Foi</td>';
			
			// }else{
			// echo '<td>Erro</td>';
			// $dao->getConexao()->rollBack();
			// return;
			
			// }
			
			// echo '</tr>';
			
			// echo '<tr>';
			// echo '<td colspan=3>';
			// echo $sqlUpdate;
			// echo '</td>';
			// if($dao->getConexao()->exec($sqlUpdate)){
			// echo '<td>Foi Update</td>';
			// }else{
			// echo '<td>Erro UPDATE</td>';
			// $dao->getConexao()->rollBack();
			// return;
			// }
			
			// echo '</tr>';
		}
		$dao->getConexao ()->commit ();
		echo '</table>';
		
		// echo 'Sucesso!';
	}
}