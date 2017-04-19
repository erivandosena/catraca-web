package br.edu.unilab.catraca.controller;

import br.edu.unilab.catraca.view.FrameSplash;
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */
public class CatracaVirtualController {
	private boolean estadoOnline;

	
	
	public CatracaVirtualController(){
		this.estadoOnline= true;
	}
	
	/**
	 * Este metodo criara um splash e deixará visível até que consiga criar as janelas e eventos. 
	 * Ele dispara o metodo que ira fazendoSincronia(), 
	 * Apos tudo feito, tornará o splash invisivel e tornará a janela de espera visivel. 
	 */
	public void iniciar(){
		FrameSplash splash = new FrameSplash();
		splash.setVisible(true);
		this.criarJanelas();
		this.criarEventos();
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		splash.setVisible(false);
		splash.dispose();
		
		
		
	}
	public void criarJanelas(){
		System.out.println("Criando janelas");
	}
	public void criarEventos(){
		System.out.println("Criando eventos");
	}
	/**
	 * Inicializar e iniciar uma Thread que faz sincronização de dados locais com o servidor. 
	 * A verificação para cada tabela poderá ser interrompida se o campo estado mudar para offline.  
	 * O campo estado poderá ser modificado pelo usuário a partir de um evento. Isso desencadeará o início da Catraca Virtual Offline. 
	 */
	public void fazendoSincronia(){
		Thread sincronizando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				while(true){
					System.out.println("Quero sincronizar, vamos começar? ");
					break;
				}
				
			}
		});
		sincronizando.start();
		
	}
	
	/**
	 * Este método será desencadeado pela atualização do estado. 
	 * 
	 */
	public void iniciarCatraca(){
		
	}
	/**
	 * 
	 */
	public void enviarDados(){
		
	}
	
	
	
	
}
