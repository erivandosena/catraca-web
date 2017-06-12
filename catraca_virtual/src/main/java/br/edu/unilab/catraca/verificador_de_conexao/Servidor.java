package br.edu.unilab.catraca.verificador_de_conexao;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
	
	private ServerSocket servidor;
	public static final int PORT = 27289;
	
	public void iniciaServico(){
		
		Thread iniciando = new Thread(new Runnable() {
			public void run() {
				try {
					servidor = new ServerSocket(Servidor.PORT, 8);
					System.out.println("Servidor iniciou. Aguardando conexões.... ");
					Socket cliente;
					while(true){
						cliente = servidor.accept();
						System.out.println("Nova conexao");
						processandoConexao(cliente);
					}
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
			}
		});
		iniciando.start();
		
	}
	private void processandoConexao(final Socket conexao){
		Thread processando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				try {
					ObjectOutputStream saida = new ObjectOutputStream(conexao.getOutputStream());
					ObjectInputStream entrada = new ObjectInputStream(conexao.getInputStream());
					String mensagem = (String) entrada.readObject();
					if(mensagem.equals("taVivo"))
					{
						saida.writeObject("sim");
					}
					conexao.close();
					
				} catch (IOException | ClassNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
			}
		});
		processando.start();
		
		
		
	}
	
	

}
