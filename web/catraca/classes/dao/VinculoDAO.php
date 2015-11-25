<?php
/**
 *
 * Cadastro de vinculo ser� feito por dois usuarios diferetnes.
 * Administra��o ou Guiche. Com suas particularidades.
 *
 * A seguir o cadastro de vinculo pelo usuario administrador.
 *
 * 1- Verifica��o de Id de usuario de base externa.
 * Esse usuario existe na base local? Captura-se o Id da base local para: $idUsuarioBaseLocal;
 * N�o existe na base local: Cadastra-se e captura-se o id da base local para: $idUsuarioBaseLocal;
 *
 *
 * 2- Verifica��o de cart�o.
 * O cart�o existe. Verifica se o Tipo cooresponde. Faz UPDATE no tipo. Retorne o seu ID. 
 * O cart�o n�o existe. Cadastre e Retorne o seu ID. 
 * 
 * 
 *
 * 3 - Verifica��o de vinculos do usuario.
 * - Não permitir cadastro de vinculo no usuario se ele tiver vinculo valido. 
 * Terá que cancelar o vinculo atual. Isto fará um update na data. 
 * 
 *
 * 4 - Verifica��o de vinculos do Cart�o.
 * - Não permitir cadastro de vinculo se o cartão tiver vinculo válido. 
 *
 *
 * 5 - Adicionar vinculo novo vinculo. 
 *
 *
 *
 */
class VinculoDAO extends DAO {
	
	public function retornaVinculosValidosDeUsuario(Usuario $usuario){
		$lista = array();
		$idUsuario = $usuario->getIdBaseExterna();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql =  "SELECT * FROM usuario INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
				LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
				LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $idUsuario)
				AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)";
		$result = $this->getConexao ()->query ($sql );
		
		foreach($result as $linha){
			$vinculo = new Vinculo();
			$vinculo->setResponsavel($usuario);
			$vinculo->setCartao(new Cartao());
			$vinculo->getCartao()->setTipo(new Tipo());
			$vinculo->getCartao()->getTipo()->setNome($linha ['tipo_nome']);
			$vinculo->getCartao()->setNumero($linha ['cart_numero']);
			$vinculo->setInicioValidade($linha ['vinc_inicio']);
			$vinculo->setFinalValidade($linha['vinc_fim']);
			$lista[] = $vinculo;
						

		}
		return $lista;
	}
	public function retornaVinculosValidosDeCartao(Cartao $cartao){
		$lista = array();
		$idCartao = $cartao->getId();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql =  "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (cartao.cart_id = $idCartao)
		AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)";
		$result = $this->getConexao ()->query ($sql );
	
		foreach($result as $linha){
			$vinculo = new Vinculo();
			$vinculo->setResponsavel(new Usuario());
			$vinculo->getResponsavel()->setIdBaseExterna($linha['id_base_externa']);
			$vinculo->setCartao(new Cartao());
			$vinculo->getCartao()->setTipo(new Tipo());
			$vinculo->getCartao()->getTipo()->setNome($linha ['tipo_nome']);
			$vinculo->getCartao()->setNumero($linha ['cart_numero']);
			$vinculo->setInicioValidade($linha ['vinc_inicio']);
			$vinculo->setFinalValidade($linha['vinc_fim']);
			$lista[] = $vinculo;
	
	
		}
		return $lista;
	}
	public function adicionaVinculo(Vinculo $vinculo) {
		$dataDeHoje = date("Y-m-d H:i:s");
		$usuarioBaseExterna = $vinculo->getResponsavel()->getIdBaseExterna();
		$numeroCartao = $vinculo->getCartao()->getNumero();
		$dataDeValidade = $vinculo->getFinalValidade();
		$tipoCartao = $vinculo->getCartao()->getTipo()->getId();
		$this->verificarUsuario($vinculo->getResponsavel());
		if(!$vinculo->getResponsavel()->getId())
			return 0;
		$idBaseLocal = $vinculo->getResponsavel()->getId();
		$this->verificaCartao($vinculo->getCartao());
		if(!$vinculo->getCartao()->getId())
			return 0;
		$idCartao = $vinculo->getCartao()->getId();
		if(!$this->getConexao()->exec("INSERT into vinculo (usua_id, cart_id, vinc_refeicoes, vinc_avulso, vinc_inicio, vinc_fim) VALUES($idBaseLocal, $idCartao, 1,FALSE,'$dataDeHoje', '$dataDeValidade')"))
			return 0;
		$idVinculo = $this->getConexao()->lastInsertId('vinculo_vinc_id_seq');
		if(!$this->getConexao()->exec("INSERT into vinculo_tipo (vinc_id, tipo_id) VALUES($idVinculo, $tipoCartao)")){
			$this->getConexao()->rollBack();
			return 0;
		}
		return true;
	}
	
	
	/**
	 * Retorna true se o cartão possuir vinculo válido. 
	 * Retorna false se o cartão não possui um vinculo válido. 
	 * 
	 * @param Cartao $cartao
	 * @return boolean
	 */
	public function cartaoTemVinculo(Cartao $cartao){
		$numero = $cartao->getNumero();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql =  "SELECT * FROM vinculo
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		WHERE (cartao.cart_numero = $numero)
		AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim) LIMIT 1";
		$resultSet = $this->getConexao()->query($sql);
		foreach($resultSet as $linha){
			$cartao->setId($linha['cart_id']);
			return true;
		}
		return false;
	}
	
	
	
	/**
	 * Atrav�s de um numero de cart�o iremos retornar seu verdadeiro ID. 
	 * Mas antes iremos alterar seu tipo. 
	 * 
	 * Caso ele nem exista a gente cadastra com o tipo oferecido aqui. 
	 * 
	 * @param int $numeroCartao
	 * @param int $idTipo
	 */
	public function verificaCartao(Cartao $cartao){
		$numeroCartao = $cartao->getNumero();
		$idTipo = $cartao->getTipo()->getId();
		
		$result = $this->getConexao()->query("SELECT * FROM cartao WHERE cart_numero = $numeroCartao");
		foreach($result as $linha){
			if($linha['tipo_id'] != $idTipo){
				if(!$this->getConexao()->exec("UPDATE cartao set tipo_id = $idTipo WHERE cart_numero = $numeroCartao"))
					return false;
			}
			$cartao->getTipo()->setId($linha['tipo_id']);
			$cartao->setId($linha['cart_id']);
			return $linha['cart_id'];
		}
		if($this->getConexao()->query("INSERT INTO cartao(cart_numero, cart_creditos, tipo_id) VALUES($numeroCartao, 0, $idTipo)")){
			foreach($this->getConexao()->query("SELECT * FROM cartao WHERE cart_numero = $numeroCartao") as $otraLinha){
				$cartao->setId($otraLinha['cart_id']);
				return $otraLinha['cart_id'];
			}
		}
		return false;
		
		
	}
	/**
	 * Vamos pegar da base exter a ecopiar para a base local.
	 * Se Nem existir na base externa, � o usuario frescando. Preciso dar nem resposta pra ele. Aborto tudo logo.
	 * Fa�amos um insert aqui.
	 * Apos esse insert iremos pegar o id inserido na base e retornalo. 
	 * Retorna 0, deu nada certo. Essa parada acaba aqui. 
	 * @param int $idBaseExterna
	 * @return int
	 */
	public function verificarUsuario(Usuario $usuario){
		
		$idBaseExterna = $usuario->getIdBaseExterna();
		
		$result = $this->getConexao()->query("SELECT id_base_externa, usua_id FROM usuario WHERE id_base_externa = $idBaseExterna");
		foreach ($result as $linha){
			$usuario->setId($linha['usua_id']);
			return $linha['usua_id'];
		}
		$daoSistemasComum = new DAO(null, DAO::TIPO_PG_SISTEMAS_COMUM);
		$result2 = 	$daoSistemasComum->getConexao()->query("SELECT * FROM vw_usuarios_autenticacao_catraca WHERE id_usuario = $idBaseExterna");
		foreach($result2 as $linha){
			$nivel = Sessao::NIVEL_COMUM;
			$nome = $linha['nome'];
			$email = $linha['email'];
			$login = $linha['login'];
			$senha = $linha['senha'];
			$idBaseExterna = $linha['id_usuario'];
			if($this->getConexao()->exec("INSERT into usuario(usua_login,usua_senha, usua_nome,usua_email, usua_nivel, id_base_externa)
					VALUES	('$login', '$senha', '$nome','$email', $nivel, $idBaseExterna)"))
			{
				foreach($this->getConexao()->query("SELECT * FROM usuario WHERE id_base_externa = $idBaseExterna") as $linha3){
					$usuario->setId($linha3['usua_id']);
					return $linha3['usua_id'];
				}
			}
		}
		return 0;
		
		
	}
	
	
}

?>