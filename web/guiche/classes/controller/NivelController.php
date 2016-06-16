<?php

class NivelController{
	
	public static function main($nivel){
		
		$nivel = new NivelController();
		$nivel->telaNivel();
		
	}
	
	public function telaNivel(){
		
		$controller = new NivelController();
		
		echo'		<div class="borda relatorio">
						<form action="" method="post" class="formulario">							
							<label for="login_usuario">
								Login Usuario: <input type="text" name="login_usuario" value="">
							</label><br>
							<input type="submit" value="Buscar" name="buscar">				
						</form>						
					</div>';
				
		if(isset($_POST['login_usuario'])){
			
			$dao = new DAO();
			$usuario = new Usuario();
			$tipo = new Tipo();
			$nivelAtual = "";
			$idUsuario = "";
			$usuario->setLogin($_POST['login_usuario']);
			$loginUsuario = $usuario->getLogin();
			$sql = "SELECT * FROM usuario WHERE usua_login = '$loginUsuario'";			
			$result = $dao->getConexao()->query($sql);
			foreach ($result as $linha){
				$idUsuario = $linha['usua_id'];
				$usuario->setNome($linha['usua_nome']);
				$usuario->setLogin($linha['usua_login']);				
				$nivel = $linha['usua_nivel'];
				
				switch ($nivel){
					
					case 1 : $nivelAtual = "Padrão";
						break;
						
					case 2 : $nivelAtual = "Admin";
						break;
						
					case 3 : $nivelAtual = "Super";
						break;
					
					case 4 : $nivelAtual = "Guichê";
						break;
					
					case 5 : $nivelAtual = "Suporte";
						break;
					
					default: $nivelAtual = "Padrão";
						break;
						
				}				
			}
			
			if(!$idUsuario){
			
				$controller->mensagem("-erro", "Usuario não encontrado!");
				
			}else{
			
			echo'	<div class="borda relatorio">
			
						<span>Usuario: '.$usuario->getNome().'</span>
						<span>Login: '.$usuario->getLogin().'</span>
						<span>Nível Atual: '.$nivelAtual.'</span><br>
						<hr class="um"><br>
			
					<form class="formulario-organizado" method="post">
						<label>
							<object data="" type="" class="rotulo">Novo Nível:</object>
							<select name="novo_nivel" id="novo_nivel">
								<option value="1">Padrão</option>
								<option value="2">Admin</option>
								<option value="3">Super</option>
								<option value="4">Guichê</option>
								<option value="5">Suporte</option>
							</select>
							</label>
						<input type="hidden" name="login_usuario" value="'.$_POST['login_usuario'].'">
						<input class="botao" type="submit" name="alterar" value="Alterar Nível">
			
					</form><br>';				
			}
		}	
	}
	
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