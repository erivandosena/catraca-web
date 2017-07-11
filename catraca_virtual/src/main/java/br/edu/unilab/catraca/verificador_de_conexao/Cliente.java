package br.edu.unilab.catraca.verificador_de_conexao;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.concurrent.Semaphore;

import javax.swing.JOptionPane;

import java.util.Scanner;

import br.edu.unilab.catraca.controller.CatracaVirtualController;

public class Cliente {
	public static final String HOST = "catracahomologacao.unilab.edu.br";
	public static final int PORT = 12345;
	private Socket conexao;
	public int tentativa = 0;
	public int ultimaInteracao = 0;
	private boolean statusConexao;
	private CatracaVirtualController catracaVirtual;
	
	
	public Cliente(){
		this.nome = "Catraca Virtual";
		this.statusConexao = true;
		semaforo = new Semaphore(1);
		tempoDeInteracao();
	}
	public void iniciar(){
		this.catracaVirtual = new CatracaVirtualController();
		this.catracaVirtual.iniciar();
		tentandoConexao();
	}
	public void tempoDeInteracao(){
		Thread contando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				while(true){
					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					try {
						semaforo.acquire();
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					if(ultimaInteracao < 100){
						ultimaInteracao++; 
					}else{
						//fechar conexao
						try {
							conexao.close();
						} catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
						ultimaInteracao = 0;
					}
					
					System.out.println("Ultima interacao: "+ultimaInteracao);
					semaforo.release();
				}
			}
		});
		contando.start();
	}
	
	public void tentandoConexao() {

		Thread tentandoConexao = new Thread(new Runnable() {

			public void run() {
				while (true) {
					
					System.out.println("Tentativa " + tentativa);

					try {
						
						conexao = new Socket(HOST, PORT);
						if(tentativa > 10){
							JOptionPane.showMessageDialog(null, "Conexão com servidor estabelecida!");
						}
						
						catracaVirtual.getFrameLogin().setVisible(false);
						catracaVirtual.getFrameCatracaVirtual().setVisible(false);
						
						setStatusConexao(true);
						processandoConexao(conexao);
						break;
					} catch (UnknownHostException e) {
						if(isStatusConexao()){

							System.out.println("Servidor Indisponivel");
							JOptionPane.showMessageDialog(null, "Sua Conexão com o servidor caiu! Erro de IO. Utilize o catraca Offline!");
							catracaVirtual.getFrameLogin().setVisible(true);
						}			
						setStatusConexao(false);					
	
	
						
					} catch (IOException e) {
						if(isStatusConexao()){

							System.out.println("Erro de IO");
							JOptionPane.showMessageDialog(null, "Sua Conexão com o servidor caiu! Erro de IO. Utilize o catraca Offline!");
							catracaVirtual.getFrameLogin().setVisible(true);
						}			
						setStatusConexao(false);
						
						
						
					}
					tentativa++;
					try {
						Thread.sleep(2000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}

				}
			}

			
		});

		tentandoConexao.start();

	}
	private void processandoConexao(final Socket conexao) {
		this.setConexao(conexao);
		Thread processando = new Thread(new Runnable() {

			@Override
			public void run() {
				ObjectOutputStream saida;
				ObjectInputStream entrada;
				try {
					saida = new ObjectOutputStream(conexao.getOutputStream());
					saida.flush();
					
					saida.writeObject("setNome(" + catracaVirtual.getCatraca().getNome() + ")");
					saida.flush();

					entrada = new ObjectInputStream(conexao.getInputStream());

					setSaida(saida);
					setEntrada(entrada);

					while (getConexao().isConnected()) {
						String mensagem = (String) entrada.readObject();
						processandoMensagem(mensagem);
					}
					if(isStatusConexao()){
						setStatusConexao(false);
						catracaVirtual.getFrameLogin().setVisible(true);
					}
					
					tentandoConexao();
					return;
					

				} catch (IOException | ClassNotFoundException e) {
					
					if(isStatusConexao()){
						setStatusConexao(false);
						catracaVirtual.getFrameLogin().setVisible(true);
					}
					tentandoConexao();
					return;
				}

			}

			
		});
		processando.start();
		
	}
	
	private Semaphore semaforo;
	
	private void processandoMensagem(String mensagem) {
		System.out.println("MEnsagem do servidor: "+mensagem);
		try {
			semaforo.acquire();
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		ultimaInteracao = 0;
		
		semaforo.release();
		
		if(mensagem.equals("atualizar")){
			Process process;
			try {
				Runtime.getRuntime().exec(" java -jar \"C:\\Program Files (x86)\\Catraca\\catraca-update.jar\"");
				
			} catch (IOException e) {
				e.printStackTrace();

			}
			System.exit(0);
			return;
			
		}
		
	}
	

	public String nome;
	
	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getNome() {
		return this.nome;
	}
	public ObjectOutputStream getSaida() {
		return saida;
	}

	public void setSaida(ObjectOutputStream saida) {
		this.saida = saida;
	}

	public ObjectInputStream getEntrada() {
		return entrada;
	}

	public void setEntrada(ObjectInputStream entrada) {
		this.entrada = entrada;
	}

	public Socket getConexao() {
		return conexao;
	}
	public void setConexao(Socket conexao) {
		this.conexao = conexao;
	}

	public Semaphore getSemaforo() {
		return semaforo;
	}
	public void setSemaforo(Semaphore semaforo) {
		this.semaforo = semaforo;
	}

	public boolean isStatusConexao() {
		return statusConexao;
	}
	public void setStatusConexao(boolean statusConexao) {
		this.statusConexao = statusConexao;
	}
	


	
	private ObjectOutputStream saida;
	private ObjectInputStream entrada;

	
}
