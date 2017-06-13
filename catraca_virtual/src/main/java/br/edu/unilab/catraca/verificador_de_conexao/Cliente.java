package br.edu.unilab.catraca.verificador_de_conexao;

import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class Cliente {
	public static final String HOST = "localhost";
	public static final int PORT = 27289;

	public void tentandoConexao() {
		Thread tentandoConexao = new Thread();

		tentandoConexao.start();

	}

	public boolean testar() {
		try {

			Socket conexao = new Socket(HOST, 37389);

		} catch (UnknownHostException e) {
			System.out.println("Servidor Indisponivel");

		} catch (IOException e) {
			System.out.println("Erro de IO");
			return false;

		}

		return true;
	}

}
