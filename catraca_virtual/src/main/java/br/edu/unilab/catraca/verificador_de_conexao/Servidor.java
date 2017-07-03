package br.edu.unilab.catraca.verificador_de_conexao;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class Servidor {

	private ServerSocket servidor;
	public static final int PORT = 12345;

	public ArrayList<Cliente> lista;
	public Servidor(){
		this.lista = new ArrayList<>();
		
	}
	
	public void iniciaServico() {

		try {
			servidor = new ServerSocket(Servidor.PORT, 8);
			System.out.println("Servidor iniciou. Aguardando conexões.... ");
			Socket cliente;
			while (true) {
				cliente = servidor.accept();
				System.out.println("Nova conexao");
				processandoConexao(cliente);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	private void processandoConexao(final Socket conexao) {
		Thread processando = new Thread(new Runnable() {

			@Override
			public void run() {
				Cliente cliente = new Cliente();
				try {
					ObjectOutputStream saida = new ObjectOutputStream(conexao.getOutputStream());
					ObjectInputStream entrada = new ObjectInputStream(conexao.getInputStream());
					
					lista.add(cliente);
					while(true){
						String mensagem = (String) entrada.readObject();
						processandoMensagem(mensagem, cliente);
					}
					
				} catch (IOException | ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		});
		processando.start();

	}

	public void processandoMensagem(final String mensagem, final Cliente cliente) {
		Thread processando = new Thread(new Runnable() {
			@Override
			public void run() {
				System.out.println("Entrei aqui");
				if (mensagem.contains("setNome") && mensagem.length() >= "setNome".length() + 2) {
					cliente.setNome(mensagem.substring("setNome(".length(), mensagem.length() - 1));
					System.out.println("Novo nome: " + cliente.getNome());
				}
				System.out.println(cliente.getNome() + ">>" + mensagem);		
			}
		});
		processando.start();
		
	}

}
