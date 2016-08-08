<?php

class NivelView{
	
	
	
	public function mensagem($tipo, $texto){
		//Tipo = -sucesso, -erro, -ajuda
		echo '	<div class="borda">
					<div class="alerta'.$tipo.'">
					   	<div class="icone icone-notification ix16"></div>
					   	<div class="titulo-alerta">Aten&ccedil&atildeo</div>
					   	<div class="subtitulo-alerta">'.$texto.'</div>
					</div>
				</div>';
	
	}
	
}


?>