package br.edu.unilab.catraca.main;

import java.util.ArrayList;

import br.edu.unilab.catraca.controller.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.dao.UsuarioDAO;
import br.edu.unilab.unicafe.model.Usuario;

public class MainTeste {

	public static void main(String[] args) {
		
		
		UsuarioRecurso recurso = new UsuarioRecurso();
		final ArrayList<Usuario> lista = recurso.obterLista();
		final UsuarioDAO dao = new UsuarioDAO();
		
		Thread inserindo = new Thread(new Runnable() {
			
			@Override
			public void run() {
				dao.limpar();
				System.out.println("Veio: "+lista.size());
				
				System.out.println("Limpei, vou inserir");
				for (Usuario usuario : lista) {
					dao.inserir(usuario);
					System.out.println("Foi");
				}
				System.out.println("Terminei a insersao");	
				
			}
		});
		Thread listando = new Thread(new Runnable() {
			
			@Override
			public void run() {
			
				for(int i = 0; i < 60; i++){

					ArrayList<Usuario> listaSelect;
					listaSelect = dao.retornaLista();
					System.out.println("Quantidade retornado: "+listaSelect.size());
					try {
						Thread.sleep(500);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
				
			}
		});
		Thread listando2 = new Thread(new Runnable() {
			
			@Override
			public void run() {
			
				for(int i = 0; i < 60; i++){

					ArrayList<Usuario> listaSelect;
					listaSelect = dao.retornaLista();
					System.out.println("Quantidade retornado: "+listaSelect.size());
					try {
						Thread.sleep(500);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
				
			}
		});
		inserindo.start();
		listando.start();
		listando2.start();
	}

}
