package br.edu.unilab.catraca.controller;

import java.net.UnknownHostException;
import java.util.ArrayList;

import javax.swing.JFrame;

import br.edu.unilab.catraca.controller.recurso.CatracaRecurso;
import br.edu.unilab.catraca.controller.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.CustoRefeicaoRecurso;
import br.edu.unilab.catraca.controller.recurso.CustoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.RegistroRecurso;
import br.edu.unilab.catraca.controller.recurso.TipoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CustoUnidadeDAO;
import br.edu.unilab.catraca.view.CatracaVirtualView;
import br.edu.unilab.catraca.view.LoginView;
import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.TurnoUnidade;

public class CatracaVirtualController {
	
	private LoginView frameLogin;
	private CatracaVirtualView frame;
	private Catraca catracaVirtual;
	private CatracaDAO dao;
	
	
	public CatracaVirtualController(){
		this.catracaVirtual = new Catraca();
	}
	public void sincronizacaoBasica(){
		CatracaRecurso catracaRecurso = new CatracaRecurso();
		catracaRecurso.sincronizar();
		
		RegistroRecurso recurso = new RegistroRecurso();
		recurso.sincronizar();
		
		UnidadeRecurso unidadeRecurso = new UnidadeRecurso();
		unidadeRecurso.sincronizar();
		
		
		
		TipoRecurso tipoRecurso = new TipoRecurso();
		tipoRecurso.sincronizar();
		
		TurnoRecurso turnoRecurso = new TurnoRecurso();
		turnoRecurso.sincronizar();
		

		
		
	}
	public void iniciar(){
		this.frameLogin = new LoginView();
		this.frameLogin.getLabelMensagem().setText("Aguarde a Sincronização dos Dados");
		
		this.frameLogin.setVisible(true);
		this.frameLogin.setExtendedState(JFrame.MAXIMIZED_BOTH);
		
		
		this.sincronizacaoBasica();
		
		try {
			this.catracaVirtual.maquinaLocal();
		} catch (UnknownHostException e) {
			System.out.println("Impossivel determinar nome da maquina. ");
			e.printStackTrace();
			return;
		}
		this.dao = new CatracaDAO();
		
		if(this.dao.retornaCatracaPorNome(this.catracaVirtual) == null){
			System.out.println("Cadastre a catraca virtual");
		}else{
			System.out.println("Catraca Virtual: "+catracaVirtual.getNome());
		}
		
		
		
		
		
//		TipoRecurso recurso = new TipoRecurso();
//		recurso.sincronizar();
//		
		
//		CatracaRecurso recurso = new CatracaRecurso();
//		recurso.sincronizar();
//		

		
		
	}
	
	
	
}
