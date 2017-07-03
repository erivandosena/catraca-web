package br.edu.unilab.catraca.admin.main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.catraca.verificador_de_conexao.Servidor;

	public class MainAdmin {
	
		private static Scanner scanner;
		private static Socket cliente;

		public static void main(String[] args) {
			

			
			do{
				
				System.out.println("CatracaAdmin digite um comando: ");
				scanner = new Scanner(System.in);
				String mensagem = scanner.nextLine();
				if(mensagem.equals("sair"))
					break;
				
				try {
					cliente = new Socket("localhost", Servidor.PORT);
					
					ObjectOutputStream saida;
					ObjectInputStream entrada;
					saida = new ObjectOutputStream(cliente.getOutputStream());
					saida.flush();
					
					saida.writeObject(UsuarioDAO.getMD5("souAdm()"));
					saida.flush();
					saida.writeObject(mensagem);
					
					entrada = new ObjectInputStream(cliente.getInputStream());
					
					String resposta = "";
					if((resposta = (String) entrada.readObject()) != null){
						System.out.println(resposta);
					}
					cliente.close();
				} catch (UnknownHostException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
				
			}while(true);
	
		}
	
	}
