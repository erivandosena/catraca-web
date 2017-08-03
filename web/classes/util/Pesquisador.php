<?php

/**
 * 
 * @author Jefferson Uchôa Ponte
 *
 */
class Pesquisador {
	private $conexao;
	private $nomeDaEntidade;
	private $campo;
	private $sgdb;
	public function Pesquisador(PDO $conexao, $nomeDaEntidade, $campo, $sgdb) {
		$this->conexao = $conexao;
		$this->nomeDaEntidade = $nomeDaEntidade;
		$this->campo = $campo;
		$this->sgdb = $sgdb;
	}
	
	public function mostraformPesquisa(){
		echo '
				<form action="" method="get">
				<input type="text" name="nome" placeholder="nome"/>
				<input type="submit" value="pesquisar"></form>';
	}
	
	public function pesquisar() {
		if (! isset ( $_GET ['nome'] )) {
			return;
		}
		$pesquisa = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $_GET ['nome'] );
		$this->buscar( strtoupper ( $pesquisa ));
		
	}
	public function buscar($pesquisa) {
		$entidade = $this->nomeDaEntidade;
		$campo = $this->campo;
		
		if ($this->sgdb == "mssql"){
			$sql = "SELECT top 10 * FROM $entidade WHERE $campo like '%$pesquisa%'";
		}
		else{
			$sql = "SELECT * FROM $entidade WHERE $campo like '%$pesquisa%'" ;
		}
		echo "<br>";
		echo $sql;
		echo "<br>";
		$result = $this->conexao->query ($sql);
		$i = 0;
		echo '<table border = 1>';
		foreach ( $result as $linha ) {
			if ($i == 0) {
				
				echo '<tr>';
				foreach ( $linha as $chave => $valor ) {
					if (! is_int ( $chave ))
						echo '<th>' . $chave . '</th>';
				}
				echo '</tr>';
				$i ++;
			}
			
			echo '<tr>';
			foreach ( $linha as $chave => $valor ) {
				if (! is_int ( $chave ))
					echo '<td>' . $valor . '</td>';
			}
			echo '</tr>';

		}
		echo '</table>';
	}
}

?>