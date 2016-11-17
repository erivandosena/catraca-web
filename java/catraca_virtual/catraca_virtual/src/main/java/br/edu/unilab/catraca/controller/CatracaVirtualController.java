package br.edu.unilab.catraca.controller;

import java.util.ArrayList;

import br.edu.unilab.catraca.controller.recurso.CatracaUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.CustoRefeicaoRecurso;
import br.edu.unilab.catraca.controller.recurso.CustoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.TipoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoRecurso;
import br.edu.unilab.catraca.controller.recurso.TurnoUnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UnidadeRecurso;
import br.edu.unilab.catraca.controller.recurso.UsuarioRecurso;
import br.edu.unilab.catraca.dao.CatracaDAO;
import br.edu.unilab.catraca.dao.CustoUnidadeDAO;
import br.edu.unilab.catraca.view.CatracaVirtualView;
import br.edu.unilab.unicafe.model.Catraca;
import br.edu.unilab.unicafe.model.TurnoUnidade;

public class CatracaVirtualController {
	
	private CatracaVirtualView frame;
	private Catraca catracaVirtual;
	private CatracaDAO dao;
	
	
	
	public void iniciar(){
		
		
//		this.catracaVirtual = new Catraca();
//		this.catracaVirtual.maquinaLocal();
//		
//		this.dao = new CatracaDAO();
//		ArrayList<Catraca> catracas = new ArrayList<Catraca>();
//		
//		catracas = this.dao.retornaLista();
//		for (Catraca catraca : catracas) {
//			if(this.catracaVirtual.getNome().equals(catraca.getNome())){
//				this.catracaVirtual = catraca;
//			}
//		}
//		System.out.println("Nome: "+this.catracaVirtual.getNome()+" - ID: "+this.catracaVirtual.getId()+" - Financeiro: "+this.catracaVirtual.isFinanceiroAtivo());
		
		TipoRecurso recurso = new TipoRecurso();
		recurso.sincronizar();
		
		
//		CatracaRecurso recurso = new CatracaRecurso();
//		recurso.sincronizar();
//		

		
		
	}
	
	
	
}
