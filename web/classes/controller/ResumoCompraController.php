<?php
/**
 * Classe utilizada para centralizar as demais instancias das classes dos pacotes(DAO, Model, View, Util).
 * Esta classe será instaciada no index.php.
 * 
 * @author Alan Cleber Morais Gomes
 * @author Francisco Kleber Rodrigues de Castro
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package Controle
 */

/**
 * Está função será utilizada para gerar uma tela, onde será mostrado ao cliente,
 * toda a transação realizada pelo operador, evitando assim, possíveis equívocos
 * por ambas as partes.
 *
 * @link https://www.catraca.unilab.edu.br/docs/index.html
 */
class ResumoCompraController {
	
	/**
	 * Metodo principal utilizada para controlar o acesso a classe através do nível de acesso do usuario.
	 *
	 * @param Sessao $nivelDeAcesso
	 *        	Recebe uma Sessão que contém o nível de acesso do usuario,
	 *        	esta Sessão é iniciada na página principal, durante o login do usuario.
	 *        	
	 * @link https://www.catraca.unilab.edu.br/docs/index.html
	 */
	public static function main($nivelDeAcesso) {
		switch ($nivelDeAcesso) {
			case Sessao::NIVEL_SUPER :
				$resumo = new ResumoCompraController ();
				$resumo->telaResumo ();
				break;
			case Sessao::NIVEL_ADMIN :
				$resumo = new ResumoCompraController ();
				$resumo->telaResumo ();
				break;
			case Sessao::NIVEL_GUICHE :
				$resumo = new ResumoCompraController ();
				$resumo->telaResumo ();
				break;
			case Sessao::NIVEL_POLIVALENTE :
				$resumo = new ResumoCompraController ();
				$resumo->telaResumo ();
				break;
			default :
				UsuarioController::main ( $nivelDeAcesso );
				break;
		}
	}
	
	/**
	 * Gera a tala Resumo, esta classe contém variáveis de sessão
	 * que devem ser geradas na classe que realizar a chamada desta função.
	 *
	 * Pois ela foi cria para trabalhar em paralelo com a classe instaciadora,
	 * sem a nessedidade de javascript.
	 *
	 * @link https://www.catraca.unilab.edu.br/docs/index.html
	 */
	public function telaResumo() {
		$transacao = @$_SESSION ['transacao'];
		$cartao = @$_SESSION ['cartao'];
		$usuario = @$_SESSION ['nome_usuario'];
		$tipo = @$_SESSION ['tipo_usuario'];
		$valorInserido = @$_SESSION ['valor_inserido'];
		$novoSaldo = @$_SESSION ['novo_saldo'];
		$saldoAtual = @$_SESSION ['saldo_anterior'];
		$autorizado = @$_SESSION ['autorizado'];
		
		echo '	<div id="resumo">
					<div class="doze colunas borda relatorio">				
						<div class="doze colunas">				
				
							<div class="duas colunas">
								<a href="http://www.unilab.edu.br">
									<img class="" src="img/logos_cooperacao_left.png" style="width:200px;">
								</a>
							</div>
	
							<div class="oito colunas">
								<h2 style="font-size:36px">Restaurante Universitário</h2>
							</div>
							<div class="duas colunas">
								<img class="" src="img/logos_cooperacao_right.png" style="width:200px;">								
							</div>
								<hr class="um"><br>
							</div>';
		
		if ($cartao != "") {
			echo '				<div class="doze colunas dados-usuario">				
								<h1 id="titulo-dois" class="centralizado" style="font-size:28px">Dados do Usuário</h1><br>				
								<hr class="um">									
							</div>
							<div class="doze colunas fundo-cinza1" style="font-size:28px;">
								<p><strong>Código da Operação: </strong>' . $transacao . '</p>
								<p><strong>Cartão: </strong>' . $cartao . '</p>
								<p><strong>Cliente: </strong>' . $usuario . '</p>
								<p><strong>Tipo Usuario: </strong>' . $tipo . '</p>
								<p><strong>Saldo Atual: R$ </strong>' . number_format ( $saldoAtual, 2, ',', '.' ) . '</p>					
							</div>';
		} else {
			echo '	<div class="doze colunas">							
										
						<div class="resumo">
							<span class=" texto-azul2">Guichê de Atendimento</span>
							<img class="imagem-responsiva" src="img/Simbolo_da_UNILAB.png" alt="">							
						</div>
					
					<!--Img para Baixar App CATRACA unilab
						<span class="maximo texto_app">Baixe o App CATRACA UNILAB</span>							
						<img class="qr_code" src="img/qr_code2.png">
					-->
					</div>';
		}
		
		if ($valorInserido != "") {
			echo '					<div class="oito colunas">
								<span class="fundo-verde2 texto-branco" style="font-size:60px;">Créditos a Inserir: R$ ' . number_format ( $valorInserido, 2, ',', '.' ) . '</span>
							</div>
										
							<div class="doze colunas">
								<span style="font-size:36px;">Novo Saldo: R$ ' . number_format ( $novoSaldo, 2, ',', '.' ) . '</span>';
			if ($autorizado == false) {
				echo '			<span class="centralizado fundo-verde2 texto-branco" style="font-size:32px;"><strong>Verifique sua compra e passe o cartão para confirmar!</span>';
			} else {
				echo '			<span class="centralizado fundo-verde2 texto-branco" style="font-size:48px;"><strong>Créditos inseridos com sucesso!</span>';
			}
		}
		
		echo '				</div>										
						</div>
					</div>

					
				
				';
	}
}

?>