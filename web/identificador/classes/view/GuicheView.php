<?php

class GuicheView{
	
	public function formDescricao($listaDescricao){
		
		@$_SESSION['transacao'] = "";
		
		echo '	<div id="caixa"class="doze colunas borda">
					<h2 id="titulo-caixa" class="texto-branco fundo-azul2 centralizado">Venda de Cr&eacuteditos<br></h2>
						<div class="sete colunas">
							<div id="infovenda" class="fundo-cinza1">
		
								<div class="doze colunas">
									<h3 class="centralizado">Descri&ccedil&atildeo da Opera&ccedil&atildeo</h1><br>
										<table class="tabela quadro no-centro">
										    <thead>
												<tr>
												    <th>Cod</th>
												    <th>Valor</th>
												    <th>Descri&ccedil&atildeo</th>
												    <th>Data</th>
													<th>Hora</th>
													<th>Cliente</th>
												</tr>
											</thead>
											<tbody>';
		$i = 1;
		foreach ($listaDescricao as $linha){				
			echo'								<tr>
											        <td>'.$linha['tran_id'].'</td>
											       	<td>R$ '.number_format($linha['tran_valor'], 2,',','.').'</td>
											        <td>'.$linha['tran_descricao'].'</td>
											        <td>'.date("d/m/Y",strtotime($linha['tran_data'])).'</td>
													<td>'.date('H:i:s',strtotime($linha['tran_data'])).'</td>
											        <td>'.ucwords(strtolower(htmlentities($linha['usua_nome']))).'</td>
											    </tr>';
			$i++;
			$tran[] = $linha['tran_id'];
		}
		
		@$_SESSION['transacao'] = $tran[0] + 1;
		if (@$_SESSION['transacao'] == 1){
			@$_SESSION['transacao'] = null;
		}
		
		echo'								</tbody>
										</table>
									</div>
								</div>';
	}
	
	public function formBuscarCartao(){
		
		echo'		<div class="cinco colunas">
						<form method="" class="formulario-organizado" >
							<input type="hidden" name="pagina" value="guiche" />
							<label for="cartao">
								N&uacutemero Cart&atildeo: <input type="number" name="cartao" id="cartao" autofocus>
							</label>							
							<input type="submit" value="Pesquisar">
						<hr>
					</form>';		
	}
	
	public function formInserirValor(){
		
		echo'	<form method="" class="formulario-organizado" >
					<input type="hidden" name="pagina" value="guiche" />
					<label for="valor">
					Valor Comprado: <input type="number" name="valor" id="valor" step="0.01">
					</label>
					<label for="valorrec">
					Valor Recebido: <input type="number" name="valorrec" id="valorrec" step="0.01">
					</label>
					<hr>
					<h2>Troco: <output id="troco"></output></h2>
					<input type="hidden" name="cartao" value="'.$_GET['cartao'].'" />					
					<input type="submit" value="Finalizar" class="botao b-sucesso" name="finalizar" >
				</form>';
		
	}
	
	public function formConsulta(Usuario $usuario, Tipo $tipo, Cartao $cartao){
		echo '	<span>Usuario: '.ucwords(strtolower(htmlentities($usuario->getNome()))).'</span>
				<span>Tipo Usuario: '.$tipo->getNome().'</span>
				<span>Saldo: '.number_format($cartao->getCreditos(), 2,',','.').'</span>
				<span>Valor Credito: '.number_format($tipo->getValorCobrado(), 2,',','.').'</span>
				<hr>';
	}
	
	public function mensagem($tipo, $texto){
		//Tipo = -sucesso, -erro, -ajuda
		echo '	<div class="alerta-'.$tipo.'">
				    	<div class="icone icone-notification ix16"></div>
				    	<div class="titulo-alerta">Aten&ccedil&atildeo</div>
				    	<div class="subtitulo-alerta">'.$texto.'</div>
				</div>
				';
			
	}
}

?>