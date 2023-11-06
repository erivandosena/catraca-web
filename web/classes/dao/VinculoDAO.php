<?php
/**
 * Classe utilizada para conxão com o Bando de Dados.
 * @author Jefferson Uchoa Ponte
 * @version 1.0
 * @copyright UNILAB - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira.
 * @package DAO
 */

/**
 * Cadastro de vinculo será feito por dois usuarios diferetnes.
 * Administração ou Guiche. Com suas particularidades.
 *
 * A seguir o cadastro de vinculo pelo usuario administrador.
 *
 * 1- Verificação de Id de usuario de base externa.
 * Esse usuario existe na base local? Captura-se o Id da base local para: $idUsuarioBaseLocal;
 * Não existe na base local: Cadastra-se e captura-se o id da base local para: $idUsuarioBaseLocal;
 *
 *
 * 2- Verificação de cartão.
 * O cartão existe. Verifica se o Tipo cooresponde. Faz UPDATE no tipo. Retorne o seu ID.
 * O cartão não existe. Cadastre e Retorne o seu ID.
 *
 *
 *
 * 3 - Verificão de vinculos do usuario.
 * - Não permitir cadastro de vinculo no usuario se ele tiver vinculo valido.
 * Terá que cancelar o vinculo atual. Isto fará um update na data.
 *
 *
 * 4 - Verificação de vinculos do Cartão.
 * - Não permitir cadastro de vinculo se o cartão tiver vinculo válido.
 *
 *
 * 5 - Adicionar vinculo novo vinculo.
 */
class VinculoDAO extends DAO {
	
	/**
	 * Realiza uma pesquisa através do IdBaseExterna do usuário, na base de dados local,
	 * na tabela de usuários, retornando os vinculos válidos do usuário.
	 *
	 * Para que um vínculo seja válido, é preciso que a Data de Validade do Vinculo seja maior que a Data e Hora Corrente,
	 * caso contrário será necessário renovar, se for possível.
	 *
	 * @param Usuario $usuario
	 *        	Objeto Usuario contendo IdBaseExterna.
	 * @return Vinculo[] Array com os Vinculos válidos do Usuario pesuisado.
	 */
	public function retornaVinculosValidosDeUsuario(Usuario $usuario) {
		$lista = array ();
		$idUsuario = $usuario->getIdBaseExterna ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
				ON vinculo.usua_id = usuario.usua_id
				LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
				LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $idUsuario)
				AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setResponsavel ( $usuario );
			
			$vinculo->setCartao ( new Cartao () );
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getCartao ()->setTipo ( new Tipo () );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->setCreditos ( $linha ['cart_creditos'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$vinculo->setDescricao ( $linha ['vinc_descricao'] );
			
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * Lista todos os Vínculos Vencidos do Usuário pesquisado.
	 * O Vínculo estará vencido quando a Data e Hora Corrente for maior que a Data de Vencimento.
	 *
	 * @param Usuario $usuario
	 *        	Objeto Usuario contendo IdBaseExterna.
	 * @return Vinculo[]
	 */
	public function retornaVinculosVencidos(Usuario $usuario) {
		$lista = array ();
		$idUsuario = $usuario->getIdBaseExterna ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $idUsuario)
		AND ('$dataTimeAtual' > vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setResponsavel ( $usuario );
			$vinculo->setCartao ( new Cartao () );
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getCartao ()->setCreditos ( $linha ['cart_creditos'] );
			$vinculo->getCartao ()->setTipo ( new Tipo () );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * 
	 * @param Usuario $usuario
	 *        	Objeto Usuario contendo IdBaseExterna.
	 */
	public function retornaVinculosFuturos(Usuario $usuario) {
		$lista = array ();
		$idUsuario = $usuario->getIdBaseExterna ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $idUsuario)
		AND ('$dataTimeAtual' < vinc_fim AND '$dataTimeAtual' < vinc_inicio)";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setResponsavel ( $usuario );
			$vinculo->setCartao ( new Cartao () );
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getCartao ()->setTipo ( new Tipo () );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * Torna inválido o vinculo do Cartão.
	 *
	 * Neste caso o campo vinc_fim ou isen_fim(no caso de isenção) será atualizado com a Data e Hora Corrente,
	 * tornando o vínculo inválido, pois o Vencimento será menor que a Data e Hora atuais.
	 *
	 * @param Vinculo $vinculo        	
	 * @return boolean
	 */
	public function invalidarVinculo(Vinculo $vinculo) {
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		
		if ($vinculo->getId ()) {
			$idVinculo = $vinculo->getId ();
			$idIsencao = $vinculo->getIsencao ()->getId ();
			$sql = "UPDATE isencao set isen_fim = '$dataTimeAtual' WHERE isen_id = $idIsencao";
			$this->getConexao ()->exec ( $sql );
		}
		
		$sql = "UPDATE vinculo set vinc_fim = '$dataTimeAtual' WHERE vinc_id = $idVinculo";
		if ($this->getConexao ()->exec ( $sql ))
			return true;
		return false;
	}
	
	/**
	 * Torna um vinculo insento inválido.
	 *
	 * Neste caso o campo isen_fim será atualizado com a Data e Hora Corrente,
	 * tornando o vínculo inválido, pois o Vencimento será menor que a Data e Hora atuais.
	 *
	 * @param Vinculo $vinculo        	
	 * @return boolean
	 */
	public function invalidarIsencaoVinculo(Vinculo $vinculo) {
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$idIsencao = $vinculo->getIsencao ()->getId ();
		$sql = "UPDATE isencao set isen_fim = '$dataTimeAtual' WHERE isen_id = $idIsencao";
		if ($this->getConexao ()->exec ( $sql ))
			return true;
		else
			return false;
	}
	
	/**
	 * Adiciona um vinculo isento ao cartão,
	 * É verificado se o cartão já possui um vinculo válido.
	 *
	 * @param Vinculo $vinculo        	
	 */
	public function adicionarIsencaoNoVinculo(Vinculo $vinculo) {
		$idCartao = $vinculo->getCartao ()->getId ();
		$inicio = $vinculo->getIsencao ()->getDataDeInicio ();
		$fim = $vinculo->getIsencao ()->getDataFinal ();
		if (! $vinculo->isActive ()) {
			return false;
		}
		$tempoA = strtotime ( $vinculo->getIsencao ()->getDataDeInicio () );
		$tempoB = strtotime ( $vinculo->getIsencao ()->getDataFinal () );
		$tempoAgora = time ();
		// Não adicionar isenção para o passado.
		if ($tempoA < strtotime ( "-1 days" )) {
			echo '<p>Não é possível adicionar isenção para o passado</p>';
			return false;
		}
		// Não adicionar caso o usuário inverta as datas.
		if ($tempoB <= $tempoA) {
			echo '<p>Talvez você tenha trocado as datas. </p>';
			return false;
		}
		$sql = "INSERT into isencao(isen_inicio,isen_fim,cart_id) VALUES('$inicio', '$fim', $idCartao)";
		if ($this->getConexao ()->exec ( $sql ))
			return true;
		return false;
	}
	
	/**
	 * 	
	 * @ignore
	 *
	 * @param Vinculo $vinculo        	
	 * @param unknown $valorVendido        	
	 * @param unknown $idUsuario        	
	 */
	public function adicionarCreditos(Vinculo $vinculo, $valorVendido, $idUsuario) {
		$novoValor = $vinculo->getCartao ()->getCreditos ();
		$idCartao = $vinculo->getCartao ()->getId ();
		$valorVendido = floatval ( $valorVendido );
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		
		$sql = "UPDATE cartao set cart_creditos = $novoValor WHERE cart_id = $idCartao";
		
		$sql2 = "INSERT into transacao(tran_valor, tran_descricao, tran_data, usua_id) 
				VALUES($valorVendido, 'Venda de Créditos','$dataTimeAtual', $idUsuario)";
		$this->getConexao ()->beginTransaction ();
		
		// echo $sql;
		if (! $this->getConexao ()->exec ( $sql )) {
			$this->getConexao ()->rollBack ();
			return false;
		}
		if (! $this->getConexao ()->exec ( $sql2 )) {
			$this->getConexao ()->rollBack ();
			return false;
		}
		$this->getConexao ()->commit ();
		return true;
	}
	
	/**
	 * Consulta um vinculo através do Id do vinculo.
	 *
	 * @param Vinculo $vinculo
	 *        	Objeto Vinculo contendo Id do Vinculo.
	 * @return Vinculo
	 */
	public function vinculoPorId(Vinculo $vinculo) {
		$idVinculo = $vinculo->getId ();
		$sql = "SELECT * FROM vinculo
		INNER JOIN usuario ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN vinculo_tipo ON vinculo.vinc_id = vinculo_tipo.vinc_id
		LEFT JOIN tipo ON vinculo_tipo.tipo_id = tipo.tipo_id
		WHERE vinculo.vinc_id = $idVinculo";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setId ( $linha ['usua_id'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->getCartao ()->setCreditos ( $linha ['cart_creditos'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->getResponsavel ()->setNivelAcesso ( $linha ['usua_nivel'] );
			$vinculo->setQuantidadeDeAlimentosPorTurno ( $linha ['vinc_refeicoes'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			return $vinculo;
		}
	}
	
	/**
	 * Consulta Vinculo Insento Válido.
	 *
	 * @param Vinculo $vinculo        	
	 */
	public function isencaoValidaDoVinculo(Vinculo $vinculo) {
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$idVinculo = $vinculo->getId ();
		$sql = "SELECT * FROM vinculo
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		INNER JOIN isencao ON cartao.cart_id = isencao.cart_id
		WHERE (vinculo.vinc_id = $idVinculo) AND  ('$dataTimeAtual' < isencao.isen_fim);";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			if (isset ( $linha ['isen_id'] )) {
				$vinculo->setIsencao ( new Isencao () );
				$vinculo->setIsento ( true );
				$vinculo->getIsencao ()->setId ( $linha ['isen_id'] );
				$vinculo->getIsencao ()->setDataDeInicio ( $linha ['isen_inicio'] );
				$vinculo->getIsencao ()->setDataFinal ( $linha ['isen_fim'] );
			}
			return $vinculo;
		}
	}
	
	/**
	 * Consulta o vinculo válido do cartão.
	 *
	 * @param Cartao $cartao        	
	 */
	public function retornaVinculosValidosDeCartao(Cartao $cartao) {
		$lista = array ();
		$idCartao = $cartao->getId ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		WHERE (cartao.cart_id = $idCartao)
		AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * 
	 * @param Cartao $cartao        	
	 */
	public function retornaVinculoValidoDeCartao(Cartao $cartao) {
		$idCartao = $cartao->getId ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		WHERE (cartao.cart_id = $idCartao)
		AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		$vinculo = NULL;
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->setQuantidadeDeAlimentosPorTurno ( $linha ['vinc_refeicoes'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->getTipo ()->setValorCobrado ( $linha ['tipo_valor'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
		}
		return $vinculo;
	}
	
	/**
	 * Consulta os vinculos do Cartão.
	 *
	 * @param Cartao $cartao        	
	 * @return Vinculo[]
	 */
	public function retornaVinculosVencidosDeCartao(Cartao $cartao) {
		$lista = array ();
		$idCartao = $cartao->getId ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		WHERE (cartao.cart_id = $idCartao)
		AND ('$dataTimeAtual' > vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * 
	 * @param Cartao $cartao        	
	 */
	public function retornaVinculosFuturosDeCartao(Cartao $cartao) {
		$lista = array ();
		$idCartao = $cartao->getId ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		WHERE (cartao.cart_id = $idCartao)
		AND ('$dataTimeAtual' < vinc_inicio AND '$dataTimeAtual' < vinc_fim)";
		$result = $this->getConexao ()->query ( $sql );
		
		foreach ( $result as $linha ) {
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 * Realiza a atualização da validade do vinculo,
	 * Aqui é realizado a atualização do campo vinc_fim com a Data e Hora atual acrescida de 3 meses.
	 *
	 * @param Vinculo $vinculo        	
	 */
	public function atualizaValidade(Vinculo $vinculo) {
		$data = $vinculo->getFinalValidade ();
		$idVinculo = $vinculo->getId ();
		
		if (! $idVinculo)
			return false;
		
		$sqlUpdate = "UPDATE vinculo set vinc_fim = '$data' WHERE vinc_id = $idVinculo";
		if ($this->getConexao ()->exec ( $sqlUpdate ))
			return true;
		return false;
	}
	
	/**
	 * Consulta se o Usuário pesuisado já possui vinculo válido.
	 * Caso possua vínculo, será retornado True.
	 * 
	 * @param Usuario $usuario
	 * @return boolean    	
	 */
	public function usuarioJaTemVinculo(Usuario $usuario) {
		$idBaseExterna = $usuario->getIdBaseExterna ();
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id WHERE (usuario.id_base_externa = $idBaseExterna)
		AND ('$dataTimeAtual' BETWEEN vinc_inicio AND vinc_fim) AND vinc_avulso = FALSE";
		// echo $sql;
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {			
			return true;
		}
		return false;
	}
	
	/**
	 * Está função cria um vinculo válido para o usuário.
	 * 
	 * @param Vinculo $vinculo        	
	 */
	public function adicionaVinculo(Vinculo $vinculo) {
		$inicio = $vinculo->getInicioValidade ();
		$usuarioBaseExterna = $vinculo->getResponsavel ()->getIdBaseExterna ();
		$numeroCartao = $vinculo->getCartao ()->getNumero ();
		$dataDeValidade = $vinculo->getFinalValidade ();
		$tipoCartao = $vinculo->getCartao ()->getTipo ()->getId ();
		$this->verificarUsuario ( $vinculo->getResponsavel () );
		if ($vinculo->invalidoParaAdicionar ()) {
			return false;
		}
		if (! $vinculo->getResponsavel ()->getId ()) {
			// echo 'Veio daqui oh';
			return false;
		}
		
		$idBaseLocal = $vinculo->getResponsavel ()->getId ();
		$this->verificaCartao ( $vinculo->getCartao () );
		if (! $vinculo->getCartao ()->getId ())
			return false;
		$idCartao = $vinculo->getCartao ()->getId ();
		$refeicoes = $vinculo->getQuantidadeDeAlimentosPorTurno ();
		$descricao = $vinculo->getDescricao ();
		$this->getConexao ()->beginTransaction ();
		
		if ($vinculo->isAvulso ())
			$sqlInsertVinculo = "INSERT INTO vinculo(usua_id, cart_id, vinc_refeicoes, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao) VALUES($idBaseLocal, $idCartao, $refeicoes,TRUE,'$inicio', '$dataDeValidade', '$descricao')";
		else
			$sqlInsertVinculo = "INSERT INTO vinculo(usua_id, cart_id, vinc_refeicoes, vinc_avulso, vinc_inicio, vinc_fim, vinc_descricao) VALUES($idBaseLocal, $idCartao, 1,FALSE,'$inicio', '$dataDeValidade', 'Padrão')";
		if (! $this->getConexao ()->exec ( $sqlInsertVinculo )) {
			$this->getConexao ()->rollBack ();
			return 0;
		}
		$idVinculo = $this->getConexao ()->lastInsertId ( 'vinculo_vinc_id_seq' );
		if (! $this->getConexao ()->exec ( "INSERT INTO vinculo_tipo(vinc_id, tipo_id) VALUES($idVinculo, $tipoCartao)" )) {
			$this->getConexao ()->rollBack ();
			return 0;
		}
		$this->getConexao ()->commit ();
		return true;
	}
	
	/**
	 * Retorna true se o cartão possuir vinculo válido.
	 *
	 * Retorna false se o cartão não possui um vinculo válido.
	 *
	 * @param Cartao $cartao        	
	 * @return boolean
	 */
	public function cartaoTemVinculo(Cartao $cartao) {
		$numero = $cartao->getNumero ();
		
		$dataTimeAtual = date ( "Y-m-d G:i:s" );
		$sql = "SELECT * FROM vinculo
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		WHERE (cartao.cart_numero = '$numero') LIMIT 1";
		$resultSet = $this->getConexao ()->query ( $sql );
		foreach ( $resultSet as $linha ) {
			$cartao->setId ( $linha ['cart_id'] );
			return true;
		}
		return false;
	}
	
	/**
	 * Através de um numero de cartão iremos retornar seu verdadeiro ID.
	 *
	 * Mas antes iremos alterar seu tipo.
	 *
	 * Caso ele nem exista a gente cadastra com o tipo oferecido aqui.
	 *
	 * @param Cartao $cartao
	 */
	public function verificaCartao(Cartao $cartao) {
		$numeroCartao = $cartao->getNumero ();
		$idTipo = $cartao->getTipo ()->getId ();
		
		$result = $this->getConexao ()->query ( "SELECT * FROM cartao WHERE cart_numero = '$numeroCartao'" );
		foreach ( $result as $linha ) {
			// if($linha['cart_creditos'] > 0)
			// return false;
			if ($linha ['tipo_id'] != $idTipo) {
				if (! $this->getConexao ()->exec ( "UPDATE cartao set tipo_id = $idTipo WHERE cart_numero = '$numeroCartao'" ))
					return false;
			}
			$cartao->getTipo ()->setId ( $linha ['tipo_id'] );
			$cartao->setId ( $linha ['cart_id'] );
			return $linha ['cart_id'];
		}
		if ($this->getConexao ()->query ( "INSERT INTO cartao(cart_numero, cart_creditos, tipo_id) VALUES('$numeroCartao', 0, $idTipo)" )) {
			foreach ( $this->getConexao ()->query ( "SELECT * FROM cartao WHERE cart_numero = '$numeroCartao'" ) as $otraLinha ) {
				$cartao->setId ( $otraLinha ['cart_id'] );
				return $otraLinha ['cart_id'];
			}
		}
		return false;
	}
	
	/**
	 * Vamos pegar da base exter a ecopiar para a base local.
	 * Se Nem existir na base externa, É o usuario frescando. Preciso dar nem resposta pra ele. Aborto tudo logo.
	 * Fa�amos um insert aqui.
	 * Apos esse insert iremos pegar o id inserido na base e retornalo.
	 * Retorna 0, deu nada certo. Essa parada acaba aqui.
	 *
	 * @param Usuario $usuario        	
	 * @return int
	 */
	public function verificarUsuario(Usuario $usuario) {
		$idBaseExterna = $usuario->getIdBaseExterna ();
		
		$result = $this->getConexao ()->query ( "SELECT id_base_externa, usua_id FROM usuario WHERE id_base_externa = $idBaseExterna" );
		foreach ( $result as $linha ) {
			$usuario->setId ( $linha ['usua_id'] );
			
			return $linha ['usua_id'];
		}
		$result2 = $this->getConexao ()->query ( "SELECT * FROM vw_usuarios_autenticacao_catraca WHERE id_usuario = $idBaseExterna" );
		foreach ( $result2 as $linha ) {
			
			$nivel = Sessao::NIVEL_COMUM;
			$nome = $linha ['nome'];
			$nome = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $nome );
			$nome = strtoupper ( $nome );
			$email = $linha ['email'];
			$login = $linha ['login'];
			$senha = $linha ['senha'];
			$idBaseExterna = $linha ['id_usuario'];
			$sqlInserir = "INSERT into usuario(usua_login,usua_senha, usua_nome,usua_email, usua_nivel, id_base_externa)
					VALUES	('$login', '$senha', '$nome','$email', $nivel, $idBaseExterna)";
			
			// echo $sqlInserir;
			if ($this->getConexao ()->exec ( $sqlInserir )) {
				
				foreach ( $this->getConexao ()->query ( "SELECT * FROM usuario WHERE id_base_externa = $idBaseExterna" ) as $linha3 ) {
					$usuario->setId ( $linha3 ['usua_id'] );
					
					return $linha3 ['usua_id'];
				}
			}
		}
		return 0;
	}
	
	/**
	 * @param DateTime $dataReferencia        	
	 * @param string $nomeUsuario        	
	 */
	public function isencoesValidas($dataReferencia = null, $nomeUsuario = null) {
		$lista = array ();
		
		if ($dataReferencia == null)
			$dataReferencia = date ( "Y-m-d G:i:s" );
		$outroFiltro = "";
		if ($nomeUsuario != null) {
			$nomeUsuario = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $nomeUsuario );
			$nomeUsuario = strtoupper ( $nomeUsuario );
			$outroFiltro = "AND usua_nome LIKE '%$nomeUsuario%'";
		}
		
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		INNER JOIN isencao ON cartao.cart_id = isencao.cart_id
		WHERE ('$dataReferencia' BETWEEN vinc_inicio AND vinc_fim) AND ('$dataReferencia' BETWEEN isen_inicio AND isen_fim) $outroFiltro LIMIT 100";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getCartao ()->setTipo ( new Tipo () );
			$vinculo->getResponsavel ()->setId ( $linha ['usua_id'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
	
	/**
	 *
	 * @param DateTime $dataReferencia        	
	 * @param string $nomeUsuario        	
	 */
	public function buscaVinculos($dataReferencia = null, $nomeUsuario = null) {
		$lista = array ();
		
		if ($dataReferencia == null)
			$dataReferencia = date ( "Y-m-d G:i:s" );
		$outroFiltro = "";
		if ($nomeUsuario != null) {
			$nomeUsuario = preg_replace ( '/[^a-zA-Z0-9\s]/', '', $nomeUsuario );
			$nomeUsuario = strtoupper ( $nomeUsuario );
			$outroFiltro = "AND usua_nome LIKE '%$nomeUsuario%'";
		}
		
		$sql = "SELECT * FROM usuario INNER JOIN vinculo
		ON vinculo.usua_id = usuario.usua_id
		LEFT JOIN cartao ON cartao.cart_id = vinculo.cart_id
		LEFT JOIN tipo ON cartao.tipo_id = tipo.tipo_id
		
		WHERE '$dataReferencia' BETWEEN vinc_inicio AND vinc_fim  $outroFiltro LIMIT 100";
		$result = $this->getConexao ()->query ( $sql );
		foreach ( $result as $linha ) {
			
			$vinculo = new Vinculo ();
			$vinculo->setId ( $linha ['vinc_id'] );
			$vinculo->getCartao ()->setTipo ( new Tipo () );
			$vinculo->getResponsavel ()->setId ( $linha ['usua_id'] );
			$vinculo->getResponsavel ()->setNome ( $linha ['usua_nome'] );
			$vinculo->getResponsavel ()->setIdBaseExterna ( $linha ['id_base_externa'] );
			$vinculo->getCartao ()->setId ( $linha ['cart_id'] );
			$vinculo->getCartao ()->getTipo ()->setNome ( $linha ['tipo_nome'] );
			$vinculo->getCartao ()->setNumero ( $linha ['cart_numero'] );
			$vinculo->setInicioValidade ( $linha ['vinc_inicio'] );
			$vinculo->setFinalValidade ( $linha ['vinc_fim'] );
			$vinculo->setAvulso ( $linha ['vinc_avulso'] );
			$lista [] = $vinculo;
		}
		return $lista;
	}
}

?>