package br.edu.unilab.catraca.update;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Properties;
import java.util.Scanner;

import javax.swing.JLabel;

import br.edu.unilab.catraca.verificador_de_conexao.Cliente;



public class Update {

	private Socket conexao;
	private BufferedReader reader;
	private ObjectInputStream entrada;
	private FileOutputStream out;
	private String linha;

	public void iniciaUpdate() {


		try {
			System.out.println("Tentar atualizar");
			conexao = new Socket(Cliente.HOST, Cliente.PORT);
			PrintStream saida = new PrintStream(conexao.getOutputStream());
			InputStream in = conexao.getInputStream();
			InputStreamReader isr = new InputStreamReader(in);
			setReader(new BufferedReader(isr));
			saida.println("podeMandar");
			saida.flush();
			File f1 = new File("C:\\Program Files (x86)\\Catraca\\Catraca.exe");
			out = new FileOutputStream(f1);
			int tamanho = 4096;
			byte[] buffer = new byte[tamanho];    
			int lidos = -1;  
			while((lidos = in.read(buffer, 0, tamanho)) != -1){
				out.write(buffer, 0, lidos);
			}
			out.flush();
			

			out.close();
			
			
			Process process;
			Scanner leitor;
			try {
				process = Runtime.getRuntime().exec("C:\\Program Files (x86)\\UniCafe\\Catraca.exe");
				leitor = new Scanner(process.getInputStream());
				while (leitor.hasNext()) {
					setLinha(leitor.nextLine());
				}
				Thread.sleep(5000);
			} catch (IOException e) {
				e.printStackTrace();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			System.exit(0);
			
			
		} catch (UnknownHostException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}


		

	}

	public String getLinha() {
		return linha;
	}

	public void setLinha(String linha) {
		this.linha = linha;
	}

	public ObjectInputStream getEntrada() {
		return entrada;
	}

	public void setEntrada(ObjectInputStream entrada) {
		this.entrada = entrada;
	}

	public BufferedReader getReader() {
		return reader;
	}

	public void setReader(BufferedReader reader) {
		this.reader = reader;
	}
}
