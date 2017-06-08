package br.edu.unilab.catraca.controller;

import java.sql.SQLException;
import java.util.ArrayList;

import javax.swing.JFrame;

import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.TurnoDAO;
import br.edu.unilab.catraca.recurso.CatracaRecurso;
import br.edu.unilab.catraca.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.recurso.TurnoRecurso;
import br.edu.unilab.catraca.recurso.TurnoUnidadeRecurso;
import br.edu.unilab.catraca.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.view.CatracaVirtualView;
import br.edu.unilab.catraca.view.FrameSplash;
import br.edu.unilab.catraca.view.LoginView;
import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.Turno;
import br.edu.unilab.unicafe.model.Unidade;
/**
 * 
 * @author Jefferson Uchoa Ponte
 *
 */
public class CatracaVirtualController {
	private ArrayList<Turno>turnos;
	private Turno turnoAtual;
	private boolean turnoAtivo;
	
	private LoginView frameLogin;
	private CatracaVirtualView frameCatracaVirtual;
	
	
	private Catraca catracaVirtual;
	private CatracaDAO dao;
	private Unidade unidade;
	
	public CatracaVirtualController(){
		this.turnoAtivo = false;
		this.catracaVirtual = new Catraca();
	}
	
	
	/**
	 * Este metodo criara um splash e deixará visível até que
	 *  consiga criar as janelas e eventos. 
	 * Ele dispara o metodo fazendoSincronia(), 
	 * Apos tudo feito, tornará o splash invisivel e 
	 * tornará a janela de login visivel. 
	 */
	public void iniciar(){
		FrameSplash splash = new FrameSplash();
		splash.setVisible(true);
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.frameLogin = new LoginView();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação da catraca.");
		this.frameLogin.setExtendedState(JFrame.MAXIMIZED_BOTH);
		splash.setVisible(false);
		this.frameLogin.setVisible(true);
		splash.dispose();
		this.catracaVirtual.maquinaLocal();
		this.verificarNomeDaCatraca();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação da Unidade Acadêmica.");
		this.verificarUnidadeDaCatraca();
		this.frameLogin.getLabelMensagem().setText("Aguardando informação de Turnos.");
		this.verificarTurnosDaUnidade();
		this.frameLogin.getLabelMensagem().setText("Preparar eventos.");
		
		
		
		
	}
	
	
	synchronized private void verificarNomeDaCatraca(){
		boolean passou = false;
		this.dao = new CatracaDAO();
		do{
			if(this.dao.preencheCatracaPorNome(this.catracaVirtual) == false){
				this.frameLogin.getLabelMensagem().setText("Cadastre a catraca virtual "+this.catracaVirtual.getNome());
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				CatracaRecurso catracaRecurso = new CatracaRecurso();
				catracaRecurso.sincronizar(this.dao.getConexao());
			}else{
				passou = true;
				this.frameLogin.getLabelMensagem().setText("Catraca Virtual: "+catracaVirtual.getNome());
				
			}	
		}while(!passou);
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	synchronized private void verificarUnidadeDaCatraca(){
		boolean passou = false;
		this.dao.novaConexao();
		do{
			this.unidade = this.dao.unidadeDaCatraca(this.catracaVirtual);
			if(this.unidade == null){
				this.frameLogin.getLabelMensagem().setText("Cadastre a catraca em alguma unidade academica");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

				UnidadeRecurso unidadeRecurso = new UnidadeRecurso();
				unidadeRecurso.sincronizar(this.dao.getConexao());
				CatracaUnidadeRecurso recurso = new CatracaUnidadeRecurso();
				recurso.sincronizar(this.dao.getConexao());
				TurnoRecurso turnoRecurso = new TurnoRecurso();
				turnoRecurso.sincronizar(this.dao.getConexao());
				
			}else{
				this.frameLogin.getLabelMensagem().setText("Unidade: "+unidade.getNome());
				passou = true;
			}
		}while(!passou);
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	synchronized private void verificarTurnosDaUnidade(){
		boolean passou = false;
		this.dao.novaConexao();
		do{
			this.turnos = this.dao.turnosDaUnidade(this.unidade);
			if(this.turnos == null || this.turnos.size() == 0){
				this.frameLogin.getLabelMensagem().setText("Adicione turnos na Unidade Academica");
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				TurnoUnidadeRecurso recurso = new TurnoUnidadeRecurso();
				recurso.sincronizar(this.dao.getConexao());
			}else{
				this.frameLogin.getLabelMensagem().setText("");
				passou = true;
			}
			
		}while(!passou);
		try {
			this.dao.getConexao().close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	synchronized public void atualizarBaseLocal(){
		
		
	}
	synchronized public void verificarEssaCatracaEUnidade(){
		
		
	}

	
	/**
	 * Só verificar condições de turno ativo para chamar o método que sincroniza. 
	 * Faz isso de minuto em minuto.     
	 */
	synchronized private void fazendoSincronia(){
		Thread sincronizando = new Thread(new Runnable() {
			
			@Override
			public void run() {
				while(true){
					if(turnoAtivo){
						//Aqui faz nada. 
					}else{
						
						//Aqui sincroniza. 
						
					}
					
					
					try {
						//Vamos esperar um minuto e sincronizar de novo. 
						Thread.sleep(60000);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
			}
		});
		sincronizando.start();
		
	}
	
	
	
	
}
