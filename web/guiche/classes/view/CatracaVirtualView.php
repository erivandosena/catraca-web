<?php


class CatracaVirtualView{
	
	
	public function formBuscaCartao(){
		echo '
				<script>
  $(document).bind(\'autofocus_ready\', function() {
    if (!("autofocus" in document.createElement("input"))) {
      $("#numero_cartao").focus();
    }
  });
</script>
	

									<form method="get" action="" class="formulario em-linha" >
										<input type="hidden" name="pagina" value="gerador" />
										<label for="numero_cartao">
											<object class="rotulo texto-preto">Buscar por Número: </object><br><br>
						
											<input class="texto-preto" type="number" name="numero_cartao" id="numero_cartao" autofocus /><br>
											 <script>$(document).trigger(\'autofocus_ready\');</script>
											<input type="submit" />
										</label>
	
									</form>';
	}
	
	public function formMensagem($tipo, $texto){
		//Tipo = -sucesso, -erro, -ajuda
		echo '	<div class="alerta'.$tipo.'">
				    	<div class="icone icone-notification ix16"></div>
				    	<div class="titulo-alerta">Aten&ccedil&atildeo</div>
				    	<div class="subtitulo-alerta">'.$texto.'</div>
				</div>';
			
	}
	
}


?>